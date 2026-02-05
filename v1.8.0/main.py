import sys
import os
from pathlib import Path
from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QTableWidgetItem, QTreeWidgetItem, QLabel, QWidget, QDialog, QListWidgetItem, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QSystemTrayIcon, QMenu
from PySide6.QtGui import QDrag, QImage, QPixmap, QWheelEvent, QIcon, QAction
from PySide6.QtCore import QMimeData, QEvent, Qt, QThread, Signal, QRect, QPoint, QTimer, QDate, QUrl, QSize, QItemSelection
from PySide6 import QtCore
from ui.ui_login import Ui_login_windows
from ui.ui_main import Ui_MainWindow

from ui.utils_ai_setting_window import open_ai_setting_window
from ui.utils_schedule_window import open_schedule_window
from ui.utils_object_setting_window import open_object_setting_window
from ui.utils_search_window import open_search_window
from ui.utils_labeling_window import open_labeling_window
from ui.utils_server_setting_window import open_server_setting_window

import resourece_rc  # Qt Resource 파일 import (PyInstaller 빌드 시 필요)

import numpy as np

import socket
import json
import requests
from requests.auth import HTTPBasicAuth
import threading
import base64
import cv2
import re

from utils import (Connect_Camera, Plot_Camera_Viewer, FadeOutWindow, NotificationManager,
                  Eng2kor, Kor2eng, load_info, save_info, 
                  print_error, check_nvidia_gpu)
import time
from datetime import datetime, timedelta
import traceback
import gc
import math

from solapi import SolapiMessageService
from solapi.model import RequestMessage
from solapi.model.kakao.kakao_option import KakaoOption

from cryptography.fernet import Fernet
from dotenv import load_dotenv

# .env 파일 로드 (OS 환경변수가 우선)
# PyInstaller 빌드 시 실행 파일과 같은 디렉토리의 .env를 탐색
if getattr(sys, 'frozen', False):
    _base_dir = os.path.dirname(sys.executable)
else:
    _base_dir = os.path.dirname(os.path.abspath(__file__))

load_dotenv(os.path.join(_base_dir, '.env'), override=False)

KEY = os.environ.get("MS_AI_ENCRYPTION_KEY")
if KEY is None:
    raise RuntimeError("MS_AI_ENCRYPTION_KEY 환경변수가 설정되지 않았습니다. .env 파일을 확인하세요.")

def load_crypography_json(info_filename):
    fernet = Fernet(KEY)
    with open(info_filename, "rb") as f:
        file = f.read()
        file_tran = fernet.decrypt(file)
        return json.loads(file_tran.decode())

def save_crypography_json(info_filename_save_path, info):
    fernet = Fernet(KEY)
    # 딕셔너리를 JSON 문자열로 변환
    json_data = json.dumps(info)
    # JSON 문자열을 바이트로 인코딩
    byte_data = json_data.encode('utf-8')

    with open(info_filename_save_path, "wb") as f:
        f.write(fernet.encrypt(byte_data))



NOTICE_DURATION = {
    0: 3000,
    1: 5000,
    2: 10000,
    3: 60000,
    4: -1,
}

ALARM_TYPE_DIC = {2 : "침입", 1 : "배회", 6 : "쓰러짐", 4 : "방화", 7 : "싸움", 5 : "무단투기"}

FIRST_NOTICE = True

class UpdateCameraImageThread(QThread):
    """카메라 이미지 업데이트를 위한 백그라운드 스레드"""
    finished = Signal(dict)  # 완료 시 camera_img_temp dict를 전달
    
    def __init__(self, ai_server_camera_info_dict, ai_server_info_dict):
        super().__init__()
        self.ai_server_camera_info_dict = ai_server_camera_info_dict
        self.ai_server_info_dict = ai_server_info_dict
        self._is_running = True
    
    def run(self):
        """백그라운드에서 카메라 이미지 가져오기"""
        camera_img_temp = {}
        
        try:
            for nvr_ip, camera_info_dict in self.ai_server_camera_info_dict.items():
                if not self._is_running:
                    break
                    
                nvr_id = self.ai_server_info_dict["NVR"][nvr_ip]["id"]
                nvr_pw = self.ai_server_info_dict["NVR"][nvr_ip]["pw"]
                auth = HTTPBasicAuth(nvr_id, nvr_pw)
                
                for camera_name, camera_info in camera_info_dict.items():
                    if not self._is_running:
                        break
                        
                    try:
                        camera_id = self.ai_server_info_dict["NVR"][nvr_ip]["cameras"][camera_name]["id"]
                        camera_img_url = f'http://{nvr_ip}/live/video{camera_id}.jpg'
                        
                        response = requests.get(camera_img_url, auth=auth, timeout=5)
                        if response.status_code == 200:
                            nparr = np.frombuffer(response.content, np.uint8)
                            decoded_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                            
                            if decoded_img is not None:
                                camera_img_temp[camera_name] = decoded_img
                            else:
                                print(f"Failed to decode image for camera {camera_name}")
                                camera_img_temp[camera_name] = np.zeros((640, 480, 3), dtype=np.uint8)
                        else:
                            print(f"Failed to get image for camera {camera_name}: HTTP {response.status_code}")
                            camera_img_temp[camera_name] = np.zeros((640, 480, 3), dtype=np.uint8)
                    except Exception as e:
                        print(f"Failed to get image for camera {camera_name}: {e}")
                        camera_img_temp[camera_name] = np.zeros((640, 480, 3), dtype=np.uint8)
            
            if self._is_running:
                self.finished.emit(camera_img_temp)
                
        except Exception as e:
            print_error(e)
    
    def stop(self):
        """스레드 중지"""
        self._is_running = False

class CheckAlarmThread(QThread):
    """AI 서버 알람 체크를 위한 백그라운드 스레드"""
    # 새로운 알람 발생 시 전달할 Signal (title, message, camera_name, alarm_time, ai_type, ai_server_ip, ai_server_port)
    new_alarm = Signal(str, str, str, str, str, str, str)
    
    def __init__(self, ai_server_info_dict):
        super().__init__()
        self.ai_server_info_dict = ai_server_info_dict
        self.ai_server_event_alarm_dict = {}
        self.ai_server_disconnect_cnt = {}
        self._is_running = True
    
    def run(self):
        """백그라운드에서 AI 서버 알람 체크 (1초마다)"""
        while self._is_running:
            try:
                for ai_server_ip, ai_server_info in self.ai_server_info_dict["AI_SERVER"].items():
                    if not self._is_running:
                        break
                        
                    ai_server_port = ai_server_info["port"]
                    alarm_url = f'http://{ai_server_ip}:{ai_server_port}/get-ai-alarm-data'

                    try:
                        # 연결 실패 횟수가 많으면 일정 주기로만 재시도
                        if self.ai_server_disconnect_cnt.get(ai_server_ip, 0) > 30 and \
                           self.ai_server_disconnect_cnt.get(ai_server_ip, 0) % 60 != 0:
                            self.ai_server_disconnect_cnt[ai_server_ip] = \
                                self.ai_server_disconnect_cnt.get(ai_server_ip, 0) + 1
                            continue

                        alarm_data = requests.get(alarm_url, timeout=1)
                        self.ai_server_disconnect_cnt[ai_server_ip] = 0

                    except Exception as e:
                        print_error(e)
                        self.ai_server_disconnect_cnt[ai_server_ip] = \
                            self.ai_server_disconnect_cnt.get(ai_server_ip, 0) + 1
                        continue

                    # 알람 데이터 처리
                    try:
                        for nvr_ip, camera_name_dict in alarm_data.json().items():
                            if nvr_ip not in self.ai_server_event_alarm_dict:
                                self.ai_server_event_alarm_dict[nvr_ip] = {}

                            for camera_name, alarm_info in camera_name_dict.items():
                                if camera_name not in self.ai_server_event_alarm_dict[nvr_ip]:
                                    self.ai_server_event_alarm_dict[nvr_ip][camera_name] = alarm_info['events']
                                    continue

                                else: 
                                    if not isinstance(alarm_info, dict) or 'events' not in alarm_info:
                                        continue
                                    
                                    # 기존 이벤트의 rowid 세트 생성
                                    existing_rowids = {event['rowid'] for event in 
                                                     self.ai_server_event_alarm_dict[nvr_ip][camera_name]}
                                    
                                    # 새로운 이벤트만 필터링
                                    new_events = [event for event in alarm_info['events'] 
                                                if event['rowid'] not in existing_rowids]
                                    
                                    if new_events:
                                        # 새로운 알람 이벤트 발생 처리
                                        for event in new_events:
                                            micro_ai_info = event.get('micro_ai', {})
                                            ai_type = ALARM_TYPE_DIC[micro_ai_info.get('type')]
                                            alarm_time = datetime.fromtimestamp(event['timestamp']).strftime("%Y-%m-%d %H:%M:%S")
                                            alarm_type = ALARM_TYPE_DIC.get(ai_type, f"이벤트 감지 (타입: {ai_type})")
                                            
                                            title = f"{camera_name} 카메라"
                                            message = f"{alarm_type}\n{alarm_time}\n(클릭하여 자세히 보기)"

                                            # Signal로 메인 스레드에 알림 전달
                                            self.new_alarm.emit(title, message, camera_name, 
                                                              alarm_time, ai_type, 
                                                              ai_server_ip, ai_server_port)
                                        
                                        # 기존 이벤트 리스트에 새로운 이벤트 추가 (최신 순으로 유지)
                                        self.ai_server_event_alarm_dict[nvr_ip][camera_name] = \
                                            new_events + self.ai_server_event_alarm_dict[nvr_ip][camera_name]
                                        
                                        # 이벤트 리스트 크기 제한 (최근 10개만 유지)
                                        self.ai_server_event_alarm_dict[nvr_ip][camera_name] = \
                                            self.ai_server_event_alarm_dict[nvr_ip][camera_name][:10]
                    except Exception as e:
                        print_error(e)
                        
            except Exception as e:
                print_error(e)
            
            # 1초 대기 (0.1초씩 나눠서 빠른 종료 가능하도록)
            for _ in range(10):
                if not self._is_running:
                    break
                time.sleep(0.1)
    
    def stop(self):
        """스레드 중지"""
        self._is_running = False

def enable_shift_selection(table_widget):
    """테이블에서 Shift 키 누른 상태로 클릭 시 범위 선택 기능 추가"""
    table_widget.last_selected_row = None
    
    # 기존 메서드 백업
    original_mousePressEvent = table_widget.mousePressEvent
    
    def custom_mousePressEvent(event):
        """마우스 클릭 이벤트 처리 - Shift 키 체크"""
        # 클릭된 행 가져오기
        clicked_row = table_widget.indexAt(event.pos()).row()
        
        # Shift 키가 눌렸고, 이전에 선택된 행이 있고, 유효한 행을 클릭한 경우
        if (event.modifiers() & Qt.ShiftModifier) and table_widget.last_selected_row is not None and clicked_row >= 0:
            # 범위 선택
            start_row = min(table_widget.last_selected_row, clicked_row)
            end_row = max(table_widget.last_selected_row, clicked_row)
            
            # 선택 모드를 임시로 변경하여 범위 선택
            table_widget.clearSelection()
            for row in range(start_row, end_row + 1):
                table_widget.selectRow(row)
            
            # 마지막 선택 행 업데이트하지 않음 (Shift 선택 유지)
        else:
            # 일반 클릭 또는 Shift 키 없이 클릭
            original_mousePressEvent(event)
            
            # 유효한 행을 클릭한 경우 마지막 선택 행 업데이트
            if clicked_row >= 0:
                table_widget.last_selected_row = clicked_row
    
    # 메서드 교체
    table_widget.mousePressEvent = custom_mousePressEvent

def make_tree_draggable_with_data(tree_widget, ai_server_info_dict):
    """Tree 위젯에서 드래그 가능하도록 설정
    - 카메라만 드래그 가능 (parent NVR은 제외)
    - Tree로의 드롭은 차단 (내용 변경 방지)
    """
    # 기존 메서드 백업
    original_startDrag = tree_widget.startDrag
    
    def custom_startDrag(supportedActions):
        """Tree에서 드래그 시작 - 카메라 정보만 전달"""
        selected_items = tree_widget.selectedItems()
        
        if selected_items:
            items_data = []
            
            for item in selected_items:
                parent = item.parent()
                
                # parent가 있는 경우만 처리 (카메라만, NVR 제외)
                if parent:
                    try:
                        # NVR 정보 추출
                        nvr_text = parent.text(0)
                        nvr_ip = nvr_text.split("(")[1].split(")")[0]
                        nvr_name = nvr_text.split("(")[0]
                        camera_name = item.text(0)
                        
                        # ai_server_info_dict["NVR"]에서 카메라 정보 찾기
                        if nvr_ip in ai_server_info_dict["NVR"].keys():
                            nvr_info = ai_server_info_dict["NVR"][nvr_ip]
                            if camera_name in nvr_info["cameras"].keys():
                                item_info = {
                                    "camera_name": camera_name,
                                    "camera_ip": nvr_info["cameras"][camera_name]["ip"],
                                    "nvr_name": nvr_name,
                                    "nvr_ip": nvr_ip,
                                    "streaming": nvr_info["cameras"][camera_name].get("streaming", ""),
                                    "camera_id": nvr_info["cameras"][camera_name].get("id", "")
                                }
                                items_data.append(item_info)
                    except Exception as e:
                        print(f"카메라 정보 추출 중 에러: {e}")
            
            # 유효한 카메라 데이터가 있으면 드래그 시작
            if items_data:
                import json
                json_text = json.dumps(items_data, ensure_ascii=False)
                
                mime_data = QMimeData()
                mime_data.setText(json_text)
                
                drag = QDrag(tree_widget)
                drag.setMimeData(mime_data)
                drag.exec(Qt.CopyAction)
                return
    
    def custom_dragEnterEvent(event):
        """Tree로 드래그 진입 차단"""
        event.ignore()
    
    def custom_dragMoveEvent(event):
        """Tree 위에서 드래그 이동 차단"""
        event.ignore()
    
    def custom_dropEvent(event):
        """Tree로 드롭 차단 (내용 변경 방지)"""
        event.ignore()
    
    # 메서드 교체
    tree_widget.startDrag = custom_startDrag
    tree_widget.dragEnterEvent = custom_dragEnterEvent
    tree_widget.dragMoveEvent = custom_dragMoveEvent
    tree_widget.dropEvent = custom_dropEvent
    
    # Tree는 드롭 받지 않음
    tree_widget.setAcceptDrops(False)

class LoginWindow(QDialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : start login window")
        
        try:
            self.client_ip = requests.get("https://api.ipify.org?format=text").text

            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(("8.8.8.8", 80))
                self.local_ip = s.getsockname()[0]
        except (requests.RequestException, socket.error, OSError) as e:
            print_error(e)
            self.client_ip = "127.0.0.1"
            self.local_ip = "127.0.0.1"

        self.ui_login = Ui_login_windows()

        self.setWindowTitle("MS-AI")
        self.ui_login.setupUi(self)
        # self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.ui_login.login_bn.clicked.connect(self.check_login)
        # self.setGeometry(200, 200, 1280, 720)

        self.setup_event_filters()
        self.ai_sever_info_path = os.path.join(os.getcwd(), "ai_sever_info.json")

        # with open(self.ai_sever_info_path, "r", encoding="UTF-8") as f:
        #     self.ai_sever_info = json.load(f)
        self.ai_sever_info = load_crypography_json(self.ai_sever_info_path)

    def setup_event_filters(self):
        # 이벤트 필터 설치
        event_filters = [
            self.ui_login.id_input,
            self.ui_login.pw_input,
        ]
        for filter in event_filters:
            filter.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() in (QEvent.FocusIn, QEvent.FocusOut):
            color = "green" if event.type() == QEvent.FocusIn else "rgb(36, 39, 44)"
            if obj == self.ui_login.id_input:
                self.set_line_style(self.ui_login.id_line, color)
            elif obj == self.ui_login.pw_input:
                self.set_line_style(self.ui_login.pw_line, color)

        return super().eventFilter(obj, event)

    def set_line_style(self, line_widget, color):
        # 라인 스타일 변경
        line_widget.setStyleSheet(f"background-color: {color}")
        
    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Enter, Qt.Key_Return):  # Enter 키 또는 Return 키를 눌렀을 경우
            self.check_login()

    def check_login(self):
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : Try login")

            if self.ui_login.id_input.text() in self.ai_sever_info["USER"].keys() and \
                self.ui_login.pw_input.text() == self.ai_sever_info["USER"][self.ui_login.id_input.text()]:
                user_info = self.ui_login.id_input.text()
                self.handle_successful_login(user_info)
            else:
                self.create_fade_out_msg(msg="아이디와 비밀번호가 일치하지 않습니다.")
                return

        except Exception as e:
            print_error(e)

    def handle_successful_login(self, user_info):
        # 로그인 성공 처리
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : succese login")

        self.close()
        self.main_window = MainWindow(user_info=user_info, 
                                      ai_server_info_dict=self.ai_sever_info,
                                      client_ip = f"{self.client_ip}@{self.local_ip}")
        self.main_window.show()
        # self.create_fade_out_msg(msg="login")
    #     self.save_ai_server_info()

    # def save_ai_server_info(self):
    #     # AI 서버 정보 저장
    #     with open(self.ai_sever_info_path, "w", encoding="UTF-8") as f:
    #         self.ai_server_info["ai_server_ip"] = self.ui_login.ai_server_ip_input.text()
    #         self.ai_server_info["ai_server_port"] = self.ui_login.ai_server_port_input.text()
    #         f.write(json.dumps(self.ai_server_info))

    def create_fade_out_msg(self, std_window=None, msg="None"):
        try:
            if not hasattr(self, 'fadeout_window') or not self.fadeout_window.isVisible():
                # std_window가 제공되면 해당 윈도우를 parent로 사용, 아니면 self 사용
                parent_window = std_window if std_window is not None else self
                self.fadeout_window = FadeOutWindow(parent_window, msg)
                # 항상 최상위에 표시되도록 설정
                self.fadeout_window.setWindowFlags(self.fadeout_window.windowFlags() | Qt.WindowStaysOnTopHint)

                if std_window is None:
                    main_window_rect = self.geometry()
                    fadeout_window_rect = self.fadeout_window.geometry()
                    self.fadeout_window.move(
                        main_window_rect.left() + (main_window_rect.width() - fadeout_window_rect.width()) // 2,
                        main_window_rect.top() + (main_window_rect.height() - fadeout_window_rect.height()) * 4 // 5
                    )
                else:
                    main_window_rect = std_window.geometry()
                    fadeout_window_rect = self.fadeout_window.geometry()
                    self.fadeout_window.move(
                        main_window_rect.left() + (main_window_rect.width() - fadeout_window_rect.width()) // 2,
                        main_window_rect.top() + (main_window_rect.height() - fadeout_window_rect.height()) * 4 // 5
                    )

            self.fadeout_window.show()
            self.fadeout_window.raise_()          # 윈도우를 최상위로 올림
            
            # 포커스를 원래 창으로 돌려줌 (단축키 유지를 위해)
            if std_window is not None:
                std_window.activateWindow()
                std_window.setFocus()
            else:
                self.activateWindow()
                self.setFocus()

        except Exception as e:
            print_error(e)

class MainWindow(QMainWindow):
    def __init__(self, user_info, ai_server_info_dict, client_ip):
        super(MainWindow, self).__init__()


        self.ai_server_info_dict = ai_server_info_dict
        self.client_ip = client_ip
        self.popup_alert_msg_list = []


        self.ui_main = Ui_MainWindow()
        self.setWindowTitle("MS-AI")
        self.ui_main.setupUi(self)

        self.ui_main.stackedWidget.setCurrentIndex(0)

        self.notification_manager = NotificationManager(on_click_callback=self.on_notification_clicked_handler)
        
        self.setup_init_GUI()
        self.setup_slot_connect()
        self.setup_event_filters()

        # 알람 체크 스레드 시작
        self.check_alarm_thread = CheckAlarmThread(self.ai_server_info_dict)
        self.check_alarm_thread.new_alarm.connect(self.notify)
        self.check_alarm_thread.start()

        self.user_info = user_info
        if self.user_info == "admin":
            self.admin_flag = True
        else:
            self.admin_flag = False
            self.ui_main.admin_bnt.hide()
            self.ui_main.tab_partion_4.hide()

    def shutdown(self):
        # QApplication.instance().quit()
        self.stop_camera_page_worker()
        if self.camera_connect_timer is not None :
            self.camera_connect_timer.stop()
            del self.camera_connect_timer
            self.camera_connect_timer = None

        # 카메라 이미지 업데이트 스레드 중지
        if self.update_camera_img_thread is not None:
            self.update_camera_img_thread.stop()
            self.update_camera_img_thread.wait()
            self.update_camera_img_thread = None

        # if self.ai_server_event_alarm_connect_timer is not None :
        #     self.ai_server_event_alarm_connect_timer.stop()
        #     del self.ai_server_event_alarm_connect_timer

        #     self.ai_server_event_alarm_connect_timer = None

        self.hide()
        # self.tray_icon.showMessage("동작 중", "프로그램이 트레이에 최소화되었습니다.")

    def quit_application(self):
        """프로그램 완전 종료 (트레이 메뉴에서 종료 클릭 시)"""
        # 모든 알림 닫기
        if hasattr(self, 'notification_manager') and self.notification_manager:
            self.notification_manager.close_all()
        
        # 리소스 정리
        self.shutdown()
        
        # 알람 체크 스레드 중지
        if hasattr(self, 'check_alarm_thread') and self.check_alarm_thread:
            self.check_alarm_thread.stop()
            self.check_alarm_thread.wait()
        
        # 트레이 아이콘 숨기기
        if hasattr(self, 'tray_icon') and self.tray_icon:
            self.tray_icon.hide()
        
        # 애플리케이션 종료
        QApplication.instance().quit()

    def closeEvent(self, event):
        """윈도우 닫기 버튼 클릭 시 트레이로 최소화"""
        event.ignore()  # 기본 닫기 동작 무시
        self.shutdown()  # 트레이로 최소화

    def notify(self, title, message, camera_name=None, alarm_time=None, ai_type=None, ai_server_ip=None, ai_server_port=None):
        global FIRST_NOTICE
        
        """커스텀 알림 표시"""
        # 최근 알림 정보 저장
        self.last_notification_info = {
            "camera_name": camera_name,
            "alarm_time": alarm_time,
            "ai_server_ip" : ai_server_ip,
            "ai_server_port" : ai_server_port
        }
        # 커스텀 알림 매니저를 통해 알림 표시
        notification_data = {
            "camera_name": camera_name,
            "alarm_time": alarm_time,
            "ai_server_ip" : ai_server_ip,
            "ai_server_port" : ai_server_port
        }

        if self.ai_server_info_dict["SETTING"]["notice"]["active"]:
            duration = self.ai_server_info_dict["SETTING"]["notice"]["duration"]
            
            # 커스텀 알림은 항상 표시
            self.notification_manager.show(title, message, notification_data, duration=NOTICE_DURATION[duration])
            
            # 윈도우가 숨겨진 상태(트레이)일 때는 추가로 시스템 트레이 알림도 표시
            # if not self.isVisible():
            #     self.tray_icon.showMessage(
            #         title, 
            #         message.replace('\n(클릭하여 자세히 보기)', ''),  # 시스템 알림용 메시지 정리
            #         QSystemTrayIcon.Information,
            #         NOTICE_DURATION[duration] if NOTICE_DURATION[duration] != -1 else 10000
            #     )


        if self.ai_server_info_dict["SETTING"]["sms"]["active"]:
            #솔라피 API를 이용한 sms 알림 전송
            for phone_num, alarm_type_dict in self.ai_server_info_dict["SETTING"]["sms"]["user"].items():
                if alarm_type_dict[Kor2eng(ai_type)]:
                    current_time = alarm_time

                    message_service = SolapiMessageService(
                        api_key=os.environ.get("SOLAPI_API_KEY", ""),
                        api_secret=os.environ.get("SOLAPI_API_SECRET", "")
                    )

                    kakao_option = KakaoOption(
                        pf_id=os.environ.get("SOLAPI_KAKAO_PF_ID", ""),
                        template_id=os.environ.get("SOLAPI_KAKAO_TEMPLATE_ID", ""),
                        variables={
                          "#{detect_type}": str(ai_type),
                          "#{camare_name}": str(camera_name),
                          "#{current_time}": str(current_time)
                        }
                    )
                    message = RequestMessage(
                        from_=os.environ.get("SOLAPI_SENDER_NUMBER", ""),
                        to=phone_num,
                        kakao_options=kakao_option,
                    )

                    try:
                        response = message_service.send(message)
                        print(f"sms 알림 전송 성공 {phone_num} {current_time} {ai_type}")
                    except Exception as e:
                        print(f"sms 알림 전송 실패 {phone_num} {current_time} {ai_type}")

    def setup_init_GUI(self):
        # 어두운 레이어 위젯 생성
        self.dark_layer = QWidget(self)
        self.dark_layer.setGeometry(QRect(0,0,9999,9999))
        self.dark_layer.setStyleSheet("background-color: rgba(0, 0, 0, 178);")  # 70% 투명도
        self.dark_layer.hide()  # 기본적으로 숨김

        # 트레이 아이콘 설정 (Qt Resource 경로 사용 - PyInstaller 빌드 호환)
        self.tray_icon = QSystemTrayIcon(QIcon(":/ui/ui/images/icon2.ico"), self)
        self.tray_icon.show()
        tray_menu = QMenu()
        restore_action = QAction("열기", self)
        restore_action.triggered.connect(self.open_main_window_tray)
        tray_menu.addAction(restore_action)
        quit_action = QAction("종료", self)
        quit_action.triggered.connect(self.quit_application)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        self.camera_page_worker = None
        self.camera_connect_timer = None
        self.ai_server_event_alarm_connect_timer = None
        self.update_camera_img_thread = None


        # 알림 메시지 클릭 시 검색 창 열기 (최근 알림 정보 사용)
        # self.tray_icon.messageClicked.connect(self.on_notification_clicked)

        self.ui_main.shutdown_bnt.setStyleSheet("""background-color: rgb(255, 49, 38);
                                            color: rgb(255, 255, 255);
                                            border-radius: 12px;
                                            """)
        self.ui_main.shutdown_bnt.setText("종료")

        #서버 테이블, 리스트 초기화
        self.ui_main.nvr_list_table.setRowCount(0)
        self.ui_main.ai_server_table.setRowCount(0)
        self.ui_main.ai_server_info_table.setRowCount(0)

        self.ui_main.nvr_list_table.setColumnWidth(0, 40)
        self.ui_main.nvr_list_table.setColumnWidth(1, 120)

        self.ui_main.ai_server_table.setColumnWidth(0, 40)
        self.ui_main.ai_server_table.setColumnWidth(1, 120)

        # ai_server_info_table에 드래그&드롭 기능 추가
        self.make_table_draggable(self.ui_main.ai_server_info_table)
        
        # ai_server_info_table에 Shift 키 범위 선택 기능 추가
        enable_shift_selection(self.ui_main.ai_server_info_table)
        
        self.ui_main.ai_server_info_table.setColumnWidth(0, 40)
        self.ui_main.ai_server_info_table.setColumnWidth(1, 160)
        self.ui_main.ai_server_info_table.setColumnWidth(2, 200)
        self.ui_main.ai_server_info_table.setColumnWidth(3, 120)

        #NVR Tree 초기화
        self.ui_main.nvr_server_tree_list.clear()
        self.ui_main.nvr_server_tree_list.setDragEnabled(True)
        self.ui_main.nvr_server_tree_list.setDragDropMode(QAbstractItemView.DragDrop)
        self.ui_main.nvr_server_tree_list.setDefaultDropAction(Qt.DropAction.CopyAction)
        self.ui_main.nvr_server_tree_list.setSelectionMode(QAbstractItemView.ExtendedSelection)

        #NVR 서버 테이블 채우기
        for nvr_ip, nvr_info in self.ai_server_info_dict["NVR"].items():
            self.add_nvr_info_to_gui(nvr_ip, nvr_info)

        # Tree 위젯에 커스텀 드래그 기능 추가
        make_tree_draggable_with_data(self.ui_main.nvr_server_tree_list, self.ai_server_info_dict)

        # NVR 검색 입력창 초기화
        self.nvr_search_first_focus = True
        
        # AI 서버 카메라 검색 입력창 초기화
        self.ai_server_camera_search_first_focus = True

        #지능형 서버 목록 채우기
        for ai_server_ip, ai_server_info in self.ai_server_info_dict["AI_SERVER"].items():
            self.add_ai_server_info_to_table(ai_server_ip, ai_server_info)

    def open_main_window_tray(self):
        """메인 창 열기"""
        self.showNormal()

    def open_main_window_tray_notify(self, camera_name=None, ai_server_ip=None, ai_server_port=None):
        """메인 창 열기"""
        self.showNormal()
        if camera_name is not None:
            self.stop_camera_page_worker()

            self.ai_server_ip = ai_server_ip
            self.ai_server_port = ai_server_port

            self.switch_ai_viewer(self.ai_server_ip, self.ai_server_port)
            self.ui_main.camera_page_name_box.setCurrentText(camera_name)

            self.switch_main_display_to_camera(tray_notify = True)


        # self.switch_main_display_to_camera(tray_notify=True)

    def on_notification_clicked_handler(self, notification_data):
        """커스텀 알림 클릭 시 호출되는 핸들러"""
        camera_name = notification_data.get("camera_name")
        alarm_time = notification_data.get("alarm_time")
        ai_server_ip = notification_data.get("ai_server_ip")
        ai_server_port = notification_data.get("ai_server_port")
        print(f"클릭된 알림 - 카메라: {camera_name}, 시간: {alarm_time}")
        # 검색 창 열기
        self.open_main_window_tray_notify(camera_name = camera_name, ai_server_ip=ai_server_ip, ai_server_port=ai_server_port)

    # def on_notification_clicked(self):
    #     """트레이 알림 메시지 클릭 시 호출되는 함수"""
    #     # 최근 알림 정보가 있으면 검색 창 열기
    #     if self.last_notification_info:
    #         camera_name = self.last_notification_info.get("camera_name")
    #         alarm_time = self.last_notification_info.get("alarm_time")
    #         ai_server_ip = self.last_notification_info.get("ai_server_ip")
    #         ai_server_port = self.last_notification_info.get("ai_server_port")
    #         print(f"클릭된 알림 기능 2 - 카메라: {camera_name}, 시간: {alarm_time}, {ai_server_ip}, {ai_server_port}")
    #         self.open_main_window_tray_notify(camera_name = camera_name, ai_server_ip=ai_server_ip, ai_server_port=ai_server_port)
    #     else:
    #         self.open_main_window_tray_notify()

    def make_table_draggable(self, table_widget, ai_server_info_dict=None, ):
        """테이블 위젯에 드래그&드롭 기능 추가
        - Tree에서 드롭 받아 행 추가
        - 테이블 외부로 드롭 시 행 삭제
        """
        table_widget.dragged_rows = []
        table_widget.is_dragging_from_self = False
        table_widget.drop_handled = False  # dropEvent가 처리했는지 플래그

        # 기존 메서드 백업
        original_startDrag = table_widget.startDrag
        original_dropEvent = table_widget.dropEvent
        original_dragEnterEvent = table_widget.dragEnterEvent
        original_dragMoveEvent = table_widget.dragMoveEvent
        
        def custom_startDrag(supportedActions):
            """테이블에서 드래그 시작"""
            table_widget.is_dragging_from_self = True
            table_widget.drop_handled = False
            table_widget.dragged_rows = sorted(set(index.row() for index in table_widget.selectedIndexes()), reverse=True)
            
            # 드래그 실행
            original_startDrag(supportedActions)

            ai_server_ip = self.ui_main.ai_server_ip_input.text()
            ai_server_port = self.ui_main.ai_server_port_input.text()

            # 지능형 알고리즘 진행 여부 확인
            camera_info_dict = load_info(host=ai_server_ip, port=ai_server_port, file_name="camera_info")
            if table_widget.is_dragging_from_self and not table_widget.drop_handled:
                if table_widget.dragged_rows:
                    for row in table_widget.dragged_rows:
                        if row < table_widget.rowCount():
                            camera_name = table_widget.item(row, 1).text()
                            nvr_ip = table_widget.item(row, 4).text()

                            if camera_info_dict[nvr_ip][camera_name]["ai"]:
                                self.create_fade_out_msg(msg=f"{camera_name} : 지능형 알고리즘 진행 중입니다.")
                                return
            
            # 드래그 완료 후 처리
            # dropEvent가 처리하지 않았으면 (외부로 드롭) 행 삭제
            if table_widget.is_dragging_from_self and not table_widget.drop_handled:
                if table_widget.dragged_rows:
                    for row in table_widget.dragged_rows:
                        if row < table_widget.rowCount():
                            camera_name = table_widget.item(row, 1).text()
                            nvr_ip = table_widget.item(row, 4).text()



                            if camera_name in self.ai_server_camera_info_dict[nvr_ip].keys():
                                del self.ai_server_camera_info_dict[nvr_ip][camera_name]
                                if self.ai_server_camera_info_dict[nvr_ip] == {}:
                                    del self.ai_server_camera_info_dict[nvr_ip]


                            table_widget.removeRow(row)


                    camera_post = f'http://{ai_server_ip}:{ai_server_port}/save-camera-info'
                    r = requests.put(camera_post, json={"msg" : self.ai_server_camera_info_dict}, timeout=1)

            # 정리
            table_widget.dragged_rows = []
            table_widget.is_dragging_from_self = False
            table_widget.drop_handled = False

            ai_server_ip = self.ui_main.ai_server_ip_input.text()

            self.load_ai_server_info_to_table()
        
        def custom_dragEnterEvent(event):
            """드래그 진입 시"""
            mime_data = event.mimeData()
            if mime_data.hasText():
                event.acceptProposedAction()
            else:
                original_dragEnterEvent(event)
        
        def custom_dragMoveEvent(event):
            """드래그 이동 시"""
            mime_data = event.mimeData()
            if mime_data.hasText():
                event.acceptProposedAction()
            else:
                original_dragMoveEvent(event)
        
        def custom_dropEvent(event):
            """드롭 이벤트 처리"""
            drop_pos = event.position().toPoint() if hasattr(event.position(), 'toPoint') else event.pos()
            is_drop_inside = table_widget.indexAt(drop_pos).isValid()
            mime_data = event.mimeData()
            
            # Tree에서 드래그된 경우 (JSON 데이터 포함)
            if mime_data.hasText() and not table_widget.is_dragging_from_self:
                try:
                    import json
                    dropped_data = json.loads(mime_data.text())
                    
                    if isinstance(dropped_data, list) and len(dropped_data) > 0:
                        if 'camera_ip' in dropped_data[0] or 'camera_name' in dropped_data[0]:

                            # Tree에서 온 카메라 데이터 - 테이블에 추가
                            for item_data in dropped_data:
                                nvr_ip = item_data.get('nvr_ip', '')
                                camera_name = item_data.get('camera_name', '')
                                
                                # 중복 체크: nvr_ip와 camera_name 모두 확인
                                if nvr_ip in self.ai_server_camera_info_dict and camera_name in self.ai_server_camera_info_dict[nvr_ip].keys():
                                    self.create_fade_out_msg(msg=f"{camera_name} : 이미 등록된 카메라입니다.")
                                    continue

                                row_position = table_widget.rowCount()
                                table_widget.setRowCount(row_position + 1)
                                
                                # 번호
                                item_num = QTableWidgetItem(str(row_position + 1))
                                item_num.setTextAlignment(Qt.AlignCenter)
                                table_widget.setItem(row_position, 0, item_num)
                                
                                # 카메라 이름
                                item_name = QTableWidgetItem(item_data.get('camera_name', ''))
                                item_name.setTextAlignment(Qt.AlignCenter)
                                table_widget.setItem(row_position, 1, item_name)
                                
                                # 카메라 IP
                                item_ip = QTableWidgetItem(item_data.get('camera_ip', ''))
                                item_ip.setTextAlignment(Qt.AlignCenter)
                                table_widget.setItem(row_position, 2, item_ip)
                                
                                # NVR 이름
                                item_nvr_name = QTableWidgetItem(item_data.get('nvr_name', ''))
                                item_nvr_name.setTextAlignment(Qt.AlignCenter)
                                table_widget.setItem(row_position, 3, item_nvr_name)
                                
                                # NVR IP
                                item_nvr_ip = QTableWidgetItem(nvr_ip)
                                item_nvr_ip.setTextAlignment(Qt.AlignCenter)
                                table_widget.setItem(row_position, 4, item_nvr_ip)

                                # ai_server_camera_info_dict에 카메라 정보 추가
                                camera_ip = item_data.get('camera_ip', '')
                                camera_id = item_data.get('camera_id', '')
                                
                                if nvr_ip not in self.ai_server_camera_info_dict.keys():
                                    self.ai_server_camera_info_dict[nvr_ip] = {}

                                self.ai_server_camera_info_dict[nvr_ip][camera_name] = load_init_camera_dict(camera_ip, camera_id)
                                
                            event.acceptProposedAction()
                            table_widget.drop_handled = True

                            ai_server_ip = self.ui_main.ai_server_ip_input.text()
                            ai_server_port = self.ui_main.ai_server_port_input.text()

                            camera_post = f'http://{ai_server_ip}:{ai_server_port}/save-camera-info'
                            r = requests.put(camera_post, json={"msg" : self.ai_server_camera_info_dict}, timeout=1)

                    self.load_ai_server_info_to_table()

                except Exception as e:
                    print_error(e)
                    self.create_fade_out_msg(msg="AI 서버 정보를 확인해주세요.")
                    return
            
            # 자체 테이블에서 드래그된 경우
            if table_widget.is_dragging_from_self:
                table_widget.drop_handled = True  # dropEvent가 처리됨을 표시
                
                if is_drop_inside:
                    # 테이블 내부로 드롭 - 무시 (변경 방지)
                    event.ignore()
                else:
                    # 이 경우는 거의 발생하지 않지만, 혹시 모르니 처리
                    event.accept()
            else:
                event.accept()
        
        # 메서드 교체
        table_widget.startDrag = custom_startDrag
        table_widget.dragEnterEvent = custom_dragEnterEvent
        table_widget.dragMoveEvent = custom_dragMoveEvent
        table_widget.dropEvent = custom_dropEvent
        
        # 드래그 설정
        table_widget.setDragEnabled(True)
        table_widget.setAcceptDrops(True)
        table_widget.setDragDropMode(QAbstractItemView.DragDrop)
        table_widget.setDefaultDropAction(Qt.DropAction.MoveAction)
        table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

    def add_ai_server_info_to_table(self, ai_server_ip, ai_server_info):
        self.ui_main.ai_server_table.setRowCount(self.ui_main.ai_server_table.rowCount() + 1)
        item = QTableWidgetItem(str(self.ui_main.ai_server_table.rowCount()))
        item.setTextAlignment(Qt.AlignCenter)
        item2 = QTableWidgetItem(ai_server_info["name"])
        item2.setTextAlignment(Qt.AlignCenter)
        item3 = QTableWidgetItem(ai_server_ip)
        item3.setTextAlignment(Qt.AlignCenter)
        self.ui_main.ai_server_table.setItem(self.ui_main.ai_server_table.rowCount() - 1, 0, item)
        self.ui_main.ai_server_table.setItem(self.ui_main.ai_server_table.rowCount() - 1, 1, item2)
        self.ui_main.ai_server_table.setItem(self.ui_main.ai_server_table.rowCount() - 1, 2, item3)

    def clicked_switch_ai_viewer(self):
        self.switch_ai_viewer()
        self.switch_main_display_to_camera(tray_notify = False)
        self.connect_camera_page_camera()

    def setup_slot_connect(self):
        self.ui_main.shutdown_bnt.clicked.connect(self.back_window)

        self.ui_main.nvr_add_bnt.clicked.connect(self.add_nvr_server)
        self.ui_main.nvr_del_bnt.clicked.connect(self.del_nvr_server)
        self.ui_main.nvr_save_bnt.clicked.connect(self.save_nvr_server)
        self.ui_main.nvr_search_input.textChanged.connect(self.filter_nvr_tree)

        self.ui_main.ai_server_save_bnt.clicked.connect(self.save_ai_server)
        self.ui_main.ai_server_add_bnt.clicked.connect(self.add_ai_server)
        self.ui_main.ai_server_del_bnt.clicked.connect(self.del_ai_server)
        self.ui_main.ai_server_camera_search_input.textChanged.connect(self.filter_ai_server_camera_table)

        self.ui_main.nvr_list_table.itemClicked.connect(self.load_nvr_server_info)
        self.ui_main.ai_server_table.itemClicked.connect(self.load_ai_server_info_to_table)
        # self.ui_main.ai_server_table.itemDoubleClicked.connect(self.switch_ai_viewer)
        self.ui_main.ai_server_table.itemDoubleClicked.connect(self.clicked_switch_ai_viewer)


        self.ui_main.camera_bnt.clicked.connect(self.switch_main_display_to_camera)
        self.ui_main.setting_bnt.clicked.connect(self.switch_main_display_to_setting)
        # self.ui_main.admin_bnt.clicked.connect(self.switch_main_display_to_admin)
        self.ui_main.admin_bnt.clicked.connect(self.switch_main_display_to_admin_2)


        self.ui_main.server_list_setting_bnt.clicked.connect(lambda click, instance = self : open_server_setting_window(click, instance))

        ##ai server viewer 카메라 페이지 설정
        self.setup_camera_viewer()
        self.ui_main.camera_page_name_box.currentTextChanged.connect(lambda: (self.connect_camera_page_camera(), self.set_camera_page_viewer()))
        self.ui_main.camera_page_detect_add_bnt.clicked.connect(self.camera_page_add_detect_type)
        self.ui_main.camera_page_detect_area_del_bnt.clicked.connect(self.camera_page_del_detect_area)
        self.ui_main.camera_page_detect_area_table.itemClicked.connect(self.camera_page_update_camera_page_viewer_roi)
        self.ui_main.camera_page_object_setting_bnt.clicked.connect(lambda click, instance = self : open_object_setting_window(click, instance))

        self.ui_main.camera_page_ai_bnt.clicked.connect(lambda click, instance = self : open_ai_setting_window(click, instance))
        self.ui_main.camera_list_table.itemDoubleClicked.connect(self.double_click_camera_list_fn)

        #ai server viewer 설정 메뉴 버튼
        self.ui_main.setting_ai_setting_save_bnt.clicked.connect(self.save_ai_setting_info)
        self.ui_main.setting_detect_bbox_active_bnt.clicked.connect(self.change_setting_info)
        self.ui_main.setting_detect_label_active_bnt.clicked.connect(self.change_setting_info)
        self.ui_main.setting_detect_roi_active_bnt.clicked.connect(self.change_setting_info)

        #ai server viewer admin 메뉴 버튼
        self.ui_main.admin_page_bnt.clicked.connect(self.login_admin_page)
        self.ui_main.admin_license_bnt.clicked.connect(lambda : (self.ui_main.stackedWidget_3.setCurrentIndex(0), self.reset_admin_license_list()))
        self.ui_main.admin_fn_permission_bnt.clicked.connect(lambda : (self.ui_main.stackedWidget_3.setCurrentIndex(1), self.reset_admin_fn_list()))
        self.ui_main.license_add_bnt.clicked.connect(self.move_active_license_list)
        self.ui_main.license_remove_bnt.clicked.connect(self.move_non_license_camera_list)
        self.ui_main.admin_self_labeling_fn_active_bnt.clicked.connect(self.change_self_labeling_fn)
        self.ui_main.admin_fn_save_bnt.clicked.connect(self.save_admin_info)
        self.ui_main.license_save_bnt.clicked.connect(self.save_admin_info)
        self.ui_main.admin_pw_input.returnPressed.connect(self.login_admin_page)

        #ai server viewer의 우측 상단 버튼 활성화
        self.ui_main.search_memu_bnt.clicked.connect(lambda click, instance = self : open_search_window(click, instance))
        self.ui_main.camera_schedule_bnt.clicked.connect(lambda click, instance = self : open_schedule_window(click, instance))
        self.ui_main.labeling_bnt.clicked.connect(lambda click, instance = self : open_labeling_window(click, instance))

        # self.ui_main.shutdown_bnt.clicked.connect(self.shutdown)

    def login_admin_page(self):
        try:
            data = {"msg" : str(self.ui_main.admin_pw_input.text())}
            url = f'http://{self.ai_server_ip}:{self.ai_server_port}/login-admin-page'
            receive_data = requests.post(url, json=data, timeout=1).json()

            if receive_data["msg"] == True:
                self.switch_main_display_to_admin_2()
            else:
                self.create_fade_out_msg(msg="Invalid PW")

        except Exception as e:
            print_error(e)

    def switch_main_display_to_admin_2(self):
        self.set_button_style('admin')
        self.ui_main.stackedWidget_2.setCurrentIndex(3)
        self.ui_main.stackedWidget_3.setCurrentIndex(0)

        self.admin_info_temp = load_info(host=self.ai_server_ip, port=self.ai_server_port, file_name="admin_info")

        self.reset_admin_license_list()
        self.reset_admin_fn_list()

    def reset_admin_license_list(self):
        try:
            self.ui_main.non_active_license_list.clear()
            self.ui_main.active_license_list.clear()

            # 카메라 번호에 대한 체크박스를 생성하고 레이아웃에 추가
            for detect_type, active_flag in self.admin_info_temp["LICENSE"]["detect_type"].items():
                item = QListWidgetItem(Eng2kor(detect_type))
                item.setTextAlignment(Qt.AlignCenter)

                self.ui_main.active_license_list.addItem(item) if active_flag == 1 else self.ui_main.non_active_license_list.addItem(item)
        
            self.ui_main.license_camera_allow_num_input.setText(str(self.admin_info_temp["LICENSE"]["allow_camera_num"]))

        except Exception as e:
            print_error(e)

    def reset_admin_fn_list(self):
        try:
            self.ui_main.admin_self_labeling_fn_active_bnt.setChecked(self.admin_info_temp["FN_PERMISSION"]["self_labeling_active"] == 1)
        except Exception as e:
            print_error(e)

    def move_active_license_list(self):
        try:
            selected_items = self.ui_main.non_active_license_list.selectedItems()
            selected_texts = [item.text() for item in selected_items]

            for detect_type in selected_texts:
                self.admin_info_temp["LICENSE"]["detect_type"][Kor2eng(detect_type)] = 1

            self.reset_admin_license_list()
        except Exception as e:
            print_error(e)

    def move_non_license_camera_list(self):
        try:
            selected_items = self.ui_main.active_license_list.selectedItems()
            selected_texts = [item.text() for item in selected_items]

            for detect_type in selected_texts:
                self.admin_info_temp["LICENSE"]["detect_type"][Kor2eng(detect_type)] = 0

            self.reset_admin_license_list()
        except Exception as e:
            print_error(e)

    def save_admin_info(self):
        try:
            # 텍스트를 정수로 변환하여 저장
            self.admin_info_temp["LICENSE"]["allow_camera_num"] = int(self.ui_main.license_camera_allow_num_input.text())
            
            save_info(host=self.ai_server_ip, port=self.ai_server_port, file_name="admin_info", info=self.admin_info_temp)
            self.create_fade_out_msg(msg="save admin info")

        except Exception as e:
            print_error(e)

    def change_self_labeling_fn(self):
        # self_labeling_active 토글
        self.admin_info_temp["FN_PERMISSION"]["self_labeling_active"] = 1 if self.admin_info_temp["FN_PERMISSION"]["self_labeling_active"] == 0 else 0
    

    def double_click_camera_list_fn(self, item):
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : change_camera from table double click")
            
            # 더블클릭된 행에서 카메라 이름 가져오기
            row = item.row()
            camera_name_item = self.ui_main.camera_list_table.item(row, 1)  # 2번 컬럼이 카메라 이름
            
            if camera_name_item:
                camera_name = camera_name_item.text()

                # 카메라 페이지로 전환
                self.switch_main_display_to_camera()
                self.set_button_style('camera')
                self.ui_main.stackedWidget_2.setCurrentIndex(0)
                
                # 카메라 선택 변경 (이것이 자동으로 connect_camera_page_camera()와 set_camera_page_viewer()를 호출함)
                index = self.ui_main.camera_page_name_box.findText(camera_name)
                if index >= 0:
                    self.ui_main.camera_page_name_box.setCurrentIndex(index)
                
        except Exception as e:
            print_error(e)


    def save_ai_setting_info(self):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : AI Setting Save")

        weight_name = self.ui_main.setting_setting_ai_weight_box.currentText()
        self.setting_info_temp["AI"]["weight"] = weight_name

        if self.ui_main.setting_self_training_auto_labeling_bnt.isChecked():
            self.setting_info_temp["AI"]["auto_label"] = 1
        else:
            self.setting_info_temp["AI"]["auto_label"] = 0

        self.setting_info_temp["AI"]["zero_shot"] = 1 if self.ui_main.setting_self_training_zeroshot_bnt.isChecked() else 0

        self.setting_info_temp["AI"]["auto_label_start_time"] = self.ui_main.setting_auto_label_time_start_box.currentText()
        self.setting_info_temp["AI"]["auto_label_end_time"] = self.ui_main.setting_auto_label_time_end_box.currentText()

        save_info(host=self.ai_server_ip, port=self.ai_server_port, file_name="setting_info", info=self.setting_info_temp)
        self.create_fade_out_msg(msg="지능형 엔진 설정이 저장되었습니다")

    def change_setting_info(self):
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : change_setting_info")
            self.setting_info_temp = load_info(host=self.ai_server_ip, port=self.ai_server_port, file_name="setting_info")

            self.setting_info_temp["DISPLAY_PLOT"]["bbox"] = int(self.ui_main.setting_detect_bbox_active_bnt.isChecked())
            self.setting_info_temp["DISPLAY_PLOT"]["label"] = int(self.ui_main.setting_detect_label_active_bnt.isChecked())
            self.setting_info_temp["DISPLAY_PLOT"]["roi"] = int(self.ui_main.setting_detect_roi_active_bnt.isChecked())

            self.camera_page_worker.plot_bbox = self.setting_info_temp["DISPLAY_PLOT"]["bbox"] == 1
            self.camera_page_worker.plot_label = self.setting_info_temp["DISPLAY_PLOT"]["label"] == 1
            self.camera_page_worker.plot_roi = self.setting_info_temp["DISPLAY_PLOT"]["roi"] == 1

            self.create_fade_out_msg(msg="설정이 저장되었습니다")
            save_info(host=self.ai_server_ip, port=self.ai_server_port, file_name="setting_info", info=self.setting_info_temp)

        except Exception as e:
            print_error(e)


    def back_window(self):
        if self.ui_main.stackedWidget.currentIndex() == 1:
            self.ui_main.stackedWidget.setCurrentIndex(0)
            self.ui_main.shutdown_bnt.setStyleSheet("""background-color: rgb(255, 49, 38);
                                                        color: rgb(255, 255, 255);
                                                        border-radius: 12px;
                                                        """)
            self.ui_main.shutdown_bnt.setText("종료")

            self.stop_camera_page_worker()

            if self.camera_connect_timer is not None :
                self.camera_connect_timer.stop()
                del self.camera_connect_timer

                self.camera_connect_timer = None
        else:
            self.shutdown()
            
    def switch_ai_viewer(self, ai_server_ip=None, ai_server_port=None):
        self.stop_camera_page_worker()
        self.ui_main.camera_page_name_box.currentTextChanged.disconnect()

        if self.admin_flag == False:
            self.ui_main.labeling_bnt.hide()
            self.ui_main.setting_self_training_auto_labeling_label.hide()
            self.ui_main.setting_self_training_auto_labeling_bnt.hide()
            self.ui_main.setting_self_training_zeroshot_label.hide()
            self.ui_main.setting_self_training_zeroshot_bnt.hide()
            self.ui_main.setting_page_email_info_label_11.hide()
            self.ui_main.setting_page_email_info_label_10.hide()
            self.ui_main.setting_page_email_info_label_9.hide()


        if ai_server_ip is not None and ai_server_port is not None:
            self.ai_server_ip = ai_server_ip
            self.ai_server_port = ai_server_port

        else:
            self.ai_server_ip = self.ui_main.ai_server_ip_input.text()
            self.ai_server_port = self.ui_main.ai_server_port_input.text()

            save_info(host=self.ai_server_ip, port=self.ai_server_port, file_name="ai_server_info", info=self.ai_server_info_dict)

        self.ai_server_camera_info_dict = load_info(host=self.ai_server_ip, port=self.ai_server_port, file_name="camera_info")

        if len(self.ai_server_camera_info_dict) == 0:
            self.create_fade_out_msg(msg="지능형 서버에 카메라 정보가 없습니다.\n카메라를 등록해 주세요")
            return False

        self.ui_main.camera_list_table.setRowCount(0)
        self.ui_main.camera_page_name_box.clear()

        self.ui_main.shutdown_bnt.setStyleSheet("""background-color: qlineargradient(
                                                    spread:pad,
                                                    x1:0, y1:0, x2:0, y2:1,
                                                    stop:0.05 rgba(46, 49, 54, 255),
                                                    stop:0.30 rgba(37, 40, 44, 255)
                                                    );
                                                    color: rgb(255, 255, 255);
                                                    border-radius: 12px;
                                                    """)
        self.ui_main.shutdown_bnt.setText("이전")
        self.ui_main.stackedWidget.setCurrentIndex(1)

        self.ui_main.camera_list_table.setColumnWidth(0, 20)
        self.ui_main.camera_list_table.setColumnWidth(1, 100)
        self.ui_main.camera_list_table.setColumnWidth(2, 120)

        self.admin_info_temp = load_info(host=self.ai_server_ip,port=self.ai_server_port,file_name="admin_info")
        self.setting_info_temp = load_info(host=self.ai_server_ip, port=self.ai_server_port, file_name="setting_info")

        self.camera_img_temp = {} #카메라 이미지 저장 dict
        
        # 지능형 프로그램 구동 상태 아이콘 설정
        self.ui_main.camera_page_ai_active_label.hide()
        self.ui_main.camera_page_ai_active_icon.hide()

        #초기 설정 탭에 설정 on/off 상태 적용
        self.update_setting()

        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : camera list setup")
        self.camera_view_list = {}

        for nvr_ip, camera_info_dict in self.ai_server_camera_info_dict.items():
            for camera_name, camera_info in camera_info_dict.items():
                row_position = self.ui_main.camera_list_table.rowCount()
                self.ui_main.camera_list_table.insertRow(row_position)

                # 새 행에 데이터 채우기
                label = QLabel()
                pixmap = QPixmap(":/ui/ui/images/ico_video_off.svg").scaled(24, 24, Qt.KeepAspectRatio)

                label.setPixmap(pixmap)
                label.setAlignment(Qt.AlignCenter)
                self.ui_main.camera_list_table.setCellWidget(row_position, 0, label)

                text = QTableWidgetItem(str(camera_name))
                text.setTextAlignment(Qt.AlignCenter)
                text.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
                self.ui_main.camera_list_table.setItem(row_position, 1, text)

                text = QTableWidgetItem(str(camera_info["camera_ip"]))
                text.setTextAlignment(Qt.AlignCenter)
                text.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
                self.ui_main.camera_list_table.setItem(row_position, 2, text)

                text = QTableWidgetItem(self.ai_server_info_dict["NVR"][nvr_ip]["name"])
                text.setTextAlignment(Qt.AlignCenter)
                text.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
                self.ui_main.camera_list_table.setItem(row_position, 3, text)

                self.ui_main.camera_page_name_box.addItems([camera_name])

        self.update_camera_img_temp()
        self.start_camera_connect_status_timer()#NVR 카메라 연결상태 확인

        # self.switch_main_display_to_camera(tray_notify = tray_notify)

        self.ui_main.camera_page_name_box.currentTextChanged.connect(lambda: (self.connect_camera_page_camera(), self.set_camera_page_viewer()))


    def camera_page_add_detect_area_point(self, point): #마우스 클릭으로 생성된 포인트를 viewer에 표시
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : camera_page_add_detect_area_point")
            camera_name = self.ui_main.camera_page_name_box.currentText()
            select_index = self.ui_main.camera_page_detect_area_table.selectionModel().selectedRows()

            nvr_ip = self.find_nvr_ip(camera_name)
            if nvr_ip is None:
                return

            if select_index:  # 선택된 행이 있다면
                select_row = select_index[0].row()

                if point.x() == -1 :
                    if len(self.ai_server_camera_info_dict[nvr_ip][camera_name]["detect_info"][select_row]) > 1:
                        self.ai_server_camera_info_dict[nvr_ip][camera_name]["detect_info"][select_row].pop()

                    else: pass
                else:
                    self.ai_server_camera_info_dict[nvr_ip][camera_name]["detect_info"][select_row].append([round(point.x()/ self.ui_main.camera_page_viewer.width(), 3), 
                                                                                            round(point.y()/self.ui_main.camera_page_viewer.height(), 3)])

                self.ui_main.camera_page_viewer.set_point(self.ai_server_camera_info_dict[nvr_ip][camera_name]["detect_info"][select_row][1:], [self.ui_main.camera_page_viewer.width(), self.ui_main.camera_page_viewer.height()])

                gray_point_list = []
                if self.ai_server_camera_info_dict[nvr_ip][camera_name]["ai"] == False:
                    for index, value in enumerate(self.ai_server_camera_info_dict[nvr_ip][camera_name]["detect_info"]):
                        # 현재 인덱스가 제외할 인덱스 목록에 없으면 결과 리스트에 추가
                        if index != select_row:
                            gray_point_list.append(value[1:])

                self.ui_main.camera_page_viewer.set_gray_point(gray_point_list)

                save_info(host=self.ai_server_ip, port=self.ai_server_port, file_name="camera_info", info=self.ai_server_camera_info_dict)

        except Exception as e:
            print_error(e)

    def setup_camera_viewer(self):
        ##AI카메라 페이지 영상 뷰어 생성
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : setup_camera_viewer")

        # 기존 viewer를 layout에서 완전히 제거
        old_viewer = self.ui_main.camera_page_viewer
        self.ui_main.ai_camera_page_verticalLayout.removeWidget(old_viewer)
        old_viewer.deleteLater()
        
        # 새 viewer 생성 및 layout에 추가 (v1.6.0 방식)
        self.ui_main.camera_page_viewer = Plot_Camera_Viewer(self.ui_main.camera_page)
        self.ui_main.camera_page_viewer.setObjectName(u"camera_page_viewer")
        self.ui_main.camera_page_viewer.setMinimumSize(QSize(472, 331))
        self.ui_main.camera_page_viewer.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
                                                "background-color: rgba(255, 255, 255, 0);")
        self.ui_main.camera_page_viewer.setScaledContents(True)
        self.ui_main.ai_camera_page_verticalLayout.addWidget(self.ui_main.camera_page_viewer)
        self.ui_main.camera_page_viewer.clicked.connect(self.camera_page_add_detect_area_point)
        # print(f"[DEBUG] Viewer recreated and added to layout (no explicit show() like v1.6.0)")

    def update_camera_img_temp(self):
        """백그라운드 스레드에서 카메라 이미지 업데이트 시작"""
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : update_camera_img_temp (thread)")
        
        # 기존 스레드가 실행 중이면 중지
        if self.update_camera_img_thread is not None:
            self.update_camera_img_thread.stop()
            self.update_camera_img_thread.wait()
            self.update_camera_img_thread = None
        
        # 새 스레드 시작
        self.update_camera_img_thread = UpdateCameraImageThread(
            self.ai_server_camera_info_dict,
            self.ai_server_info_dict
        )
        self.update_camera_img_thread.finished.connect(self.on_camera_img_updated)
        self.update_camera_img_thread.start()
    
    def on_camera_img_updated(self, camera_img_temp):
        """카메라 이미지 업데이트 완료 시 호출"""
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : camera images updated ({len(camera_img_temp)} cameras)")
        self.camera_img_temp = camera_img_temp

    def start_camera_connect_status_timer(self):
        self.last_notification_info = None  # 최근 알림 정보 저장 (카메라 이름, 시간)

        if self.camera_connect_timer is not None :
            self.camera_connect_timer.stop()
            del self.camera_connect_timer

        self.check_camera_connect_status()

        self.camera_connect_timer = QTimer(self)
        self.camera_connect_timer.timeout.connect(self.check_camera_connect_status)

        self.camera_connect_timer.start(5000)  # 타이머 시작 5초에 한번씩

    def check_camera_connect_status(self):
        try:
            on_camera_pix = QPixmap(u":/ui/ui/images/ico_video_on.svg").scaled(24, 24, Qt.KeepAspectRatio)
            off_camera_pix = QPixmap(u":/ui/ui/images/ico_video_off.svg").scaled(24, 24, Qt.KeepAspectRatio)

            for nvr_ip, camera_info_dict in self.ai_server_camera_info_dict.items():
                nvr_id = self.ai_server_info_dict["NVR"][nvr_ip]["id"]
                nvr_pw = self.ai_server_info_dict["NVR"][nvr_ip]["pw"]
                auth = HTTPBasicAuth(nvr_id, nvr_pw) # NVR에 대한 ID / PW

                for camera_name, camera_info in camera_info_dict.items():
                    camera_id = self.ai_server_info_dict["NVR"][nvr_ip]["cameras"][camera_name]["id"]
                    camera_post = f'http://{nvr_ip}/api/cameras/{camera_id}'
                    r = requests.get(camera_post,auth=auth, timeout= 1).json()
                    for row_index in range(self.ui_main.camera_list_table.rowCount()):
                        item = self.ui_main.camera_list_table.item(row_index, 1)  # 첫 번째 열의 항목 가져오기

                        if item is not None and camera_name in item.text():
                            row_index = row_index
                            break
                    
                    if r["connected"] == True:
                        label = QLabel()
                        label.setAlignment(Qt.AlignCenter)
                        label.setPixmap(on_camera_pix)
                        self.ui_main.camera_list_table.setCellWidget(row_index, 0, label)

                    else:
                        label = QLabel()
                        label.setAlignment(Qt.AlignCenter)
                        label.setPixmap(off_camera_pix)
                        self.ui_main.camera_list_table.setCellWidget(row_index, 0, label)



        except Exception as e:
            print_error(e)

    def stop_camera_page_worker(self):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : stop camera page camera")

        if self.camera_page_worker != None :
            self.camera_page_worker.stop()
            del self.camera_page_worker
            self.camera_page_worker = None

    def connect_camera_page_camera(self, camera_name = None, tray_notify=False):
        try:
            self.stop_camera_page_worker()

            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : connect_camera_page_camera")
            print("live_viewer_blcok_active", tray_notify)
            if camera_name == None:
                camera_name = self.ui_main.camera_page_name_box.currentText()

            # print(f"[DEBUG] camera_name: {camera_name}")
            # print(f"[DEBUG] ai_server_camera_info_dict keys: {list(self.ai_server_camera_info_dict.keys())}")
            
            for nvr_ip, camera_info_dict in self.ai_server_camera_info_dict.items():
                # print(f"[DEBUG] nvr_ip: {nvr_ip}, cameras: {list(camera_info_dict.keys())}")
                if camera_name in camera_info_dict.keys():
                    print(camera_name)
                    nvr_id = self.ai_server_info_dict["NVR"][nvr_ip]["id"]
                    nvr_pw = self.ai_server_info_dict["NVR"][nvr_ip]["pw"]
                    camera_id = self.ai_server_info_dict['NVR'][nvr_ip]['cameras'][camera_name]['id']
                    # pipe = f"{nvr_id}:{nvr_pw}@{nvr_ip}/video{camera_id}"
                    pipe = f"{nvr_id}:{nvr_pw}@{nvr_ip}/normal{camera_id}"


                    # print(f"[DEBUG] camera_id: {camera_id}")
                    # print(f"[DEBUG] pipe: {pipe}")
                    # print(f"[DEBUG] viewer: {self.ui_main.camera_page_viewer}")
                
                    if tray_notify and self.ai_server_info_dict["ADMIN"]["live_viewer_block_active"]:
                        live_viewer_blcok_active = False
                        # 10초 타이머 설정하여 다시 연결
                        QTimer.singleShot(10000, lambda: self.connect_camera_page_camera(camera_name))

                    else:
                        live_viewer_blcok_active = self.ai_server_info_dict["ADMIN"]["live_viewer_block_active"]

                    print(tray_notify)
                    print(self.ai_server_info_dict["ADMIN"]["live_viewer_block_active"])
                    print("live_viewer_blcok_active" ,live_viewer_blcok_active)
                    self.camera_page_worker = Connect_Camera(pipe = pipe,
                                                            host=self.ai_server_ip, 
                                                            port=self.ai_server_port, 
                                                            camera_name = camera_name, 
                                                            # camera_num=camera_info["Num"], 
                                                            roi_thickness = 2,
                                                            plot_bbox=self.setting_info_temp["DISPLAY_PLOT"]["bbox"],
                                                            plot_label=self.setting_info_temp["DISPLAY_PLOT"]["label"],
                                                            plot_roi = self.setting_info_temp["DISPLAY_PLOT"]["roi"],
                                                            viewer = self.ui_main.camera_page_viewer,
                                                            live_viewer_blcok_active = live_viewer_blcok_active)

                    # print(f"[DEBUG] Worker created: {self.camera_page_worker}")
                    # print(f"[DEBUG] Connecting signal to viewer: {self.ui_main.camera_page_viewer}")
                    self.camera_page_worker.ImageUpdated.connect(lambda image, viewer=self.ui_main.camera_page_viewer: self.ShowCamera(viewer, image))
                    self.camera_page_worker.start()
                    # print(f"[DEBUG] Worker started")

                    break

                else:
                    print(f"[DEBUG] {camera_name} 선택된 카메라는 존재하지 않습니다.")
                
        except Exception as e:
            print_error(e)

    @QtCore.Slot()
    def ShowCamera(self, view, frame: QImage) -> None:
        # print(f"[DEBUG] ShowCamera called - view: {view}, frame size: {frame.width()}x{frame.height()}")
        # print(f"[DEBUG] Viewer visible: {view.isVisible()}, size: {view.width()}x{view.height()}")
        # print(f"[DEBUG] Viewer parent: {view.parent()}")
        # frame = frame.scaled(view.width(), view.height(), Qt.IgnoreAspectRatio, Qt.FastTransformation)
        view.setPixmap(QPixmap.fromImage(frame))
        view.update()  # 강제로 화면 업데이트
        # print(f"[DEBUG] Pixmap set successfully and update() called")

    def set_camera_page_viewer(self, camera_name = None):
        try:
            if camera_name == None:
                camera_name = self.ui_main.camera_page_name_box.currentText()

            # if camera_name in self.camera_info_dict_temp.keys():
            nvr_ip = self.find_nvr_ip(camera_name)
            if nvr_ip is None:
                return

            if camera_name in self.ai_server_camera_info_dict[nvr_ip].keys():
                camera_info = self.ai_server_camera_info_dict[nvr_ip][camera_name]

                self.reset_detect_area_list(camera_info["detect_info"])
                try:
                    self.ui_main.camera_page_viewer.reset()
                except (AttributeError, RuntimeError):
                    pass
                gray_point_list = []

                if camera_info["ai"] == False:
                    for index, value in enumerate(camera_info["detect_info"]):
                        # 현재 인덱스가 제외할 인덱스 목록에 없으면 결과 리스트에 추가
                        gray_point_list.append(value[1:])
                    self.ui_main.camera_page_ai_active_label.hide()
                    self.ui_main.camera_page_ai_active_icon.hide()
                    if self.camera_page_worker is not None:
                        self.camera_page_worker.ai_active = False
                else:
                    self.ui_main.camera_page_ai_active_label.show()
                    self.ui_main.camera_page_ai_active_icon.show()
                    if self.camera_page_worker is not None:
                        self.camera_page_worker.ai_active = True

                self.ui_main.camera_page_viewer.set_gray_point(gray_point_list)

        except Exception as e:
            print_error(e)

    def find_nvr_ip(self, camera_name):
        for nvr_ip, camera_info_dict in self.ai_server_camera_info_dict.items():
            if camera_name in camera_info_dict.keys():
                return nvr_ip
        return None

    def camera_page_add_detect_type(self):
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : camera_page_add_detect_type")
            camera_name = self.ui_main.camera_page_name_box.currentText()
            detect_type = self.ui_main.camera_page_camera_event_box.currentText()

            detect_type = Kor2eng(detect_type)

            nvr_ip = self.find_nvr_ip(camera_name)

            #add_detect_type
            if detect_type in ["Intrusion", "Loitering", "Falldown", "Fire", "Fight", "Trash"]:
                self.ai_server_camera_info_dict[nvr_ip][camera_name]["detect_info"].append([detect_type])
                for i in ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]:
                    self.ai_server_camera_info_dict[nvr_ip][camera_name]["detect_schedule"][str(i)][detect_type] = [[0, 24]]

            self.reset_detect_area_list(self.ai_server_camera_info_dict[nvr_ip][camera_name]["detect_info"])

            lastRow = self.ui_main.camera_page_detect_area_table.rowCount() - 1  
            if lastRow >= 0:
                # 마지막 행의 첫 번째 셀을 현재 셀로 설정
                self.ui_main.camera_page_detect_area_table.setCurrentCell(lastRow, 0)
            else:
                self.create_fade_out_msg(msg="테이블이 비어 있습니다.")
                

            gray_point_list = []
            if self.ai_server_camera_info_dict[nvr_ip][camera_name]["ai"] == False:
                for index, value in enumerate(self.ai_server_camera_info_dict[nvr_ip][camera_name]["detect_info"]):
                    # 현재 인덱스가 제외할 인덱스 목록에 없으면 결과 리스트에 추가
                    gray_point_list.append(value[1:])

            self.ui_main.camera_page_viewer.reset_green_area()
            self.ui_main.camera_page_viewer.set_gray_point(gray_point_list)

            save_info(host=self.ai_server_ip, port=self.ai_server_port, file_name="camera_info", info=self.ai_server_camera_info_dict)

            self.create_fade_out_msg(msg=f"{Eng2kor(detect_type)} 감지 영역이 추가되었습니다.")

        except Exception as e:
            print_error(e)

    def camera_page_del_detect_area(self):
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : camera_page_del_detect_area")
            camera_name = self.ui_main.camera_page_name_box.currentText()

            nvr_ip = self.find_nvr_ip(camera_name)
            if nvr_ip is None:
                return

            select_index = self.ui_main.camera_page_detect_area_table.selectionModel().selectedRows()
            if select_index:  # 선택된 행이 있다면
                select_row = select_index[0].row()
                del self.ai_server_camera_info_dict[nvr_ip][camera_name]["detect_info"][select_row]

            self.reset_detect_area_list(self.ai_server_camera_info_dict[nvr_ip][camera_name]["detect_info"])
            self.ui_main.camera_page_viewer.reset_green_area()

            save_info(host=self.ai_server_ip, port=self.ai_server_port, file_name="camera_info", info=self.ai_server_camera_info_dict)

            self.create_fade_out_msg(msg=f"감지 영역이 삭제되었습니다.")


        except Exception as e:
            print_error(e)

    def camera_page_update_camera_page_viewer_roi(self, item):
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : camera_page_update_roi")
            row = item.row()  # 클릭한 아이템의 행 인덱스
            camera_name = self.ui_main.camera_page_name_box.currentText()
            nvr_ip = self.find_nvr_ip(camera_name)
            if nvr_ip is None:
                return

            self.ui_main.camera_page_viewer.set_point(self.ai_server_camera_info_dict[nvr_ip][camera_name]["detect_info"][row][1:], [self.ui_main.camera_page_viewer.width(), self.ui_main.camera_page_viewer.height()])

            gray_point_list = []
            if self.ai_server_camera_info_dict[nvr_ip][camera_name]["ai"] == False:
                for index, value in enumerate(self.ai_server_camera_info_dict[nvr_ip][camera_name]["detect_info"]):
                    # 현재 인덱스가 제외할 인덱스 목록에 없으면 결과 리스트에 추가
                    if index != row:
                        gray_point_list.append(value[1:])
            self.ui_main.camera_page_viewer.set_gray_point(gray_point_list)

            save_info(host=self.ai_server_ip, port=self.ai_server_port, file_name="camera_info", info=self.ai_server_camera_info_dict)

        except Exception as e:
            print_error(e)

    def reset_detect_area_list(self, camera_detect_info):
        self.ui_main.camera_page_detect_area_table.setRowCount(0)

        for detect_type_list in camera_detect_info:
            detect_type_text = Eng2kor(detect_type_list[0])

            row_position = self.ui_main.camera_page_detect_area_table.rowCount()
            self.ui_main.camera_page_detect_area_table.insertRow(row_position)
            text = QTableWidgetItem(detect_type_text)
            text.setTextAlignment(Qt.AlignCenter)
            text.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
            self.ui_main.camera_page_detect_area_table.setItem(row_position, 0, text)

    def switch_main_display_to_camera(self, tray_notify=False):
        try:
            self.set_button_style('camera')
            self.ui_main.stackedWidget_2.setCurrentIndex(0)
            self.ui_main.camera_page_camera_event_box.clear()

            self.ai_server_camera_info_dict = load_info(host=self.ai_server_ip, port=self.ai_server_port, file_name="camera_info")
            self.admin_info_temp = load_info(host=self.ai_server_ip, port=self.ai_server_port, file_name="admin_info")
            self.setting_info_temp = load_info(host=self.ai_server_ip, port=self.ai_server_port, file_name="setting_info")

            if self.ai_server_info_dict["ADMIN"]["live_viewer_block_active"] == 0:
                self.ui_main.camera_page_block_label.hide()
            else:
                self.ui_main.camera_page_block_label.show()

            self.connect_camera_page_camera(camera_name=self.ui_main.camera_page_name_box.currentText(), tray_notify=tray_notify)
            self.set_camera_page_viewer(camera_name=self.ui_main.camera_page_name_box.currentText())

            for detect_type in self.admin_info_temp["LICENSE"]["detect_type"]:
                if self.admin_info_temp["LICENSE"]["detect_type"][detect_type] == 1:
                    self.ui_main.camera_page_camera_event_box.addItems([Eng2kor(detect_type)])


        except Exception as e:
            print_error(e)

    def switch_main_display_to_setting(self):
        try:
            save_info(host=self.ai_server_ip, port=self.ai_server_port, file_name="camera_info", info=self.ai_server_camera_info_dict)

            self.set_button_style('setting')
            self.ui_main.stackedWidget_2.setCurrentIndex(1)
            self.stop_camera_page_worker()

            self.setting_info_temp = load_info(host=self.ai_server_ip, port=self.ai_server_port, file_name="setting_info")
            self.update_setting()


        except Exception as e:
            print_error(e)

    def switch_main_display_to_admin(self):
        try:
            save_info(host=self.ai_server_ip, port=self.ai_server_port, file_name="camera_info", info=self.ai_server_camera_info_dict)

            self.set_button_style('admin')
            self.ui_main.stackedWidget_2.setCurrentIndex(2)

            self.ui_main.admin_pw_input.clear()

        except Exception as e:
            print_error(e)

    def update_setting(self):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : setting update")

        self.setting_info_temp = load_info(host=self.ai_server_ip, port=self.ai_server_port, file_name="setting_info")

        self.ui_main.setting_detect_bbox_active_bnt.setChecked(self.setting_info_temp["DISPLAY_PLOT"]["bbox"]) # 지능형 검출 결과 BBOX 출력 여부
        self.ui_main.setting_detect_label_active_bnt.setChecked(self.setting_info_temp["DISPLAY_PLOT"]["label"]) # 지능형 검출 결과 class 출력 여부
        self.ui_main.setting_detect_roi_active_bnt.setChecked(self.setting_info_temp["DISPLAY_PLOT"]["roi"]) # 지능형 검출 결과 class 출력 여부
        
        url = f'http://{self.ai_server_ip}:{self.ai_server_port}/get-ai-weight-list'
        receive_data = requests.get(url, timeout=1).json()
        self.ui_main.setting_setting_ai_weight_box.clear()

        for weight_name in receive_data["weight_list"]:
            self.ui_main.setting_setting_ai_weight_box.addItems([weight_name])

        self.ui_main.setting_self_training_zeroshot_bnt.setChecked(self.setting_info_temp["AI"]["zero_shot"])
        self.ui_main.setting_self_training_auto_labeling_bnt.setChecked(self.setting_info_temp["AI"]["auto_label"])

        items_text = [self.ui_main.setting_setting_ai_weight_box.itemText(i) for i in range(self.ui_main.setting_setting_ai_weight_box.count())]

        if self.setting_info_temp["AI"]["weight"] != 0:
            if self.setting_info_temp["AI"]["weight"] in items_text:
                index_num = items_text.index(self.setting_info_temp["AI"]["weight"])
                self.ui_main.setting_setting_ai_weight_box.setCurrentIndex(index_num)

        else:
            index_num = items_text.index("default")
            self.ui_main.setting_setting_ai_weight_box.setCurrentIndex(index_num)

        self.ui_main.setting_auto_label_time_start_box.setCurrentText(self.setting_info_temp["AI"]["auto_label_start_time"])
        self.ui_main.setting_auto_label_time_end_box.setCurrentText(self.setting_info_temp["AI"]["auto_label_end_time"])

        if self.admin_info_temp["FN_PERMISSION"]["self_labeling_active"] == 1:
            self.ui_main.setting_self_labeling_widget.show()
            self.ui_main.setting_partion_4.show()
        else:
            self.ui_main.setting_self_labeling_widget.hide()
            self.ui_main.setting_partion_4.hide()

    def load_nvr_server_info(self):
        selected_row_index = self.ui_main.nvr_list_table.currentRow()
        if selected_row_index != -1:
            nvr_ip = self.ui_main.nvr_list_table.item(selected_row_index, 2).text()
            self.ui_main.nvr_name_input.setText(self.ai_server_info_dict["NVR"][nvr_ip]["name"])
            self.ui_main.nvr_ip_input.setText(nvr_ip)
            self.ui_main.nvr_port_input.setText(self.ai_server_info_dict["NVR"][nvr_ip]["port"])
            self.ui_main.nvr_http_port_input.setText(self.ai_server_info_dict["NVR"][nvr_ip]["http_port"])
            self.ui_main.nvr_id_input.setText(self.ai_server_info_dict["NVR"][nvr_ip]["id"])
            self.ui_main.nvr_passward_input.setText(self.ai_server_info_dict["NVR"][nvr_ip]["pw"])

    def load_ai_server_info_to_table(self):
        self.ui_main.ai_server_info_table.setRowCount(0)
        selected_row_index = self.ui_main.ai_server_table.currentRow()
        if selected_row_index != -1:
            ai_server_ip = self.ui_main.ai_server_table.item(selected_row_index, 2).text()
            ai_server_port = self.ai_server_info_dict["AI_SERVER"][ai_server_ip]["port"]

            self.ui_main.ai_server_name_input.setText(self.ai_server_info_dict["AI_SERVER"][ai_server_ip]["name"])
            self.ui_main.ai_server_ip_input.setText(ai_server_ip)
            self.ui_main.ai_server_port_input.setText(self.ai_server_info_dict["AI_SERVER"][ai_server_ip]["port"])
            self.ui_main.ai_server_id_input.setText(self.ai_server_info_dict["AI_SERVER"][ai_server_ip]["id"])
            self.ui_main.ai_server_passward_input.setText(self.ai_server_info_dict["AI_SERVER"][ai_server_ip]["pw"])

            camera_post = f'http://{ai_server_ip}:{ai_server_port}/get-camera-info'
            r = requests.get(camera_post, json={"msg" : ""}, timeout=1)
            if str(r) == "<Response [200]>":
                self.ai_server_camera_info_dict = r.json()["camera_info_dict"]

                for nvr_ip, camera_info_dict in self.ai_server_camera_info_dict.items():
                    for camera_name, camera_info in camera_info_dict.items():
                        self.ui_main.ai_server_info_table.setRowCount(self.ui_main.ai_server_info_table.rowCount() + 1)

                        item = QTableWidgetItem(str(self.ui_main.ai_server_info_table.rowCount()))
                        item.setTextAlignment(Qt.AlignCenter)
                        item2 = QTableWidgetItem(camera_name)
                        item2.setTextAlignment(Qt.AlignCenter)
                        item3 = QTableWidgetItem(camera_info["camera_ip"])
                        item3.setTextAlignment(Qt.AlignCenter)

                        try:
                            item4 = QTableWidgetItem(self.ai_server_info_dict["NVR"][nvr_ip]["name"])
                            item4.setTextAlignment(Qt.AlignCenter)
                        except (KeyError, TypeError):
                            item4 = QTableWidgetItem("알 수 없음")
                            item4.setTextAlignment(Qt.AlignCenter)

                        try:
                            item5 = QTableWidgetItem(nvr_ip)
                            item5.setTextAlignment(Qt.AlignCenter)
                        except (TypeError, ValueError):
                            item5 = QTableWidgetItem("알 수 없음")
                            item5.setTextAlignment(Qt.AlignCenter)

                        self.ui_main.ai_server_info_table.setItem(self.ui_main.ai_server_info_table.rowCount() - 1, 0, item)
                        self.ui_main.ai_server_info_table.setItem(self.ui_main.ai_server_info_table.rowCount() - 1, 1, item2)
                        self.ui_main.ai_server_info_table.setItem(self.ui_main.ai_server_info_table.rowCount() - 1, 2, item3)
                        self.ui_main.ai_server_info_table.setItem(self.ui_main.ai_server_info_table.rowCount() - 1, 3, item4)
                        self.ui_main.ai_server_info_table.setItem(self.ui_main.ai_server_info_table.rowCount() - 1, 4, item5)

    def save_ai_server(self):
        ai_server_name = self.ui_main.ai_server_name_input.text()
        ai_server_ip = self.ui_main.ai_server_ip_input.text()
        ai_server_port = self.ui_main.ai_server_port_input.text()
        ai_server_id = self.ui_main.ai_server_id_input.text()
        ai_server_passward = self.ui_main.ai_server_passward_input.text()

        camera_post = f'http://{ai_server_ip}:{ai_server_port}/get-camera-info'
        r = requests.get(camera_post, json={"msg" : ""}, timeout=1)
        if str(r) == "<Response [200]>":
            camera_info_ori = r.json()
            
            if ai_server_ip in self.ai_server_info_dict["AI_SERVER"].keys():
                self.ai_server_info_dict["AI_SERVER"][ai_server_ip] = {"id" : ai_server_id,
                                                                "pw" : ai_server_passward,
                                                                "port" : ai_server_port,
                                                                "name" : ai_server_name,
                                                                }
            else:
                self.add_ai_server_info_to_table(ai_server_ip, {
                                                                "id" : ai_server_id,
                                                                "pw" : ai_server_passward,
                                                                "port" : ai_server_port,
                                                                "name" : ai_server_name,
                                                            })
            
                self.ai_server_info_dict["AI_SERVER"][ai_server_ip] = {"id" : ai_server_id,
                                                                    "pw" : ai_server_passward,
                                                                    "port" : ai_server_port,
                                                                    "name" : ai_server_name,
                                                                    }

            # with open(os.path.join(os.getcwd(), "ai_sever_info.json"), "w", encoding="UTF-8") as f:
                # json.dump(self.ai_server_info_dict, f, ensure_ascii=False, indent=4)

            save_crypography_json(os.path.join(os.getcwd(), "ai_sever_info.json"), self.ai_server_info_dict)

            self.create_fade_out_msg(msg="AI 서버 정보 저장 성공")

        else:
            self.create_fade_out_msg(msg="AI 서버 저장 실패\nAI 서버 정보를 확인해주세요.")
            return

    def add_ai_server(self):
        self.ui_main.ai_server_name_input.clear()
        self.ui_main.ai_server_ip_input.clear()
        self.ui_main.ai_server_port_input.setText("65432")
        self.ui_main.ai_server_id_input.clear()
        self.ui_main.ai_server_passward_input.clear()

    def del_ai_server(self):
        selected_row_index = self.ui_main.ai_server_table.currentRow()
        if selected_row_index != -1:
            # self.ui_main.ai_server_table.removeRow(selected_row_index)
            self.ai_server_info_dict["AI_SERVER"].pop(list(self.ai_server_info_dict["AI_SERVER"].keys())[selected_row_index])
            # with open(os.path.join(os.getcwd(), "ai_sever_info.json"), "w", encoding="UTF-8") as f:
                # json.dump(self.ai_server_info_dict, f, ensure_ascii=False, indent=4)

            save_crypography_json(os.path.join(os.getcwd(), "ai_sever_info.json"), self.ai_server_info_dict)
            

            self.ui_main.ai_server_table.setRowCount(0)

            #지능형 서버 목록 채우기
            for ai_server_ip, ai_server_info in self.ai_server_info_dict["AI_SERVER"].items():
                self.add_ai_server_info_to_table(ai_server_ip, ai_server_info)

        else:
            self.create_fade_out_msg(msg="삭제할 AI 서버를 선택해주세요.")
            return

    def add_nvr_server(self):
        self.ui_main.nvr_name_input.clear()
        self.ui_main.nvr_ip_input.clear()
        self.ui_main.nvr_port_input.setText("8081")
        self.ui_main.nvr_http_port_input.setText("80")
        self.ui_main.nvr_id_input.clear()
        self.ui_main.nvr_passward_input.clear()

    def del_nvr_server(self):
        selected_row_index = self.ui_main.nvr_list_table.currentRow()
        if selected_row_index != -1:

            nvr_ip = self.ui_main.nvr_list_table.item(selected_row_index, 2).text()
            self.ai_server_info_dict["NVR"].pop(nvr_ip)
            self.ui_main.nvr_list_table.removeRow(selected_row_index)



            # with open(os.path.join(os.getcwd(), "ai_sever_info.json"), "w", encoding="UTF-8") as f:
                # json.dump(self.ai_server_info_dict, f, ensure_ascii=False, indent=4)

            save_crypography_json(os.path.join(os.getcwd(), "ai_sever_info.json"), self.ai_server_info_dict)

            self.ui_main.nvr_server_tree_list.clear()
            self.ui_main.nvr_list_table.setRowCount(0)
            for nvr_ip, nvr_info in self.ai_server_info_dict["NVR"].items():
                self.add_nvr_info_to_gui(nvr_ip, nvr_info)

            self.add_nvr_server()
            self.create_fade_out_msg(msg="NVR 서버 삭제 완료")

        else:
            self.create_fade_out_msg(msg="삭제할 NVR 서버를 선택해주세요.")
            return

    def save_nvr_server(self):
        nvr_name = self.ui_main.nvr_name_input.text()
        nvr_ip = self.ui_main.nvr_ip_input.text()
        nvr_port = self.ui_main.nvr_port_input.text()
        nvr_http_port = self.ui_main.nvr_http_port_input.text()
        nvr_id = self.ui_main.nvr_id_input.text()
        nvr_passward = self.ui_main.nvr_passward_input.text()

        auth = HTTPBasicAuth(nvr_id, nvr_passward)  # NVR에 대한 ID / PW
        camera_post = f'http://{nvr_ip}/api/cameras'
        r = requests.get(camera_post, auth=auth, timeout=1)

        #nvr 응답이 있는 경우
        if str(r) == "<Response [200]>":
            #기존 정보를 수정하는 경우
            if nvr_ip in self.ai_server_info_dict["NVR"].keys():
                self.ai_server_info_dict["NVR"][nvr_ip] = { "id" : nvr_id,
                                                    "pw" : nvr_passward,
                                                    "port" : nvr_port,
                                                    "http_port" : nvr_http_port,
                                                    "name" : nvr_name,
                                                    "cameras": {},
                                                    }
            #새롭게 서버를 등록하는 경우
            else:
                self.ai_server_info_dict["NVR"][nvr_ip] = { "id" : nvr_id,
                                                    "pw" : nvr_passward,
                                                    "port" : nvr_port,
                                                    "http_port" : nvr_http_port,
                                                    "name" : nvr_name,
                                                    "cameras": {},
                                                    }

                # with open(os.path.join(os.getcwd(), "ai_sever_info.json"), "w", encoding="UTF-8") as f:
                    # json.dump(self.ai_server_info_dict, f, ensure_ascii=False, indent=4)
                save_crypography_json(os.path.join(os.getcwd(), "ai_sever_info.json"), self.ai_server_info_dict)
                

            self.ui_main.nvr_server_tree_list.clear()
            self.ui_main.nvr_list_table.setRowCount(0)

            for nvr_ip, nvr_info in self.ai_server_info_dict["NVR"].items():
                self.add_nvr_info_to_gui(nvr_ip, nvr_info)

            # with open(os.path.join(os.getcwd(), "ai_sever_info.json"), "w", encoding="UTF-8") as f:
                # json.dump(self.ai_server_info_dict, f, ensure_ascii=False, indent=4)

            save_crypography_json(os.path.join(os.getcwd(), "ai_sever_info.json"), self.ai_server_info_dict)

            self.create_fade_out_msg(msg="NVR 서버 저장 완료")
        else:
            self.create_fade_out_msg(msg="NVR 서버 정보를 확인해주세요.")
            return

    def filter_nvr_tree(self):
        """NVR 트리를 검색어로 필터링"""
        try:
            search_text = self.ui_main.nvr_search_input.text().lower().strip()
            
            # 검색어가 비어있으면 모든 항목 표시
            if not search_text:
                for i in range(self.ui_main.nvr_server_tree_list.topLevelItemCount()):
                    parent_item = self.ui_main.nvr_server_tree_list.topLevelItem(i)
                    parent_item.setHidden(False)
                    for j in range(parent_item.childCount()):
                        child_item = parent_item.child(j)
                        child_item.setHidden(False)
                return
            
            # 검색어가 있으면 필터링
            for i in range(self.ui_main.nvr_server_tree_list.topLevelItemCount()):
                parent_item = self.ui_main.nvr_server_tree_list.topLevelItem(i)
                parent_text = parent_item.text(0).lower()
                
                # 부모 NVR 이름이 검색어와 매칭되는지 확인
                parent_match = search_text in parent_text
                
                # 자식 카메라 중 하나라도 매칭되는지 확인
                any_child_match = False
                for j in range(parent_item.childCount()):
                    child_item = parent_item.child(j)
                    child_text = child_item.text(0).lower()
                    child_match = search_text in child_text
                    
                    # 자식 항목은 매칭되거나 부모가 매칭되면 표시
                    child_item.setHidden(not (child_match or parent_match))
                    
                    if child_match:
                        any_child_match = True
                
                # 부모 항목은 본인이 매칭되거나 자식 중 하나라도 매칭되면 표시
                parent_item.setHidden(not (parent_match or any_child_match))
                
                # 부모가 표시될 때는 자동으로 확장
                if not parent_item.isHidden():
                    parent_item.setExpanded(True)
                    
        except Exception as e:
            print_error(e)

    def filter_ai_server_camera_table(self):
        """AI 서버 카메라 테이블을 검색어로 필터링"""
        try:
            search_text = self.ui_main.ai_server_camera_search_input.text().lower().strip()
            
            # 검색어가 비어있으면 모든 행 표시
            if not search_text:
                for row in range(self.ui_main.ai_server_info_table.rowCount()):
                    self.ui_main.ai_server_info_table.setRowHidden(row, False)
                return
            
            # 검색어가 있으면 필터링
            for row in range(self.ui_main.ai_server_info_table.rowCount()):
                match_found = False
                
                # 각 컬럼의 텍스트를 검색 (번호, 카메라명, 카메라IP, NVR명, NVR IP)
                for col in range(self.ui_main.ai_server_info_table.columnCount()):
                    item = self.ui_main.ai_server_info_table.item(row, col)
                    if item and search_text in item.text().lower():
                        match_found = True
                        break
                
                # 매칭되지 않으면 행 숨김
                self.ui_main.ai_server_info_table.setRowHidden(row, not match_found)
                    
        except Exception as e:
            print_error(e)

    def add_nvr_info_to_gui(self, nvr_ip, nvr_info):

        self.ui_main.nvr_list_table.setRowCount(self.ui_main.nvr_list_table.rowCount() + 1)

        item = QTableWidgetItem(str(self.ui_main.nvr_list_table.rowCount()))
        item.setTextAlignment(Qt.AlignCenter)
        item2 = QTableWidgetItem(nvr_info["name"])
        item2.setTextAlignment(Qt.AlignCenter)
        item3 = QTableWidgetItem(nvr_ip)
        item3.setTextAlignment(Qt.AlignCenter)

        self.ui_main.nvr_list_table.setItem(self.ui_main.nvr_list_table.rowCount() - 1, 0, item)
        self.ui_main.nvr_list_table.setItem(self.ui_main.nvr_list_table.rowCount() - 1, 1, item2)
        self.ui_main.nvr_list_table.setItem(self.ui_main.nvr_list_table.rowCount() - 1, 2, item3)

        # NVR Camera 목록 불러오기
        auth = HTTPBasicAuth(nvr_info["id"], nvr_info["pw"])  # NVR에 대한 ID / PW
        camera_post = f'http://{nvr_ip}/api/cameras'
        r = requests.get(camera_post, auth=auth, timeout=1)
        if str(r) == "<Response [200]>":
            camera_info_ori = r.json()
            tree_parent = QTreeWidgetItem([f"{nvr_info['name']}({nvr_ip})"])

            for camera_info in camera_info_ori["cameras"]:
                tree_parent.addChild(QTreeWidgetItem([f"{camera_info['name']}"]))
                # self.nvr_camera_info_dict[nvr_ip]["cameras"][f"{camera_info['id']}"] = {
                #     "ip": camera_info["address"],
                #     "camera_name": camera_info["name"],
                #     "streaming": camera_info["streaming"],
                # }

                self.ai_server_info_dict["NVR"][nvr_ip]["cameras"][camera_info["name"]] = {"ip": camera_info["address"],
                                                                                            "streaming": camera_info["streaming"],
                                                                                            "id": camera_info['id'],
                                                                                        }

            self.ui_main.nvr_server_tree_list.addTopLevelItem(tree_parent)

        else:
            self.create_fade_out_msg(msg=f"{nvr_info['name']} 서버 접속 실패")
            return

    def set_button_style(self, active_button):
        # 모든 버튼을 기본 스타일로 설정
        default_style = "color: white; border: 1px solid rgba(191, 64, 64, 0); background-color: rgba(191, 64, 64, 0);"
        active_style = "color: green; border: 1px solid rgba(191, 64, 64, 0); background-color: rgba(191, 64, 64, 0);"
        
        buttons = {
            'camera': self.ui_main.camera_bnt,
            'setting': self.ui_main.setting_bnt,
            'admin': self.ui_main.admin_bnt,
        }
        
        for key, button in buttons.items():
            button.setStyleSheet(active_style if key == active_button else default_style)

    def create_fade_out_msg(self, std_window=None, msg="None"):
        try:
            if not hasattr(self, 'fadeout_window') or not self.fadeout_window.isVisible():
                # std_window가 제공되면 해당 윈도우를 parent로 사용, 아니면 self 사용
                parent_window = std_window if std_window is not None else self
                self.fadeout_window = FadeOutWindow(parent_window, msg)
                # 항상 최상위에 표시되도록 설정
                self.fadeout_window.setWindowFlags(self.fadeout_window.windowFlags() | Qt.WindowStaysOnTopHint)

                if std_window is None:
                    main_window_rect = self.geometry()
                    fadeout_window_rect = self.fadeout_window.geometry()
                    self.fadeout_window.move(
                        main_window_rect.left() + (main_window_rect.width() - fadeout_window_rect.width()) // 2,
                        main_window_rect.top() + (main_window_rect.height() - fadeout_window_rect.height()) * 4 // 5
                    )
                else:
                    main_window_rect = std_window.geometry()
                    fadeout_window_rect = self.fadeout_window.geometry()
                    self.fadeout_window.move(
                        main_window_rect.left() + (main_window_rect.width() - fadeout_window_rect.width()) // 2,
                        main_window_rect.top() + (main_window_rect.height() - fadeout_window_rect.height()) * 4 // 5
                    )

            self.fadeout_window.show()
            self.fadeout_window.raise_()          # 윈도우를 최상위로 올림
            
            # 포커스를 원래 창으로 돌려줌 (단축키 유지를 위해)
            if std_window is not None:
                std_window.activateWindow()
                std_window.setFocus()
            else:
                self.activateWindow()
                self.setFocus()

        except Exception as e:
            print_error(e)

    def setup_event_filters(self):
        # 이벤트 필터 설치
        event_filters = [
            self.ui_main.admin_pw_input,
            self.ui_main.license_camera_allow_num_input,
            self.ui_main.ai_server_name_input,
            self.ui_main.ai_server_ip_input,
            self.ui_main.ai_server_port_input,
            self.ui_main.ai_server_id_input,
            self.ui_main.ai_server_passward_input,
            self.ui_main.nvr_name_input,
            self.ui_main.nvr_ip_input,
            self.ui_main.nvr_port_input,
            self.ui_main.nvr_http_port_input,
            self.ui_main.nvr_id_input,
            self.ui_main.nvr_passward_input,
            self.ui_main.nvr_search_input,
            self.ui_main.ai_server_camera_search_input,

        ]
        for filter in event_filters:
            filter.installEventFilter(self)


    def eventFilter(self, obj, event):
        # NVR 검색 입력창 특별 처리 - 처음 포커스시 텍스트 제거
        if obj == self.ui_main.nvr_search_input:
            if event.type() == QEvent.FocusIn and self.nvr_search_first_focus:
                self.ui_main.nvr_search_input.clear()
                self.nvr_search_first_focus = False
        
        # AI 서버 카메라 검색 입력창 특별 처리 - 처음 포커스시 텍스트 제거
        if obj == self.ui_main.ai_server_camera_search_input:
            if event.type() == QEvent.FocusIn and self.ai_server_camera_search_first_focus:
                self.ui_main.ai_server_camera_search_input.clear()
                self.ai_server_camera_search_first_focus = False
        
        self.input_field_styles = {
            self.ui_main.admin_pw_input: self.ui_main.admin_pw_input_line,
            self.ui_main.license_camera_allow_num_input: self.ui_main.license_camera_allow_num_input_line,
            self.ui_main.ai_server_name_input: self.ui_main.ai_server_name_input_line,
            self.ui_main.ai_server_ip_input: self.ui_main.ai_server_ip_input_line,
            self.ui_main.ai_server_port_input: self.ui_main.ai_server_port_input_line,
            self.ui_main.ai_server_id_input: self.ui_main.ai_server_id_input_line,
            self.ui_main.ai_server_passward_input: self.ui_main.ai_server_passward_input_line,
            self.ui_main.nvr_name_input: self.ui_main.nvr_name_input_line,
            self.ui_main.nvr_ip_input: self.ui_main.nvr_ip_input_line,
            self.ui_main.nvr_port_input: self.ui_main.nvr_port_input_line,
            self.ui_main.nvr_http_port_input: self.ui_main.nvr_http_port_input_line,
            self.ui_main.nvr_id_input: self.ui_main.nvr_id_input_line,
            self.ui_main.nvr_passward_input: self.ui_main.nvr_passward_input_line,
        }

        if obj in self.input_field_styles:
            line_edit = self.input_field_styles[obj]
            if event.type() == QEvent.FocusIn:
                line_edit.setStyleSheet("background-color: green")
            elif event.type() == QEvent.FocusOut:
                line_edit.setStyleSheet("background-color: rgb(36, 39, 44)")

        return super().eventFilter(obj, event)

def generate_camera_grid(n):
    cols = math.ceil(math.sqrt(n))  # 열 개수
    rows = math.ceil(n / cols)  # 행 개수
    
    grid = [(r+1, c+1) for r in range(rows) for c in range(cols)][:n]  # 좌표 생성
    return grid

def load_init_camera_dict(camera_ip, camera_id):
    return {
        "camera_ip": camera_ip,
        "camera_id": camera_id,
        "detect_info": [],
        "ai": False,
        "cls": [True, True, True],
        "conf": [33, 33, 33],
        "detect_schedule": {
            "sunday": {
                "Intrusion": [],
                "Fire": [],
                "Loitering": [],
                "Falldown": [],
                "Fight": []
            },
            "monday": {
                "Intrusion": [],
                "Fire": [],
                "Loitering": [],
                "Falldown": [],
                "Fight": []
            },
            "tuesday": {
                "Intrusion": [],
                "Fire": [],
                "Loitering": [],
                "Falldown": [],
                "Fight": []
            },
            "wednesday": {
                "Intrusion": [],
                "Fire": [],
                "Loitering": [],
                "Falldown": [],
                "Fight": []
            },
            "thursday": {
                "Intrusion": [],
                "Fire": [],
                "Loitering": [],
                "Falldown": [],
                "Fight": []
            },
            "friday": {
                "Intrusion": [],
                "Fire": [],
                "Loitering": [],
                "Falldown": [],
                "Fight": []
            },
            "saturday": {
                "Intrusion": [],
                "Fire": [],
                "Loitering": [],
                "Falldown": [],
                "Fight": []
            }
        }
    }

def main():
    try:
        # time.sleep(1)

        app = QApplication(sys.argv)
        window = LoginWindow()
        window.show()
        app.exec()

    except Exception as e:
            print_error(e)

    finally:
            
            # input("Press Enter to close...")  # 실행 후 입력을 기다림
            pass
    
if __name__ == "__main__":
        main()




from typing import Any
from PySide6.QtWidgets import QDialog
from ui.ui_server_setting import Ui_server_setting_window
from datetime import datetime
from PySide6.QtCore import QTimer
import requests

from PySide6.QtGui import QImage, QPixmap, QPainter, QPen, QColor, QPolygon, QBrush, QFont, QStandardItem, QStandardItemModel, QIcon
from PySide6.QtCore import Qt, QThread, Signal, QPoint, QObject, QEvent, QTimer, QPropertyAnimation, QEasingCurve, QRect, QSize
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget, QGridLayout)

from utils import save_info, load_info, Eng2kor, print_error, Kor2eng
import resourece_rc


import cv2
import numpy as np
import math 
import json
import os
import re

def open_server_setting_window(click, self):
    self.dark_layer.show()
    self.server_setting_window = QDialog()  # QDialog 인스턴스 생성
    self.server_setting_window.setWindowFlag(Qt.FramelessWindowHint)

    self.server_setting_ui = Ui_server_setting_window()
    self.server_setting_ui.setupUi(self.server_setting_window)

    # 활성화된 detect_type 필터링
    self.active_detect_types = []
    for ai_server_ip, ai_server_info in self.ai_server_info_dict["AI_SERVER"].items():
        ai_server_port = ai_server_info["port"]
        try:
            admin_info_temp = load_info(host=ai_server_ip, port=ai_server_port, file_name="admin_info")
            for detect_type, active_flag in admin_info_temp["LICENSE"]["detect_type"].items():
                if detect_type not in self.active_detect_types:
                    if active_flag == 1:
                        self.active_detect_types.append(detect_type)
        except Exception as e:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : {e}")
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : 지능형 서버 응답 없음")
            
            continue

    self.server_setting_ui.alarm_memu_bnt.clicked.connect(lambda click, instance = self : alarm_memu_bnt_clicked(click, instance))
    self.server_setting_ui.admin_setting_but.clicked.connect(lambda click, instance = self : admin_setting_but_clicked(click, instance))
    self.server_setting_ui.user_setting_bnt.clicked.connect(lambda click, instance = self : user_setting_bnt_clicked(click, instance))
    self.server_setting_ui.setting_event_pop_up_save_bnt.clicked.connect(lambda click, instance = self : change_setting_info(click, instance))
    self.server_setting_ui.setting_notice_phone_add_bnt.clicked.connect(lambda click, instance = self : add_notice_phone_number(click, instance))
    self.server_setting_ui.setting_notice_phone_del_bnt.clicked.connect(lambda click, instance = self : del_notice_phone_number(click, instance))
    self.server_setting_ui.setting_notice_phone_list.itemClicked.connect(lambda click, instance = self : load_notion_detect_type_button_states(click, instance))
    self.server_setting_ui.setting_notice_phone_save_bnt.clicked.connect(lambda click, instance = self : change_setting_info(click, instance))

    self.server_setting_ui.setting_user_save_bnt.clicked.connect(lambda click, instance = self : setting_change_user_info(click, instance))

    self.server_setting_ui.admin_sms_alarm_fn_active_bnt.clicked.connect(lambda click, instance = self : change_sms_alarm_fn(click, instance))
    self.server_setting_ui.admin_fn_save_bnt.clicked.connect(lambda click, instance = self : save_admin_info(click, instance))

    self.server_setting_ui.admin_live_viewer_block_bnt.clicked.connect(lambda click, instance = self : change_live_viewer_block_fn(click, instance))

    self.server_setting_ui.shutdown_bnt.clicked.connect(lambda click, instance = self : shutdown(click, instance))

    update_notion_detect_type_buttons(self)
    update_setting(self)

    if self.admin_flag == False:
        self.server_setting_ui.admin_setting_but.hide()

    self.server_setting_window.show()

    # 메인 윈도우의 중앙에 팝업 윈도우 위치 계산
    # mapToGlobal을 사용하여 다른 팝업(fadeout_window 등)의 영향을 받지 않도록 함
    main_center = self.mapToGlobal(self.rect().center())

    popupWindowGeometry = self.server_setting_window.frameGeometry()

    # 팝업 윈도우의 좌상단 좌표를 계산
    topLeftPoint = QPoint(
        main_center.x() - popupWindowGeometry.width() // 2,
        main_center.y() - popupWindowGeometry.height() // 2
    )
    self.server_setting_window.move(topLeftPoint)

def shutdown(click, self):
    self.server_setting_window.close()
    self.dark_layer.hide()

def change_setting_info(click, self):
    """설정 정보 변경 함수"""
    self.ai_server_info_dict["SETTING"]["notice"]["active"] = self.server_setting_ui.setting_event_pop_up_active_bnt.isChecked()
    self.ai_server_info_dict["SETTING"]["notice"]["duration"] = self.server_setting_ui.setting_event_pop_up_duration_box.currentIndex()
    
    if self.server_setting_ui.setting_notice_phone_active_bnt.isChecked():
        self.ai_server_info_dict["SETTING"]["sms"]["active"] = 1
    else:
        self.ai_server_info_dict["SETTING"]["sms"]["active"] = 0

    with open(os.path.join(os.getcwd(), "ai_sever_info.json"), "w", encoding="UTF-8") as f:
        json.dump(self.ai_server_info_dict, f, ensure_ascii=False, indent=4)

    self.create_fade_out_msg(std_window=self.server_setting_window, msg="설정 정보가 저장되었습니다")

def update_setting(self):
    """기존 저장된 설정 정보 불러오는 함수"""
    if self.ai_server_info_dict["SETTING"]["notice"]["active"] == 1:
        self.server_setting_ui.setting_event_pop_up_active_bnt.setChecked(True)
    else:
        self.server_setting_ui.setting_event_pop_up_active_bnt.setChecked(False)
    
    self.server_setting_ui.setting_event_pop_up_duration_box.setCurrentIndex(self.ai_server_info_dict["SETTING"]["notice"]["duration"])

    if self.ai_server_info_dict["SETTING"]["sms"]["active"] == 1:
        self.server_setting_ui.setting_notice_phone_active_bnt.setChecked(True)
    else:
        self.server_setting_ui.setting_notice_phone_active_bnt.setChecked(False)

    if self.ai_server_info_dict["ADMIN"]["sms_active"] == 1:
        self.server_setting_ui.setting_sms_widget.show()
        self.server_setting_ui.admin_sms_alarm_fn_active_bnt.setChecked(True)
    else:
        self.server_setting_ui.setting_sms_widget.hide()
        self.server_setting_ui.admin_sms_alarm_fn_active_bnt.setChecked(False)

    if self.ai_server_info_dict["ADMIN"]["live_viewer_block_active"] == 1:
        self.server_setting_ui.admin_live_viewer_block_bnt.setChecked(True)
    else:
        self.server_setting_ui.admin_live_viewer_block_bnt.setChecked(False)

    # QTableWidget의 모든 행 제거
    self.server_setting_ui.setting_notice_phone_list.setRowCount(0)
    for user_phone, user_notice_detect_type in self.ai_server_info_dict["SETTING"]["sms"]["user"].items():
        row = self.server_setting_ui.setting_notice_phone_list.rowCount()
        self.server_setting_ui.setting_notice_phone_list.insertRow(row)
        item = QTableWidgetItem(user_phone)
        item.setTextAlignment(Qt.AlignCenter)
        self.server_setting_ui.setting_notice_phone_list.setItem(row, 0, item)

    self.server_setting_ui.admin_sms_alarm_allow_phone_num_input.setText(str(self.ai_server_info_dict["ADMIN"]["sms_allow_phone_num"]))
    self.server_setting_ui.setting_user_id_input.setText(self.user_info)

def setting_change_user_info(click, self):
    try:
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : setting_change_user_info")


        for user_id in self.ai_server_info_dict["USER"].keys():
            if self.server_setting_ui.setting_user_id_input.text() == user_id:
                if self.server_setting_ui.setting_user_pw_input.text() == self.ai_server_info_dict["USER"][user_id]:
                    if self.server_setting_ui.setting_user_new_pw_input.text() == self.server_setting_ui.setting_user_new_pw_input2.text():
                        self.ai_server_info_dict["USER"][user_id] = self.server_setting_ui.setting_user_new_pw_input.text()
                        break
                    else:
                        self.create_fade_out_msg(std_window=self.server_setting_window, msg="비밀번호가 일치하지 않습니다")
                        return
                else:
                    self.create_fade_out_msg(std_window=self.server_setting_window, msg="비밀번호가 일치하지 않습니다")
                    return


        self.create_fade_out_msg(std_window=self.server_setting_window, msg="사용자 정보가 저장되었습니다")
        with open(os.path.join(os.getcwd(), "ai_sever_info.json"), "w", encoding="UTF-8") as f:
            json.dump(self.ai_server_info_dict, f, ensure_ascii=False, indent=4)

    except Exception as e:
        print_error(e)


def add_notice_phone_number(click, self):
    """전화번호 추가 함수"""
    try:
        # 입력된 전화번호 가져오기
        phone_input = self.server_setting_ui.setting_notice_phone_num_input.text().strip()
        
        if not phone_input:
            self.create_fade_out_msg(std_window=self.server_setting_window, msg="전화번호를 입력해주세요")
            return

        # 최대 허용 전화번호 개수 체크
        current_phone_count = len(self.ai_server_info_dict["SETTING"]["sms"]["user"])
        max_allowed = self.ai_server_info_dict["ADMIN"]["sms_allow_phone_num"]
        
        if current_phone_count >= max_allowed:
            self.create_fade_out_msg(std_window=self.server_setting_window, msg=f"최대 전화번호 개수({max_allowed}개)를 초과했습니다")
            return
            
        # 전화번호 형식 검증 (정규표현식)
        # 1. XXX-XXXX-XXXX
        # 2. XXX.XXXX.XXXX
        # 3. XXXXXXXXXXX (11자리 숫자)
        pattern = r'^(\d{3}[-.]?\d{4}[-.]?\d{4})$'
        
        if not re.match(pattern, phone_input):
            self.create_fade_out_msg(std_window=self.server_setting_window, msg="올바른 전화번호 형식이 아닙니다")
            return
        
        # 전화번호를 숫자만 추출 (구분자 제거)
        phone_number = re.sub(r'[-.]', '', phone_input)
        
        # 이미 존재하는 전화번호인지 확인
        if phone_number in self.ai_server_info_dict["SETTING"]["sms"]["user"]:
            self.create_fade_out_msg(std_window=self.server_setting_window, msg="이미 등록된 전화번호입니다")
            return
        
        # 모든 detect_type 가져오기
        detect_types_dict = {}
        for detect_type in self.active_detect_types:
            detect_types_dict[detect_type] = 0
        
        # 전화번호 추가
        self.ai_server_info_dict["SETTING"]["sms"]["user"][phone_number] = detect_types_dict
        
        # 서버에 저장
        with open(os.path.join(os.getcwd(), "ai_sever_info.json"), "w", encoding="UTF-8") as f:
            json.dump(self.ai_server_info_dict, f, ensure_ascii=False, indent=4)
        update_setting(self)
        self.create_fade_out_msg(std_window=self.server_setting_window, msg="전화번호가 추가되었습니다")
        
    except Exception as e:
        print_error(e)

def del_notice_phone_number(click, self):
    """전화번호 삭제 함수"""
    try:
        selected_items = self.server_setting_ui.setting_notice_phone_list.selectedItems()
        
        if not selected_items:
            self.create_fade_out_msg(std_window=self.server_setting_window, msg="삭제할 전화번호를 선택해주세요")
            return
        
        # 선택된 행의 인덱스를 수집 (역순으로 정렬)
        selected_rows = []
        selected_phones = []
        
        for item in selected_items:
            row = self.server_setting_ui.setting_notice_phone_list.row(item)
            phone_number = item.text()
            selected_rows.append(row)
            selected_phones.append(phone_number)
        
        # setting_info_temp에서 전화번호 삭제
        for phone_number in selected_phones:
            if phone_number in self.ai_server_info_dict["SETTING"]["sms"]["user"]:
                del self.ai_server_info_dict["SETTING"]["sms"]["user"][phone_number]
        
        # 서버에 저장
        with open(os.path.join(os.getcwd(), "ai_sever_info.json"), "w", encoding="UTF-8") as f:
            json.dump(self.ai_server_info_dict, f, ensure_ascii=False, indent=4)
        
        update_setting(self)
        self.create_fade_out_msg(std_window=self.server_setting_window, msg="전화번호가 삭제되었습니다")
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : Deleted phone numbers: {selected_phones}")
    except Exception as e:
        print_error(e)

def load_notion_detect_type_button_states(click, self):
    """선택된 전화번호의 설정에 따라 버튼 상태 로드"""
    try:
        # 현재 선택된 전화번호 가져오기
        selected_row = self.server_setting_ui.setting_notice_phone_list.currentRow()
        
        if selected_row < 0:
            return
        
        phone_number = self.server_setting_ui.setting_notice_phone_list.item(selected_row, 0).text()
        
        # 전화번호가 존재하는지 확인
        if phone_number not in self.ai_server_info_dict["SETTING"]["sms"]["user"]:
            return
        
        # 레이아웃에서 모든 버튼 가져오기
        layout = self.server_setting_ui.setting_notion_detect_type_widget.layout()
        if layout is not None:
            for i in range(layout.count()):
                button = layout.itemAt(i).widget()
                if isinstance(button, QPushButton):
                    button_label = button.text()
                    detect_type = Kor2eng(button_label)
                    
                    # 버튼 상태 설정
                    if detect_type in self.ai_server_info_dict["SETTING"]["sms"]["user"][phone_number]:
                        is_active = self.ai_server_info_dict["SETTING"]["sms"]["user"][phone_number][detect_type] == 1
                        button.setChecked(is_active)
                    
    except Exception as e:
        print_error(e)

def alarm_memu_bnt_clicked(click, self):
    self.server_setting_ui.stackedWidget.setCurrentIndex(0)
    update_setting(self)
def admin_setting_but_clicked(click, self):
    self.server_setting_ui.stackedWidget.setCurrentIndex(1)
    update_setting(self)
def user_setting_bnt_clicked(click, self):
    self.server_setting_ui.stackedWidget.setCurrentIndex(2)
    update_setting(self)

def update_notion_detect_type_buttons(self):
        """알림 감지 타입 버튼들을 동적으로 생성"""
        try:
            # 기존 레이아웃의 모든 위젯 제거
            if self.server_setting_ui.setting_notion_detect_type_widget.layout() is not None:
                layout = self.server_setting_ui.setting_notion_detect_type_widget.layout()
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()
                # 기존 레이아웃 삭제
                QWidget().setLayout(layout)
            
            # 새 그리드 레이아웃 생성
            grid_layout = QGridLayout(self.server_setting_ui.setting_notion_detect_type_widget)
            grid_layout.setSpacing(10)
            grid_layout.setContentsMargins(0, 0, 0, 0)
                    
            # 2열로 버튼 배치
            for index, detect_type in enumerate(self.active_detect_types):
                row = index // 2
                col = index % 2
                
                # 버튼 생성
                button = QPushButton(Eng2kor(detect_type))
                button.setCheckable(True)
                button.setMinimumSize(QSize(60, 35))
                button.setMaximumSize(QSize(60, 35))

                button.setStyleSheet(
                    "QPushButton {\n"
                    "    color: rgb(255, 255, 255);\n"
                    "    background-color: rgb(36, 39, 44);\n"
                    "    border-radius: 5px;\n"
                    "}\n"
                    "QPushButton:checked {\n"
                    "    background-color: rgb(30, 195, 55);\n"
                    "}"
                )
                
                # 버튼 클릭 이벤트 연결 (버튼 객체도 함께 전달)
                button.clicked.connect(lambda checked, instance = self, dt=detect_type, btn=button: on_notion_detect_type_button_clicked(checked, instance, dt, btn))
                
                # 그리드에 버튼 추가
                grid_layout.addWidget(button, row, col)
            
            # 버튼 생성 후 현재 선택된 전화번호의 설정 로드
            load_notion_detect_type_button_states(True, self)
            
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : notion detect type buttons updated")
            
        except Exception as e:
            print_error(e)

def on_notion_detect_type_button_clicked(checked, self, detect_type, button):
        """알림 감지 타입 버튼 클릭 시 처리"""
        try:
            # 현재 선택된 전화번호 가져오기
            selected_items = self.server_setting_ui.setting_notice_phone_list.selectedItems()
            
            if not selected_items:
                self.create_fade_out_msg(std_window=self.server_setting_window, msg="전화번호를 선택해주세요")
                # 버튼 상태를 원래대로 되돌림
                button.setChecked(not checked)
                return
            
            # 선택된 행의 전화번호 가져오기
            selected_row = self.server_setting_ui.setting_notice_phone_list.currentRow()
            phone_number = self.server_setting_ui.setting_notice_phone_list.item(selected_row, 0).text()
            
            # setting_info_temp 업데이트
            if phone_number in self.ai_server_info_dict["SETTING"]["sms"]["user"]:
                self.ai_server_info_dict["SETTING"]["sms"]["user"][phone_number][detect_type] = 1 if checked else 0
                with open(os.path.join(os.getcwd(), "ai_sever_info.json"), "w", encoding="UTF-8") as f:
                    json.dump(self.ai_server_info_dict, f, ensure_ascii=False, indent=4)
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : Updated {phone_number} - {detect_type}: {1 if checked else 0}")
            else:
                self.create_fade_out_msg(std_window=self.server_setting_window, msg="전화번호 정보를 찾을 수 없습니다")
                # 버튼 상태를 원래대로 되돌림
                button.setChecked(not checked)
                
        except Exception as e:
            print_error(e)
            # 에러 발생 시에도 버튼 상태 복원
            button.setChecked(not checked)


def change_sms_alarm_fn(click, self):
    self.ai_server_info_dict["ADMIN"]["sms_active"] = 1 if self.ai_server_info_dict["ADMIN"]["sms_active"] == 0 else 0

def change_live_viewer_block_fn(click, self):
    self.ai_server_info_dict["ADMIN"]["live_viewer_block_active"] = 1 if self.ai_server_info_dict["ADMIN"]["live_viewer_block_active"] == 0 else 0

def save_admin_info(click, self):
    try:
        self.server_setting_ui.setting_sms_widget.show() if self.ai_server_info_dict["ADMIN"]["sms_active"] == 1 else self.server_setting_ui.setting_sms_widget.hide()

        # 텍스트를 정수로 변환하여 저장
        self.ai_server_info_dict["ADMIN"]["sms_allow_phone_num"] = int(self.server_setting_ui.admin_sms_alarm_allow_phone_num_input.text())
        self.ai_server_info_dict["ADMIN"]["live_viewer_block_active"] = self.server_setting_ui.admin_live_viewer_block_bnt.isChecked()

        with open(os.path.join(os.getcwd(), "ai_sever_info.json"), "w", encoding="UTF-8") as f:
            json.dump(self.ai_server_info_dict, f, ensure_ascii=False, indent=4)
        self.create_fade_out_msg(std_window=self.server_setting_window, msg="save admin info")

    except Exception as e:
        print_error(e)
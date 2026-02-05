import sys
import os
from pathlib import Path

from PySide6.QtWidgets import QDialog, QTableWidgetItem, QLabel, QToolButton, QVBoxLayout, QHBoxLayout, QSizePolicy, QWidget, QScrollArea, QGridLayout, QMenu, QFileDialog
from datetime import datetime, timedelta
from PySide6.QtCore import QDate, Qt, Signal, QRect, QSize, QEvent
from PySide6.QtGui import  QImage, QPixmap, QFont, QAction

from requests.auth import HTTPBasicAuth
import requests
from utils import Connect_Playback, save_info, get_datetime_from_path, get_datetime_from_list

from ui.ui_search import Ui_Search_window
import cv2
import numpy as np 
import base64
from io import BytesIO
import traceback
import math

from utils import Eng2kor
import resourece_rc

ALARM_TYPE_DIC = {2 : "침입", 1 : "배회", 6 : "쓰러짐", 4 : "방화", 7 : "싸움", 5 : "무단투기"}

class SearchPageViewer(QLabel):
    Checked = Signal(QLabel)
    def __init__(self, base_viewer, camera_name, name_label, main_instance, search_instance):
        super().__init__(base_viewer)

        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy2)

        self.setScaledContents(True)
        
        # 부모 위젯의 전체 크기를 채우도록 설정
        self.setGeometry(0, 0, base_viewer.width(), base_viewer.height())

        self.checked = False
        self.camera_name = camera_name
        self.name_label = name_label

        self.main_instance = main_instance
        self.search_instance = search_instance

        self.frame_flag = False
        
        # 부모 위젯 크기 변경 시 자동으로 리사이즈되도록 이벤트 필터 설치
        base_viewer.installEventFilter(self)

    def setChecked(self, checked):
        # for camera_name, camera_viewer in self.search_instance.search_page_camera_view_list.items():
            # if camera_viewer.checked:
            #     camera_viewer.checked = False
            #     camera_viewer.updateStyle()
                
        self.checked = checked
        self.updateStyle()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setChecked(not self.checked)

    def enterEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.setChecked(True)
    
    def eventFilter(self, obj, event):
        # 부모 위젯의 리사이즈 이벤트를 감지하여 자신도 리사이즈
        if event.type() == QEvent.Resize:
            self.setGeometry(0, 0, obj.width(), obj.height())
        return super().eventFilter(obj, event)
            
    def updateStyle(self):
            if self.checked:
                if self.frame_flag:
                    self.setStyleSheet("""
                        QLabel {
                            border: 2px solid rgb(56, 188, 56);
                        }
                    """)

                    self.set_img(self.frame, 1)
                    self.name_label.setStyleSheet("""
                            QLabel {
                                        color: rgb(56, 188, 56);
                                        border: 1px solid rgb(56, 188, 56);
                                    }
                                """)
            else:
                if self.frame_flag:
                    self.setStyleSheet("""
                        QLabel {
                            border: 1px solid rgb(119, 118, 123);
                        }
                    """)
                    self.set_img(self.frame, 0.5)
                    # self.ai_check_box.setPixmap(self.ai_off_img)
                    self.name_label.setStyleSheet("""
                            QLabel {
                                        color: rgb(255, 255, 255);
                                        border: 1px solid rgb(119, 118, 123);
                                    }
                                """)

    def set_img(self, img, brightness = 1):
        self.frame_flag = True
        self.frame = img.copy()
        cv_image = self.frame.astype('float32')
        cv_image = cv_image * brightness
        cv_image = np.clip(cv_image, 0, 255)
        cv_image = cv_image.astype('uint8')

        height, width, channels = cv_image.shape
        # Calculate the number of bytes per line.
        bytes_per_line = width * channels
        # Convert image from BGR (cv2 default color format) to RGB (Qt default color format).
        cv_rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        # print(cv_rgb_image.shape)
        # Convert the image to Qt format.
        qt_rgb_image = QImage(cv_rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)

        self.setPixmap(QPixmap.fromImage(qt_rgb_image))

def create_search_camera_grid_page(search_ui, page_index, camera_list, main_instance, search_instance):
    """
    4x4 그리드 레이아웃으로 검색 카메라 뷰를 생성하는 함수
    항상 16개 칸을 생성하며, 빈 칸은 비활성화 상태로 표시됨
    
    Args:
        search_ui: UI 인스턴스
        page_index: 페이지 인덱스 (0부터 시작)
        camera_list: 이 페이지에 표시할 카메라 정보 리스트 [(camera_name, camera_info), ...]
        main_instance: 메인 인스턴스
        search_instance: 검색 다이얼로그 인스턴스
    
    Returns:
        page_widget: 생성된 페이지 위젯
        camera_views: 생성된 카메라 뷰 딕셔너리 {camera_name: SearchPageViewer}
    """
    # 페이지 위젯 생성
    page_widget = QWidget()
    page_widget.setObjectName(f"search_page_{page_index}")
    
    # 메인 레이아웃
    main_layout = QHBoxLayout(page_widget)
    main_layout.setSpacing(0)
    main_layout.setContentsMargins(0, 0, 0, 0)
    
    # 그리드 레이아웃을 담을 위젯
    grid_widget = QWidget(page_widget)
    grid_widget.setObjectName(f"search_grid_widget_{page_index}")
    
    grid_layout = QGridLayout(grid_widget)
    grid_layout.setSpacing(0)
    grid_layout.setContentsMargins(-1, 0, 0, 0)
    
    # 그리드의 각 행과 열에 균등한 stretch 설정
    for i in range(4):
        grid_layout.setRowStretch(i, 1)
        grid_layout.setColumnStretch(i, 1)
    
    camera_views = {}
    
    # 항상 4x4 (16칸) 그리드 생성
    for idx in range(16):
        row = idx // 4
        col = idx % 4
        
        # VBoxLayout 생성
        camera_layout = QVBoxLayout()
        camera_layout.setSpacing(0)
        camera_layout.setObjectName(f"search_camera_view_layout_{page_index}_{idx}")
        
        # 카메라가 있는 경우
        if idx < len(camera_list):
            camera_name, camera_info = camera_list[idx]
            
            # 카메라 이름 라벨 생성
            name_label = QLabel(grid_widget)
            name_label.setObjectName(f"camera_view_name_{page_index}_{idx}")
            
            sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
            sizePolicy.setHeightForWidth(name_label.sizePolicy().hasHeightForWidth())
            name_label.setSizePolicy(sizePolicy)
            name_label.setMaximumSize(QSize(722, 20))
            
            font = QFont()
            font.setFamilies(["NanumSquareRound"])
            font.setPointSize(11)
            font.setBold(False)
            name_label.setFont(font)
            name_label.setStyleSheet(
                "color: rgb(255, 255, 255);\n"
                "background-color: rgba(0, 0, 0, 170);\n"
                "border: 1px solid rgb(119, 118, 123);"
            )
            name_label.setMargin(0)
            name_label.setIndent(15)
            name_label.setText(camera_name)
            
            camera_layout.addWidget(name_label)
            
            # 카메라 뷰 라벨 생성 (실제 영상이 표시될 부분)
            view_label = QLabel(grid_widget)
            view_label.setObjectName(f"camera_view_{page_index}_{idx}")
            
            sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            sizePolicy1.setHeightForWidth(view_label.sizePolicy().hasHeightForWidth())
            view_label.setSizePolicy(sizePolicy1)
            
            font2 = QFont()
            font2.setFamilies(["NanumBarunGothic"])
            font2.setPointSize(16)
            view_label.setFont(font2)
            view_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
            view_label.setStyleSheet(
                "border: 1px solid rgb(119, 118, 123);\n"
                "color: rgb(255, 255, 255);"
            )
            view_label.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
            view_label.setScaledContents(False)
            view_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            camera_layout.addWidget(view_label)
            
            # SearchPageViewer 인스턴스 생성 (view_label 위에 오버레이)
            camera_view = SearchPageViewer(
                base_viewer=view_label,
                camera_name=camera_name,
                name_label=name_label,
                main_instance=main_instance,
                search_instance=search_instance
            )
            
            camera_views[camera_name] = camera_view
        
        else:
            # 빈 칸 - 카메라가 없는 경우
            # 빈 이름 라벨 생성 (공간 유지용)
            name_label = QLabel(grid_widget)
            name_label.setObjectName(f"empty_camera_view_name_{page_index}_{idx}")
            
            sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
            sizePolicy.setHeightForWidth(name_label.sizePolicy().hasHeightForWidth())
            name_label.setSizePolicy(sizePolicy)
            name_label.setMaximumSize(QSize(722, 20))
            
            name_label.setStyleSheet(
                "color: rgb(100, 100, 100);\n"
                "background-color: rgba(0, 0, 0, 170);\n"
                "border: 1px solid rgb(119, 118, 123);"
            )
            name_label.setMargin(0)
            name_label.setIndent(15)
            name_label.setText("")
            
            camera_layout.addWidget(name_label)
            
            # 빈 뷰 라벨 생성 (비활성화 상태)
            view_label = QLabel(grid_widget)
            view_label.setObjectName(f"empty_camera_view_{page_index}_{idx}")
            
            sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            sizePolicy1.setHeightForWidth(view_label.sizePolicy().hasHeightForWidth())
            view_label.setSizePolicy(sizePolicy1)
            
            view_label.setStyleSheet(
                "border: 1px solid rgb(119, 118, 123);\n"
                "color: rgb(100, 100, 100);\n"
                "background-color: rgba(30, 30, 30, 100);"
            )
            view_label.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
            view_label.setScaledContents(False)
            view_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            # 클릭 이벤트 비활성화
            view_label.setAttribute(Qt.WA_TransparentForMouseEvents, True)
            view_label.setEnabled(False)
            
            camera_layout.addWidget(view_label)
        
        # 그리드 레이아웃에 추가
        grid_layout.addLayout(camera_layout, row, col, 1, 1)
    
    main_layout.addWidget(grid_widget)
    
    return page_widget, camera_views

class SearchDialog(QDialog):
    def __init__(self, parent=None, camera_name=None, alarm_time=None):
        super().__init__(parent)

        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : open search window")
        self.search_page_worker = None
        # self.search_window = QDialog()  # QDialog 인스턴스 생성
        self.search_ui = Ui_Search_window()
        self.search_ui.setupUi(self)
        self.parent = parent

        self.search_ui.event_search_bnt.hide()

        # 메인 윈도우의 중앙에 팝업 윈도우 위치 계산
        mainWindowGeometry = self.parent.frameGeometry()
        centerPoint = mainWindowGeometry.center() - self.rect().center()
        self.move(centerPoint.x(), centerPoint.y())

        self.switch_event_search_page()
        self.search_ui.stackedWidget.setCurrentIndex(0)
        self.search_ui.page_undo_bnt.clicked.connect(lambda: self.search_ui.stackedWidget.setCurrentIndex(0))

        self.search_ui.time_day_start_input.setDate(QDate.currentDate())
        self.search_ui.time_day_end_input.setDate(QDate.currentDate())
        self.search_ui.time_hour_end_box.setCurrentText("23:59")

        self.search_page_camera_view_list = {}
        self.search_current_page = 0

        save_info(host=self.parent.ai_server_ip, port=self.parent.ai_server_port, file_name="camera_info", info=self.parent.ai_server_camera_info_dict)

        # 카메라 리스트를 정렬 self.ui_main.camera_list_table 순서 기준
        camera_items = []
        for row in range(self.parent.ui_main.camera_list_table.rowCount()):
            camera_name = self.parent.ui_main.camera_list_table.item(row, 1).text()
            # 해당 카메라의 nvr_ip를 찾고, camera_info를 가져옴
            nvr_ip = self.parent.find_nvr_ip(camera_name)
            if nvr_ip and camera_name in self.parent.ai_server_camera_info_dict[nvr_ip]:
                camera_info = self.parent.ai_server_camera_info_dict[nvr_ip][camera_name]
                camera_items.append((camera_name, camera_info))
        
        # 카메라 개수에 따라 페이지 수 계산 (16개씩)
        total_cameras = len(camera_items)
        cameras_per_page = 16
        total_pages = max(1, math.ceil(total_cameras / cameras_per_page))  # 최소 1페이지
        
        # stackedWidget_4의 기존 페이지 모두 제거
        while self.search_ui.stackedWidget_4.count() > 0:
            widget = self.search_ui.stackedWidget_4.widget(0)
            self.search_ui.stackedWidget_4.removeWidget(widget)
            if widget:
                widget.deleteLater()
        
        # 각 페이지 생성
        for page_idx in range(total_pages):
            start_idx = page_idx * cameras_per_page
            end_idx = min(start_idx + cameras_per_page, total_cameras)
            page_cameras = camera_items[start_idx:end_idx]
            
            # 4x4 그리드 페이지 생성 (카메라가 없어도 빈 그리드 생성)
            page_widget, camera_views = create_search_camera_grid_page(
                self.search_ui, 
                page_idx, 
                page_cameras, 
                self.parent,
                self
            )
            
            # stackedWidget에 페이지 추가
            self.search_ui.stackedWidget_4.addWidget(page_widget)
            
            # 카메라 뷰 리스트에 추가
            self.search_page_camera_view_list.update(camera_views)
        
        # 카메라 이미지 설정
        for camera_name, camera_viewer in self.search_page_camera_view_list.items():
            if camera_name in self.parent.camera_img_temp.keys():
                img = self.parent.camera_img_temp[camera_name]
                # frame = cv2.resize(img, (camera_viewer.width(), camera_viewer.height()))
                camera_viewer.set_img(img, 0.5)
            else:
                camera_viewer.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
                camera_viewer.setAlignment(Qt.AlignCenter)
        
        # 페이지 네비게이션 버튼 연결
        self.search_ui.search_camera_next_page_bnt_2.clicked.connect(lambda: self.change_search_page(1))
        self.search_ui.search_camera_undo_page_bnt_2.clicked.connect(lambda: self.change_search_page(-1))
        
        # 페이지 네비게이션 버튼 표시/숨김 처리
        self.update_search_page_navigation_buttons(total_pages)

        self.search_ui.event_table.setColumnWidth(0, 30)
        self.search_ui.event_table.setColumnWidth(1, 120)
        self.search_ui.event_table.setColumnWidth(2, 80)

        # event_table 컨텍스트 메뉴 설정(보고서 작성 기능 잠시 억제)
        """self.search_ui.event_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.search_ui.event_table.customContextMenuRequested.connect(self.show_event_table_context_menu)"""

        self.search_detect_type = []

        for detect_type in self.parent.admin_info_temp["LICENSE"]["detect_type"]:
            if self.parent.admin_info_temp["LICENSE"]["detect_type"][detect_type] == 1:
                self.search_ui.event_box.addItems([Eng2kor(detect_type)])
                self.search_detect_type.append(Eng2kor(detect_type))

        # self.search_ui.event_search_bnt.clicked.connect(lambda click, instance = self : get_alarm_info(click, instance))
        self.search_ui.search_bnt.clicked.connect(self.get_alarm_info)

        # self.search_ui.event_table.itemDoubleClicked.connect(lambda click, instance = self : search_viewer_playback(click, instance))
        self.search_ui.event_table.itemDoubleClicked.connect(self.search_viewer_playback)

        self.search_ui.time_day_start_input.installEventFilter(self.parent)
        self.search_ui.time_day_end_input.installEventFilter(self.parent)

        # self.search_ui.close_bnt.clicked.connect(lambda click, instance = self : search_close_window(click, instance))
        self.search_ui.close_bnt.clicked.connect(self.search_close_window)
        self.search_ui.camera_select_all_bnt.clicked.connect(self.select_all_camera)

        self.search_ui.event_search_bnt.clicked.connect(self.switch_event_search_page)

        self.search_ui.camera_select_undo_bnt.clicked.connect(lambda checked: self.search_ui.stackedWidget.setCurrentIndex(0))

    def change_search_page(self, direction):
        """
        검색 페이지를 변경하는 함수
        
        Args:
            direction: 1 (다음 페이지) 또는 -1 (이전 페이지)
        """
        total_pages = self.search_ui.stackedWidget_4.count()
        new_page = self.search_current_page + direction
        
        # 페이지 범위 체크
        if 0 <= new_page < total_pages:
            self.search_current_page = new_page
            self.search_ui.stackedWidget_4.setCurrentIndex(new_page)
            self.update_search_page_navigation_buttons(total_pages)
    
    def update_search_page_navigation_buttons(self, total_pages):
        """
        검색 페이지 네비게이션 버튼의 표시/숨김을 업데이트하는 함수
        
        Args:
            total_pages: 전체 페이지 수
        """
        # 페이지가 1개면 네비게이션 버튼 숨김
        if total_pages <= 1:
            self.search_ui.search_camera_next_page_bnt_2.hide()
            self.search_ui.search_camera_undo_page_bnt_2.hide()
        else:
            # 첫 페이지면 이전 버튼 숨김
            if self.search_current_page == 0:
                self.search_ui.search_camera_undo_page_bnt_2.hide()
            else:
                self.search_ui.search_camera_undo_page_bnt_2.show()
            
            # 마지막 페이지면 다음 버튼 숨김
            if self.search_current_page == total_pages - 1:
                self.search_ui.search_camera_next_page_bnt_2.hide()
            else:
                self.search_ui.search_camera_next_page_bnt_2.show()

    def switch_event_search_page(self):
        self.search_ui.event_search_bnt.setStyleSheet("""
                                                    background-color: rgb(30, 195, 55);
                                                    color: rgb(255, 255, 255);
                                                    border-radius: 10px;
                                                    """)
        
        if self.search_page_worker is not None:
            self.search_page_worker.stop()  # 기존 쓰레드를 종료
            self.search_page_worker.wait()  # 종료를 기다림
            self.search_page_worker = None  # 참조를 해제

    def select_all_camera(self):
        all_check_flag = False
        for camera_name, camera_viewer in self.search_page_camera_view_list.items():
            if camera_viewer.checked == False:
                camera_viewer.setChecked(True)
                all_check_flag = True

        if all_check_flag == False:
            for camera_name, camera_viewer in self.search_page_camera_view_list.items():
                camera_viewer.setChecked(False)


    def get_alarm_info(self, click):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : get alarm info")

        self.search_ui.event_table.setRowCount(0)

        day_start = self.search_ui.time_day_start_input.text()
        start_day = datetime.strptime(day_start, "%Y. %m. %d").strftime("%Y-%m-%d")

        day_end = self.search_ui.time_day_end_input.text()
        end_day = datetime.strptime(day_end, "%Y. %m. %d").strftime("%Y-%m-%d")

        time_start = self.search_ui.time_hour_start_box.currentText()
        time_end = self.search_ui.time_hour_end_box.currentText()

        time_start += ":00"
        time_end += ":00"

        time_start = datetime.strptime(time_start, "%H:%M:%S").strftime("%H:%M:%S")

        time_end = datetime.strptime(time_end, "%H:%M:%S").strftime("%H:%M:%S")

        order = 0 if self.search_ui.sort_box.currentText() == "최신순" else 1

        nvr_camera_name_dict = {}
        
        for camera_name, camera_viewer in self.search_page_camera_view_list.items():
            if camera_viewer.checked == True:
                for nvr_ip, nvr_camera_info in self.parent.ai_server_camera_info_dict.items():
                    if camera_name in nvr_camera_info.keys():
                        if nvr_ip not in nvr_camera_name_dict.keys():
                            nvr_camera_name_dict[nvr_ip] = {}
                        nvr_camera_name_dict[nvr_ip][str(int(nvr_camera_info[camera_name]["camera_id"])-1)] = camera_name
                        

        search_detect_type_temp = self.search_detect_type if self.search_ui.event_box.currentText() == "전체" else self.search_ui.event_box.currentText()

        detect_type_list = []

        if search_detect_type_temp != "전체":
            for index, detect_type in ALARM_TYPE_DIC.items():
                if search_detect_type_temp == detect_type:
                    detect_type_list.append(index)
                    break
        else:
            detect_type_list = [0]
        
            """
            types: event types (default: *, start from 0)
            devices : device numbers (default: *, start from 0)
            sort : sort type (default: 0, see below)
            since : YYYY-MM-DD or YYYY-MM-DDtHH:MM:SS format (default: NULL)
            until : YYYY-MM-DD or YYYY-MM-DDtHH:MM:SS format (default: NULL)
            limit : the maximum number of search result (default: 10, 1~1000)
            total : get the total number of events (default: false) (slower)
            offset : the offset of search result (default: 0)
            last : last rowid/timestamp of search result (default: NULL) (ex: rowid:12345678,timestamp:1531094400)
            Event types and device numbers can be described like 0,3-4,7.
            For example, you can request a search like:

            http://192.168.1.100/api/events?types=0,3-4,7&since=2020-01-01t00:00:00&until=2020-01-01t23:59:59&devices=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15&sort=0

            """
        event_info_ori_list = []
        camera_id_input = ""

        for nvr_ip, camera_id_list in nvr_camera_name_dict.items():
            for camera_id in camera_id_list.keys():
                camera_id_input += f"{camera_id},"

            auth = HTTPBasicAuth(self.parent.ai_server_info_dict["NVR"][nvr_ip]["id"], self.parent.ai_server_info_dict["NVR"][nvr_ip]["pw"]) # NVR에 대한 ID / PW
            event_info_post = f'http://{nvr_ip}/api/events?types=70&since={start_day}t{time_start}&until={end_day}t{time_end}&devices={camera_id_input}&sort={order}&total=true&limit=1000&micro_ai_type={detect_type_list}'
            r = requests.get(event_info_post, auth=auth, timeout= 1)
            """r.json() =>
            {'total': 2, 'offset': 0, 'limit': 10, 
            'events': [
                {'type': 70, 'timestamp': 1761121687, 'rowid': 151944, 'devices': [0], 'micro_ai': {'type': 2, 'object': 1, 'direction': 0}}, 
                {'type': 70, 'timestamp': 1761121687, 'rowid': 151943, 'devices': [0], 'micro_ai': {'type': 2, 'object': 1, 'direction': 0}}, 
            """
            if r.status_code == 200:
                # 데이터 파싱
                for event_info in r.json()["events"]:
                    camera_name = camera_id_list[str(event_info["devices"][0])]
                    detect_time = datetime.fromtimestamp(event_info["timestamp"]).strftime("%y.%m.%d %H:%M:%S")
                    # .get()을 사용하여 키가 없는 경우에도 안전하게 처리
                    alarm_type = ALARM_TYPE_DIC.get(event_info.get("micro_ai", {}).get("type"), "Unknown Type")
                    event_info_ori_list.append({"camera_name": camera_name, "detect_time": detect_time, "alarm_type": alarm_type})

        order = 1 if self.search_ui.sort_box.currentText() == "최신순" else 0

        event_info_ori_list.sort(key=lambda x: x['detect_time'], reverse=order)
        print(event_info_ori_list)

        for row_position, event_info in enumerate(event_info_ori_list):
            self.search_ui.event_table.insertRow(row_position)
            
            # 0번 열: 순번 (정렬 후 순번)
            item_num = QTableWidgetItem(str(row_position + 1))
            item_num.setTextAlignment(Qt.AlignCenter)
            item_num.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.search_ui.event_table.setItem(row_position, 0, item_num)

            # 1번 열: 카메라 이름
            item_cam = QTableWidgetItem(str(event_info["camera_name"]))
            item_cam.setTextAlignment(Qt.AlignCenter)
            item_cam.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.search_ui.event_table.setItem(row_position, 1, item_cam)

            # 2번 열: 알람 타입
            item_alarm = QTableWidgetItem(str(event_info["alarm_type"]))
            item_alarm.setTextAlignment(Qt.AlignCenter)
            item_alarm.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.search_ui.event_table.setItem(row_position, 2, item_alarm)

            # 3번 열: 감지 시간
            item_time = QTableWidgetItem(str(event_info["detect_time"]))
            item_time.setTextAlignment(Qt.AlignCenter)
            item_time.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.search_ui.event_table.setItem(row_position, 3, item_time)

        #     # 카메라 이름 찾기 (기존 로직과 동일)
        #     camera_name = "Unknown"  # 기본값
        #     for nvr_ip, camera_id_list in nvr_camera_name_dict.items():
        #         if str(event_info["devices"][0]) in camera_id_list.keys():
        #             camera_name = camera_id_list[str(event_info["devices"][0])]
        #             break

        #     # 데이터 파싱
        #     detect_time = datetime.fromtimestamp(event_info["timestamp"]).strftime("%y.%m.%d %H:%M:%S")
        #     # .get()을 사용하여 키가 없는 경우에도 안전하게 처리
        #     alarm_type = ALARM_TYPE_DIC.get(event_info.get("micro_ai", {}).get("type"), "Unknown Type")

        #     # 테이블 아이템 생성 및 설정 (기존 로직과 동일)
            
        #     # 0번 열: 순번 (정렬 후 순번)
        #     item_num = QTableWidgetItem(str(row_position + 1))
        #     item_num.setTextAlignment(Qt.AlignCenter)
        #     item_num.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        #     self.search_ui.event_table.setItem(row_position, 0, item_num)

        #     # 1번 열: 카메라 이름
        #     item_cam = QTableWidgetItem(str(camera_name))
        #     item_cam.setTextAlignment(Qt.AlignCenter)
        #     item_cam.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        #     self.search_ui.event_table.setItem(row_position, 1, item_cam)

        #     # 2번 열: 알람 타입
        #     item_alarm = QTableWidgetItem(str(alarm_type))
        #     item_alarm.setTextAlignment(Qt.AlignCenter)
        #     item_alarm.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        #     self.search_ui.event_table.setItem(row_position, 2, item_alarm)

        #     # 3번 열: 감지 시간
        #     item_time = QTableWidgetItem(str(detect_time))
        #     item_time.setTextAlignment(Qt.AlignCenter)
        #     item_time.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        #     self.search_ui.event_table.setItem(row_position, 3, item_time)

        self.parent.create_fade_out_msg(std_window=self, msg="이벤트 검색 완료")

    def search_viewer_playback(self, click):
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : play alarm video")

            if self.search_page_worker is not None:
                self.search_page_worker.stop()  # 기존 쓰레드를 종료
                self.search_page_worker.wait()  # 종료를 기다림
                self.search_page_worker = None  # 참조를 해제

            selected_indexes = self.search_ui.event_table.selectedIndexes()

            if selected_indexes:
                selected_row = selected_indexes[0].row()

                camera_name = self.search_ui.event_table.item(selected_row, 1).text()
                detect_type = self.search_ui.event_table.item(selected_row, 2).text()

                video_time = self.search_ui.event_table.item(selected_row, 3).text()
                video_time = datetime.strptime(video_time, "%y.%m.%d %H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")

                video_time_start = datetime.strptime(video_time, "%Y-%m-%dT%H:%M:%S") - timedelta(seconds=5)
                video_time_start = video_time_start.strftime("%Y-%m-%dT%H:%M:%S")
                video_time_end = datetime.strptime(video_time, "%Y-%m-%dT%H:%M:%S") + timedelta(seconds=5)
                video_time_end = video_time_end.strftime("%Y-%m-%dT%H:%M:%S")

                streaming_nvr_ip = None

                for nvr_ip, nvr_camera_info in self.parent.ai_server_camera_info_dict.items():
                    if camera_name in nvr_camera_info.keys():
                        streaming_nvr_ip = nvr_ip
                        camera_num = int(nvr_camera_info[camera_name]["camera_id"])
                        break

                if streaming_nvr_ip is None:
                    self.parent.create_fade_out_msg(std_window=self, msg="스트리밍 중인 NVR를 찾을 수 없습니다.")
                    return

                # /playback/videoN?start=START&end=END&speed=SPEED
                # /playback/videoN?start=2021-01-20T15:14:00&end=2021-01-20T15:24:00&speed=1.0

                rtsp_url = f'{self.parent.ai_server_info_dict["NVR"][streaming_nvr_ip]["id"]}:{self.parent.ai_server_info_dict["NVR"][streaming_nvr_ip]["pw"]}@{streaming_nvr_ip}/playback/video{camera_num}?start={video_time_start}&end={video_time_end}&speed={self.search_ui.time_video_time_speed_input.text()}'

                viewer = self.search_ui.search_viewer
                self.search_page_worker = Connect_Playback(rtsp_url, viewers_widget = viewer)

                self.search_page_worker.ImageUpdated.connect(lambda image, viewer=viewer: self.parent.ShowCamera(viewer, image))
                self.search_page_worker.start()
    
                self.search_ui.stackedWidget.setCurrentIndex(1)
                self.parent.create_fade_out_msg(std_window=self, msg="이벤트 재생 시작")

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    # def search_close_window(click, self):
    def search_close_window(self, click):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : close search window")

        self.close()

        if self.search_page_worker is not None:
            self.search_page_worker.stop()  # 기존 쓰레드를 종료
            self.search_page_worker.wait()  # 종료를 기다림
            self.search_page_worker = None  # 참조를 해제

    def show_event_table_context_menu(self, pos):
        """이벤트 테이블 컨텍스트 메뉴 표시"""
        # 선택된 행이 있는지 확인
        selected_items = self.search_ui.event_table.selectedItems()
        if not selected_items:
            return
        
        # 선택된 행의 정보 가져오기
        selected_indexes = self.search_ui.event_table.selectedIndexes()
        selected_row = selected_indexes[0].row()
        
        camera_name = self.search_ui.event_table.item(selected_row, 1).text()
        alarm_type = self.search_ui.event_table.item(selected_row, 2).text()
        detect_time = self.search_ui.event_table.item(selected_row, 3).text()
        
        # 보고서 존재 여부 확인
        report_exists = self.check_report_exists(camera_name, alarm_type, detect_time)
        
        # QMenu 생성
        context_menu = QMenu(self)
        context_menu.setStyleSheet("""
            QMenu {
                font-size: 11pt;
                color: rgb(255, 255, 255);
                background-color: rgb(45, 45, 45);
            }
            QMenu::item {
                padding: 5px 20px;
            }
            QMenu::item:hover {
                background-color: rgba(0, 196, 0, 255);
            }
            QMenu::item:selected {
                background-color: rgba(0, 196, 0, 255);
            }
            QMenu::item:disabled {
                color: rgb(120, 120, 120);
                background-color: transparent;
            }
        """)

        # 메뉴 항목 추가
        write_report_action = QAction("이벤트 보고서 작성 요청", self)
        download_report_action = QAction("이벤트 보고서 다운로드", self)

        # 보고서 존재 여부에 따라 활성화/비활성화
        if report_exists:
            # 보고서가 존재하면 다운로드 활성화
            download_report_action.setEnabled(True)
            # 작성 요청도 활성화 (재생성 가능하도록)
            write_report_action.setEnabled(True)
        else:
            # 보고서가 없으면 다운로드 비활성화
            download_report_action.setEnabled(False)
            # 작성 요청만 활성화
            write_report_action.setEnabled(True)

        # 메뉴에 항목 추가
        context_menu.addAction(write_report_action)
        context_menu.addAction(download_report_action)

        # 메뉴 항목에 기능 연결
        write_report_action.triggered.connect(self.write_report)
        download_report_action.triggered.connect(self.download_report)
        
        # 컨텍스트 메뉴를 마우스 클릭 위치에 표시
        context_menu.exec(self.search_ui.event_table.viewport().mapToGlobal(pos))

    def check_report_exists(self, camera_name, alarm_type, detect_time):
        """보고서가 존재하는지 확인"""
        try:
            # detect_time 형식 변환: "25.10.30 10:36:36" -> "2025-10-30T10-36-36"
            dt = datetime.strptime(detect_time, "%y.%m.%d %H:%M:%S")
            detect_time_formatted = dt.strftime("%Y-%m-%dT%H-%M-%S")
            
            # 보고서 파일 경로 생성 (카메라 이름의 공백을 언더스코어로 변경)
            camera_name_formatted = camera_name.replace(" ", "_")
            
            # API로 보고서 존재 여부 확인
            url = f'http://{self.parent.HOST}:{self.parent.PORT}/check_report_exists'
            data = {
                "msg": {
                    "camera_name": camera_name_formatted,
                    "detect_time": detect_time_formatted
                }
            }
            
            response = requests.get(url, json=data, timeout=2)
            if response.status_code == 200:
                result = response.json()
                return result.get("exists", False)
            
            return False
        except Exception as e:
            print(f"보고서 확인 중 오류 발생: {e}")
            # API 오류 시 로컬 파일 시스템 체크 (대체 방법)
            import os
            report_path = os.path.join("..", "backup", "trash_data", "report", f"{camera_name_formatted}_{detect_time_formatted}.pdf")
            return os.path.exists(report_path)

    def download_report(self):
        """선택된 이벤트의 보고서 다운로드"""

        report_save_path = QFileDialog.getExistingDirectory(self, "보고서 저장 위치 선택")
        if not report_save_path:
            print("보고서 저장 위치를 선택하지 않았습니다.")
            return

        selected_indexes = self.search_ui.event_table.selectedIndexes()
        
        selected_row = selected_indexes[0].row()
        camera_name = self.search_ui.event_table.item(selected_row, 1).text()
        alarm_type = self.search_ui.event_table.item(selected_row, 2).text()
        detect_time = self.search_ui.event_table.item(selected_row, 3).text()

        camera_name_formatted = camera_name.replace(" ", "_")

        dt = datetime.strptime(detect_time, "%y.%m.%d %H:%M:%S")
        detect_time_formatted = dt.strftime("%Y-%m-%dT%H-%M-%S")

        url = f'http://{self.parent.HOST}:{self.parent.PORT}/download_report'
        data = {
            "msg": {
                "camera_name": camera_name_formatted,
                "detect_time": detect_time_formatted
            }
        }
        response = requests.get(url, json=data, timeout=30)
        if response.status_code == 200:
            response_data = response.json()
            if response_data.get("exists", False):
                image_buffer = response_data.get("image", [])
                
                if not image_buffer:
                    print("이미지 데이터가 없습니다.")
                    self.parent.create_fade_out_msg(std_window=self, msg="보고서 이미지가 없습니다.")
                    return
                
                # 이미지 저장
                saved_files = []
                for i, image_base64 in enumerate(image_buffer):
                    try:
                        # base64 문자열을 bytes로 디코딩
                        image_bytes = base64.b64decode(image_base64)
                        # bytes를 numpy array로 변환
                        image_array = np.frombuffer(image_bytes, np.uint8)
                        # numpy array를 이미지로 디코딩
                        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
                        
                        if image is not None:
                            # 저장 경로 생성
                            save_filename = f"{camera_name_formatted}_{detect_time_formatted}_{i+1}.png"
                            save_path = os.path.join(report_save_path, save_filename)
                            cv2.imwrite(save_path, image)
                            saved_files.append(save_filename)
                            print(f"이미지 저장 완료: {save_path}")
                        else:
                            print(f"이미지 {i+1} 디코딩 실패")
                    except Exception as e:
                        print(f"이미지 {i+1} 처리 중 오류: {e}")
                        traceback.print_exc()
                
                if saved_files:
                    self.parent.create_fade_out_msg(
                        std_window=self, 
                        msg=f"보고서 다운로드 완료\n{len(saved_files)}개 이미지 저장\n위치: {report_save_path}"
                    )
                    print(f"보고서 다운로드 완료: {len(saved_files)}개 파일")
                else:
                    self.parent.create_fade_out_msg(std_window=self, msg="이미지 저장 실패")
            else:
                print("보고서가 존재하지 않습니다.")
                self.parent.create_fade_out_msg(std_window=self, msg="보고서가 존재하지 않습니다.")
        else:
            print(f"보고서 다운로드 실패: 상태 코드 {response.status_code}")
            self.parent.create_fade_out_msg(std_window=self, msg=f"보고서 다운로드 실패\n상태 코드: {response.status_code}")

        # try:
        #     # detect_time 형식 변환: "25.10.30 10:36:36" -> "2025-10-30T10-36-36"
        #     dt = datetime.strptime(detect_time, "%y.%m.%d %H:%M:%S")
        #     detect_time_formatted = dt.strftime("%Y-%m-%dT%H-%M-%S")
            
        #     camera_name_formatted = camera_name.replace(" ", "_")
            
        #     # 저장 위치 선택
        #     default_filename = f"{camera_name_formatted}_{detect_time_formatted}_보고서.pdf"
        #     save_path, _ = QFileDialog.getSaveFileName(
        #         self, 
        #         "보고서 저장", 
        #         default_filename, 
        #         "PDF Files (*.pdf)"
        #     )
            
        #     if not save_path:
        #         print("저장 위치를 선택하지 않았습니다.")
        #         return
            
        #     # API로 보고서 다운로드 요청
        #     url = f'http://{self.parent.HOST}:{self.parent.PORT}/download_report'
        #     data = {
        #         "msg": {
        #             "camera_name": camera_name_formatted,
        #             "detect_time": detect_time_formatted
        #         }
        #     }
            
        #     response = requests.get(url, json=data, timeout=30)
            
        #     if response.status_code == 200:
        #         # 파일로 저장
        #         with open(save_path, 'wb') as f:
        #             f.write(response.content)
                
        #         self.parent.create_fade_out_msg(std_window=self, msg=f"보고서 다운로드 완료\n저장 위치: {save_path}")
        #         print(f"보고서 다운로드 완료: {save_path}")
        #     else:
        #         self.parent.create_fade_out_msg(std_window=self, msg=f"보고서 다운로드 실패\n상태 코드: {response.status_code}")
        #         print(f"보고서 다운로드 실패: {response.status_code}")
                
        # except Exception as e:
        #     print(f"보고서 다운로드 오류: {e}")
        #     traceback.print_exc()
        #     self.parent.create_fade_out_msg(std_window=self, msg=f"보고서 다운로드 오류\n{str(e)}")

    def write_report(self):
        """선택된 이벤트의 보고서 작성"""
        selected_indexes = self.search_ui.event_table.selectedIndexes()
        
        selected_row = selected_indexes[0].row()
        index = self.search_ui.event_table.item(selected_row, 0).text()
        camera_name = self.search_ui.event_table.item(selected_row, 1).text()
        alarm_type = self.search_ui.event_table.item(selected_row, 2).text()
        detect_time = self.search_ui.event_table.item(selected_row, 3).text()

        print(f"index: {index}, camera_name: {camera_name}, alarm_type: {alarm_type}, detect_time: {detect_time}")

        # 카메라 번호 찾기
        camera_num = None
        for cam_name, camera_viewer in self.search_page_camera_view_list.items():
            if cam_name == camera_name:
                camera_num = camera_viewer.camera_num
                break

        if camera_num is None:
            print(f"카메라 번호를 찾을 수 없습니다: {camera_name}")
            return

        # detect_time 형식 변환: "25.10.30 10:36:36" -> "2025-10-30 10-36"
        try:
            dt = datetime.strptime(detect_time, "%y.%m.%d %H:%M:%S")
            detect_time_formatted = dt.strftime("%Y-%m-%dT%H-%M-%S")
        except Exception as e:
            print(f"시간 형식 변환 오류: {e}")
            return

        # FastAPI 엔드포인트로 전송할 데이터 준비
        data = {
            "msg": {
                "camera_name": camera_name.replace(" ", "_"),
                "camera_num": camera_num,
                "detect_time": detect_time_formatted,
                "nvr_info": {
                    "nvr_ip": self.parent.login_info_temp["NVR"]["IP"],
                    "nvr_id": self.parent.login_info_temp["NVR"]["ID"],
                    "nvr_pw": self.parent.login_info_temp["NVR"]["PW"]
                }
            }
        }

        # FastAPI 엔드포인트로 POST 요청
        try:
            url = f'http://{self.parent.HOST}:{self.parent.PORT}/request_backtracking_trash'
            print(f"역추적 요청 전송: {url}")
            print(f"전송 데이터: {data}")
            
            requests.put(url, json=data)

            self.parent.create_fade_out_msg(std_window = self, msg=f"보고서 생성 요청\n 예상 소요 시간 : 1분 이내")
            
                # TODO: 보고서 저장 로직 추가
        except Exception as e:
            print(f"역추적 요청 오류: {e}")
            traceback.print_exc()


    
def open_search_window(click, self):
    self.search_window = SearchDialog(self)
    self.search_window.show()
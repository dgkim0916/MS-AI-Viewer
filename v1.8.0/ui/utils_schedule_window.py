from PySide6.QtWidgets import QDialog, QListWidgetItem, QPushButton, QLabel, QTableWidgetSelectionRange, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout, QSizePolicy
from PySide6.QtGui import  QIcon, QImage, QPixmap, QFont
from PySide6.QtCore import Qt, QTimer, Signal, QRect, QSize
from PySide6 import QtCore
from ui.ui_schedule import Ui_schedule_window

from utils import FadeOutWindow, FadeOutInWindow,\
                  Eng2kor, Kor2eng, save_info

from datetime import datetime, timedelta
import numpy as np
import cv2
import requests
import resourece_rc
import math


week_dict = {"sunday" : 0, "monday" : 1, "tuesday" : 2, "wednesday" : 3, "thursday" : 4, "friday" : 5, "saturday" : 6}

class SchedulePageView(QLabel):
    Checked = Signal(QLabel)
    def __init__(self, base_viewer, camera_name, nvr_ip, name_label, main_instance, schedule_instance, time_table):
        super().__init__(base_viewer)
        # self.setGeometry(QRect(1, 1, base_viewer.width(), base_viewer.height()))
        self.setGeometry(QRect(1, 1, 204, 135))

        self.checked = False
        self.camera_name = camera_name
        self.name_label = name_label
        self.nvr_ip = nvr_ip
        self.main_instance = main_instance
        self.schedule_instance = schedule_instance

        self.time_table = time_table

        self.frame_flag = False

    def setChecked(self, checked):
        for camera_name, camera_viewer in self.schedule_instance.schedule_page_camera_view_list.items():
            if camera_viewer.checked:
                camera_viewer.checked = False
                camera_viewer.updateStyle()
                
        self.checked = checked
        self.schedule_instance.schedule_ui.event_box.clear()
        for detect_info in self.main_instance.ai_server_camera_info_dict[self.nvr_ip][self.camera_name]["detect_info"]:
            self.schedule_instance.schedule_ui.event_box.addItem(Eng2kor(detect_info[0]))

        self.updateStyle()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setChecked(not self.checked)

    def enterEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.setChecked(True)
            
    def updateStyle(self):
            if self.checked:
                self.time_table.clearSelection()
                for week_str, schedule_info in self.main_instance.ai_server_camera_info_dict[self.nvr_ip][self.camera_name]["detect_schedule"].items():
                    for detect_type, time_table_info in schedule_info.items():
                        if Eng2kor(detect_type) == self.schedule_instance.schedule_ui.event_box.currentText():
                            for start, end in time_table_info:
                                for i in range(start, end):
                                    item_1 = self.time_table.item(i, week_dict[week_str])
                                
                                    if item_1 is not None:  # 셀이 존재하는 경우에만 선택 처리
                                        item_1.setSelected(True)
                                    else:
                                        print(f"Cell at row {i} and column {week_str} does not exist.")

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

def create_schedule_camera_grid_page(schedule_ui, page_index, camera_list, main_instance, schedule_instance, time_table):
    """
    4x4 그리드 레이아웃으로 스케줄 카메라 뷰를 생성하는 함수
    항상 16개 칸을 생성하며, 빈 칸은 비활성화 상태로 표시됨
    
    Args:
        schedule_ui: UI 인스턴스
        page_index: 페이지 인덱스 (0부터 시작)
        camera_list: 이 페이지에 표시할 카메라 정보 리스트 [(camera_name, camera_info, nvr_ip), ...]
        main_instance: 메인 인스턴스
        schedule_instance: 스케줄 다이얼로그 인스턴스
        time_table: 타임 테이블 위젯
    
    Returns:
        page_widget: 생성된 페이지 위젯
        camera_views: 생성된 카메라 뷰 딕셔너리 {camera_name: SchedulePageView}
    """
    # 페이지 위젯 생성
    page_widget = QWidget()
    page_widget.setObjectName(f"schedule_page_{page_index}")
    
    # 메인 레이아웃
    main_layout = QHBoxLayout(page_widget)
    main_layout.setSpacing(0)
    main_layout.setContentsMargins(0, 0, 0, 0)
    
    # 그리드 레이아웃을 담을 위젯
    grid_widget = QWidget(page_widget)
    grid_widget.setObjectName(f"schedule_grid_widget_{page_index}")
    
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
        camera_layout.setObjectName(f"schedule_camera_view_layout_{page_index}_{idx}")
        
        # 카메라가 있는 경우
        if idx < len(camera_list):
            camera_name, camera_info, nvr_ip = camera_list[idx]
            
            # 카메라 이름 라벨 생성
            name_label = QLabel(grid_widget)
            name_label.setObjectName(f"camera_view_name_{page_index}_{idx}")
            
            sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
            sizePolicy.setHeightForWidth(name_label.sizePolicy().hasHeightForWidth())
            name_label.setSizePolicy(sizePolicy)
            name_label.setMaximumSize(QSize(722, 20))
            
            font = QFont()
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
            
            # SchedulePageView 인스턴스 생성
            camera_view = SchedulePageView(
                base_viewer=view_label,
                camera_name=camera_name,
                nvr_ip=nvr_ip,
                name_label=name_label,
                main_instance=main_instance,
                schedule_instance=schedule_instance,
                time_table=time_table
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

class ScheduleDialog(QDialog):
    def __init__(self, parent=None):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : open schedule window")
        super().__init__(parent)

        self.parent = parent


        self.schedule_ui = Ui_schedule_window()
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.schedule_ui.setupUi(self)

        self.schedule_ui.schedule_time_table.setSelectionMode(QTableWidget.MultiSelection)

        self.schedule_ui.event_box.clear()

        for row in range(24):
            for column in range(7):
                item = QTableWidgetItem(f" ")
                self.schedule_ui.schedule_time_table.setItem(row, column, item)

        # 메인 윈도우의 중앙에 팝업 윈도우 위치 계산
        mainWindowGeometry = self.parent.frameGeometry()
        centerPoint = mainWindowGeometry.center() - self.rect().center()
        self.move(centerPoint.x(), centerPoint.y())

        self.schedule_page_camera_view_list = {}
        self.schedule_current_page = 0

        # 카메라 리스트를 정렬 self.ui_main.camera_list_table 순서 기준
        camera_items = []
        for row in range(self.parent.ui_main.camera_list_table.rowCount()):
            camera_name = self.parent.ui_main.camera_list_table.item(row, 1).text()
            # 해당 카메라의 nvr_ip를 찾고, camera_info를 가져옴
            nvr_ip = self.parent.find_nvr_ip(camera_name)
            if nvr_ip and camera_name in self.parent.ai_server_camera_info_dict[nvr_ip]:
                camera_info = self.parent.ai_server_camera_info_dict[nvr_ip][camera_name]
                camera_items.append((camera_name, camera_info, nvr_ip))
        
        # 카메라 개수에 따라 페이지 수 계산 (16개씩)
        total_cameras = len(camera_items)
        cameras_per_page = 16
        total_pages = max(1, math.ceil(total_cameras / cameras_per_page))  # 최소 1페이지
        
        # stackedWidget_5의 기존 페이지 모두 제거
        while self.schedule_ui.stackedWidget_5.count() > 0:
            widget = self.schedule_ui.stackedWidget_5.widget(0)
            self.schedule_ui.stackedWidget_5.removeWidget(widget)
            if widget:
                widget.deleteLater()
        
        # 각 페이지 생성
        for page_idx in range(total_pages):
            start_idx = page_idx * cameras_per_page
            end_idx = min(start_idx + cameras_per_page, total_cameras)
            page_cameras = camera_items[start_idx:end_idx]
            
            # 4x4 그리드 페이지 생성 (카메라가 없어도 빈 그리드 생성)
            page_widget, camera_views = create_schedule_camera_grid_page(
                self.schedule_ui, 
                page_idx, 
                page_cameras, 
                self.parent,
                self,
                self.schedule_ui.schedule_time_table
            )
            
            # stackedWidget에 페이지 추가
            self.schedule_ui.stackedWidget_5.addWidget(page_widget)
            
            # 카메라 뷰 리스트에 추가
            self.schedule_page_camera_view_list.update(camera_views)
        
        # 카메라 이미지 설정
        for camera_name, camera_viewer in self.schedule_page_camera_view_list.items():
            if camera_name in self.parent.camera_img_temp.keys():
                img = self.parent.camera_img_temp[camera_name]
                frame = cv2.resize(img, (camera_viewer.width(), camera_viewer.height()))
                camera_viewer.set_img(frame, 0.5)
            else:
                camera_viewer.setPixmap(QPixmap(u":/newPrefix/ui/images/ico_video_off.svg"))
                camera_viewer.setAlignment(Qt.AlignCenter)
        
        # 페이지 네비게이션 버튼 찾기
        try:
            self.schedule_ui.schedule_camera_next_page_bnt.clicked.connect(lambda: self.change_schedule_page(1))
            self.schedule_ui.schedule_camera_undo_page_bnt.clicked.connect(lambda: self.change_schedule_page(-1))
            
            # 페이지 네비게이션 버튼 표시/숨김 처리
            self.update_schedule_page_navigation_buttons(total_pages)
        except AttributeError:
            # 버튼이 없으면 무시
            pass

        self.schedule_ui.event_box.currentIndexChanged.connect(lambda index: self.change_time_table(index))

        self.schedule_ui.schedule_apply_bnt.clicked.connect(lambda click, instance = self.parent: self.apply_schedule(click, instance))
        self.schedule_ui.schedule_close_bnt.clicked.connect(lambda click, instance = self.parent: self.schedule_close_window(click, instance))
        self.schedule_ui.schedule_all_remove_bnt.clicked.connect(self.schedule_ui.schedule_time_table.clearSelection)

    def change_schedule_page(self, direction):
        """
        스케줄 페이지를 변경하는 함수
        
        Args:
            direction: 1 (다음 페이지) 또는 -1 (이전 페이지)
        """
        total_pages = self.schedule_ui.stackedWidget_5.count()
        new_page = self.schedule_current_page + direction
        
        # 페이지 범위 체크
        if 0 <= new_page < total_pages:
            self.schedule_current_page = new_page
            self.schedule_ui.stackedWidget_5.setCurrentIndex(new_page)
            self.update_schedule_page_navigation_buttons(total_pages)
    
    def update_schedule_page_navigation_buttons(self, total_pages):
        """
        스케줄 페이지 네비게이션 버튼의 표시/숨김을 업데이트하는 함수
        
        Args:
            total_pages: 전체 페이지 수
        """
        try:
            # 페이지가 1개면 네비게이션 버튼 숨김
            if total_pages <= 1:
                self.schedule_ui.schedule_camera_next_page_bnt.hide()
                self.schedule_ui.schedule_camera_undo_page_bnt.hide()
            else:
                # 첫 페이지면 이전 버튼 숨김
                if self.schedule_current_page == 0:
                    self.schedule_ui.schedule_camera_undo_page_bnt.hide()
                else:
                    self.schedule_ui.schedule_camera_undo_page_bnt.show()
                
                # 마지막 페이지면 다음 버튼 숨김
                if self.schedule_current_page == total_pages - 1:
                    self.schedule_ui.schedule_camera_next_page_bnt.hide()
                else:
                    self.schedule_ui.schedule_camera_next_page_bnt.show()
        except AttributeError:
            # 버튼이 없으면 무시
            pass
        
    def schedule_close_window(self, click, parent):
        save_info(host=parent.ai_server_ip, port=parent.ai_server_port, file_name="camera_info", info=parent.ai_server_camera_info_dict)
        data = {"msg" : {"ai_server_info_dict" : parent.ai_server_info_dict}}

        url = f'http://{parent.ai_server_ip}:{parent.ai_server_port}/run-ms-ai'
        receive_data = requests.put(url, json=data).json()

        self.close()

    def apply_schedule(self, click, instance):
        selected_indexes_dict = {"sunday" : [], "monday" : [], "tuesday" : [], "wednesday" : [], "thursday" : [], "friday" : [], "saturday" : []}
        selected_indexes = self.schedule_ui.schedule_time_table.selectedIndexes()

        for index in selected_indexes:
            time = index.row()
            day = index.column()
            selected_indexes_dict[list(week_dict.keys())[day]].append(time)

        for day, info in selected_indexes_dict.items():
            for camera_name, camera_viewer in self.schedule_page_camera_view_list.items():
                if camera_viewer.checked:
                    instance.ai_server_camera_info_dict[camera_viewer.nvr_ip][camera_name]["detect_schedule"][day][Kor2eng(self.schedule_ui.event_box.currentText())] = group_ranges(info)
                    break

        # instance.create_fade_out_msg(std_window = instance.schedule_window, msg="저장 완료")
        instance.create_fade_out_msg(std_window = self, msg="스케줄 저장 완료")

    def change_time_table(self, index):
        for camera_name, camera_viewer in self.schedule_page_camera_view_list.items():
            if camera_viewer.checked:
                camera_viewer.updateStyle()
                break

    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_S and event.modifiers() == Qt.ControlModifier) :
            self.apply_schedule(None, self.parent)

def group_ranges(lst):
    if not lst:
        return []

    lst = sorted(lst) 
    result = []
    start = lst[0]
    end = lst[0]

    for num in lst[1:]:
        if num == end + 1:
            end = num
        else:
            result.append([start, end + 1]) 
            start = num
            end = num

    result.append([start, end + 1])
    return result

def open_schedule_window(click, self):
    self.labeling_window = ScheduleDialog(self)
    self.labeling_window.show()

    


    

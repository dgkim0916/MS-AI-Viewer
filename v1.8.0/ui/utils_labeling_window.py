import sys
import os
from pathlib import Path
import cv2
import numpy as np
import shutil

from PySide6.QtWidgets import QDialog, QTableWidgetItem, QLabel, QApplication, QMainWindow, QPushButton
from datetime import datetime
from PySide6.QtCore import QTimer, QDate, Qt, QSize, Signal, QPoint, QRect, QEvent
from PySide6.QtGui import QImage, QPainter, QPen, QColor, QPolygon, QBrush, QMouseEvent, QPixmap, QCursor, QFont
from PySide6.QtWidgets import QSizePolicy
import requests

from ui.ui_ai_labeling import Ui_labeling_window
import base64

COLOR = {
    0: (95, 150, 0),     # Grass Green - person
    1: (255, 242, 0),    # yellow - bicycle (변경)
    2: (70, 130, 180),   # Steel Blue - car
    3: (255, 140, 0),    # Dark Orange - motorcycle
    4: (147, 112, 219),  # Medium Purple - bus
    5: (72, 209, 204),   # Medium Turquoise - truck
    6: (255, 20, 147)    # Deep Pink - fire
}

class Labeling_Viewer(QLabel):
    clicked = Signal(QPoint)  # 사용자가 클릭한 위치를 전달하는 시그널

    def __init__(self, parent, main_instance):
        super().__init__(parent)
        
        self.point_list = []
        self.non_active_point_list = []
        self.setPixmap(QPixmap(u":/ui/ui/images/logo.png"))
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet(f"border: 1px solid rgb(119, 118, 123);\n"
                            "border-radius: 10px;\n"
                            )
        self.parent = parent
        self.main_instance = main_instance
        self.label_list = []
        self.selected_box = None
        self.dragging = False
        self.drawing_new_box = False
        self.drag_start_pos = None
        self.resize_corner = None
        self.resizing = False
        self.mouse_pos = None
        self.box_resize_mode = False
        self.checked_cls_num = None


        self.cls_bnt_list = []
        self.class_name_dict = { 0 : "사람", 1 : "자전거", 2 : "차량", 3 : "오토바이", 4 : "버스", 5 : "트럭", 6 : "화재"}

        for num, cls_name in self.class_name_dict.items():
            # self.label_ui.label_image_viewer.make_cls_bnt(num, num, self.color(num))
            self.make_cls_bnt(num, num, COLOR[num])

    # 새로운 메서드 추가
    def handle_button_toggled(self, checked, button):
        checked_flag = True
        if checked:
            # 현재 체크된 버튼을 제외한 나머지 버튼들은 체크 해제
            for btn in self.cls_bnt_list:
                if btn != button:
                    btn.setChecked(False)

        # 체크된 버튼의 인덱스를 찾습니다.
        for index, button in enumerate(self.cls_bnt_list):
            if button.isChecked():
                self.checked_cls_num = index
                checked_flag = False
                break
        
        #어떠한 클래스 버튼도 체크가 되어 있지 않을때
        if checked_flag:
            self.checked_cls_num = None

    def make_cls_bnt(self, bnt_num, cls, color):
        cls_bnt = QPushButton(self.parent.label_ui.label_class_widget)
        bnt_name = f"{self.class_name_dict[cls]}"
        cls_bnt.setObjectName(bnt_name)
        cls_bnt.setMinimumSize(QSize(55, 25))

        if cls == 3:
            cls_bnt.setMinimumSize(QSize(75, 25))

        # cls_bnt.setMaximumSize(QSize(550, 25))

        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(cls_bnt.sizePolicy().hasHeightForWidth())
        cls_bnt.setSizePolicy(sizePolicy2)

        font = QFont()
        font.setFamilies([u"Sans"])
        font.setPointSize(10)
        cls_bnt.setFont(font)
        cls_bnt.setCursor(QCursor(Qt.PointingHandCursor))

        if cls == 1:
            cls_bnt.setStyleSheet(
                                "QPushButton{\n"
                                f"background-color: rgb({color[0]}, {color[1]}, {color[2]});\n"
                                "color: rgb(0, 0, 0);\n"
                                "border-radius: 9px;\n"
                                "border: 1px solid rgba(255, 255, 255, 100);\n"
                                "}\n"
                                                
                                "QPushButton:checked {\n"
                                "color: white;\n"
                                "border-radius: 9px;\n"
                                "border: 2px solid rgb(255, 255, 255);\n"
                                "}"
                                )

        else:
            cls_bnt.setStyleSheet(
                                "QPushButton{\n"
                                f"background-color: rgb({color[0]}, {color[1]}, {color[2]});\n"
                                "color: rgb(255, 255, 255);\n"
                                "border-radius: 9px;\n"
                                "border: 1px solid rgba(255, 255, 255, 100);\n"
                                "}\n"
                                                
                                "QPushButton:checked {\n"
                                "color: white;\n"
                                "border-radius: 9px;\n"
                                "border: 2px solid rgb(255, 255, 255);\n"
                                "}"
                                )
        cls_bnt.setText(str(self.class_name_dict[cls]))
        cls_bnt.setCheckable(True)


        # 버튼이 체크될 때, 나머지 버튼의 체크를 해제하는 메서드 연결
        cls_bnt.toggled.connect(lambda checked, btn=cls_bnt: self.handle_button_toggled(checked, btn))

        self.parent.label_ui.horizontalLayout_7.insertWidget(bnt_num, cls_bnt)

        self.cls_bnt_list.append(cls_bnt)

    def display_label_image(self):
        self.label_list = []
        if 0 <= self.parent.cnt < len(self.parent.img_buffer):
            img = self.parent.img_buffer[self.parent.cnt]

            if len(self.parent.label_buffer[self.parent.cnt]):
                for cls, xc, yc, w, h in self.parent.label_buffer[self.parent.cnt]:
                    self.label_list.append([int(cls), float(xc), float(yc), float(w), float(h), COLOR[cls]])
                    
            else: self.label_list = []
            
            img = cv2.resize(img, dsize=(self.width(), self.height()))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            height, width, channel = img.shape
            bytes_per_line = 3 * width
            q_img = QImage(img.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_img)
            self.setPixmap(pixmap)
            self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        for label in self.label_list:
            cls, xc, yc, w, h, color = label
            x1 = int((xc - w / 2) * self.width())
            y1 = int((yc - h / 2) * self.height())
            x2 = int((xc + w / 2) * self.width())
            y2 = int((yc + h / 2) * self.height())
            rect = QRect(x1, y1, x2 - x1, y2 - y1)

            pen = QPen(QColor(color[0], color[1], color[2]), 3)
            painter.setPen(pen)
            brush = QBrush(QColor(color[0], color[1], color[2], 100))  # 100 is the alpha value for transparency
            painter.setBrush(brush)

            painter.drawRect(rect)
            # Draw corners as circles
            corner_radius = 3
            painter.setBrush(QBrush(QColor(color[0], color[1], color[2])))
            corners = [(x1, y1), (x2, y1), (x1, y2), (x2, y2)]
            for corner in corners:
                painter.drawEllipse(QPoint(corner[0], corner[1]), corner_radius, corner_radius)
        
        #새로운 박스 생성시 점선 네모표시
        if self.drawing_new_box and self.drag_start_pos and self.mouse_pos :
            
            for index, button in enumerate(self.cls_bnt_list):
                if button.isChecked():
                    self.checked_cls_num = index
                    break

            if self.checked_cls_num is None:
                self.main_instance.create_fade_out_msg(std_window=self.parent, msg="객체 상자를 추가하기 전에 클래스 번호를 선택하세요.")
                return
            
            color = COLOR[self.checked_cls_num]

            pen = QPen(QColor(color[0], color[1], color[2]), 2, Qt.DashLine)
            painter.setPen(pen)
            brush = QBrush(QColor(0, 0, 0, 0))
            painter.setBrush(brush)

            painter.drawRect(QRect(self.drag_start_pos, self.mouse_pos))

        #마우스 위치에 초록 십자선 표시
        if self.mouse_pos:
            pen = QPen(QColor(81, 174, 50), 2)
            painter.setPen(pen)
            painter.drawLine(0, self.mouse_pos.y(), self.width(), self.mouse_pos.y())
            painter.drawLine(self.mouse_pos.x(), 0, self.mouse_pos.x(), self.height())

            corner = self.get_corner(self.mouse_pos)
            if corner:
                if corner == 'top_left':
                    self.setCursor(QCursor(Qt.SizeFDiagCursor))  # ↖↘ 방향
                elif corner == 'top_right':
                    self.setCursor(QCursor(Qt.SizeBDiagCursor))  # ↗↙ 방향
                elif corner == 'bottom_left':
                    self.setCursor(QCursor(Qt.SizeBDiagCursor))  # ↗↙ 방향
                elif corner == 'bottom_right':
                    self.setCursor(QCursor(Qt.SizeFDiagCursor))  # ↖↘ 방향
            else:
                self.setCursor(QCursor(Qt.ArrowCursor))  # 기본 포인터


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton :
            if self.checked_cls_num is None:
                self.main_instance.create_fade_out_msg(std_window=self.parent, msg="객체 상자를 추가하기 전에 클래스 번호를 선택하세요.")
                return

            self.drag_start_pos = event.pos()
            self.drawing_new_box = True
            for index, label in enumerate(self.label_list):
                cls, xc, yc, w, h, color = label
                x1 = int((xc - w / 2) * self.width()) - 3
                y1 = int((yc - h / 2) * self.height()) - 3
                x2 = int((xc + w / 2) * self.width()) + 3
                y2 = int((yc + h / 2) * self.height()) + 3
                rect = QRect(x1, y1, x2 - x1, y2 - y1)

                if rect.contains(event.pos()):
                    self.drawing_new_box = False
                    self.selected_box = index
                    corner = self.get_resize_corner(event.pos())

                    if corner:
                        self.resizing = True
                        self.resize_corner = corner
                    else:
                        self.dragging = True

                    break

        if event.button() == Qt.RightButton :
            check_index = {}

            for index, label in enumerate(self.label_list):
                cls, xc, yc, w, h, color = label
                x1 = int((xc - w / 2) * self.width())
                y1 = int((yc - h / 2) * self.height())
                x2 = int((xc + w / 2) * self.width())
                y2 = int((yc + h / 2) * self.height())
                rect = QRect(x1, y1, x2 - x1, y2 - y1)

                if rect.contains(event.pos()):
                    check_index[index] = [cls, abs(event.pos().x() - xc*self.width()) + abs(event.pos().y() - yc*self.height())]
            
            min_distance = None
            del_index = None

            if check_index:
                for index, info in check_index.items():
                    cls = info[0]
                    distance = info[1]

                    if cls != self.checked_cls_num:
                        if min_distance == None:
                            del_index = index
                            min_distance = distance

                        elif min_distance > distance:
                            del_index = index
                            min_distance = distance

                if del_index == None:
                    for index, info in check_index.items():
                        distance = info[1]
                        if min_distance == None:
                            del_index = index
                            min_distance = distance

                        elif min_distance > distance:
                            del_index = index
                            min_distance = distance

                del self.label_list[del_index]
                del self.parent.label_buffer[self.parent.cnt][del_index]

                # self.cls_bnt_list[del_index].deleteLater()
                # del self.cls_bnt_list[del_index]
                self.update()

    def mouseMoveEvent(self, event):
        self.mouse_pos = event.pos()

        if self.drawing_new_box:
            self.update()

        elif self.dragging and self.selected_box is not None:
            dx = event.pos().x() - self.drag_start_pos.x()
            dy = event.pos().y() - self.drag_start_pos.y()
            cls, xc, yc, w, h, color = self.label_list[self.selected_box]


            new_xc = (int(xc * self.width()) + dx) / self.width()
            new_yc = (int(yc * self.height()) + dy) / self.height()

            # xc = (int(xc * self.width()) + dx) / self.width()
            # yc = (int(yc * self.height()) + dy) / self.height()

            if (new_xc - w/2) <= 0 or (new_xc + w/2) >= 1 : xc = xc
            else: xc = new_xc
            if (new_yc - h/2) <= 0 or (new_yc + h/2) >= 1 : yc = yc
            else: yc = new_yc

            self.label_list[self.selected_box] = [cls, xc, yc, w, h, color]
            self.parent.label_buffer[self.parent.cnt][self.selected_box] = [cls, xc, yc, w, h]
            self.drag_start_pos = event.pos()
            self.update()

        elif self.resizing and self.selected_box is not None:
            dx = event.pos().x() - self.drag_start_pos.x()
            dy = event.pos().y() - self.drag_start_pos.y()

            cls, xc, yc, w, h, color = self.label_list[self.selected_box]

            dx /= self.width()
            dy /= self.height()

            x1 = (xc - w / 2)
            y1 = (yc - h / 2)
            x2 = (xc + w / 2)
            y2 = (yc + h / 2)

            # Resize based on the corner being dragged
            if self.resize_corner == 'top_left':
                x1 += dx
                y1 += dy
            elif self.resize_corner == 'top_right':
                x2 += dx
                y1 += dy
            elif self.resize_corner == 'bottom_left':
                x1 += dx
                y2 += dy
            elif self.resize_corner == 'bottom_right':
                x2 += dx
                y2 += dy

            new_xc = (x2 + x1) / 2
            new_yc = (y2 + y1) / 2
            new_w = (x2 - x1) 
            new_h = (y2 - y1) 

            # 경계 조건 체크 수정: new_w와 new_h 사용
            if (new_xc - new_w / 2) < 0 or (new_xc + new_w / 2) > 1:
                new_xc = xc
                new_w = w

            if (new_yc - new_h / 2) < 0 or (new_yc + new_h / 2) > 1:
                new_yc = yc
                new_h = h

            # Update the bounding box size and position
            self.label_list[self.selected_box][1] = new_xc
            self.label_list[self.selected_box][2] = new_yc
            self.label_list[self.selected_box][3] = new_w
            self.label_list[self.selected_box][4] = new_h

            self.parent.label_buffer[self.parent.cnt][self.selected_box] = [cls, new_xc, new_yc, new_w, new_h]
            self.drag_start_pos = event.pos()

            self.update()

        else:
            self.update()

    def mouseReleaseEvent(self, event):
        if self.drawing_new_box:
            self.create_new_box(event.pos())
        self.dragging = False
        self.resizing = False
        self.resize_corner = None
        self.drawing_new_box = False

    def enterEvent(self, event):
        self.setMouseTracking(True)
        self.mouse_pos = None
        self.update()

    def leaveEvent(self, event):
        self.setMouseTracking(False)
        self.mouse_pos = None
        self.update()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.display_label_image()


    def create_new_box(self, end_pos):
        start_x = self.drag_start_pos.x()
        start_y = self.drag_start_pos.y()
        end_x = end_pos.x()
        end_y = end_pos.y()

        # end_x와 end_y가 화면의 너비와 높이를 벗어나지 않도록 제한
        if end_x < 0:
            end_x = 0
        if end_x > self.width():
            end_x = self.width()
        if end_y < 0:
            end_y = 0
        if end_y > self.height():
            end_y = self.height()

        new_xc = (start_x + end_x) / 2 / self.width()
        new_yc = (start_y + end_y) / 2 / self.height()
        new_w = abs(end_x - start_x) / self.width()
        new_h = abs(end_y - start_y) / self.height()

        # 체크된 버튼의 인덱스를 찾습니다.
        for index, button in enumerate(self.cls_bnt_list):
            if button.isChecked():
                self.checked_cls_num = index
                break
        # 만약 체크된 버튼이 없다면, 경고 메시지를 출력하고 종료
        if self.checked_cls_num is None:
            self.main_instance.create_fade_out_msg(std_window=self.parent, msg="객체 상자를 추가하기 전에 클래스 번호를 선택하세요.")
            return
            
        if new_w * new_h * self.width() * self.height() > 100:
            color = COLOR[self.checked_cls_num]

            self.label_list.append([self.checked_cls_num, new_xc, new_yc, new_w, new_h, color])
            self.parent.label_buffer[self.parent.cnt].append([self.checked_cls_num, new_xc, new_yc, new_w, new_h])


            # 필요한 경우 버튼을 추가하는 로직이 있는지 확인
            # self.cls_bnt_list.append(self.make_cls_bnt(len(self.cls_bnt_list), 0, color))

            self.update()

    def get_resize_corner(self, pos):
        """Determine which corner is being dragged."""
        if not self.label_list[self.selected_box]:
            return None
        cls, xc, yc, w, h, color = self.label_list[self.selected_box]
        x1 = int((xc - w / 2) * self.width())
        y1 = int((yc - h / 2) * self.height())
        x2 = int((xc + w / 2) * self.width())
        y2 = int((yc + h / 2) * self.height())
        corners = {
            'top_left': QPoint(x1, y1),
            'top_right': QPoint(x2, y1),
            'bottom_left': QPoint(x1, y2),
            'bottom_right': QPoint(x2, y2)
        }
        for corner, point in corners.items():
            if (point - pos).manhattanLength() < 4:  # Tolerance for detecting corner clicks
                return corner
        return False


    def get_corner(self, pos):
        for cls, xc, yc, w, h, color in self.label_list:
            x1 = int((xc - w / 2) * self.width())
            y1 = int((yc - h / 2) * self.height())
            x2 = int((xc + w / 2) * self.width())
            y2 = int((yc + h / 2) * self.height())

            corners = {
                'top_left': QPoint(x1, y1),
                'top_right': QPoint(x2, y1),
                'bottom_left': QPoint(x1, y2),
                'bottom_right': QPoint(x2, y2)
            }

            # 탐지 범위를 확대하여 마우스 위치를 비교
            for corner, point in corners.items():
                if (point - pos).manhattanLength() < 4:  # 허용 범위: 10픽셀
                    return corner
                
        return None


class LabelingDialog(QDialog):
    def __init__(self, parent=None):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : open labeling window")

        super().__init__(parent)
        self.label_ui = Ui_labeling_window()
        self.label_ui.setupUi(self)
        self.parent = parent

        self.label_ui.cls_1.hide()

        self.event_data_exist = False
        self.cnt = 0
        self.img_buffer = []
        self.label_buffer = []

        # 메인 윈도우의 중앙에 팝업 윈도우 위치 계산
        mainWindowGeometry = parent.frameGeometry()
        centerPoint = mainWindowGeometry.center() - self.rect().center()
        self.move(centerPoint.x(), centerPoint.y())

        # 카메라 페이지 영상 뷰어
        self.label_ui.label_image_viewer.hide()
        self.label_ui.label_image_viewer = Labeling_Viewer(self, self.parent)
        self.label_ui.label_image_viewer.setObjectName(u"camera_page_viewer")
        self.label_ui.label_image_viewer.setMinimumSize(QSize(343, 581))
        self.label_ui.label_image_viewer.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
                                                         "background-color: rgba(255, 255, 255, 0);")
        self.label_ui.label_image_viewer.setScaledContents(False)
        self.label_ui.verticalLayout_3.addWidget(self.label_ui.label_image_viewer)

        self.label_data_refresh(bnt_flag=False)

        self.label_ui.camera_name_box.currentTextChanged.connect(self.set_date_list)
        self.label_ui.event_date_box.currentTextChanged.connect(self.set_event_list)
        # self.label_ui.label_list_table.itemSelectionChanged.connect(self.load_event_data)
        self.label_ui.label_list_table.itemDoubleClicked.connect(self.load_event_data)

        self.label_ui.shutdown_bnt.clicked.connect(self.close_window)
        self.label_ui.label_save_bnt.clicked.connect(self.save_label_buffer)
        self.label_ui.label_del_bnt.clicked.connect(self.del_all_label)
        self.label_ui.self_labeling_bnt.clicked.connect(self.start_self_labeling)
        self.label_ui.train_bnt.clicked.connect(self.start_train)
        self.label_ui.label_refresh_bnt.clicked.connect(self.label_data_refresh)
        self.label_ui.label_data_del_bnt.clicked.connect(self.del_label_data)

        self.label_ui.camera_name_box.setCurrentIndex(0)

        self.setFocusPolicy(Qt.StrongFocus)
        self.installEventFilter(self)

    def label_data_refresh(self, bnt_flag = True):
        data = {"msg" : {"cmd" : "get_label_info"}} 
        url = f'http://{self.parent.ai_server_ip}:{self.parent.ai_server_port}/get-auto-label-info'
        receive_data = requests.get(url, json=data).json()
        
        self.label_data_info = receive_data["label_data_info"]

        self.label_flag = receive_data["label_flag"]
        self.train_flag = receive_data["train_flag"]

        current_name_box_text = self.label_ui.camera_name_box.currentText()

        self.label_ui.camera_name_box.clear()
        for camera_name, camera_info in receive_data["label_data_info"].items():
            if len(camera_info):
                self.label_ui.camera_name_box.addItems([camera_name])
        try:
            index = self.label_ui.camera_name_box.findText(current_name_box_text)

            self.label_ui.camera_name_box.setCurrentIndex(index)
        except :
            print(f"camera_name_box not found {current_name_box_text}")
        if self.label_flag == True:
            #자동 라벨링 진행중
            self.label_ui.self_labeling_bnt.setStyleSheet("""
                                                        background-color: rgb(30, 195, 55);
                                                        color: rgb(255, 255, 255);
                                                        border-radius: 15px;
                                                        """)
            self.label_ui.self_labeling_bnt.setText("자동 라벨링 진행중")
            
        else:
            self.label_ui.self_labeling_bnt.setStyleSheet("""
                                            background-color: rgb(36, 39, 44);
                                            color: rgb(255, 255, 255);
                                            border-radius: 15px;
                                            """)
            
            self.label_ui.self_labeling_bnt.setText("자동 라벨링 시작")

        if self.train_flag == True:
            #자동 라벨링 진행중
            self.label_ui.train_bnt.setStyleSheet("""
                                                        background-color: rgb(30, 195, 55);
                                                        color: rgb(255, 255, 255);
                                                        border-radius: 15px;
                                                        """)
            self.label_ui.train_bnt.setText("학습 진행중")
            
        else:
            self.label_ui.train_bnt.setStyleSheet("""
                                            background-color: rgb(36, 39, 44);
                                            color: rgb(255, 255, 255);
                                            border-radius: 15px;
                                            """)
            
            self.label_ui.train_bnt.setText("학습 시작")

        self.set_date_list()
        self.set_event_list()
        if bnt_flag:
            self.parent.create_fade_out_msg(std_window = self, msg="새로고침")

    def start_train(self):
        if self.train_flag == False:
            data = {"msg" : ""} 
            url = f'http://{self.parent.ai_server_ip}:{self.parent.ai_server_port}/start-training'
            receive_data = requests.post(url, json=data).json()

            self.parent.create_fade_out_msg(std_window = self, msg="모델 학습 시작")

        else:
            data = {"msg" : "ms_train"} 
            url = f'http://{self.parent.ai_server_ip}:{self.parent.ai_server_port}/stop-self-labeling-training'
            receive_data = requests.put(url, json=data).json()

            self.parent.create_fade_out_msg(std_window = self, msg="자동 라벨링 정지")


        self.label_data_refresh()

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress:
            self.keyPressEvent(event)
            return True
        return super(LabelingDialog, self).eventFilter(source, event)

    def start_self_labeling(self):
        if self.label_flag == False:
            
            data = {"msg" : self.parent.ai_server_info_dict["NVR"]} 
            url = f'http://{self.parent.ai_server_ip}:{self.parent.ai_server_port}/run-self-labeling'
            receive_data = requests.post(url, json=data).json()
            print(receive_data)

            if receive_data["success"] == True:
                self.label_flag = True
                self.parent.create_fade_out_msg(std_window = self, msg="자동 라벨링 시작")
                #자동 라벨링 진행중

        else:
            data = {"msg" : "ms_labeling"} 
            url = f'http://{self.parent.ai_server_ip}:{self.parent.ai_server_port}/stop-self-labeling-training'
            receive_data = requests.put(url, json=data).json()

        self.label_data_refresh()

    def del_all_label(self):
        self.label_buffer[self.cnt] = []
        self.label_ui.label_image_viewer.display_label_image()

        self.parent.create_fade_out_msg(std_window = self, msg="라벨 데이터 모두 삭제 완료")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_D:
            self.cnt += 1
            if self.cnt >= len(self.img_buffer):
                self.cnt = 0  # 다시 처음 이미지로 돌아가도록

            self.label_ui.img_cur_num.setText(str(self.cnt + 1))
            self.label_ui.label_image_viewer.display_label_image()
        elif event.key() == Qt.Key_A:
            self.cnt -= 1
            if self.cnt < 0:
                self.cnt = len(self.img_buffer) - 1  # 마지막 이미지로 돌아가도록
 
            self.label_ui.label_image_viewer.display_label_image()
            self.label_ui.img_cur_num.setText(str(self.cnt + 1))

        elif event.key() == Qt.Key_W:
            self.label_ui.label_image_viewer.box_resize_mode = True

        elif event.key() == Qt.Key_F:
            self.del_label_data()
            
        # elif (event.key() == Qt.Key_S and event.modifiers() == Qt.ControlModifier) or event.key() == Qt.Key_Space:
        elif (event.key() == Qt.Key_S) or event.key() == Qt.Key_Space:
            # 현재 선택된 행을 save_label_buffer() 호출 전에 저장
            selected_indexes = self.label_ui.label_list_table.selectedIndexes()
            current_row = None
            total_rows = self.label_ui.label_list_table.rowCount()
            
            if selected_indexes:
                current_row = selected_indexes[0].row()
            
            # 라벨 버퍼 저장
            self.save_label_buffer()
            
            # 저장 후 다음 행으로 이동 (current_row가 유효한 경우만)
            if current_row is not None and current_row + 1 < total_rows:
                self.label_ui.label_list_table.selectRow(current_row + 1)
                self.load_event_data()

        elif event.key() == Qt.Key_Q:
            self.del_all_label()

        elif event.key() == Qt.Key_1:
            self.label_ui.label_image_viewer.cls_bnt_list[0].setChecked(True)

        elif event.key() == Qt.Key_2:
            self.label_ui.label_image_viewer.cls_bnt_list[1].setChecked(True)

        elif event.key() == Qt.Key_3:
            self.label_ui.label_image_viewer.cls_bnt_list[2].setChecked(True)

        elif event.key() == Qt.Key_4:
            self.label_ui.label_image_viewer.cls_bnt_list[3].setChecked(True)

        elif event.key() == Qt.Key_5:
            self.label_ui.label_image_viewer.cls_bnt_list[4].setChecked(True)

        elif event.key() == Qt.Key_6:
            self.label_ui.label_image_viewer.cls_bnt_list[5].setChecked(True)

        elif event.key() == Qt.Key_7:
            self.label_ui.label_image_viewer.cls_bnt_list[6].setChecked(True)


    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_W:
            self.label_ui.label_image_viewer.box_resize_mode = False

    def close_window(self):
        self.close()

    def set_date_list(self):
        camera_name = self.label_ui.camera_name_box.currentText()
        self.label_ui.event_date_box.clear()
        
        if camera_name in self.label_data_info.keys():
            date_list = self.label_data_info[camera_name].keys()
            try:
                date_list = sorted(date_list, key=lambda date: datetime.strptime(date, "%Y-%m-%d"))
            except Exception:
                date_list = sorted(date_list, key=lambda date: datetime.strptime(date, "%y.%m.%d"))

            self.label_ui.event_date_box.clear()

            for date in date_list:
                self.label_ui.event_date_box.addItems([date])

    def set_event_list(self):
        self.label_ui.label_list_table.setRowCount(0)
        camera_name = self.label_ui.camera_name_box.currentText()
        date = self.label_ui.event_date_box.currentText()

        if camera_name in self.label_data_info.keys() and date in self.label_data_info[camera_name].keys():
            event_data_list = self.label_data_info[camera_name][date]
            event_data_list = sorted(event_data_list)

            for event_data in event_data_list:
                row_position = self.label_ui.label_list_table.rowCount()
                self.label_ui.label_list_table.insertRow(row_position)
                text = QTableWidgetItem(str(event_data))
                text.setTextAlignment(Qt.AlignCenter)
                text.setFlags(Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                self.label_ui.label_list_table.setItem(row_position, 0, text)

            if self.label_ui.label_list_table.rowCount() > 0:
                self.label_ui.label_list_table.setCurrentCell(0, 0)

    def load_event_data(self):
        # self.parent.create_fade_out_msg(std_window = self, msg="라벨 데이터 로딩중")

        self.img_buffer = []
        selected_indexes = self.label_ui.label_list_table.selectedIndexes()

        if selected_indexes:
            selected_row = selected_indexes[0].row()
            data = {"msg" : {"cmd" : "get_label_data", 
                            "camera_name" : self.label_ui.camera_name_box.currentText(),
                            "date" : self.label_ui.event_date_box.currentText(),
                            "event_name" : self.label_ui.label_list_table.item(selected_row, 0).text(),
                            "nvr_ip" : self.parent.find_nvr_ip(self.label_ui.camera_name_box.currentText())
                            },
                            
                            }

            print(data)
            url = f'http://{self.parent.ai_server_ip}:{self.parent.ai_server_port}/get-auto-label-info'
            self.receive_data = requests.get(url, json=data).json()

            for img_base64 in self.receive_data["image"]:
                img_data = base64.b64decode(img_base64)
                np_array = np.frombuffer(img_data, np.uint8)
                img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
                self.img_buffer.append(img)


            self.label_buffer = self.receive_data["label"]
            self.cnt = 0

            if len(self.img_buffer):
                self.label_ui.label_image_viewer.display_label_image()
                self.label_ui.img_cur_num.setText(str(1))
                self.label_ui.img_total_num.setText(str(len(self.img_buffer)))

    def del_label_data(self):
        camera_name = self.label_ui.camera_name_box.currentText()
        date = self.label_ui.event_date_box.currentText()
        selected_indexes = self.label_ui.label_list_table.selectedIndexes()

        event_name_list = []
        if selected_indexes:
            for i in range(len(selected_indexes)):
                selected_row = selected_indexes[i].row()
                event_name = self.label_ui.label_list_table.item(selected_row, 0).text()
                # print(event_name)
                event_name_list.append(event_name)

            data = {"msg" : {"cmd" : "del_label_data", 
                            "camera_name" : camera_name,
                            "date" : date,
                            "event_name" : event_name_list,
                            "nvr_ip" : self.parent.find_nvr_ip(self.label_ui.camera_name_box.currentText())
                            },
                            
                            } 
            
            url = f'http://{self.parent.ai_server_ip}:{self.parent.ai_server_port}/get-auto-label-info'
            self.receive_data = requests.get(url, json=data).json()

            if self.receive_data["msg"] == True:
                data = {"msg" : {"cmd" : "get_label_info"}} 
                url = f'http://{self.parent.ai_server_ip}:{self.parent.ai_server_port}/get-auto-label-info'
                receive_data = requests.get(url, json=data).json()
                self.label_data_info = receive_data["label_data_info"]

                self.label_flag = receive_data["label_flag"]
                self.set_event_list()
                self.label_ui.label_list_table.selectRow(selected_row)
                self.load_event_data()

        self.parent.create_fade_out_msg(std_window = self, msg="라벨 데이터 삭제 완료")

    def save_label_buffer(self):
        camera_name = self.label_ui.camera_name_box.currentText()
        date = self.label_ui.event_date_box.currentText()
        selected_indexes = self.label_ui.label_list_table.selectedIndexes()
        if selected_indexes:
            selected_row = selected_indexes[0].row()
            event_name = self.label_ui.label_list_table.item(selected_row, 0).text()

            data = {"msg" : {"cmd" : "save_label", 
                            "camera_name" : camera_name,
                            "date" : date,
                            "event_name" : event_name,
                            "label_buffer" : self.label_buffer,
                            "nvr_ip" : self.parent.find_nvr_ip(self.label_ui.camera_name_box.currentText())
                            },
                            } 
            
            url = f'http://{self.parent.ai_server_ip}:{self.parent.ai_server_port}/get-auto-label-info'
            self.receive_data = requests.get(url, json=data).json()

            if self.receive_data["msg"] == True:
                data = {"msg" : {"cmd" : "get_label_info"}} 
                url = f'http://{self.parent.ai_server_ip}:{self.parent.ai_server_port}/get-auto-label-info'
                receive_data = requests.get(url, json=data).json()
                self.label_data_info = receive_data["label_data_info"]

                self.label_flag = receive_data["label_flag"]
                self.set_event_list()
                # 현재 행 유지 (행 이동은 keyPressEvent에서 처리)
                self.label_ui.label_list_table.selectRow(selected_row)
                self.load_event_data()
            self.parent.create_fade_out_msg(std_window = self, msg="라벨 데이터 저장 완료")
            
def open_labeling_window(click, self):
    self.labeling_window = LabelingDialog(self)
    self.labeling_window.show()

def event_key(file_name):
    date_time_str = file_name.split('_')[0]
    # date_time = datetime.strptime(date_time_str, "%H.%M.%S")
    date_time = datetime.strptime("%H.%M.%S")

    return date_time


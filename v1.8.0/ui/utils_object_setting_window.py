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

from ui.ui_object_setting import Ui_object_setting
import base64

class Object_settint_Dialog(QDialog):
    def __init__(self, parent=None):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : open object_setting window")

        super().__init__(parent)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.object_setting_ui = Ui_object_setting()
        self.object_setting_ui.setupUi(self)
        self.parent = parent

        camera_name = self.parent.ui_main.camera_page_name_box.currentText()
        nvr_ip = self.parent.find_nvr_ip(camera_name)
        if nvr_ip is None:
            return

        cls_list = self.parent.ai_server_camera_info_dict[nvr_ip][camera_name]["cls"]
        conf_list = self.parent.ai_server_camera_info_dict[nvr_ip][camera_name]["conf"]

        self.object_setting_ui.person_active_bnt.setChecked(cls_list[0])
        self.object_setting_ui.car_active_bnt.setChecked(cls_list[1])
        self.object_setting_ui.fire_active_bnt.setChecked(cls_list[2])

        self.object_setting_ui.person_conf_slider.valueChanged.connect(
            lambda value, 
                    intance = self,
                    std = self.object_setting_ui.person_conf_slider, 
                    target = self.object_setting_ui.person_conf_value, 
                    index = 0
                    : set_conf(intance, std, target, index))
        
        self.object_setting_ui.person_conf_value.valueChanged.connect(
            lambda value, 
                    intance = self,
                    std = self.object_setting_ui.person_conf_value, 
                    target = self.object_setting_ui.person_conf_slider, 
                    index = 0 : 
                    set_conf(intance, std, target, index))

        self.object_setting_ui.car_conf_slider.valueChanged.connect(
            lambda value, 
                    intance = self,
                    std = self.object_setting_ui.car_conf_slider, 
                    target = self.object_setting_ui.car_conf_value, 
                    index = 1 
                    : set_conf(intance, std, target, index))
        
        self.object_setting_ui.car_conf_value.valueChanged.connect(
            lambda value, 
                    intance = self,
                    std = self.object_setting_ui.car_conf_value, 
                    target = self.object_setting_ui.car_conf_slider, 
                    index = 1
                    : set_conf(intance, std, target, index))

        self.object_setting_ui.fire_conf_slider.valueChanged.connect(
            lambda value, 
                    intance = self,
                    std = self.object_setting_ui.fire_conf_slider, 
                    target = self.object_setting_ui.fire_conf_value, 
                    index = 2
                    : set_conf(intance, std, target, index))
        
        self.object_setting_ui.fire_conf_value.valueChanged.connect(
            lambda value,
                    intance = self,
                    std = self.object_setting_ui.fire_conf_value, 
                    target = self.object_setting_ui.fire_conf_slider, 
                    index = 2
                    : set_conf(intance, std, target, index))
        

        self.object_setting_ui.person_conf_slider.setValue(conf_list[0])
        self.object_setting_ui.car_conf_slider.setValue(conf_list[1])
        self.object_setting_ui.fire_conf_slider.setValue(conf_list[2])


        self.object_setting_ui.shutdown_bnt.clicked.connect(self.close_window)

    def close_window(self):
        camera_name = self.parent.ui_main.camera_page_name_box.currentText()
        nvr_ip = self.parent.find_nvr_ip(camera_name)
        if nvr_ip is None:
            return

        self.parent.ai_server_camera_info_dict[nvr_ip][camera_name]["cls"][0] = self.object_setting_ui.person_active_bnt.isChecked()
        self.parent.ai_server_camera_info_dict[nvr_ip][camera_name]["cls"][1] = self.object_setting_ui.car_active_bnt.isChecked()
        self.parent.ai_server_camera_info_dict[nvr_ip][camera_name]["cls"][2] = self.object_setting_ui.fire_active_bnt.isChecked()

        self.close()


def set_conf(intance, std, target, index):
    target.setValue(std.value())
    camera_name = intance.parent.ui_main.camera_page_name_box.currentText()
    nvr_ip = intance.parent.find_nvr_ip(camera_name)
    if nvr_ip is None:
        return

    intance.parent.ai_server_camera_info_dict[nvr_ip][camera_name]["conf"][index] = std.value()

def open_object_setting_window(click, self):
    self.labeling_window = Object_settint_Dialog(self)
    self.labeling_window.show()


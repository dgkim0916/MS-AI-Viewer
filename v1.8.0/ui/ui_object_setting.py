# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'object_settingDdRcCe.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)
import resourece_rc

class Ui_object_setting(object):
    def setupUi(self, object_setting):
        if not object_setting.objectName():
            object_setting.setObjectName(u"object_setting")
        object_setting.setWindowModality(Qt.WindowModality.ApplicationModal)
        object_setting.resize(508, 192)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(object_setting.sizePolicy().hasHeightForWidth())
        object_setting.setSizePolicy(sizePolicy)
        object_setting.setMaximumSize(QSize(1260, 16777215))
        object_setting.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        object_setting.setWindowTitle(u"object_setting")
        object_setting.setStyleSheet(u"background-color: rgb(3, 3, 13);")
        self.horizontalLayout_5 = QHBoxLayout(object_setting)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.top_logo = QLabel(object_setting)
        self.top_logo.setObjectName(u"top_logo")
        sizePolicy.setHeightForWidth(self.top_logo.sizePolicy().hasHeightForWidth())
        self.top_logo.setSizePolicy(sizePolicy)
        self.top_logo.setMinimumSize(QSize(202, 32))
        self.top_logo.setMaximumSize(QSize(202, 32))
        font = QFont()
        font.setFamilies([u"Sans"])
        self.top_logo.setFont(font)
        self.top_logo.setPixmap(QPixmap(u":/ui/ui/images/logo.png"))
        self.top_logo.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.top_logo)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.shutdown_bnt = QPushButton(object_setting)
        self.shutdown_bnt.setObjectName(u"shutdown_bnt")
        self.shutdown_bnt.setMinimumSize(QSize(61, 31))
        self.shutdown_bnt.setMaximumSize(QSize(61, 31))
        font1 = QFont()
        font1.setFamilies([u"NanumSquareRound"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.shutdown_bnt.setFont(font1)
        self.shutdown_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.shutdown_bnt.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.shutdown_bnt.setStyleSheet(u"background-color: rgb(237, 51, 59);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")

        self.horizontalLayout_6.addWidget(self.shutdown_bnt)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.widget = QWidget(object_setting)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.person_label = QLabel(self.widget)
        self.person_label.setObjectName(u"person_label")
        self.person_label.setMinimumSize(QSize(203, 28))
        self.person_label.setMaximumSize(QSize(203, 28))
        font2 = QFont()
        font2.setFamilies([u"Sans"])
        font2.setPointSize(11)
        self.person_label.setFont(font2)
        self.person_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.person_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.person_label)

        self.person_active_bnt = QPushButton(self.widget)
        self.person_active_bnt.setObjectName(u"person_active_bnt")
        self.person_active_bnt.setMinimumSize(QSize(61, 25))
        self.person_active_bnt.setMaximumSize(QSize(61, 25))
        self.person_active_bnt.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0px; /* \ud328\ub529\ub3c4 0\uc73c\ub85c \uc124\uc815 */\n"
"    outline: none;\n"
"}\n"
"\n"
"/* hover, pressed \uc0c1\ud0dc\uc5d0\ub3c4 \uc544\ubb34 \ud6a8\uacfc \uc5c6\uc74c */\n"
"QPushButton:hover {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/ui/ui/images/icon-switch-off.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/ui/ui/images/icon-switch-on.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.person_active_bnt.setIcon(icon)
        self.person_active_bnt.setIconSize(QSize(55, 103))
        self.person_active_bnt.setCheckable(True)

        self.horizontalLayout.addWidget(self.person_active_bnt)

        self.person_conf_slider = QSlider(self.widget)
        self.person_conf_slider.setObjectName(u"person_conf_slider")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.person_conf_slider.sizePolicy().hasHeightForWidth())
        self.person_conf_slider.setSizePolicy(sizePolicy1)
        self.person_conf_slider.setMinimumSize(QSize(114, 31))
        self.person_conf_slider.setMaximumSize(QSize(16777215, 31))
        font3 = QFont()
        font3.setPointSize(11)
        self.person_conf_slider.setFont(font3)
        self.person_conf_slider.setStyleSheet(u"QSlider::handle:horizontal {\n"
"    background-color: rgb(192, 191, 188);\n"
"    border: 1px solid #5c5c5c; /* \ud578\ub4e4\uc758 \ud14c\ub450\ub9ac */\n"
"    width: 20px; /* \ud578\ub4e4\uc758 \ub108\ube44 */\n"
"    height: 5px; /* \ud578\ub4e4\uc758 \ub108\ube44 */\n"
"     margin: -4px 0px; /* \ud578\ub4e4\uc758 \uc704, \uc544\ub798 \uc5ec\ubc31 */\n"
"    border-radius: 4px; /* \ud578\ub4e4\uc758 \ubaa8\uc11c\ub9ac \ub465\uae00\uac8c */\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 5px; /* \uc2ac\ub77c\uc774\ub354\uc758 \ud2b8\ub799 \ub192\uc774 */\n"
"    background: rgb(100, 100, 100); /* \uc2ac\ub77c\uc774\ub354 \ud2b8\ub799\uc758 \uae30\ubcf8 \uc0c9\uc0c1 */\n"
"    border-radius: 4px;\n"
"    margin: 0px; /* \ud2b8\ub799\uc758 \uc5ec\ubc31\uc744 \uc5c6\uc570 */\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(30, 195, 55); /* \uac8c\uc774\uc9c0 \uc0c9\uc0c1 */\n"
"    border: 1px solid #777;\n"
"    height: 5px; /* \ud2b8\ub799\uacfc"
                        " \ub3d9\uc77c\ud55c \ub192\uc774\ub85c \uc124\uc815 */\n"
"    border-radius: 4px;\n"
"    margin: 0px; /* \uac8c\uc774\uc9c0 \uc5ec\ubc31\uc744 \uc5c6\uc570 */\n"
"}\n"
"")
        self.person_conf_slider.setMinimum(0)
        self.person_conf_slider.setMaximum(100)
        self.person_conf_slider.setSingleStep(2)
        self.person_conf_slider.setValue(33)
        self.person_conf_slider.setTracking(False)
        self.person_conf_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.person_conf_slider)

        self.person_conf_value = QSpinBox(self.widget)
        self.person_conf_value.setObjectName(u"person_conf_value")
        sizePolicy.setHeightForWidth(self.person_conf_value.sizePolicy().hasHeightForWidth())
        self.person_conf_value.setSizePolicy(sizePolicy)
        self.person_conf_value.setMinimumSize(QSize(70, 31))
        self.person_conf_value.setMaximumSize(QSize(16777215, 31))
        font4 = QFont()
        font4.setPointSize(10)
        self.person_conf_value.setFont(font4)
        self.person_conf_value.setStyleSheet(u"\n"
"    QSpinBox {\n"
"        subcontrol-origin: padding;\n"
"        subcontrol-position: top right;\n"
"        background: rgb(13, 16, 23);\n"
"        color: rgb(255, 255, 255);\n"
"\n"
"    }")
        self.person_conf_value.setMinimum(1)
        self.person_conf_value.setMaximum(100)
        self.person_conf_value.setValue(33)

        self.horizontalLayout.addWidget(self.person_conf_value)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.car_label = QLabel(self.widget)
        self.car_label.setObjectName(u"car_label")
        self.car_label.setMinimumSize(QSize(203, 28))
        self.car_label.setMaximumSize(QSize(203, 28))
        self.car_label.setFont(font2)
        self.car_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.car_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.car_label)

        self.car_active_bnt = QPushButton(self.widget)
        self.car_active_bnt.setObjectName(u"car_active_bnt")
        self.car_active_bnt.setMinimumSize(QSize(61, 25))
        self.car_active_bnt.setMaximumSize(QSize(61, 25))
        self.car_active_bnt.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.car_active_bnt.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0px; /* \ud328\ub529\ub3c4 0\uc73c\ub85c \uc124\uc815 */\n"
"    outline: none;\n"
"}\n"
"\n"
"/* hover, pressed \uc0c1\ud0dc\uc5d0\ub3c4 \uc544\ubb34 \ud6a8\uacfc \uc5c6\uc74c */\n"
"QPushButton:hover {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.car_active_bnt.setIcon(icon)
        self.car_active_bnt.setIconSize(QSize(55, 103))
        self.car_active_bnt.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.car_active_bnt)

        self.car_conf_slider = QSlider(self.widget)
        self.car_conf_slider.setObjectName(u"car_conf_slider")
        sizePolicy1.setHeightForWidth(self.car_conf_slider.sizePolicy().hasHeightForWidth())
        self.car_conf_slider.setSizePolicy(sizePolicy1)
        self.car_conf_slider.setMinimumSize(QSize(114, 31))
        self.car_conf_slider.setMaximumSize(QSize(16777215, 31))
        self.car_conf_slider.setFont(font3)
        self.car_conf_slider.setStyleSheet(u"QSlider::handle:horizontal {\n"
"    background-color: rgb(192, 191, 188);\n"
"    border: 1px solid #5c5c5c; /* \ud578\ub4e4\uc758 \ud14c\ub450\ub9ac */\n"
"    width: 20px; /* \ud578\ub4e4\uc758 \ub108\ube44 */\n"
"    height: 5px; /* \ud578\ub4e4\uc758 \ub108\ube44 */\n"
"     margin: -4px 0px; /* \ud578\ub4e4\uc758 \uc704, \uc544\ub798 \uc5ec\ubc31 */\n"
"    border-radius: 4px; /* \ud578\ub4e4\uc758 \ubaa8\uc11c\ub9ac \ub465\uae00\uac8c */\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 5px; /* \uc2ac\ub77c\uc774\ub354\uc758 \ud2b8\ub799 \ub192\uc774 */\n"
"    background: rgb(100, 100, 100); /* \uc2ac\ub77c\uc774\ub354 \ud2b8\ub799\uc758 \uae30\ubcf8 \uc0c9\uc0c1 */\n"
"    border-radius: 4px;\n"
"    margin: 0px; /* \ud2b8\ub799\uc758 \uc5ec\ubc31\uc744 \uc5c6\uc570 */\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(30, 195, 55); /* \uac8c\uc774\uc9c0 \uc0c9\uc0c1 */\n"
"    border: 1px solid #777;\n"
"    height: 5px; /* \ud2b8\ub799\uacfc"
                        " \ub3d9\uc77c\ud55c \ub192\uc774\ub85c \uc124\uc815 */\n"
"    border-radius: 4px;\n"
"    margin: 0px; /* \uac8c\uc774\uc9c0 \uc5ec\ubc31\uc744 \uc5c6\uc570 */\n"
"}\n"
"")
        self.car_conf_slider.setMinimum(0)
        self.car_conf_slider.setMaximum(100)
        self.car_conf_slider.setSingleStep(2)
        self.car_conf_slider.setValue(33)
        self.car_conf_slider.setTracking(False)
        self.car_conf_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_2.addWidget(self.car_conf_slider)

        self.car_conf_value = QSpinBox(self.widget)
        self.car_conf_value.setObjectName(u"car_conf_value")
        sizePolicy.setHeightForWidth(self.car_conf_value.sizePolicy().hasHeightForWidth())
        self.car_conf_value.setSizePolicy(sizePolicy)
        self.car_conf_value.setMinimumSize(QSize(70, 31))
        self.car_conf_value.setMaximumSize(QSize(16777215, 31))
        self.car_conf_value.setFont(font4)
        self.car_conf_value.setStyleSheet(u"\n"
"    QSpinBox {\n"
"        subcontrol-origin: padding;\n"
"        subcontrol-position: top right;\n"
"        background: rgb(13, 16, 23);\n"
"        color: rgb(255, 255, 255);\n"
"\n"
"    }")
        self.car_conf_value.setMinimum(1)
        self.car_conf_value.setMaximum(100)
        self.car_conf_value.setValue(33)

        self.horizontalLayout_2.addWidget(self.car_conf_value)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.fire_label = QLabel(self.widget)
        self.fire_label.setObjectName(u"fire_label")
        self.fire_label.setMinimumSize(QSize(203, 28))
        self.fire_label.setMaximumSize(QSize(203, 28))
        self.fire_label.setFont(font2)
        self.fire_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.fire_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.fire_label)

        self.fire_active_bnt = QPushButton(self.widget)
        self.fire_active_bnt.setObjectName(u"fire_active_bnt")
        self.fire_active_bnt.setMinimumSize(QSize(61, 25))
        self.fire_active_bnt.setMaximumSize(QSize(61, 25))
        self.fire_active_bnt.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0px; /* \ud328\ub529\ub3c4 0\uc73c\ub85c \uc124\uc815 */\n"
"    outline: none;\n"
"}\n"
"\n"
"/* hover, pressed \uc0c1\ud0dc\uc5d0\ub3c4 \uc544\ubb34 \ud6a8\uacfc \uc5c6\uc74c */\n"
"QPushButton:hover {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.fire_active_bnt.setIcon(icon)
        self.fire_active_bnt.setIconSize(QSize(55, 103))
        self.fire_active_bnt.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.fire_active_bnt)

        self.fire_conf_slider = QSlider(self.widget)
        self.fire_conf_slider.setObjectName(u"fire_conf_slider")
        sizePolicy1.setHeightForWidth(self.fire_conf_slider.sizePolicy().hasHeightForWidth())
        self.fire_conf_slider.setSizePolicy(sizePolicy1)
        self.fire_conf_slider.setMinimumSize(QSize(114, 31))
        self.fire_conf_slider.setMaximumSize(QSize(16777215, 31))
        self.fire_conf_slider.setFont(font3)
        self.fire_conf_slider.setStyleSheet(u"QSlider::handle:horizontal {\n"
"    background-color: rgb(192, 191, 188);\n"
"    border: 1px solid #5c5c5c; /* \ud578\ub4e4\uc758 \ud14c\ub450\ub9ac */\n"
"    width: 20px; /* \ud578\ub4e4\uc758 \ub108\ube44 */\n"
"    height: 5px; /* \ud578\ub4e4\uc758 \ub108\ube44 */\n"
"     margin: -4px 0px; /* \ud578\ub4e4\uc758 \uc704, \uc544\ub798 \uc5ec\ubc31 */\n"
"    border-radius: 4px; /* \ud578\ub4e4\uc758 \ubaa8\uc11c\ub9ac \ub465\uae00\uac8c */\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 5px; /* \uc2ac\ub77c\uc774\ub354\uc758 \ud2b8\ub799 \ub192\uc774 */\n"
"    background: rgb(100, 100, 100); /* \uc2ac\ub77c\uc774\ub354 \ud2b8\ub799\uc758 \uae30\ubcf8 \uc0c9\uc0c1 */\n"
"    border-radius: 4px;\n"
"    margin: 0px; /* \ud2b8\ub799\uc758 \uc5ec\ubc31\uc744 \uc5c6\uc570 */\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(30, 195, 55); /* \uac8c\uc774\uc9c0 \uc0c9\uc0c1 */\n"
"    border: 1px solid #777;\n"
"    height: 5px; /* \ud2b8\ub799\uacfc"
                        " \ub3d9\uc77c\ud55c \ub192\uc774\ub85c \uc124\uc815 */\n"
"    border-radius: 4px;\n"
"    margin: 0px; /* \uac8c\uc774\uc9c0 \uc5ec\ubc31\uc744 \uc5c6\uc570 */\n"
"}\n"
"")
        self.fire_conf_slider.setMinimum(0)
        self.fire_conf_slider.setMaximum(100)
        self.fire_conf_slider.setSingleStep(2)
        self.fire_conf_slider.setValue(33)
        self.fire_conf_slider.setTracking(False)
        self.fire_conf_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_3.addWidget(self.fire_conf_slider)

        self.fire_conf_value = QSpinBox(self.widget)
        self.fire_conf_value.setObjectName(u"fire_conf_value")
        sizePolicy.setHeightForWidth(self.fire_conf_value.sizePolicy().hasHeightForWidth())
        self.fire_conf_value.setSizePolicy(sizePolicy)
        self.fire_conf_value.setMinimumSize(QSize(70, 31))
        self.fire_conf_value.setMaximumSize(QSize(16777215, 31))
        self.fire_conf_value.setFont(font4)
        self.fire_conf_value.setStyleSheet(u"\n"
"    QSpinBox {\n"
"        subcontrol-origin: padding;\n"
"        subcontrol-position: top right;\n"
"        background: rgb(13, 16, 23);\n"
"        color: rgb(255, 255, 255);\n"
"\n"
"    }")
        self.fire_conf_value.setMinimum(1)
        self.fire_conf_value.setMaximum(100)
        self.fire_conf_value.setValue(33)

        self.horizontalLayout_3.addWidget(self.fire_conf_value)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.verticalLayout_2.addWidget(self.widget)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.retranslateUi(object_setting)

        QMetaObject.connectSlotsByName(object_setting)
    # setupUi

    def retranslateUi(self, object_setting):
        self.top_logo.setText("")
        self.shutdown_bnt.setText(QCoreApplication.translate("object_setting", u"\ub2eb\uae30", None))
        self.person_label.setText(QCoreApplication.translate("object_setting", u"\uc0ac\ub78c", None))
        self.person_active_bnt.setText("")
        self.car_label.setText(QCoreApplication.translate("object_setting", u"\ud0c8\uac83(\uc790\ub3d9\ucc28, \uc790\uc804\uac70, \uc624\ud1a0\ubc14\uc774)", None))
        self.car_active_bnt.setText("")
        self.fire_label.setText(QCoreApplication.translate("object_setting", u"\ubd88", None))
        self.fire_active_bnt.setText("")
        pass
    # retranslateUi


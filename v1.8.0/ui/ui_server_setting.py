# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'server_settingECTgcW.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resourece_rc
import resourece_rc

class Ui_server_setting_window(object):
    def setupUi(self, server_setting_window):
        if not server_setting_window.objectName():
            server_setting_window.setObjectName(u"server_setting_window")
        server_setting_window.setWindowModality(Qt.WindowModality.WindowModal)
        server_setting_window.resize(678, 689)
        icon = QIcon()
        icon.addFile(u":/ui/ui/images/icon2.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        server_setting_window.setWindowIcon(icon)
        server_setting_window.setStyleSheet(u"background-color: rgb(16,16, 16);")
        self.verticalLayout_5 = QVBoxLayout(server_setting_window)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.top_logo_2 = QLabel(server_setting_window)
        self.top_logo_2.setObjectName(u"top_logo_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_logo_2.sizePolicy().hasHeightForWidth())
        self.top_logo_2.setSizePolicy(sizePolicy)
        self.top_logo_2.setMinimumSize(QSize(202, 32))
        self.top_logo_2.setMaximumSize(QSize(202, 32))
        font = QFont()
        font.setFamilies([u"Sans"])
        self.top_logo_2.setFont(font)
        self.top_logo_2.setPixmap(QPixmap(u":/ui/ui/images/logo.png"))
        self.top_logo_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.top_logo_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.shutdown_bnt = QPushButton(server_setting_window)
        self.shutdown_bnt.setObjectName(u"shutdown_bnt")
        self.shutdown_bnt.setMinimumSize(QSize(61, 31))
        self.shutdown_bnt.setMaximumSize(QSize(61, 31))
        font1 = QFont()
        font1.setFamilies([u"NanumSquareRound"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.shutdown_bnt.setFont(font1)
        self.shutdown_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.shutdown_bnt.setStyleSheet(u"background-color: rgb(237, 51, 59);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")

        self.horizontalLayout_4.addWidget(self.shutdown_bnt)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(server_setting_window)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(25, 25, 25);\n"
"\n"
"border-radius: 19px;\n"
"")
        self.verticalLayout_50 = QVBoxLayout(self.widget_2)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.alarm_memu_bnt = QPushButton(self.widget_2)
        self.alarm_memu_bnt.setObjectName(u"alarm_memu_bnt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.alarm_memu_bnt.sizePolicy().hasHeightForWidth())
        self.alarm_memu_bnt.setSizePolicy(sizePolicy1)
        self.alarm_memu_bnt.setMinimumSize(QSize(171, 41))
        self.alarm_memu_bnt.setMaximumSize(QSize(171, 41))
        font2 = QFont()
        font2.setFamilies([u"Sans"])
        font2.setPointSize(11)
        self.alarm_memu_bnt.setFont(font2)
        self.alarm_memu_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.alarm_memu_bnt.setStyleSheet(u"border-radius: 20px;\n"
"border: 1px solid rgb(179,179,179);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(30, 30, 30);\n"
"")
        self.alarm_memu_bnt.setCheckable(True)
        self.alarm_memu_bnt.setChecked(False)
        self.alarm_memu_bnt.setAutoExclusive(True)

        self.verticalLayout_48.addWidget(self.alarm_memu_bnt)

        self.user_setting_bnt = QPushButton(self.widget_2)
        self.user_setting_bnt.setObjectName(u"user_setting_bnt")
        sizePolicy1.setHeightForWidth(self.user_setting_bnt.sizePolicy().hasHeightForWidth())
        self.user_setting_bnt.setSizePolicy(sizePolicy1)
        self.user_setting_bnt.setMinimumSize(QSize(171, 41))
        self.user_setting_bnt.setMaximumSize(QSize(171, 41))
        self.user_setting_bnt.setFont(font2)
        self.user_setting_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.user_setting_bnt.setStyleSheet(u"border-radius: 20px;\n"
"border: 1px solid rgb(179,179,179);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(30, 30, 30);\n"
"")
        self.user_setting_bnt.setCheckable(True)
        self.user_setting_bnt.setChecked(False)
        self.user_setting_bnt.setAutoExclusive(True)

        self.verticalLayout_48.addWidget(self.user_setting_bnt)

        self.admin_setting_but = QPushButton(self.widget_2)
        self.admin_setting_but.setObjectName(u"admin_setting_but")
        sizePolicy1.setHeightForWidth(self.admin_setting_but.sizePolicy().hasHeightForWidth())
        self.admin_setting_but.setSizePolicy(sizePolicy1)
        self.admin_setting_but.setMinimumSize(QSize(171, 41))
        self.admin_setting_but.setMaximumSize(QSize(171, 41))
        self.admin_setting_but.setFont(font2)
        self.admin_setting_but.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.admin_setting_but.setStyleSheet(u"border-radius: 20px;\n"
"border: 1px solid rgb(179,179,179);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(30, 30, 30);\n"
"")
        self.admin_setting_but.setCheckable(True)
        self.admin_setting_but.setChecked(False)
        self.admin_setting_but.setAutoExclusive(True)

        self.verticalLayout_48.addWidget(self.admin_setting_but)


        self.verticalLayout_49.addLayout(self.verticalLayout_48)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_49.addItem(self.verticalSpacer_23)


        self.verticalLayout_50.addLayout(self.verticalLayout_49)


        self.horizontalLayout.addWidget(self.widget_2)

        self.stackedWidget = QStackedWidget(server_setting_window)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_14 = QWidget(self.page)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMaximumSize(QSize(16777215, 166))
        self.verticalLayout_62 = QVBoxLayout(self.widget_14)
        self.verticalLayout_62.setSpacing(8)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalSpacer_56 = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_56)

        self.setting_event_pop_up_label = QLabel(self.widget_14)
        self.setting_event_pop_up_label.setObjectName(u"setting_event_pop_up_label")
        self.setting_event_pop_up_label.setMinimumSize(QSize(197, 28))
        self.setting_event_pop_up_label.setMaximumSize(QSize(9999, 28))
        font3 = QFont()
        font3.setFamilies([u"Sans"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.setting_event_pop_up_label.setFont(font3)
        self.setting_event_pop_up_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_event_pop_up_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_62.addWidget(self.setting_event_pop_up_label)

        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_50)


        self.verticalLayout_62.addLayout(self.horizontalLayout_62)

        self.horizontalLayout_100 = QHBoxLayout()
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalSpacer_58 = QSpacerItem(115, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_58)

        self.setting_event_pop_up_active_label = QLabel(self.widget_14)
        self.setting_event_pop_up_active_label.setObjectName(u"setting_event_pop_up_active_label")
        self.setting_event_pop_up_active_label.setMinimumSize(QSize(91, 28))
        self.setting_event_pop_up_active_label.setMaximumSize(QSize(140, 28))
        self.setting_event_pop_up_active_label.setFont(font2)
        self.setting_event_pop_up_active_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_event_pop_up_active_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_100.addWidget(self.setting_event_pop_up_active_label)

        self.setting_event_pop_up_active_bnt = QPushButton(self.widget_14)
        self.setting_event_pop_up_active_bnt.setObjectName(u"setting_event_pop_up_active_bnt")
        self.setting_event_pop_up_active_bnt.setMinimumSize(QSize(61, 25))
        self.setting_event_pop_up_active_bnt.setMaximumSize(QSize(61, 25))
        self.setting_event_pop_up_active_bnt.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/ui/ui/images/icon-switch-off.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/ui/ui/images/icon-switch-on.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon1.addFile(u":/ui/ui/images/icon-switch-off.png", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        icon1.addFile(u":/ui/ui/images/icon-switch-on.png", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.setting_event_pop_up_active_bnt.setIcon(icon1)
        self.setting_event_pop_up_active_bnt.setIconSize(QSize(55, 103))
        self.setting_event_pop_up_active_bnt.setCheckable(True)

        self.horizontalLayout_100.addWidget(self.setting_event_pop_up_active_bnt)

        self.horizontalSpacer_59 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_59)


        self.verticalLayout_62.addLayout(self.horizontalLayout_100)

        self.horizontalLayout_101 = QHBoxLayout()
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalSpacer_139 = QSpacerItem(115, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_101.addItem(self.horizontalSpacer_139)

        self.setting_event_pop_up_duration_bnt = QLabel(self.widget_14)
        self.setting_event_pop_up_duration_bnt.setObjectName(u"setting_event_pop_up_duration_bnt")
        self.setting_event_pop_up_duration_bnt.setMinimumSize(QSize(91, 28))
        self.setting_event_pop_up_duration_bnt.setMaximumSize(QSize(120, 28))
        self.setting_event_pop_up_duration_bnt.setFont(font2)
        self.setting_event_pop_up_duration_bnt.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_event_pop_up_duration_bnt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_101.addWidget(self.setting_event_pop_up_duration_bnt)

        self.setting_event_pop_up_duration_box = QComboBox(self.widget_14)
        self.setting_event_pop_up_duration_box.addItem("")
        self.setting_event_pop_up_duration_box.addItem("")
        self.setting_event_pop_up_duration_box.addItem("")
        self.setting_event_pop_up_duration_box.addItem("")
        self.setting_event_pop_up_duration_box.addItem("")
        self.setting_event_pop_up_duration_box.setObjectName(u"setting_event_pop_up_duration_box")
        sizePolicy.setHeightForWidth(self.setting_event_pop_up_duration_box.sizePolicy().hasHeightForWidth())
        self.setting_event_pop_up_duration_box.setSizePolicy(sizePolicy)
        self.setting_event_pop_up_duration_box.setMinimumSize(QSize(80, 24))
        self.setting_event_pop_up_duration_box.setMaximumSize(QSize(68, 24))
        font4 = QFont()
        font4.setFamilies([u"Sans"])
        font4.setPointSize(10)
        font4.setBold(False)
        self.setting_event_pop_up_duration_box.setFont(font4)
        self.setting_event_pop_up_duration_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(13, 16, 23);\n"
"\n"
"")
        self.setting_event_pop_up_duration_box.setEditable(True)
        self.setting_event_pop_up_duration_box.setMinimumContentsLength(0)

        self.horizontalLayout_101.addWidget(self.setting_event_pop_up_duration_box)

        self.horizontalSpacer_140 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_101.addItem(self.horizontalSpacer_140)


        self.verticalLayout_62.addLayout(self.horizontalLayout_101)

        self.horizontalLayout_102 = QHBoxLayout()
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalSpacer_141 = QSpacerItem(224, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_102.addItem(self.horizontalSpacer_141)

        self.setting_event_pop_up_save_bnt = QPushButton(self.widget_14)
        self.setting_event_pop_up_save_bnt.setObjectName(u"setting_event_pop_up_save_bnt")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.setting_event_pop_up_save_bnt.sizePolicy().hasHeightForWidth())
        self.setting_event_pop_up_save_bnt.setSizePolicy(sizePolicy2)
        self.setting_event_pop_up_save_bnt.setMinimumSize(QSize(71, 41))
        self.setting_event_pop_up_save_bnt.setMaximumSize(QSize(71, 41))
        font5 = QFont()
        font5.setFamilies([u"Sans"])
        font5.setPointSize(10)
        self.setting_event_pop_up_save_bnt.setFont(font5)
        self.setting_event_pop_up_save_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setting_event_pop_up_save_bnt.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.0 rgba(112, 210, 112, 255),\n"
"    stop:0.3 rgba(0, 196, 0, 255)\n"
");\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 19px;\n"
"\n"
"")

        self.horizontalLayout_102.addWidget(self.setting_event_pop_up_save_bnt)

        self.horizontalSpacer_142 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_102.addItem(self.horizontalSpacer_142)


        self.verticalLayout_62.addLayout(self.horizontalLayout_102)


        self.verticalLayout.addWidget(self.widget_14)

        self.setting_partion_4 = QFrame(self.page)
        self.setting_partion_4.setObjectName(u"setting_partion_4")
        sizePolicy.setHeightForWidth(self.setting_partion_4.sizePolicy().hasHeightForWidth())
        self.setting_partion_4.setSizePolicy(sizePolicy)
        self.setting_partion_4.setMinimumSize(QSize(246, 3))
        self.setting_partion_4.setMaximumSize(QSize(434, 3))
        font6 = QFont()
        font6.setFamilies([u"Sans"])
        font6.setPointSize(5)
        font6.setStrikeOut(False)
        self.setting_partion_4.setFont(font6)
        self.setting_partion_4.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setting_partion_4.setAutoFillBackground(False)
        self.setting_partion_4.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.setting_partion_4.setFrameShape(QFrame.Shape.HLine)
        self.setting_partion_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.setting_partion_4)

        self.setting_sms_widget = QWidget(self.page)
        self.setting_sms_widget.setObjectName(u"setting_sms_widget")
        self.verticalLayout_17 = QVBoxLayout(self.setting_sms_widget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_61 = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_61)

        self.setting_notice_label = QLabel(self.setting_sms_widget)
        self.setting_notice_label.setObjectName(u"setting_notice_label")
        sizePolicy.setHeightForWidth(self.setting_notice_label.sizePolicy().hasHeightForWidth())
        self.setting_notice_label.setSizePolicy(sizePolicy)
        self.setting_notice_label.setMinimumSize(QSize(153, 31))
        font7 = QFont()
        font7.setFamilies([u"Sans"])
        font7.setPointSize(12)
        font7.setBold(True)
        self.setting_notice_label.setFont(font7)
        self.setting_notice_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_notice_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_15.addWidget(self.setting_notice_label)

        self.horizontalSpacer_150 = QSpacerItem(54, 13, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_150)

        self.setting_notice_phone_active_bnt = QPushButton(self.setting_sms_widget)
        self.setting_notice_phone_active_bnt.setObjectName(u"setting_notice_phone_active_bnt")
        self.setting_notice_phone_active_bnt.setMinimumSize(QSize(61, 25))
        self.setting_notice_phone_active_bnt.setMaximumSize(QSize(61, 25))
        self.setting_notice_phone_active_bnt.setStyleSheet(u"QPushButton {\n"
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
        self.setting_notice_phone_active_bnt.setIcon(icon1)
        self.setting_notice_phone_active_bnt.setIconSize(QSize(55, 103))
        self.setting_notice_phone_active_bnt.setCheckable(True)

        self.horizontalLayout_15.addWidget(self.setting_notice_phone_active_bnt)

        self.horizontalSpacer_62 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_62)


        self.verticalLayout_17.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_145 = QSpacerItem(26, 13, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_145)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.setting_notice_phone_num_input = QLineEdit(self.setting_sms_widget)
        self.setting_notice_phone_num_input.setObjectName(u"setting_notice_phone_num_input")
        self.setting_notice_phone_num_input.setMaximumSize(QSize(121, 41))
        self.setting_notice_phone_num_input.setFont(font5)
        self.setting_notice_phone_num_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setting_notice_phone_num_input.setStyleSheet(u"qproperty-frame: false;\n"
"font-size:10pt;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_19.addWidget(self.setting_notice_phone_num_input)

        self.setting_notice_phone_add_bnt = QPushButton(self.setting_sms_widget)
        self.setting_notice_phone_add_bnt.setObjectName(u"setting_notice_phone_add_bnt")
        sizePolicy.setHeightForWidth(self.setting_notice_phone_add_bnt.sizePolicy().hasHeightForWidth())
        self.setting_notice_phone_add_bnt.setSizePolicy(sizePolicy)
        self.setting_notice_phone_add_bnt.setMinimumSize(QSize(31, 31))
        self.setting_notice_phone_add_bnt.setFont(font5)
        self.setting_notice_phone_add_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setting_notice_phone_add_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/ui/ui/images/ico_add_circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setting_notice_phone_add_bnt.setIcon(icon2)
        self.setting_notice_phone_add_bnt.setIconSize(QSize(31, 50))

        self.horizontalLayout_19.addWidget(self.setting_notice_phone_add_bnt)

        self.setting_notice_phone_del_bnt = QPushButton(self.setting_sms_widget)
        self.setting_notice_phone_del_bnt.setObjectName(u"setting_notice_phone_del_bnt")
        sizePolicy.setHeightForWidth(self.setting_notice_phone_del_bnt.sizePolicy().hasHeightForWidth())
        self.setting_notice_phone_del_bnt.setSizePolicy(sizePolicy)
        self.setting_notice_phone_del_bnt.setMinimumSize(QSize(31, 31))
        self.setting_notice_phone_del_bnt.setFont(font5)
        self.setting_notice_phone_del_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setting_notice_phone_del_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/ui/ui/images/ico_delete.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setting_notice_phone_del_bnt.setIcon(icon3)
        self.setting_notice_phone_del_bnt.setIconSize(QSize(31, 50))

        self.horizontalLayout_19.addWidget(self.setting_notice_phone_del_bnt)

        self.horizontalSpacer_146 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_146)


        self.verticalLayout_18.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_17.addLayout(self.verticalLayout_18)


        self.verticalLayout_17.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(1)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_147 = QSpacerItem(13, 13, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_147)

        self.setting_notice_phone_list = QTableWidget(self.setting_sms_widget)
        if (self.setting_notice_phone_list.columnCount() < 1):
            self.setting_notice_phone_list.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.setting_notice_phone_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.setting_notice_phone_list.setObjectName(u"setting_notice_phone_list")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.setting_notice_phone_list.sizePolicy().hasHeightForWidth())
        self.setting_notice_phone_list.setSizePolicy(sizePolicy3)
        self.setting_notice_phone_list.setMinimumSize(QSize(203, 273))
        self.setting_notice_phone_list.setMaximumSize(QSize(203, 9999))
        self.setting_notice_phone_list.setFont(font)
        self.setting_notice_phone_list.setStyleSheet(u"QTableWidget {\n"
"    background-color: rgb(25, 25, 25); /* \ud14c\uc774\ube14 \uc804\uccb4 \ubc30\uacbd\uc0c9 */\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: rgb(209, 209, 209); /* \ud5e4\ub354 \ud14d\uc2a4\ud2b8 \uc0c9\uc0c1 - \ud68c\uc0c9 */\n"
"background-color: rgb(7, 7, 16); /* \ud14c\uc774\ube14 \uc804\uccb4 \ubc30\uacbd\uc0c9 */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    color: rgb(255, 255, 255); /* \uae30\ubcf8 \uc0c1\ud0dc\uc5d0\uc11c\uc758 \ud14d\uc2a4\ud2b8 \uc0c9\uc0c1 - \ud770\uc0c9 */\n"
"\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(32,39,49); /* \uc120\ud0dd\ub41c \uc140\uc758 \ubc30\uacbd\uc0c9 */\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #999999;\n"
"    background: #b3b3b3c6;\n"
"    width: 8px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"background: #2f2f2f; \n"
"min-height: 10px;\n"
"width: 8px;\n"
"\n"
"}\n"
"")
        self.setting_notice_phone_list.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.setting_notice_phone_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setting_notice_phone_list.setDragDropOverwriteMode(False)
        self.setting_notice_phone_list.setAlternatingRowColors(False)
        self.setting_notice_phone_list.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setting_notice_phone_list.setShowGrid(False)
        self.setting_notice_phone_list.setGridStyle(Qt.PenStyle.NoPen)
        self.setting_notice_phone_list.setWordWrap(False)
        self.setting_notice_phone_list.setCornerButtonEnabled(False)
        self.setting_notice_phone_list.horizontalHeader().setHighlightSections(False)
        self.setting_notice_phone_list.horizontalHeader().setStretchLastSection(True)
        self.setting_notice_phone_list.verticalHeader().setVisible(False)
        self.setting_notice_phone_list.verticalHeader().setHighlightSections(False)

        self.horizontalLayout_20.addWidget(self.setting_notice_phone_list)

        self.widget_7 = QWidget(self.setting_sms_widget)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_19 = QVBoxLayout(self.widget_7)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.setting_notice_label_2 = QLabel(self.widget_7)
        self.setting_notice_label_2.setObjectName(u"setting_notice_label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.setting_notice_label_2.sizePolicy().hasHeightForWidth())
        self.setting_notice_label_2.setSizePolicy(sizePolicy4)
        self.setting_notice_label_2.setMinimumSize(QSize(104, 27))
        self.setting_notice_label_2.setMaximumSize(QSize(104, 27))
        self.setting_notice_label_2.setFont(font2)
        self.setting_notice_label_2.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_notice_label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_19.addWidget(self.setting_notice_label_2)

        self.setting_notion_detect_type_widget = QWidget(self.widget_7)
        self.setting_notion_detect_type_widget.setObjectName(u"setting_notion_detect_type_widget")
        self.gridLayout = QGridLayout(self.setting_notion_detect_type_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.setting_notion_detect_type_bnt1 = QPushButton(self.setting_notion_detect_type_widget)
        self.setting_notion_detect_type_bnt1.setObjectName(u"setting_notion_detect_type_bnt1")
        self.setting_notion_detect_type_bnt1.setStyleSheet(u"color: rgb(179,179,179);\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/ui/ui/images/check_off.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/ui/ui/images/check.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.setting_notion_detect_type_bnt1.setIcon(icon4)
        self.setting_notion_detect_type_bnt1.setCheckable(True)

        self.gridLayout.addWidget(self.setting_notion_detect_type_bnt1, 0, 0, 1, 1)

        self.setting_notion_detect_type_bnt2 = QPushButton(self.setting_notion_detect_type_widget)
        self.setting_notion_detect_type_bnt2.setObjectName(u"setting_notion_detect_type_bnt2")
        self.setting_notion_detect_type_bnt2.setStyleSheet(u"color: rgb(179,179,179);\n"
"")
        self.setting_notion_detect_type_bnt2.setIcon(icon4)
        self.setting_notion_detect_type_bnt2.setCheckable(True)

        self.gridLayout.addWidget(self.setting_notion_detect_type_bnt2, 0, 1, 1, 1)

        self.setting_notion_detect_type_bnt3 = QPushButton(self.setting_notion_detect_type_widget)
        self.setting_notion_detect_type_bnt3.setObjectName(u"setting_notion_detect_type_bnt3")
        self.setting_notion_detect_type_bnt3.setStyleSheet(u"color: rgb(179,179,179);\n"
"")
        self.setting_notion_detect_type_bnt3.setIcon(icon4)
        self.setting_notion_detect_type_bnt3.setCheckable(True)

        self.gridLayout.addWidget(self.setting_notion_detect_type_bnt3, 1, 0, 1, 1)

        self.setting_notion_detect_type_bnt4 = QPushButton(self.setting_notion_detect_type_widget)
        self.setting_notion_detect_type_bnt4.setObjectName(u"setting_notion_detect_type_bnt4")
        self.setting_notion_detect_type_bnt4.setStyleSheet(u"color: rgb(179,179,179);\n"
"")
        self.setting_notion_detect_type_bnt4.setIcon(icon4)
        self.setting_notion_detect_type_bnt4.setCheckable(True)

        self.gridLayout.addWidget(self.setting_notion_detect_type_bnt4, 1, 1, 1, 1)


        self.verticalLayout_19.addWidget(self.setting_notion_detect_type_widget)

        self.verticalSpacer = QSpacerItem(20, 162, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer)


        self.horizontalLayout_20.addWidget(self.widget_7)

        self.horizontalSpacer_151 = QSpacerItem(40, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_151)


        self.verticalLayout_17.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalSpacer_148 = QSpacerItem(224, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_148)

        self.setting_notice_phone_save_bnt = QPushButton(self.setting_sms_widget)
        self.setting_notice_phone_save_bnt.setObjectName(u"setting_notice_phone_save_bnt")
        sizePolicy2.setHeightForWidth(self.setting_notice_phone_save_bnt.sizePolicy().hasHeightForWidth())
        self.setting_notice_phone_save_bnt.setSizePolicy(sizePolicy2)
        self.setting_notice_phone_save_bnt.setMinimumSize(QSize(76, 41))
        self.setting_notice_phone_save_bnt.setMaximumSize(QSize(71, 41))
        self.setting_notice_phone_save_bnt.setFont(font5)
        self.setting_notice_phone_save_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setting_notice_phone_save_bnt.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.0 rgba(112, 210, 112, 255),\n"
"    stop:0.3 rgba(0, 196, 0, 255)\n"
");\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 19px;\n"
"\n"
"")

        self.horizontalLayout_97.addWidget(self.setting_notice_phone_save_bnt)

        self.horizontalSpacer_149 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_149)


        self.verticalLayout_17.addLayout(self.horizontalLayout_97)


        self.verticalLayout.addWidget(self.setting_sms_widget)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_40)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.admin_sms_alarm_fn_active_label = QLabel(self.page_2)
        self.admin_sms_alarm_fn_active_label.setObjectName(u"admin_sms_alarm_fn_active_label")
        self.admin_sms_alarm_fn_active_label.setMinimumSize(QSize(160, 25))
        self.admin_sms_alarm_fn_active_label.setMaximumSize(QSize(200, 25))
        self.admin_sms_alarm_fn_active_label.setFont(font2)
        self.admin_sms_alarm_fn_active_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.admin_sms_alarm_fn_active_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_44.addWidget(self.admin_sms_alarm_fn_active_label)

        self.admin_sms_alarm_fn_active_bnt = QPushButton(self.page_2)
        self.admin_sms_alarm_fn_active_bnt.setObjectName(u"admin_sms_alarm_fn_active_bnt")
        self.admin_sms_alarm_fn_active_bnt.setMinimumSize(QSize(61, 25))
        self.admin_sms_alarm_fn_active_bnt.setMaximumSize(QSize(61, 25))
        self.admin_sms_alarm_fn_active_bnt.setStyleSheet(u"QPushButton {\n"
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
        icon5 = QIcon()
        icon5.addFile(u":/ui/ui/images/icon-switch-off.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/ui/ui/images/icon-switch-on.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.admin_sms_alarm_fn_active_bnt.setIcon(icon5)
        self.admin_sms_alarm_fn_active_bnt.setIconSize(QSize(55, 103))
        self.admin_sms_alarm_fn_active_bnt.setCheckable(True)

        self.horizontalLayout_44.addWidget(self.admin_sms_alarm_fn_active_bnt)


        self.horizontalLayout_45.addLayout(self.horizontalLayout_44)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_41)


        self.verticalLayout_2.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_98 = QHBoxLayout()
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalSpacer_137 = QSpacerItem(98, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_98.addItem(self.horizontalSpacer_137)

        self.horizontalLayout_99 = QHBoxLayout()
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.admin_sms_alarm_allow_phone_num_label = QLabel(self.page_2)
        self.admin_sms_alarm_allow_phone_num_label.setObjectName(u"admin_sms_alarm_allow_phone_num_label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.admin_sms_alarm_allow_phone_num_label.sizePolicy().hasHeightForWidth())
        self.admin_sms_alarm_allow_phone_num_label.setSizePolicy(sizePolicy5)
        self.admin_sms_alarm_allow_phone_num_label.setMinimumSize(QSize(129, 27))
        self.admin_sms_alarm_allow_phone_num_label.setMaximumSize(QSize(155, 27))
        self.admin_sms_alarm_allow_phone_num_label.setFont(font2)
        self.admin_sms_alarm_allow_phone_num_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.admin_sms_alarm_allow_phone_num_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_99.addWidget(self.admin_sms_alarm_allow_phone_num_label)

        self.verticalLayout_61 = QVBoxLayout()
        self.verticalLayout_61.setSpacing(1)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.admin_sms_alarm_allow_phone_num_input = QLineEdit(self.page_2)
        self.admin_sms_alarm_allow_phone_num_input.setObjectName(u"admin_sms_alarm_allow_phone_num_input")
        sizePolicy.setHeightForWidth(self.admin_sms_alarm_allow_phone_num_input.sizePolicy().hasHeightForWidth())
        self.admin_sms_alarm_allow_phone_num_input.setSizePolicy(sizePolicy)
        self.admin_sms_alarm_allow_phone_num_input.setMinimumSize(QSize(94, 19))
        self.admin_sms_alarm_allow_phone_num_input.setMaximumSize(QSize(94, 19))
        self.admin_sms_alarm_allow_phone_num_input.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.admin_sms_alarm_allow_phone_num_input.setEchoMode(QLineEdit.EchoMode.Normal)
        self.admin_sms_alarm_allow_phone_num_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_61.addWidget(self.admin_sms_alarm_allow_phone_num_input)

        self.admin_sms_alarm_allow_phone_num_input_line = QFrame(self.page_2)
        self.admin_sms_alarm_allow_phone_num_input_line.setObjectName(u"admin_sms_alarm_allow_phone_num_input_line")
        sizePolicy.setHeightForWidth(self.admin_sms_alarm_allow_phone_num_input_line.sizePolicy().hasHeightForWidth())
        self.admin_sms_alarm_allow_phone_num_input_line.setSizePolicy(sizePolicy)
        self.admin_sms_alarm_allow_phone_num_input_line.setMinimumSize(QSize(94, 3))
        self.admin_sms_alarm_allow_phone_num_input_line.setMaximumSize(QSize(94, 3))
        self.admin_sms_alarm_allow_phone_num_input_line.setFont(font6)
        self.admin_sms_alarm_allow_phone_num_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.admin_sms_alarm_allow_phone_num_input_line.setAutoFillBackground(False)
        self.admin_sms_alarm_allow_phone_num_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.admin_sms_alarm_allow_phone_num_input_line.setFrameShape(QFrame.Shape.HLine)
        self.admin_sms_alarm_allow_phone_num_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_61.addWidget(self.admin_sms_alarm_allow_phone_num_input_line)


        self.horizontalLayout_99.addLayout(self.verticalLayout_61)


        self.horizontalLayout_98.addLayout(self.horizontalLayout_99)

        self.horizontalSpacer_138 = QSpacerItem(40, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_98.addItem(self.horizontalSpacer_138)


        self.verticalLayout_2.addLayout(self.horizontalLayout_98)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_60 = QSpacerItem(43, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_60)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(17)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.admin_live_viewer_block_label = QLabel(self.page_2)
        self.admin_live_viewer_block_label.setObjectName(u"admin_live_viewer_block_label")
        self.admin_live_viewer_block_label.setMinimumSize(QSize(160, 25))
        self.admin_live_viewer_block_label.setMaximumSize(QSize(167, 25))
        self.admin_live_viewer_block_label.setFont(font2)
        self.admin_live_viewer_block_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.admin_live_viewer_block_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.admin_live_viewer_block_label)

        self.admin_live_viewer_block_bnt = QPushButton(self.page_2)
        self.admin_live_viewer_block_bnt.setObjectName(u"admin_live_viewer_block_bnt")
        self.admin_live_viewer_block_bnt.setMinimumSize(QSize(61, 25))
        self.admin_live_viewer_block_bnt.setMaximumSize(QSize(61, 25))
        self.admin_live_viewer_block_bnt.setStyleSheet(u"QPushButton {\n"
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
        self.admin_live_viewer_block_bnt.setIcon(icon5)
        self.admin_live_viewer_block_bnt.setIconSize(QSize(55, 103))
        self.admin_live_viewer_block_bnt.setCheckable(True)

        self.horizontalLayout_23.addWidget(self.admin_live_viewer_block_bnt)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_23)

        self.horizontalSpacer_63 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_63)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalSpacer_48 = QSpacerItem(267, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_48)

        self.admin_fn_save_bnt = QPushButton(self.page_2)
        self.admin_fn_save_bnt.setObjectName(u"admin_fn_save_bnt")
        sizePolicy1.setHeightForWidth(self.admin_fn_save_bnt.sizePolicy().hasHeightForWidth())
        self.admin_fn_save_bnt.setSizePolicy(sizePolicy1)
        self.admin_fn_save_bnt.setMinimumSize(QSize(71, 41))
        self.admin_fn_save_bnt.setMaximumSize(QSize(71, 41))
        font8 = QFont()
        font8.setPointSize(10)
        self.admin_fn_save_bnt.setFont(font8)
        self.admin_fn_save_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.admin_fn_save_bnt.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.0 rgba(112, 210, 112, 255),\n"
"    stop:0.3 rgba(0, 196, 0, 255)\n"
");\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"\n"
"")

        self.horizontalLayout_55.addWidget(self.admin_fn_save_bnt)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_49)


        self.verticalLayout_2.addLayout(self.horizontalLayout_55)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 441, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_4 = QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_15 = QWidget(self.page_3)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_54 = QVBoxLayout(self.widget_15)
        self.verticalLayout_54.setSpacing(7)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalSpacer_53 = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_53)

        self.user_setting_label = QLabel(self.widget_15)
        self.user_setting_label.setObjectName(u"user_setting_label")
        sizePolicy4.setHeightForWidth(self.user_setting_label.sizePolicy().hasHeightForWidth())
        self.user_setting_label.setSizePolicy(sizePolicy4)
        self.user_setting_label.setMinimumSize(QSize(135, 22))
        self.user_setting_label.setMaximumSize(QSize(179, 22))
        self.user_setting_label.setFont(font3)
        self.user_setting_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.user_setting_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_85.addWidget(self.user_setting_label)

        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_54)


        self.verticalLayout_54.addLayout(self.horizontalLayout_85)

        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setSpacing(6)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalSpacer_55 = QSpacerItem(36, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_86.addItem(self.horizontalSpacer_55)

        self.horizontalLayout_87 = QHBoxLayout()
        self.horizontalLayout_87.setSpacing(5)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.setting_user_id_label = QLabel(self.widget_15)
        self.setting_user_id_label.setObjectName(u"setting_user_id_label")
        sizePolicy4.setHeightForWidth(self.setting_user_id_label.sizePolicy().hasHeightForWidth())
        self.setting_user_id_label.setSizePolicy(sizePolicy4)
        self.setting_user_id_label.setMinimumSize(QSize(104, 22))
        self.setting_user_id_label.setMaximumSize(QSize(104, 22))
        self.setting_user_id_label.setFont(font2)
        self.setting_user_id_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_user_id_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_87.addWidget(self.setting_user_id_label)

        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.setting_user_id_input = QLineEdit(self.widget_15)
        self.setting_user_id_input.setObjectName(u"setting_user_id_input")
        sizePolicy.setHeightForWidth(self.setting_user_id_input.sizePolicy().hasHeightForWidth())
        self.setting_user_id_input.setSizePolicy(sizePolicy)
        self.setting_user_id_input.setMinimumSize(QSize(246, 19))
        self.setting_user_id_input.setMaximumSize(QSize(9999, 19))
        self.setting_user_id_input.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.setting_user_id_input.setReadOnly(True)

        self.verticalLayout_56.addWidget(self.setting_user_id_input)

        self.setting_user_id_input_line = QFrame(self.widget_15)
        self.setting_user_id_input_line.setObjectName(u"setting_user_id_input_line")
        sizePolicy.setHeightForWidth(self.setting_user_id_input_line.sizePolicy().hasHeightForWidth())
        self.setting_user_id_input_line.setSizePolicy(sizePolicy)
        self.setting_user_id_input_line.setMinimumSize(QSize(246, 3))
        self.setting_user_id_input_line.setMaximumSize(QSize(246, 3))
        self.setting_user_id_input_line.setFont(font6)
        self.setting_user_id_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setting_user_id_input_line.setAutoFillBackground(False)
        self.setting_user_id_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.setting_user_id_input_line.setFrameShape(QFrame.Shape.HLine)
        self.setting_user_id_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_56.addWidget(self.setting_user_id_input_line)


        self.horizontalLayout_87.addLayout(self.verticalLayout_56)


        self.horizontalLayout_86.addLayout(self.horizontalLayout_87)

        self.horizontalSpacer_125 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_86.addItem(self.horizontalSpacer_125)


        self.verticalLayout_54.addLayout(self.horizontalLayout_86)

        self.horizontalLayout_88 = QHBoxLayout()
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalSpacer_126 = QSpacerItem(36, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_88.addItem(self.horizontalSpacer_126)

        self.horizontalLayout_89 = QHBoxLayout()
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.setting_user_pw_label = QLabel(self.widget_15)
        self.setting_user_pw_label.setObjectName(u"setting_user_pw_label")
        sizePolicy4.setHeightForWidth(self.setting_user_pw_label.sizePolicy().hasHeightForWidth())
        self.setting_user_pw_label.setSizePolicy(sizePolicy4)
        self.setting_user_pw_label.setMinimumSize(QSize(104, 22))
        self.setting_user_pw_label.setMaximumSize(QSize(104, 22))
        self.setting_user_pw_label.setFont(font2)
        self.setting_user_pw_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_user_pw_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_89.addWidget(self.setting_user_pw_label)

        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.setting_user_pw_input = QLineEdit(self.widget_15)
        self.setting_user_pw_input.setObjectName(u"setting_user_pw_input")
        sizePolicy.setHeightForWidth(self.setting_user_pw_input.sizePolicy().hasHeightForWidth())
        self.setting_user_pw_input.setSizePolicy(sizePolicy)
        self.setting_user_pw_input.setMinimumSize(QSize(246, 19))
        self.setting_user_pw_input.setMaximumSize(QSize(9999, 19))
        self.setting_user_pw_input.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.setting_user_pw_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_57.addWidget(self.setting_user_pw_input)

        self.setting_user_pw_input_line = QFrame(self.widget_15)
        self.setting_user_pw_input_line.setObjectName(u"setting_user_pw_input_line")
        sizePolicy.setHeightForWidth(self.setting_user_pw_input_line.sizePolicy().hasHeightForWidth())
        self.setting_user_pw_input_line.setSizePolicy(sizePolicy)
        self.setting_user_pw_input_line.setMinimumSize(QSize(246, 3))
        self.setting_user_pw_input_line.setMaximumSize(QSize(246, 3))
        self.setting_user_pw_input_line.setFont(font6)
        self.setting_user_pw_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setting_user_pw_input_line.setAutoFillBackground(False)
        self.setting_user_pw_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.setting_user_pw_input_line.setFrameShape(QFrame.Shape.HLine)
        self.setting_user_pw_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_57.addWidget(self.setting_user_pw_input_line)


        self.horizontalLayout_89.addLayout(self.verticalLayout_57)


        self.horizontalLayout_88.addLayout(self.horizontalLayout_89)

        self.horizontalSpacer_127 = QSpacerItem(40, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_88.addItem(self.horizontalSpacer_127)


        self.verticalLayout_54.addLayout(self.horizontalLayout_88)

        self.horizontalLayout_90 = QHBoxLayout()
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalSpacer_128 = QSpacerItem(36, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_90.addItem(self.horizontalSpacer_128)

        self.horizontalLayout_91 = QHBoxLayout()
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.setting_user_new_pw_label = QLabel(self.widget_15)
        self.setting_user_new_pw_label.setObjectName(u"setting_user_new_pw_label")
        sizePolicy4.setHeightForWidth(self.setting_user_new_pw_label.sizePolicy().hasHeightForWidth())
        self.setting_user_new_pw_label.setSizePolicy(sizePolicy4)
        self.setting_user_new_pw_label.setMinimumSize(QSize(104, 22))
        self.setting_user_new_pw_label.setMaximumSize(QSize(104, 22))
        self.setting_user_new_pw_label.setFont(font2)
        self.setting_user_new_pw_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_user_new_pw_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_91.addWidget(self.setting_user_new_pw_label)

        self.verticalLayout_58 = QVBoxLayout()
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.setting_user_new_pw_input = QLineEdit(self.widget_15)
        self.setting_user_new_pw_input.setObjectName(u"setting_user_new_pw_input")
        sizePolicy.setHeightForWidth(self.setting_user_new_pw_input.sizePolicy().hasHeightForWidth())
        self.setting_user_new_pw_input.setSizePolicy(sizePolicy)
        self.setting_user_new_pw_input.setMinimumSize(QSize(246, 19))
        self.setting_user_new_pw_input.setMaximumSize(QSize(9999, 19))
        self.setting_user_new_pw_input.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.setting_user_new_pw_input.setFrame(True)
        self.setting_user_new_pw_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_58.addWidget(self.setting_user_new_pw_input)

        self.setting_user_new_pw_input_line = QFrame(self.widget_15)
        self.setting_user_new_pw_input_line.setObjectName(u"setting_user_new_pw_input_line")
        sizePolicy.setHeightForWidth(self.setting_user_new_pw_input_line.sizePolicy().hasHeightForWidth())
        self.setting_user_new_pw_input_line.setSizePolicy(sizePolicy)
        self.setting_user_new_pw_input_line.setMinimumSize(QSize(246, 3))
        self.setting_user_new_pw_input_line.setMaximumSize(QSize(246, 3))
        self.setting_user_new_pw_input_line.setFont(font6)
        self.setting_user_new_pw_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setting_user_new_pw_input_line.setAutoFillBackground(False)
        self.setting_user_new_pw_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.setting_user_new_pw_input_line.setFrameShape(QFrame.Shape.HLine)
        self.setting_user_new_pw_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_58.addWidget(self.setting_user_new_pw_input_line)


        self.horizontalLayout_91.addLayout(self.verticalLayout_58)


        self.horizontalLayout_90.addLayout(self.horizontalLayout_91)

        self.horizontalSpacer_129 = QSpacerItem(40, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_90.addItem(self.horizontalSpacer_129)


        self.verticalLayout_54.addLayout(self.horizontalLayout_90)

        self.horizontalLayout_92 = QHBoxLayout()
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalSpacer_130 = QSpacerItem(36, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_130)

        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.setting_user_new_pw_label2 = QLabel(self.widget_15)
        self.setting_user_new_pw_label2.setObjectName(u"setting_user_new_pw_label2")
        sizePolicy4.setHeightForWidth(self.setting_user_new_pw_label2.sizePolicy().hasHeightForWidth())
        self.setting_user_new_pw_label2.setSizePolicy(sizePolicy4)
        self.setting_user_new_pw_label2.setMinimumSize(QSize(104, 27))
        self.setting_user_new_pw_label2.setMaximumSize(QSize(104, 27))
        self.setting_user_new_pw_label2.setFont(font2)
        self.setting_user_new_pw_label2.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_user_new_pw_label2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_93.addWidget(self.setting_user_new_pw_label2)

        self.verticalLayout_59 = QVBoxLayout()
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.setting_user_new_pw_input2 = QLineEdit(self.widget_15)
        self.setting_user_new_pw_input2.setObjectName(u"setting_user_new_pw_input2")
        sizePolicy.setHeightForWidth(self.setting_user_new_pw_input2.sizePolicy().hasHeightForWidth())
        self.setting_user_new_pw_input2.setSizePolicy(sizePolicy)
        self.setting_user_new_pw_input2.setMinimumSize(QSize(246, 19))
        self.setting_user_new_pw_input2.setMaximumSize(QSize(9999, 19))
        self.setting_user_new_pw_input2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.setting_user_new_pw_input2.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_59.addWidget(self.setting_user_new_pw_input2)

        self.setting_user_new_pw_input2_line = QFrame(self.widget_15)
        self.setting_user_new_pw_input2_line.setObjectName(u"setting_user_new_pw_input2_line")
        sizePolicy.setHeightForWidth(self.setting_user_new_pw_input2_line.sizePolicy().hasHeightForWidth())
        self.setting_user_new_pw_input2_line.setSizePolicy(sizePolicy)
        self.setting_user_new_pw_input2_line.setMinimumSize(QSize(246, 3))
        self.setting_user_new_pw_input2_line.setMaximumSize(QSize(246, 3))
        self.setting_user_new_pw_input2_line.setFont(font6)
        self.setting_user_new_pw_input2_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setting_user_new_pw_input2_line.setAutoFillBackground(False)
        self.setting_user_new_pw_input2_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.setting_user_new_pw_input2_line.setFrameShape(QFrame.Shape.HLine)
        self.setting_user_new_pw_input2_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_59.addWidget(self.setting_user_new_pw_input2_line)


        self.horizontalLayout_93.addLayout(self.verticalLayout_59)


        self.horizontalLayout_92.addLayout(self.horizontalLayout_93)

        self.horizontalSpacer_131 = QSpacerItem(40, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_131)


        self.verticalLayout_54.addLayout(self.horizontalLayout_92)

        self.horizontalLayout_94 = QHBoxLayout()
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalSpacer_57 = QSpacerItem(338, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_94.addItem(self.horizontalSpacer_57)

        self.setting_user_save_bnt = QPushButton(self.widget_15)
        self.setting_user_save_bnt.setObjectName(u"setting_user_save_bnt")
        self.setting_user_save_bnt.setMinimumSize(QSize(71, 41))
        self.setting_user_save_bnt.setMaximumSize(QSize(71, 41))
        self.setting_user_save_bnt.setFont(font5)
        self.setting_user_save_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setting_user_save_bnt.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.0 rgba(112, 210, 112, 255),\n"
"    stop:0.3 rgba(0, 196, 0, 255)\n"
");\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 19px;\n"
"\n"
"")

        self.horizontalLayout_94.addWidget(self.setting_user_save_bnt)

        self.horizontalSpacer_132 = QSpacerItem(40, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_94.addItem(self.horizontalSpacer_132)


        self.verticalLayout_54.addLayout(self.horizontalLayout_94)


        self.verticalLayout_4.addWidget(self.widget_15)

        self.verticalSpacer_4 = QSpacerItem(20, 337, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.retranslateUi(server_setting_window)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(server_setting_window)
    # setupUi

    def retranslateUi(self, server_setting_window):
        server_setting_window.setWindowTitle(QCoreApplication.translate("server_setting_window", u"Server Setting", None))
        self.top_logo_2.setText("")
        self.shutdown_bnt.setText(QCoreApplication.translate("server_setting_window", u"\ub2eb\uae30", None))
        self.alarm_memu_bnt.setText(QCoreApplication.translate("server_setting_window", u"\uc54c\ub9bc \uc124\uc815", None))
        self.user_setting_bnt.setText(QCoreApplication.translate("server_setting_window", u"\uc0ac\uc6a9\uc790 \uc815\ubcf4 \uc124\uc815", None))
        self.admin_setting_but.setText(QCoreApplication.translate("server_setting_window", u"\uad00\ub9ac\uc790 \uc124\uc815", None))
        self.setting_event_pop_up_label.setText(QCoreApplication.translate("server_setting_window", u"\uc774\ubca4\ud2b8 \uc54c\ub9bc \ud31d\uc5c5 \uc124\uc815", None))
        self.setting_event_pop_up_active_label.setText(QCoreApplication.translate("server_setting_window", u"\uc54c\ub9bc \ud31d\uc5c5 \ud65c\uc131\ud654", None))
        self.setting_event_pop_up_active_bnt.setText("")
        self.setting_event_pop_up_duration_bnt.setText(QCoreApplication.translate("server_setting_window", u"\uc54c\ub9bc \uc9c0\uc18d \uc2dc\uac04", None))
        self.setting_event_pop_up_duration_box.setItemText(0, QCoreApplication.translate("server_setting_window", u"3\ucd08", None))
        self.setting_event_pop_up_duration_box.setItemText(1, QCoreApplication.translate("server_setting_window", u"5\ucd08", None))
        self.setting_event_pop_up_duration_box.setItemText(2, QCoreApplication.translate("server_setting_window", u"10\ucd08", None))
        self.setting_event_pop_up_duration_box.setItemText(3, QCoreApplication.translate("server_setting_window", u"60\ucd08", None))
        self.setting_event_pop_up_duration_box.setItemText(4, QCoreApplication.translate("server_setting_window", u"\uc5c6\uc74c", None))

        self.setting_event_pop_up_save_bnt.setText(QCoreApplication.translate("server_setting_window", u"\uc800\uc7a5", None))
        self.setting_notice_label.setText(QCoreApplication.translate("server_setting_window", u"\uc54c\ub9bc \uc804\ub2ec \uc5f0\ub77d\ucc98 \uc124\uc815", None))
        self.setting_notice_phone_active_bnt.setText("")
#if QT_CONFIG(whatsthis)
        self.setting_notice_phone_num_input.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.setting_notice_phone_num_input.setInputMask("")
        self.setting_notice_phone_num_input.setText("")
        self.setting_notice_phone_num_input.setPlaceholderText(QCoreApplication.translate("server_setting_window", u"010-xxxx-xxxx", None))
        self.setting_notice_phone_add_bnt.setText("")
        self.setting_notice_phone_del_bnt.setText("")
        ___qtablewidgetitem = self.setting_notice_phone_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("server_setting_window", u"\uc54c\ub78c \uc804\uc1a1 \uc804\ud654\ubc88\ud638 \ub9ac\uc2a4\ud2b8", None));
        self.setting_notice_label_2.setText(QCoreApplication.translate("server_setting_window", u"\uc54c\ub9bc \uc885\ub958 \uc120\ud0dd", None))
        self.setting_notion_detect_type_bnt1.setText(QCoreApplication.translate("server_setting_window", u"\uce68\uc785", None))
        self.setting_notion_detect_type_bnt2.setText(QCoreApplication.translate("server_setting_window", u"\uce68\uc785", None))
        self.setting_notion_detect_type_bnt3.setText(QCoreApplication.translate("server_setting_window", u"\uce68\uc785", None))
        self.setting_notion_detect_type_bnt4.setText(QCoreApplication.translate("server_setting_window", u"\uce68\uc785", None))
        self.setting_notice_phone_save_bnt.setText(QCoreApplication.translate("server_setting_window", u"\uc800\uc7a5", None))
        self.admin_sms_alarm_fn_active_label.setText(QCoreApplication.translate("server_setting_window", u"SMS \uc54c\ub9bc \uc804\uc1a1 \uae30\ub2a5 \ud65c\uc131\ud654", None))
        self.admin_sms_alarm_fn_active_bnt.setText("")
        self.admin_sms_alarm_allow_phone_num_label.setText(QCoreApplication.translate("server_setting_window", u"\uc804\ud654\ubc88\ud638 \ub4f1\ub85d \ud5c8\uc6a9 \uc218", None))
        self.admin_sms_alarm_allow_phone_num_input.setText("")
        self.admin_live_viewer_block_label.setText(QCoreApplication.translate("server_setting_window", u"\ub77c\uc774\ube0c \ud654\uba74 \ucc28\ub2e8 \ud65c\uc131\ud654", None))
        self.admin_live_viewer_block_bnt.setText("")
        self.admin_fn_save_bnt.setText(QCoreApplication.translate("server_setting_window", u"\uc800\uc7a5", None))
        self.user_setting_label.setText(QCoreApplication.translate("server_setting_window", u"\uc0ac\uc6a9\uc790 \ub85c\uadf8\uc778 \ubcc0\uacbd", None))
        self.setting_user_id_label.setText(QCoreApplication.translate("server_setting_window", u"\ud604\uc7ac \uc544\uc774\ub514", None))
        self.setting_user_id_input.setText("")
        self.setting_user_pw_label.setText(QCoreApplication.translate("server_setting_window", u"\uae30\uc874 \ube44\ubc00\ubc88\ud638", None))
        self.setting_user_pw_input.setText("")
        self.setting_user_new_pw_label.setText(QCoreApplication.translate("server_setting_window", u"\uc2e0\uaddc \ube44\ubc00\ubc88\ud638", None))
        self.setting_user_new_pw_input.setText("")
        self.setting_user_new_pw_label2.setText(QCoreApplication.translate("server_setting_window", u"\ube44\ubc00\ubc88\ud638 \ud655\uc778", None))
        self.setting_user_new_pw_input2.setText("")
        self.setting_user_save_bnt.setText(QCoreApplication.translate("server_setting_window", u"\ubcc0\uacbd", None))
    # retranslateUi


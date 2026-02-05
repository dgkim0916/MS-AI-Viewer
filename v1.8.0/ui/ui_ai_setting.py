# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ai_settingRqkDUn.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import resourece_rc

class Ui_Ai_Setting_Window(object):
    def setupUi(self, Ai_Setting_Window):
        if not Ai_Setting_Window.objectName():
            Ai_Setting_Window.setObjectName(u"Ai_Setting_Window")
        Ai_Setting_Window.setWindowModality(Qt.WindowModality.ApplicationModal)
        Ai_Setting_Window.resize(1043, 653)
        Ai_Setting_Window.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        Ai_Setting_Window.setWindowTitle(u"\uc9c0\ub2a5\ud615 \ubd84\uc11d \uc124\uc815")
        icon = QIcon()
        icon.addFile(u":/newPrefix/images/icon2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Ai_Setting_Window.setWindowIcon(icon)
        Ai_Setting_Window.setStyleSheet(u"background-color: rgb(3, 3, 13);")
        self.verticalLayout = QVBoxLayout(Ai_Setting_Window)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Ai_Setting_Window)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ai_setting_info_label = QLabel(self.widget)
        self.ai_setting_info_label.setObjectName(u"ai_setting_info_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ai_setting_info_label.sizePolicy().hasHeightForWidth())
        self.ai_setting_info_label.setSizePolicy(sizePolicy)
        self.ai_setting_info_label.setMaximumSize(QSize(9999, 37))
        font = QFont()
        font.setFamilies([u"NanumBarunGothic"])
        font.setPointSize(14)
        font.setBold(False)
        self.ai_setting_info_label.setFont(font)
        self.ai_setting_info_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ai_setting_info_label.setIndent(0)
        self.ai_setting_info_label.setOpenExternalLinks(False)

        self.horizontalLayout.addWidget(self.ai_setting_info_label)

        self.all_select_bnt = QPushButton(self.widget)
        self.all_select_bnt.setObjectName(u"all_select_bnt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.all_select_bnt.sizePolicy().hasHeightForWidth())
        self.all_select_bnt.setSizePolicy(sizePolicy1)
        self.all_select_bnt.setMinimumSize(QSize(70, 25))
        self.all_select_bnt.setMaximumSize(QSize(70, 16777215))
        font1 = QFont()
        font1.setFamilies([u"NanumBarunGothic"])
        font1.setPointSize(10)
        self.all_select_bnt.setFont(font1)
        self.all_select_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.all_select_bnt.setStyleSheet(u"background-color: rgb(36, 39, 44);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.all_select_bnt)

        self.all_release_bnt = QPushButton(self.widget)
        self.all_release_bnt.setObjectName(u"all_release_bnt")
        sizePolicy1.setHeightForWidth(self.all_release_bnt.sizePolicy().hasHeightForWidth())
        self.all_release_bnt.setSizePolicy(sizePolicy1)
        self.all_release_bnt.setMinimumSize(QSize(70, 25))
        self.all_release_bnt.setMaximumSize(QSize(70, 16777215))
        self.all_release_bnt.setFont(font1)
        self.all_release_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.all_release_bnt.setStyleSheet(u"background-color: rgb(36, 39, 44);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.all_release_bnt)

        self.horizontalSpacer = QSpacerItem(601, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.camera_save_bnt = QPushButton(self.widget)
        self.camera_save_bnt.setObjectName(u"camera_save_bnt")
        sizePolicy1.setHeightForWidth(self.camera_save_bnt.sizePolicy().hasHeightForWidth())
        self.camera_save_bnt.setSizePolicy(sizePolicy1)
        self.camera_save_bnt.setMinimumSize(QSize(61, 31))
        self.camera_save_bnt.setMaximumSize(QSize(61, 31))
        font2 = QFont()
        font2.setFamilies([u"Sans Serif"])
        font2.setPointSize(10)
        self.camera_save_bnt.setFont(font2)
        self.camera_save_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.camera_save_bnt.setStyleSheet(u"background-color: rgb(30, 195, 55);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.camera_save_bnt)

        self.close_bnt = QPushButton(self.widget)
        self.close_bnt.setObjectName(u"close_bnt")
        self.close_bnt.setMinimumSize(QSize(61, 31))
        self.close_bnt.setMaximumSize(QSize(61, 31))
        self.close_bnt.setFont(font2)
        self.close_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_bnt.setStyleSheet(u"background-color: rgb(237, 51, 59);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.close_bnt)


        self.verticalLayout.addWidget(self.widget)

        self.widget_4 = QWidget(Ai_Setting_Window)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.widget_4)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy2)
        self.widget_11.setMinimumSize(QSize(60, 0))
        self.widget_11.setMaximumSize(QSize(60, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.widget_11)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)

        self.ai_setting_camera_undo_page_bnt = QPushButton(self.widget_11)
        self.ai_setting_camera_undo_page_bnt.setObjectName(u"ai_setting_camera_undo_page_bnt")
        self.ai_setting_camera_undo_page_bnt.setMinimumSize(QSize(60, 41))
        self.ai_setting_camera_undo_page_bnt.setMaximumSize(QSize(60, 41))
        font3 = QFont()
        font3.setPointSize(10)
        self.ai_setting_camera_undo_page_bnt.setFont(font3)
        self.ai_setting_camera_undo_page_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ai_setting_camera_undo_page_bnt.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ai_setting_camera_undo_page_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"Rotation: ( origin.x: 25; origin.y: 25; angle: 45);")
        icon1 = QIcon()
        icon1.addFile(u":/ui/ui/images/ico_arrow_left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ai_setting_camera_undo_page_bnt.setIcon(icon1)
        self.ai_setting_camera_undo_page_bnt.setIconSize(QSize(31, 50))

        self.verticalLayout_7.addWidget(self.ai_setting_camera_undo_page_bnt)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_7.addItem(self.verticalSpacer_10)


        self.horizontalLayout_5.addWidget(self.widget_11)

        self.stackedWidget_5 = QStackedWidget(self.widget_4)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.horizontalLayout_10 = QHBoxLayout(self.page_11)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.page_11)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_4 = QGridLayout(self.widget_12)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.search_camera_view_layout_65 = QVBoxLayout()
        self.search_camera_view_layout_65.setSpacing(0)
        self.search_camera_view_layout_65.setObjectName(u"search_camera_view_layout_65")
        self.camera_view_name_17 = QLabel(self.widget_12)
        self.camera_view_name_17.setObjectName(u"camera_view_name_17")
        sizePolicy.setHeightForWidth(self.camera_view_name_17.sizePolicy().hasHeightForWidth())
        self.camera_view_name_17.setSizePolicy(sizePolicy)
        self.camera_view_name_17.setMaximumSize(QSize(722, 20))
        font4 = QFont()
        font4.setFamilies([u"NanumSquareRound"])
        font4.setPointSize(11)
        font4.setBold(False)
        self.camera_view_name_17.setFont(font4)
        self.camera_view_name_17.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_17.setMargin(0)
        self.camera_view_name_17.setIndent(15)

        self.search_camera_view_layout_65.addWidget(self.camera_view_name_17)

        self.camera_view_17 = QLabel(self.widget_12)
        self.camera_view_17.setObjectName(u"camera_view_17")
        sizePolicy1.setHeightForWidth(self.camera_view_17.sizePolicy().hasHeightForWidth())
        self.camera_view_17.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setFamilies([u"NanumBarunGothic"])
        font5.setPointSize(16)
        self.camera_view_17.setFont(font5)
        self.camera_view_17.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_17.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_17.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_17.setScaledContents(False)
        self.camera_view_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_65.addWidget(self.camera_view_17)


        self.gridLayout_4.addLayout(self.search_camera_view_layout_65, 4, 1, 1, 1)

        self.search_camera_view_layout_66 = QVBoxLayout()
        self.search_camera_view_layout_66.setSpacing(0)
        self.search_camera_view_layout_66.setObjectName(u"search_camera_view_layout_66")
        self.camera_view_name_18 = QLabel(self.widget_12)
        self.camera_view_name_18.setObjectName(u"camera_view_name_18")
        sizePolicy.setHeightForWidth(self.camera_view_name_18.sizePolicy().hasHeightForWidth())
        self.camera_view_name_18.setSizePolicy(sizePolicy)
        self.camera_view_name_18.setMaximumSize(QSize(722, 20))
        self.camera_view_name_18.setFont(font4)
        self.camera_view_name_18.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_18.setMargin(0)
        self.camera_view_name_18.setIndent(15)

        self.search_camera_view_layout_66.addWidget(self.camera_view_name_18)

        self.camera_view_18 = QLabel(self.widget_12)
        self.camera_view_18.setObjectName(u"camera_view_18")
        sizePolicy1.setHeightForWidth(self.camera_view_18.sizePolicy().hasHeightForWidth())
        self.camera_view_18.setSizePolicy(sizePolicy1)
        self.camera_view_18.setFont(font5)
        self.camera_view_18.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_18.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_18.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_18.setScaledContents(False)
        self.camera_view_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_66.addWidget(self.camera_view_18)


        self.gridLayout_4.addLayout(self.search_camera_view_layout_66, 4, 0, 1, 1)

        self.search_camera_view_layout_67 = QVBoxLayout()
        self.search_camera_view_layout_67.setSpacing(0)
        self.search_camera_view_layout_67.setObjectName(u"search_camera_view_layout_67")
        self.camera_view_name_19 = QLabel(self.widget_12)
        self.camera_view_name_19.setObjectName(u"camera_view_name_19")
        sizePolicy.setHeightForWidth(self.camera_view_name_19.sizePolicy().hasHeightForWidth())
        self.camera_view_name_19.setSizePolicy(sizePolicy)
        self.camera_view_name_19.setMaximumSize(QSize(722, 20))
        self.camera_view_name_19.setFont(font4)
        self.camera_view_name_19.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_19.setMargin(0)
        self.camera_view_name_19.setIndent(15)

        self.search_camera_view_layout_67.addWidget(self.camera_view_name_19)

        self.camera_view_19 = QLabel(self.widget_12)
        self.camera_view_19.setObjectName(u"camera_view_19")
        sizePolicy1.setHeightForWidth(self.camera_view_19.sizePolicy().hasHeightForWidth())
        self.camera_view_19.setSizePolicy(sizePolicy1)
        self.camera_view_19.setFont(font5)
        self.camera_view_19.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_19.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_19.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_19.setScaledContents(False)
        self.camera_view_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_67.addWidget(self.camera_view_19)


        self.gridLayout_4.addLayout(self.search_camera_view_layout_67, 1, 0, 1, 1)

        self.search_camera_view_layout_68 = QVBoxLayout()
        self.search_camera_view_layout_68.setSpacing(0)
        self.search_camera_view_layout_68.setObjectName(u"search_camera_view_layout_68")
        self.camera_view_name_20 = QLabel(self.widget_12)
        self.camera_view_name_20.setObjectName(u"camera_view_name_20")
        sizePolicy.setHeightForWidth(self.camera_view_name_20.sizePolicy().hasHeightForWidth())
        self.camera_view_name_20.setSizePolicy(sizePolicy)
        self.camera_view_name_20.setMaximumSize(QSize(722, 20))
        self.camera_view_name_20.setFont(font4)
        self.camera_view_name_20.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_20.setMargin(0)
        self.camera_view_name_20.setIndent(15)

        self.search_camera_view_layout_68.addWidget(self.camera_view_name_20)

        self.camera_view_20 = QLabel(self.widget_12)
        self.camera_view_20.setObjectName(u"camera_view_20")
        sizePolicy1.setHeightForWidth(self.camera_view_20.sizePolicy().hasHeightForWidth())
        self.camera_view_20.setSizePolicy(sizePolicy1)
        self.camera_view_20.setFont(font5)
        self.camera_view_20.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_20.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_20.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_20.setScaledContents(False)
        self.camera_view_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_68.addWidget(self.camera_view_20)


        self.gridLayout_4.addLayout(self.search_camera_view_layout_68, 2, 2, 1, 1)

        self.search_camera_view_layout_69 = QVBoxLayout()
        self.search_camera_view_layout_69.setSpacing(0)
        self.search_camera_view_layout_69.setObjectName(u"search_camera_view_layout_69")
        self.camera_view_name_21 = QLabel(self.widget_12)
        self.camera_view_name_21.setObjectName(u"camera_view_name_21")
        sizePolicy.setHeightForWidth(self.camera_view_name_21.sizePolicy().hasHeightForWidth())
        self.camera_view_name_21.setSizePolicy(sizePolicy)
        self.camera_view_name_21.setMaximumSize(QSize(722, 20))
        self.camera_view_name_21.setFont(font4)
        self.camera_view_name_21.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_21.setMargin(0)
        self.camera_view_name_21.setIndent(15)

        self.search_camera_view_layout_69.addWidget(self.camera_view_name_21)

        self.camera_view_21 = QLabel(self.widget_12)
        self.camera_view_21.setObjectName(u"camera_view_21")
        sizePolicy1.setHeightForWidth(self.camera_view_21.sizePolicy().hasHeightForWidth())
        self.camera_view_21.setSizePolicy(sizePolicy1)
        self.camera_view_21.setFont(font5)
        self.camera_view_21.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_21.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_21.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_21.setScaledContents(False)
        self.camera_view_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_69.addWidget(self.camera_view_21)


        self.gridLayout_4.addLayout(self.search_camera_view_layout_69, 1, 3, 1, 1)

        self.search_camera_view_layout_70 = QVBoxLayout()
        self.search_camera_view_layout_70.setSpacing(0)
        self.search_camera_view_layout_70.setObjectName(u"search_camera_view_layout_70")
        self.camera_view_name_22 = QLabel(self.widget_12)
        self.camera_view_name_22.setObjectName(u"camera_view_name_22")
        sizePolicy.setHeightForWidth(self.camera_view_name_22.sizePolicy().hasHeightForWidth())
        self.camera_view_name_22.setSizePolicy(sizePolicy)
        self.camera_view_name_22.setMaximumSize(QSize(722, 20))
        self.camera_view_name_22.setFont(font4)
        self.camera_view_name_22.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_22.setMargin(0)
        self.camera_view_name_22.setIndent(15)

        self.search_camera_view_layout_70.addWidget(self.camera_view_name_22)

        self.camera_view_22 = QLabel(self.widget_12)
        self.camera_view_22.setObjectName(u"camera_view_22")
        sizePolicy1.setHeightForWidth(self.camera_view_22.sizePolicy().hasHeightForWidth())
        self.camera_view_22.setSizePolicy(sizePolicy1)
        self.camera_view_22.setFont(font5)
        self.camera_view_22.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_22.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_22.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_22.setScaledContents(False)
        self.camera_view_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_70.addWidget(self.camera_view_22)


        self.gridLayout_4.addLayout(self.search_camera_view_layout_70, 4, 2, 1, 1)

        self.search_camera_view_layout_71 = QVBoxLayout()
        self.search_camera_view_layout_71.setSpacing(0)
        self.search_camera_view_layout_71.setObjectName(u"search_camera_view_layout_71")
        self.camera_view_name_23 = QLabel(self.widget_12)
        self.camera_view_name_23.setObjectName(u"camera_view_name_23")
        sizePolicy.setHeightForWidth(self.camera_view_name_23.sizePolicy().hasHeightForWidth())
        self.camera_view_name_23.setSizePolicy(sizePolicy)
        self.camera_view_name_23.setMaximumSize(QSize(722, 20))
        self.camera_view_name_23.setFont(font4)
        self.camera_view_name_23.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_23.setMargin(0)
        self.camera_view_name_23.setIndent(15)

        self.search_camera_view_layout_71.addWidget(self.camera_view_name_23)

        self.camera_view_23 = QLabel(self.widget_12)
        self.camera_view_23.setObjectName(u"camera_view_23")
        sizePolicy1.setHeightForWidth(self.camera_view_23.sizePolicy().hasHeightForWidth())
        self.camera_view_23.setSizePolicy(sizePolicy1)
        self.camera_view_23.setFont(font5)
        self.camera_view_23.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_23.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_23.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_23.setScaledContents(False)
        self.camera_view_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_71.addWidget(self.camera_view_23)


        self.gridLayout_4.addLayout(self.search_camera_view_layout_71, 3, 0, 1, 1)

        self.search_camera_view_layout_72 = QVBoxLayout()
        self.search_camera_view_layout_72.setSpacing(0)
        self.search_camera_view_layout_72.setObjectName(u"search_camera_view_layout_72")
        self.camera_view_name_24 = QLabel(self.widget_12)
        self.camera_view_name_24.setObjectName(u"camera_view_name_24")
        sizePolicy.setHeightForWidth(self.camera_view_name_24.sizePolicy().hasHeightForWidth())
        self.camera_view_name_24.setSizePolicy(sizePolicy)
        self.camera_view_name_24.setMaximumSize(QSize(722, 20))
        self.camera_view_name_24.setFont(font4)
        self.camera_view_name_24.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_24.setMargin(0)
        self.camera_view_name_24.setIndent(15)

        self.search_camera_view_layout_72.addWidget(self.camera_view_name_24)

        self.camera_view_24 = QLabel(self.widget_12)
        self.camera_view_24.setObjectName(u"camera_view_24")
        sizePolicy1.setHeightForWidth(self.camera_view_24.sizePolicy().hasHeightForWidth())
        self.camera_view_24.setSizePolicy(sizePolicy1)
        self.camera_view_24.setFont(font5)
        self.camera_view_24.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_24.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_24.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_24.setScaledContents(False)
        self.camera_view_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_72.addWidget(self.camera_view_24)


        self.gridLayout_4.addLayout(self.search_camera_view_layout_72, 3, 2, 1, 1)

        self.search_camera_view_layout_73 = QVBoxLayout()
        self.search_camera_view_layout_73.setSpacing(0)
        self.search_camera_view_layout_73.setObjectName(u"search_camera_view_layout_73")
        self.camera_view_name_25 = QLabel(self.widget_12)
        self.camera_view_name_25.setObjectName(u"camera_view_name_25")
        sizePolicy.setHeightForWidth(self.camera_view_name_25.sizePolicy().hasHeightForWidth())
        self.camera_view_name_25.setSizePolicy(sizePolicy)
        self.camera_view_name_25.setMaximumSize(QSize(722, 20))
        self.camera_view_name_25.setFont(font4)
        self.camera_view_name_25.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_25.setMargin(0)
        self.camera_view_name_25.setIndent(15)

        self.search_camera_view_layout_73.addWidget(self.camera_view_name_25)

        self.camera_view_25 = QLabel(self.widget_12)
        self.camera_view_25.setObjectName(u"camera_view_25")
        sizePolicy1.setHeightForWidth(self.camera_view_25.sizePolicy().hasHeightForWidth())
        self.camera_view_25.setSizePolicy(sizePolicy1)
        self.camera_view_25.setFont(font5)
        self.camera_view_25.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_25.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_25.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_25.setScaledContents(False)
        self.camera_view_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_73.addWidget(self.camera_view_25)


        self.gridLayout_4.addLayout(self.search_camera_view_layout_73, 4, 3, 1, 1)

        self.search_camera_view_layout_74 = QVBoxLayout()
        self.search_camera_view_layout_74.setSpacing(0)
        self.search_camera_view_layout_74.setObjectName(u"search_camera_view_layout_74")
        self.camera_view_name_26 = QLabel(self.widget_12)
        self.camera_view_name_26.setObjectName(u"camera_view_name_26")
        sizePolicy.setHeightForWidth(self.camera_view_name_26.sizePolicy().hasHeightForWidth())
        self.camera_view_name_26.setSizePolicy(sizePolicy)
        self.camera_view_name_26.setMaximumSize(QSize(722, 20))
        self.camera_view_name_26.setFont(font4)
        self.camera_view_name_26.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_26.setMargin(0)
        self.camera_view_name_26.setIndent(15)

        self.search_camera_view_layout_74.addWidget(self.camera_view_name_26)

        self.camera_view_26 = QLabel(self.widget_12)
        self.camera_view_26.setObjectName(u"camera_view_26")
        sizePolicy1.setHeightForWidth(self.camera_view_26.sizePolicy().hasHeightForWidth())
        self.camera_view_26.setSizePolicy(sizePolicy1)
        self.camera_view_26.setFont(font5)
        self.camera_view_26.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_26.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_26.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_26.setScaledContents(False)
        self.camera_view_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_74.addWidget(self.camera_view_26)


        self.gridLayout_4.addLayout(self.search_camera_view_layout_74, 2, 3, 1, 1)

        self.search_camera_view_layout_75 = QVBoxLayout()
        self.search_camera_view_layout_75.setSpacing(0)
        self.search_camera_view_layout_75.setObjectName(u"search_camera_view_layout_75")
        self.camera_view_name_27 = QLabel(self.widget_12)
        self.camera_view_name_27.setObjectName(u"camera_view_name_27")
        sizePolicy.setHeightForWidth(self.camera_view_name_27.sizePolicy().hasHeightForWidth())
        self.camera_view_name_27.setSizePolicy(sizePolicy)
        self.camera_view_name_27.setMaximumSize(QSize(722, 20))
        self.camera_view_name_27.setFont(font4)
        self.camera_view_name_27.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_27.setMargin(0)
        self.camera_view_name_27.setIndent(15)

        self.search_camera_view_layout_75.addWidget(self.camera_view_name_27)

        self.camera_view_27 = QLabel(self.widget_12)
        self.camera_view_27.setObjectName(u"camera_view_27")
        sizePolicy1.setHeightForWidth(self.camera_view_27.sizePolicy().hasHeightForWidth())
        self.camera_view_27.setSizePolicy(sizePolicy1)
        self.camera_view_27.setFont(font5)
        self.camera_view_27.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_27.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_27.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_27.setScaledContents(False)
        self.camera_view_27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_75.addWidget(self.camera_view_27)


        self.gridLayout_4.addLayout(self.search_camera_view_layout_75, 3, 3, 1, 1)

        self.search_camera_view_layout_76 = QVBoxLayout()
        self.search_camera_view_layout_76.setSpacing(0)
        self.search_camera_view_layout_76.setObjectName(u"search_camera_view_layout_76")
        self.camera_view_name_28 = QLabel(self.widget_12)
        self.camera_view_name_28.setObjectName(u"camera_view_name_28")
        sizePolicy.setHeightForWidth(self.camera_view_name_28.sizePolicy().hasHeightForWidth())
        self.camera_view_name_28.setSizePolicy(sizePolicy)
        self.camera_view_name_28.setMaximumSize(QSize(722, 20))
        self.camera_view_name_28.setFont(font4)
        self.camera_view_name_28.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_28.setMargin(0)
        self.camera_view_name_28.setIndent(15)

        self.search_camera_view_layout_76.addWidget(self.camera_view_name_28)

        self.camera_view_28 = QLabel(self.widget_12)
        self.camera_view_28.setObjectName(u"camera_view_28")
        sizePolicy1.setHeightForWidth(self.camera_view_28.sizePolicy().hasHeightForWidth())
        self.camera_view_28.setSizePolicy(sizePolicy1)
        self.camera_view_28.setFont(font5)
        self.camera_view_28.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_28.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_28.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_28.setScaledContents(False)
        self.camera_view_28.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_76.addWidget(self.camera_view_28)


        self.gridLayout_4.addLayout(self.search_camera_view_layout_76, 1, 2, 1, 1)

        self.search_camera_view_layout_77 = QVBoxLayout()
        self.search_camera_view_layout_77.setSpacing(0)
        self.search_camera_view_layout_77.setObjectName(u"search_camera_view_layout_77")
        self.camera_view_name_29 = QLabel(self.widget_12)
        self.camera_view_name_29.setObjectName(u"camera_view_name_29")
        sizePolicy.setHeightForWidth(self.camera_view_name_29.sizePolicy().hasHeightForWidth())
        self.camera_view_name_29.setSizePolicy(sizePolicy)
        self.camera_view_name_29.setMaximumSize(QSize(722, 20))
        self.camera_view_name_29.setFont(font4)
        self.camera_view_name_29.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_29.setMargin(0)
        self.camera_view_name_29.setIndent(15)

        self.search_camera_view_layout_77.addWidget(self.camera_view_name_29)

        self.camera_view_29 = QLabel(self.widget_12)
        self.camera_view_29.setObjectName(u"camera_view_29")
        sizePolicy1.setHeightForWidth(self.camera_view_29.sizePolicy().hasHeightForWidth())
        self.camera_view_29.setSizePolicy(sizePolicy1)
        self.camera_view_29.setFont(font5)
        self.camera_view_29.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_29.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_29.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_29.setScaledContents(False)
        self.camera_view_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_77.addWidget(self.camera_view_29)


        self.gridLayout_4.addLayout(self.search_camera_view_layout_77, 2, 1, 1, 1)

        self.search_camera_view_layout_78 = QVBoxLayout()
        self.search_camera_view_layout_78.setSpacing(0)
        self.search_camera_view_layout_78.setObjectName(u"search_camera_view_layout_78")
        self.camera_view_name_30 = QLabel(self.widget_12)
        self.camera_view_name_30.setObjectName(u"camera_view_name_30")
        sizePolicy.setHeightForWidth(self.camera_view_name_30.sizePolicy().hasHeightForWidth())
        self.camera_view_name_30.setSizePolicy(sizePolicy)
        self.camera_view_name_30.setMaximumSize(QSize(722, 20))
        self.camera_view_name_30.setFont(font4)
        self.camera_view_name_30.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_30.setMargin(0)
        self.camera_view_name_30.setIndent(15)

        self.search_camera_view_layout_78.addWidget(self.camera_view_name_30)

        self.camera_view_30 = QLabel(self.widget_12)
        self.camera_view_30.setObjectName(u"camera_view_30")
        sizePolicy1.setHeightForWidth(self.camera_view_30.sizePolicy().hasHeightForWidth())
        self.camera_view_30.setSizePolicy(sizePolicy1)
        self.camera_view_30.setFont(font5)
        self.camera_view_30.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_30.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_30.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_30.setScaledContents(False)
        self.camera_view_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_78.addWidget(self.camera_view_30)


        self.gridLayout_4.addLayout(self.search_camera_view_layout_78, 3, 1, 1, 1)

        self.search_camera_view_layout_79 = QVBoxLayout()
        self.search_camera_view_layout_79.setSpacing(0)
        self.search_camera_view_layout_79.setObjectName(u"search_camera_view_layout_79")
        self.camera_view_name_31 = QLabel(self.widget_12)
        self.camera_view_name_31.setObjectName(u"camera_view_name_31")
        sizePolicy.setHeightForWidth(self.camera_view_name_31.sizePolicy().hasHeightForWidth())
        self.camera_view_name_31.setSizePolicy(sizePolicy)
        self.camera_view_name_31.setMaximumSize(QSize(722, 20))
        self.camera_view_name_31.setFont(font4)
        self.camera_view_name_31.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_31.setMargin(0)
        self.camera_view_name_31.setIndent(15)

        self.search_camera_view_layout_79.addWidget(self.camera_view_name_31)

        self.camera_view_31 = QLabel(self.widget_12)
        self.camera_view_31.setObjectName(u"camera_view_31")
        sizePolicy1.setHeightForWidth(self.camera_view_31.sizePolicy().hasHeightForWidth())
        self.camera_view_31.setSizePolicy(sizePolicy1)
        self.camera_view_31.setFont(font5)
        self.camera_view_31.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_31.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_31.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_31.setScaledContents(False)
        self.camera_view_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_79.addWidget(self.camera_view_31)


        self.gridLayout_4.addLayout(self.search_camera_view_layout_79, 2, 0, 1, 1)

        self.search_camera_view_layout_80 = QVBoxLayout()
        self.search_camera_view_layout_80.setSpacing(0)
        self.search_camera_view_layout_80.setObjectName(u"search_camera_view_layout_80")
        self.camera_view_name_32 = QLabel(self.widget_12)
        self.camera_view_name_32.setObjectName(u"camera_view_name_32")
        sizePolicy.setHeightForWidth(self.camera_view_name_32.sizePolicy().hasHeightForWidth())
        self.camera_view_name_32.setSizePolicy(sizePolicy)
        self.camera_view_name_32.setMaximumSize(QSize(722, 20))
        self.camera_view_name_32.setFont(font4)
        self.camera_view_name_32.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_32.setMargin(0)
        self.camera_view_name_32.setIndent(15)

        self.search_camera_view_layout_80.addWidget(self.camera_view_name_32)

        self.camera_view_32 = QLabel(self.widget_12)
        self.camera_view_32.setObjectName(u"camera_view_32")
        sizePolicy1.setHeightForWidth(self.camera_view_32.sizePolicy().hasHeightForWidth())
        self.camera_view_32.setSizePolicy(sizePolicy1)
        self.camera_view_32.setFont(font5)
        self.camera_view_32.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_32.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_32.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_32.setScaledContents(False)
        self.camera_view_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_80.addWidget(self.camera_view_32)


        self.gridLayout_4.addLayout(self.search_camera_view_layout_80, 1, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.widget_12)

        self.stackedWidget_5.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.verticalLayout_8 = QVBoxLayout(self.page_12)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.stackedWidget_5.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.stackedWidget_5.addWidget(self.page_13)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.stackedWidget_5.addWidget(self.page_14)

        self.horizontalLayout_5.addWidget(self.stackedWidget_5)

        self.widget_13 = QWidget(self.widget_4)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy2.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy2)
        self.widget_13.setMinimumSize(QSize(60, 0))
        self.widget_13.setMaximumSize(QSize(60, 16777215))
        self.verticalLayout_9 = QVBoxLayout(self.widget_13)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_9.addItem(self.verticalSpacer_11)

        self.ai_setting_camera_next_page_bnt = QPushButton(self.widget_13)
        self.ai_setting_camera_next_page_bnt.setObjectName(u"ai_setting_camera_next_page_bnt")
        self.ai_setting_camera_next_page_bnt.setMinimumSize(QSize(60, 41))
        self.ai_setting_camera_next_page_bnt.setMaximumSize(QSize(60, 41))
        self.ai_setting_camera_next_page_bnt.setFont(font3)
        self.ai_setting_camera_next_page_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ai_setting_camera_next_page_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/ui/ui/images/ico_arrow_right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ai_setting_camera_next_page_bnt.setIcon(icon2)
        self.ai_setting_camera_next_page_bnt.setIconSize(QSize(31, 50))

        self.verticalLayout_9.addWidget(self.ai_setting_camera_next_page_bnt)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_9.addItem(self.verticalSpacer_12)


        self.horizontalLayout_5.addWidget(self.widget_13)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_2 = QWidget(Ai_Setting_Window)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)

        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(Ai_Setting_Window)

        self.stackedWidget_5.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Ai_Setting_Window)
    # setupUi

    def retranslateUi(self, Ai_Setting_Window):
        self.ai_setting_info_label.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uc9c0\ub2a5\ud615 \ubd84\uc11d \uce74\uba54\ub77c \uc120\ud0dd", None))
        self.all_select_bnt.setText(QCoreApplication.translate("Ai_Setting_Window", u"\ubaa8\ub450 \uc120\ud0dd", None))
        self.all_release_bnt.setText(QCoreApplication.translate("Ai_Setting_Window", u"\ubaa8\ub450 \ud574\uc81c", None))
        self.camera_save_bnt.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uc801\uc6a9", None))
        self.close_bnt.setText(QCoreApplication.translate("Ai_Setting_Window", u"\ub2eb\uae30", None))
        self.ai_setting_camera_undo_page_bnt.setText("")
        self.camera_view_name_17.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c14", None))
        self.camera_view_17.setText("")
        self.camera_view_name_18.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c13", None))
        self.camera_view_18.setText("")
        self.camera_view_name_19.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c1", None))
        self.camera_view_19.setText("")
        self.camera_view_name_20.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c7", None))
        self.camera_view_20.setText("")
        self.camera_view_name_21.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c4", None))
        self.camera_view_21.setText("")
        self.camera_view_name_22.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c15", None))
        self.camera_view_22.setText("")
        self.camera_view_name_23.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c9", None))
        self.camera_view_23.setText("")
        self.camera_view_name_24.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c11", None))
        self.camera_view_24.setText("")
        self.camera_view_name_25.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c16", None))
        self.camera_view_25.setText("")
        self.camera_view_name_26.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c8", None))
        self.camera_view_26.setText("")
        self.camera_view_name_27.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c12", None))
        self.camera_view_27.setText("")
        self.camera_view_name_28.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c3", None))
        self.camera_view_28.setText("")
        self.camera_view_name_29.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c6", None))
        self.camera_view_29.setText("")
        self.camera_view_name_30.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c10", None))
        self.camera_view_30.setText("")
        self.camera_view_name_31.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c5", None))
        self.camera_view_31.setText("")
        self.camera_view_name_32.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c2", None))
        self.camera_view_32.setText("")
        self.ai_setting_camera_next_page_bnt.setText("")
        pass
    # retranslateUi


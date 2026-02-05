# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchrppzeT.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QComboBox,
    QDateEdit, QDateTimeEdit, QDoubleSpinBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resourece_rc
import resourece_rc

class Ui_Search_window(object):
    def setupUi(self, Search_window):
        if not Search_window.objectName():
            Search_window.setObjectName(u"Search_window")
        Search_window.setWindowModality(Qt.WindowModality.ApplicationModal)
        Search_window.resize(1336, 720)
        Search_window.setMinimumSize(QSize(1280, 720))
        Search_window.setMaximumSize(QSize(1600, 900))
        Search_window.setWindowTitle(u"Search")
        Search_window.setStyleSheet(u"background-color: rgb(3, 3, 13);")
        self.verticalLayout_37 = QVBoxLayout(Search_window)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, -1, 0, -1)
        self.top_logo_2 = QLabel(Search_window)
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

        self.horizontalLayout_20.addWidget(self.top_logo_2)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_13)

        self.close_bnt = QPushButton(Search_window)
        self.close_bnt.setObjectName(u"close_bnt")
        self.close_bnt.setMinimumSize(QSize(61, 31))
        self.close_bnt.setMaximumSize(QSize(61, 31))
        font1 = QFont()
        font1.setFamilies([u"Sans"])
        font1.setPointSize(10)
        self.close_bnt.setFont(font1)
        self.close_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_bnt.setStyleSheet(u"background-color: rgb(255, 49, 38);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")

        self.horizontalLayout_20.addWidget(self.close_bnt)


        self.verticalLayout_28.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.stackedWidget = QStackedWidget(Search_window)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.camera_select_page = QWidget()
        self.camera_select_page.setObjectName(u"camera_select_page")
        self.verticalLayout_26 = QVBoxLayout(self.camera_select_page)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_5 = QWidget(self.camera_select_page)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 35))
        self.verticalLayout_25 = QVBoxLayout(self.widget_5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(-1, 0, -1, 9)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.camera_select_label = QLabel(self.widget_5)
        self.camera_select_label.setObjectName(u"camera_select_label")
        font2 = QFont()
        font2.setFamilies([u"Sans"])
        font2.setPointSize(13)
        self.camera_select_label.setFont(font2)
        self.camera_select_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(191, 64, 64, 0);")
        self.camera_select_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_18.addWidget(self.camera_select_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_2)

        self.camera_select_all_bnt = QPushButton(self.widget_5)
        self.camera_select_all_bnt.setObjectName(u"camera_select_all_bnt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.camera_select_all_bnt.sizePolicy().hasHeightForWidth())
        self.camera_select_all_bnt.setSizePolicy(sizePolicy1)
        self.camera_select_all_bnt.setMinimumSize(QSize(79, 22))
        self.camera_select_all_bnt.setMaximumSize(QSize(120, 30))
        self.camera_select_all_bnt.setFont(font1)
        self.camera_select_all_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.camera_select_all_bnt.setStyleSheet(u"background-color: rgb(36, 39, 44);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"")

        self.horizontalLayout_18.addWidget(self.camera_select_all_bnt)


        self.verticalLayout_25.addLayout(self.horizontalLayout_18)


        self.verticalLayout_18.addWidget(self.widget_5)

        self.widget_4 = QWidget(self.camera_select_page)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy2)
        self.widget_8.setMaximumSize(QSize(39, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.search_camera_undo_page_bnt_2 = QPushButton(self.widget_8)
        self.search_camera_undo_page_bnt_2.setObjectName(u"search_camera_undo_page_bnt_2")
        self.search_camera_undo_page_bnt_2.setMaximumSize(QSize(34, 41))
        font3 = QFont()
        font3.setPointSize(10)
        self.search_camera_undo_page_bnt_2.setFont(font3)
        self.search_camera_undo_page_bnt_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.search_camera_undo_page_bnt_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.search_camera_undo_page_bnt_2.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"Rotation: ( origin.x: 25; origin.y: 25; angle: 45);")
        icon = QIcon()
        icon.addFile(u":/ui/ui/images/ico_arrow_left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_camera_undo_page_bnt_2.setIcon(icon)
        self.search_camera_undo_page_bnt_2.setIconSize(QSize(31, 50))

        self.verticalLayout_4.addWidget(self.search_camera_undo_page_bnt_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)


        self.horizontalLayout_3.addWidget(self.widget_8)

        self.stackedWidget_4 = QStackedWidget(self.widget_4)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.horizontalLayout_4 = QHBoxLayout(self.page_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_9 = QWidget(self.page_7)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_3 = QGridLayout(self.widget_9)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.search_camera_view_layout_49 = QVBoxLayout()
        self.search_camera_view_layout_49.setSpacing(0)
        self.search_camera_view_layout_49.setObjectName(u"search_camera_view_layout_49")
        self.camera_view_name_14 = QLabel(self.widget_9)
        self.camera_view_name_14.setObjectName(u"camera_view_name_14")
        sizePolicy.setHeightForWidth(self.camera_view_name_14.sizePolicy().hasHeightForWidth())
        self.camera_view_name_14.setSizePolicy(sizePolicy)
        self.camera_view_name_14.setMaximumSize(QSize(722, 20))
        font4 = QFont()
        font4.setFamilies([u"NanumSquareRound"])
        font4.setPointSize(11)
        font4.setBold(False)
        self.camera_view_name_14.setFont(font4)
        self.camera_view_name_14.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_14.setMargin(0)
        self.camera_view_name_14.setIndent(15)

        self.search_camera_view_layout_49.addWidget(self.camera_view_name_14)

        self.camera_view_14 = QLabel(self.widget_9)
        self.camera_view_14.setObjectName(u"camera_view_14")
        sizePolicy1.setHeightForWidth(self.camera_view_14.sizePolicy().hasHeightForWidth())
        self.camera_view_14.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setFamilies([u"NanumBarunGothic"])
        font5.setPointSize(16)
        self.camera_view_14.setFont(font5)
        self.camera_view_14.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_14.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_14.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_14.setScaledContents(False)
        self.camera_view_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_49.addWidget(self.camera_view_14)


        self.gridLayout_3.addLayout(self.search_camera_view_layout_49, 4, 1, 1, 1)

        self.search_camera_view_layout_50 = QVBoxLayout()
        self.search_camera_view_layout_50.setSpacing(0)
        self.search_camera_view_layout_50.setObjectName(u"search_camera_view_layout_50")
        self.camera_view_name_13 = QLabel(self.widget_9)
        self.camera_view_name_13.setObjectName(u"camera_view_name_13")
        sizePolicy.setHeightForWidth(self.camera_view_name_13.sizePolicy().hasHeightForWidth())
        self.camera_view_name_13.setSizePolicy(sizePolicy)
        self.camera_view_name_13.setMaximumSize(QSize(722, 20))
        self.camera_view_name_13.setFont(font4)
        self.camera_view_name_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_13.setMargin(0)
        self.camera_view_name_13.setIndent(15)

        self.search_camera_view_layout_50.addWidget(self.camera_view_name_13)

        self.camera_view_13 = QLabel(self.widget_9)
        self.camera_view_13.setObjectName(u"camera_view_13")
        sizePolicy1.setHeightForWidth(self.camera_view_13.sizePolicy().hasHeightForWidth())
        self.camera_view_13.setSizePolicy(sizePolicy1)
        self.camera_view_13.setFont(font5)
        self.camera_view_13.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_13.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_13.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_13.setScaledContents(False)
        self.camera_view_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_50.addWidget(self.camera_view_13)


        self.gridLayout_3.addLayout(self.search_camera_view_layout_50, 4, 0, 1, 1)

        self.search_camera_view_layout_51 = QVBoxLayout()
        self.search_camera_view_layout_51.setSpacing(0)
        self.search_camera_view_layout_51.setObjectName(u"search_camera_view_layout_51")
        self.camera_view_name_1 = QLabel(self.widget_9)
        self.camera_view_name_1.setObjectName(u"camera_view_name_1")
        sizePolicy.setHeightForWidth(self.camera_view_name_1.sizePolicy().hasHeightForWidth())
        self.camera_view_name_1.setSizePolicy(sizePolicy)
        self.camera_view_name_1.setMaximumSize(QSize(722, 20))
        self.camera_view_name_1.setFont(font4)
        self.camera_view_name_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_1.setMargin(0)
        self.camera_view_name_1.setIndent(15)

        self.search_camera_view_layout_51.addWidget(self.camera_view_name_1)

        self.camera_view_1 = QLabel(self.widget_9)
        self.camera_view_1.setObjectName(u"camera_view_1")
        sizePolicy1.setHeightForWidth(self.camera_view_1.sizePolicy().hasHeightForWidth())
        self.camera_view_1.setSizePolicy(sizePolicy1)
        self.camera_view_1.setFont(font5)
        self.camera_view_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_1.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_1.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_1.setScaledContents(False)
        self.camera_view_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_51.addWidget(self.camera_view_1)


        self.gridLayout_3.addLayout(self.search_camera_view_layout_51, 1, 0, 1, 1)

        self.search_camera_view_layout_52 = QVBoxLayout()
        self.search_camera_view_layout_52.setSpacing(0)
        self.search_camera_view_layout_52.setObjectName(u"search_camera_view_layout_52")
        self.camera_view_name_7 = QLabel(self.widget_9)
        self.camera_view_name_7.setObjectName(u"camera_view_name_7")
        sizePolicy.setHeightForWidth(self.camera_view_name_7.sizePolicy().hasHeightForWidth())
        self.camera_view_name_7.setSizePolicy(sizePolicy)
        self.camera_view_name_7.setMaximumSize(QSize(722, 20))
        self.camera_view_name_7.setFont(font4)
        self.camera_view_name_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_7.setMargin(0)
        self.camera_view_name_7.setIndent(15)

        self.search_camera_view_layout_52.addWidget(self.camera_view_name_7)

        self.camera_view_7 = QLabel(self.widget_9)
        self.camera_view_7.setObjectName(u"camera_view_7")
        sizePolicy1.setHeightForWidth(self.camera_view_7.sizePolicy().hasHeightForWidth())
        self.camera_view_7.setSizePolicy(sizePolicy1)
        self.camera_view_7.setFont(font5)
        self.camera_view_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_7.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_7.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_7.setScaledContents(False)
        self.camera_view_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_52.addWidget(self.camera_view_7)


        self.gridLayout_3.addLayout(self.search_camera_view_layout_52, 2, 2, 1, 1)

        self.search_camera_view_layout_53 = QVBoxLayout()
        self.search_camera_view_layout_53.setSpacing(0)
        self.search_camera_view_layout_53.setObjectName(u"search_camera_view_layout_53")
        self.camera_view_name_4 = QLabel(self.widget_9)
        self.camera_view_name_4.setObjectName(u"camera_view_name_4")
        sizePolicy.setHeightForWidth(self.camera_view_name_4.sizePolicy().hasHeightForWidth())
        self.camera_view_name_4.setSizePolicy(sizePolicy)
        self.camera_view_name_4.setMaximumSize(QSize(722, 20))
        self.camera_view_name_4.setFont(font4)
        self.camera_view_name_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_4.setMargin(0)
        self.camera_view_name_4.setIndent(15)

        self.search_camera_view_layout_53.addWidget(self.camera_view_name_4)

        self.camera_view_4 = QLabel(self.widget_9)
        self.camera_view_4.setObjectName(u"camera_view_4")
        sizePolicy1.setHeightForWidth(self.camera_view_4.sizePolicy().hasHeightForWidth())
        self.camera_view_4.setSizePolicy(sizePolicy1)
        self.camera_view_4.setFont(font5)
        self.camera_view_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_4.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_4.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_4.setScaledContents(False)
        self.camera_view_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_53.addWidget(self.camera_view_4)


        self.gridLayout_3.addLayout(self.search_camera_view_layout_53, 1, 3, 1, 1)

        self.search_camera_view_layout_54 = QVBoxLayout()
        self.search_camera_view_layout_54.setSpacing(0)
        self.search_camera_view_layout_54.setObjectName(u"search_camera_view_layout_54")
        self.camera_view_name_15 = QLabel(self.widget_9)
        self.camera_view_name_15.setObjectName(u"camera_view_name_15")
        sizePolicy.setHeightForWidth(self.camera_view_name_15.sizePolicy().hasHeightForWidth())
        self.camera_view_name_15.setSizePolicy(sizePolicy)
        self.camera_view_name_15.setMaximumSize(QSize(722, 20))
        self.camera_view_name_15.setFont(font4)
        self.camera_view_name_15.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_15.setMargin(0)
        self.camera_view_name_15.setIndent(15)

        self.search_camera_view_layout_54.addWidget(self.camera_view_name_15)

        self.camera_view_15 = QLabel(self.widget_9)
        self.camera_view_15.setObjectName(u"camera_view_15")
        sizePolicy1.setHeightForWidth(self.camera_view_15.sizePolicy().hasHeightForWidth())
        self.camera_view_15.setSizePolicy(sizePolicy1)
        self.camera_view_15.setFont(font5)
        self.camera_view_15.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_15.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_15.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_15.setScaledContents(False)
        self.camera_view_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_54.addWidget(self.camera_view_15)


        self.gridLayout_3.addLayout(self.search_camera_view_layout_54, 4, 2, 1, 1)

        self.search_camera_view_layout_55 = QVBoxLayout()
        self.search_camera_view_layout_55.setSpacing(0)
        self.search_camera_view_layout_55.setObjectName(u"search_camera_view_layout_55")
        self.camera_view_name_9 = QLabel(self.widget_9)
        self.camera_view_name_9.setObjectName(u"camera_view_name_9")
        sizePolicy.setHeightForWidth(self.camera_view_name_9.sizePolicy().hasHeightForWidth())
        self.camera_view_name_9.setSizePolicy(sizePolicy)
        self.camera_view_name_9.setMaximumSize(QSize(722, 20))
        self.camera_view_name_9.setFont(font4)
        self.camera_view_name_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_9.setMargin(0)
        self.camera_view_name_9.setIndent(15)

        self.search_camera_view_layout_55.addWidget(self.camera_view_name_9)

        self.camera_view_9 = QLabel(self.widget_9)
        self.camera_view_9.setObjectName(u"camera_view_9")
        sizePolicy1.setHeightForWidth(self.camera_view_9.sizePolicy().hasHeightForWidth())
        self.camera_view_9.setSizePolicy(sizePolicy1)
        self.camera_view_9.setFont(font5)
        self.camera_view_9.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_9.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_9.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_9.setScaledContents(False)
        self.camera_view_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_55.addWidget(self.camera_view_9)


        self.gridLayout_3.addLayout(self.search_camera_view_layout_55, 3, 0, 1, 1)

        self.search_camera_view_layout_56 = QVBoxLayout()
        self.search_camera_view_layout_56.setSpacing(0)
        self.search_camera_view_layout_56.setObjectName(u"search_camera_view_layout_56")
        self.camera_view_name_11 = QLabel(self.widget_9)
        self.camera_view_name_11.setObjectName(u"camera_view_name_11")
        sizePolicy.setHeightForWidth(self.camera_view_name_11.sizePolicy().hasHeightForWidth())
        self.camera_view_name_11.setSizePolicy(sizePolicy)
        self.camera_view_name_11.setMaximumSize(QSize(722, 20))
        self.camera_view_name_11.setFont(font4)
        self.camera_view_name_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_11.setMargin(0)
        self.camera_view_name_11.setIndent(15)

        self.search_camera_view_layout_56.addWidget(self.camera_view_name_11)

        self.camera_view_11 = QLabel(self.widget_9)
        self.camera_view_11.setObjectName(u"camera_view_11")
        sizePolicy1.setHeightForWidth(self.camera_view_11.sizePolicy().hasHeightForWidth())
        self.camera_view_11.setSizePolicy(sizePolicy1)
        self.camera_view_11.setFont(font5)
        self.camera_view_11.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_11.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_11.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_11.setScaledContents(False)
        self.camera_view_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_56.addWidget(self.camera_view_11)


        self.gridLayout_3.addLayout(self.search_camera_view_layout_56, 3, 2, 1, 1)

        self.search_camera_view_layout_57 = QVBoxLayout()
        self.search_camera_view_layout_57.setSpacing(0)
        self.search_camera_view_layout_57.setObjectName(u"search_camera_view_layout_57")
        self.camera_view_name_16 = QLabel(self.widget_9)
        self.camera_view_name_16.setObjectName(u"camera_view_name_16")
        sizePolicy.setHeightForWidth(self.camera_view_name_16.sizePolicy().hasHeightForWidth())
        self.camera_view_name_16.setSizePolicy(sizePolicy)
        self.camera_view_name_16.setMaximumSize(QSize(722, 20))
        self.camera_view_name_16.setFont(font4)
        self.camera_view_name_16.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_16.setMargin(0)
        self.camera_view_name_16.setIndent(15)

        self.search_camera_view_layout_57.addWidget(self.camera_view_name_16)

        self.camera_view_16 = QLabel(self.widget_9)
        self.camera_view_16.setObjectName(u"camera_view_16")
        sizePolicy1.setHeightForWidth(self.camera_view_16.sizePolicy().hasHeightForWidth())
        self.camera_view_16.setSizePolicy(sizePolicy1)
        self.camera_view_16.setFont(font5)
        self.camera_view_16.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_16.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_16.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_16.setScaledContents(False)
        self.camera_view_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_57.addWidget(self.camera_view_16)


        self.gridLayout_3.addLayout(self.search_camera_view_layout_57, 4, 3, 1, 1)

        self.search_camera_view_layout_58 = QVBoxLayout()
        self.search_camera_view_layout_58.setSpacing(0)
        self.search_camera_view_layout_58.setObjectName(u"search_camera_view_layout_58")
        self.camera_view_name_8 = QLabel(self.widget_9)
        self.camera_view_name_8.setObjectName(u"camera_view_name_8")
        sizePolicy.setHeightForWidth(self.camera_view_name_8.sizePolicy().hasHeightForWidth())
        self.camera_view_name_8.setSizePolicy(sizePolicy)
        self.camera_view_name_8.setMaximumSize(QSize(722, 20))
        self.camera_view_name_8.setFont(font4)
        self.camera_view_name_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_8.setMargin(0)
        self.camera_view_name_8.setIndent(15)

        self.search_camera_view_layout_58.addWidget(self.camera_view_name_8)

        self.camera_view_8 = QLabel(self.widget_9)
        self.camera_view_8.setObjectName(u"camera_view_8")
        sizePolicy1.setHeightForWidth(self.camera_view_8.sizePolicy().hasHeightForWidth())
        self.camera_view_8.setSizePolicy(sizePolicy1)
        self.camera_view_8.setFont(font5)
        self.camera_view_8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_8.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_8.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_8.setScaledContents(False)
        self.camera_view_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_58.addWidget(self.camera_view_8)


        self.gridLayout_3.addLayout(self.search_camera_view_layout_58, 2, 3, 1, 1)

        self.search_camera_view_layout_59 = QVBoxLayout()
        self.search_camera_view_layout_59.setSpacing(0)
        self.search_camera_view_layout_59.setObjectName(u"search_camera_view_layout_59")
        self.camera_view_name_12 = QLabel(self.widget_9)
        self.camera_view_name_12.setObjectName(u"camera_view_name_12")
        sizePolicy.setHeightForWidth(self.camera_view_name_12.sizePolicy().hasHeightForWidth())
        self.camera_view_name_12.setSizePolicy(sizePolicy)
        self.camera_view_name_12.setMaximumSize(QSize(722, 20))
        self.camera_view_name_12.setFont(font4)
        self.camera_view_name_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_12.setMargin(0)
        self.camera_view_name_12.setIndent(15)

        self.search_camera_view_layout_59.addWidget(self.camera_view_name_12)

        self.camera_view_12 = QLabel(self.widget_9)
        self.camera_view_12.setObjectName(u"camera_view_12")
        sizePolicy1.setHeightForWidth(self.camera_view_12.sizePolicy().hasHeightForWidth())
        self.camera_view_12.setSizePolicy(sizePolicy1)
        self.camera_view_12.setFont(font5)
        self.camera_view_12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_12.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_12.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_12.setScaledContents(False)
        self.camera_view_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_59.addWidget(self.camera_view_12)


        self.gridLayout_3.addLayout(self.search_camera_view_layout_59, 3, 3, 1, 1)

        self.search_camera_view_layout_60 = QVBoxLayout()
        self.search_camera_view_layout_60.setSpacing(0)
        self.search_camera_view_layout_60.setObjectName(u"search_camera_view_layout_60")
        self.camera_view_name_3 = QLabel(self.widget_9)
        self.camera_view_name_3.setObjectName(u"camera_view_name_3")
        sizePolicy.setHeightForWidth(self.camera_view_name_3.sizePolicy().hasHeightForWidth())
        self.camera_view_name_3.setSizePolicy(sizePolicy)
        self.camera_view_name_3.setMaximumSize(QSize(722, 20))
        self.camera_view_name_3.setFont(font4)
        self.camera_view_name_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_3.setMargin(0)
        self.camera_view_name_3.setIndent(15)

        self.search_camera_view_layout_60.addWidget(self.camera_view_name_3)

        self.camera_view_3 = QLabel(self.widget_9)
        self.camera_view_3.setObjectName(u"camera_view_3")
        sizePolicy1.setHeightForWidth(self.camera_view_3.sizePolicy().hasHeightForWidth())
        self.camera_view_3.setSizePolicy(sizePolicy1)
        self.camera_view_3.setFont(font5)
        self.camera_view_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_3.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_3.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_3.setScaledContents(False)
        self.camera_view_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_60.addWidget(self.camera_view_3)


        self.gridLayout_3.addLayout(self.search_camera_view_layout_60, 1, 2, 1, 1)

        self.search_camera_view_layout_61 = QVBoxLayout()
        self.search_camera_view_layout_61.setSpacing(0)
        self.search_camera_view_layout_61.setObjectName(u"search_camera_view_layout_61")
        self.camera_view_name_6 = QLabel(self.widget_9)
        self.camera_view_name_6.setObjectName(u"camera_view_name_6")
        sizePolicy.setHeightForWidth(self.camera_view_name_6.sizePolicy().hasHeightForWidth())
        self.camera_view_name_6.setSizePolicy(sizePolicy)
        self.camera_view_name_6.setMaximumSize(QSize(722, 20))
        self.camera_view_name_6.setFont(font4)
        self.camera_view_name_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_6.setMargin(0)
        self.camera_view_name_6.setIndent(15)

        self.search_camera_view_layout_61.addWidget(self.camera_view_name_6)

        self.camera_view_6 = QLabel(self.widget_9)
        self.camera_view_6.setObjectName(u"camera_view_6")
        sizePolicy1.setHeightForWidth(self.camera_view_6.sizePolicy().hasHeightForWidth())
        self.camera_view_6.setSizePolicy(sizePolicy1)
        self.camera_view_6.setFont(font5)
        self.camera_view_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_6.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_6.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_6.setScaledContents(False)
        self.camera_view_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_61.addWidget(self.camera_view_6)


        self.gridLayout_3.addLayout(self.search_camera_view_layout_61, 2, 1, 1, 1)

        self.search_camera_view_layout_62 = QVBoxLayout()
        self.search_camera_view_layout_62.setSpacing(0)
        self.search_camera_view_layout_62.setObjectName(u"search_camera_view_layout_62")
        self.camera_view_name_10 = QLabel(self.widget_9)
        self.camera_view_name_10.setObjectName(u"camera_view_name_10")
        sizePolicy.setHeightForWidth(self.camera_view_name_10.sizePolicy().hasHeightForWidth())
        self.camera_view_name_10.setSizePolicy(sizePolicy)
        self.camera_view_name_10.setMaximumSize(QSize(722, 20))
        self.camera_view_name_10.setFont(font4)
        self.camera_view_name_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_10.setMargin(0)
        self.camera_view_name_10.setIndent(15)

        self.search_camera_view_layout_62.addWidget(self.camera_view_name_10)

        self.camera_view_10 = QLabel(self.widget_9)
        self.camera_view_10.setObjectName(u"camera_view_10")
        sizePolicy1.setHeightForWidth(self.camera_view_10.sizePolicy().hasHeightForWidth())
        self.camera_view_10.setSizePolicy(sizePolicy1)
        self.camera_view_10.setFont(font5)
        self.camera_view_10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_10.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_10.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_10.setScaledContents(False)
        self.camera_view_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_62.addWidget(self.camera_view_10)


        self.gridLayout_3.addLayout(self.search_camera_view_layout_62, 3, 1, 1, 1)

        self.search_camera_view_layout_63 = QVBoxLayout()
        self.search_camera_view_layout_63.setSpacing(0)
        self.search_camera_view_layout_63.setObjectName(u"search_camera_view_layout_63")
        self.camera_view_name_5 = QLabel(self.widget_9)
        self.camera_view_name_5.setObjectName(u"camera_view_name_5")
        sizePolicy.setHeightForWidth(self.camera_view_name_5.sizePolicy().hasHeightForWidth())
        self.camera_view_name_5.setSizePolicy(sizePolicy)
        self.camera_view_name_5.setMaximumSize(QSize(722, 20))
        self.camera_view_name_5.setFont(font4)
        self.camera_view_name_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_5.setMargin(0)
        self.camera_view_name_5.setIndent(15)

        self.search_camera_view_layout_63.addWidget(self.camera_view_name_5)

        self.camera_view_5 = QLabel(self.widget_9)
        self.camera_view_5.setObjectName(u"camera_view_5")
        sizePolicy1.setHeightForWidth(self.camera_view_5.sizePolicy().hasHeightForWidth())
        self.camera_view_5.setSizePolicy(sizePolicy1)
        self.camera_view_5.setFont(font5)
        self.camera_view_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_5.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_5.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_5.setScaledContents(False)
        self.camera_view_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_63.addWidget(self.camera_view_5)


        self.gridLayout_3.addLayout(self.search_camera_view_layout_63, 2, 0, 1, 1)

        self.search_camera_view_layout_64 = QVBoxLayout()
        self.search_camera_view_layout_64.setSpacing(0)
        self.search_camera_view_layout_64.setObjectName(u"search_camera_view_layout_64")
        self.camera_view_name_2 = QLabel(self.widget_9)
        self.camera_view_name_2.setObjectName(u"camera_view_name_2")
        sizePolicy.setHeightForWidth(self.camera_view_name_2.sizePolicy().hasHeightForWidth())
        self.camera_view_name_2.setSizePolicy(sizePolicy)
        self.camera_view_name_2.setMaximumSize(QSize(722, 20))
        self.camera_view_name_2.setFont(font4)
        self.camera_view_name_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_2.setMargin(0)
        self.camera_view_name_2.setIndent(15)

        self.search_camera_view_layout_64.addWidget(self.camera_view_name_2)

        self.camera_view_2 = QLabel(self.widget_9)
        self.camera_view_2.setObjectName(u"camera_view_2")
        sizePolicy1.setHeightForWidth(self.camera_view_2.sizePolicy().hasHeightForWidth())
        self.camera_view_2.setSizePolicy(sizePolicy1)
        self.camera_view_2.setFont(font5)
        self.camera_view_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_2.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_2.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_2.setScaledContents(False)
        self.camera_view_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_64.addWidget(self.camera_view_2)


        self.gridLayout_3.addLayout(self.search_camera_view_layout_64, 1, 1, 1, 1)


        self.horizontalLayout_4.addWidget(self.widget_9)

        self.stackedWidget_4.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_6 = QVBoxLayout(self.page_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget_4.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.stackedWidget_4.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.stackedWidget_4.addWidget(self.page_10)

        self.horizontalLayout_3.addWidget(self.stackedWidget_4)

        self.widget_10 = QWidget(self.widget_4)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy2.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy2)
        self.widget_10.setMaximumSize(QSize(39, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.widget_10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_5.addItem(self.verticalSpacer_7)

        self.search_camera_next_page_bnt_2 = QPushButton(self.widget_10)
        self.search_camera_next_page_bnt_2.setObjectName(u"search_camera_next_page_bnt_2")
        self.search_camera_next_page_bnt_2.setMaximumSize(QSize(34, 41))
        self.search_camera_next_page_bnt_2.setFont(font3)
        self.search_camera_next_page_bnt_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.search_camera_next_page_bnt_2.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/ui/ui/images/ico_arrow_right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_camera_next_page_bnt_2.setIcon(icon1)
        self.search_camera_next_page_bnt_2.setIconSize(QSize(31, 50))

        self.verticalLayout_5.addWidget(self.search_camera_next_page_bnt_2)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_5.addItem(self.verticalSpacer_8)


        self.horizontalLayout_3.addWidget(self.widget_10)


        self.verticalLayout_18.addWidget(self.widget_4)


        self.verticalLayout_26.addLayout(self.verticalLayout_18)

        self.stackedWidget.addWidget(self.camera_select_page)
        self.event_video_viewer = QWidget()
        self.event_video_viewer.setObjectName(u"event_video_viewer")
        self.verticalLayout_27 = QVBoxLayout(self.event_video_viewer)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_6 = QWidget(self.event_video_viewer)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_23 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_12)

        self.page_undo_bnt = QPushButton(self.widget_6)
        self.page_undo_bnt.setObjectName(u"page_undo_bnt")
        self.page_undo_bnt.setMinimumSize(QSize(61, 31))
        self.page_undo_bnt.setMaximumSize(QSize(61, 31))
        self.page_undo_bnt.setFont(font1)
        self.page_undo_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.page_undo_bnt.setStyleSheet(u"background-color: rgb(255, 49, 38);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")

        self.horizontalLayout_22.addWidget(self.page_undo_bnt)


        self.horizontalLayout_23.addLayout(self.horizontalLayout_22)


        self.verticalLayout_20.addWidget(self.widget_6)

        self.search_viewer = QLabel(self.event_video_viewer)
        self.search_viewer.setObjectName(u"search_viewer")
        self.search_viewer.setMinimumSize(QSize(640, 480))
        self.search_viewer.setMaximumSize(QSize(1280, 720))
        self.search_viewer.setFont(font)
        self.search_viewer.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"border-radius: 10px ;")
        self.search_viewer.setPixmap(QPixmap(u":/ui/ui/images/logo.png"))
        self.search_viewer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.search_viewer)


        self.verticalLayout_27.addLayout(self.verticalLayout_20)

        self.stackedWidget.addWidget(self.event_video_viewer)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_40 = QVBoxLayout(self.page_3)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(-1, -1, 9, -1)
        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.par_total_result_count_label = QLabel(self.page_3)
        self.par_total_result_count_label.setObjectName(u"par_total_result_count_label")
        self.par_total_result_count_label.setFont(font2)
        self.par_total_result_count_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(191, 64, 64, 0);")
        self.par_total_result_count_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_39.addWidget(self.par_total_result_count_label)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_41)

        self.camera_select_undo_bnt = QPushButton(self.page_3)
        self.camera_select_undo_bnt.setObjectName(u"camera_select_undo_bnt")
        sizePolicy1.setHeightForWidth(self.camera_select_undo_bnt.sizePolicy().hasHeightForWidth())
        self.camera_select_undo_bnt.setSizePolicy(sizePolicy1)
        self.camera_select_undo_bnt.setMinimumSize(QSize(79, 22))
        self.camera_select_undo_bnt.setMaximumSize(QSize(120, 30))
        self.camera_select_undo_bnt.setFont(font1)
        self.camera_select_undo_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.camera_select_undo_bnt.setStyleSheet(u"background-color: rgb(36, 39, 44);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"")

        self.horizontalLayout_39.addWidget(self.camera_select_undo_bnt)


        self.verticalLayout_38.addLayout(self.horizontalLayout_39)


        self.verticalLayout_40.addLayout(self.verticalLayout_38)

        self.scrollArea = QScrollArea(self.page_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 98, 28))
        self.verticalLayout_44 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(-1, 0, -1, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_40.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout_17.addWidget(self.stackedWidget)

        self.widget = QWidget(Search_window)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(472, 0))
        self.widget.setMaximumSize(QSize(472, 16777215))
        self.verticalLayout_21 = QVBoxLayout(self.widget)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.time_label_2 = QLabel(self.widget)
        self.time_label_2.setObjectName(u"time_label_2")
        self.time_label_2.setFont(font2)
        self.time_label_2.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(191, 64, 64, 0);")
        self.time_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_16.addWidget(self.time_label_2)

        self.event_search_bnt = QPushButton(self.widget)
        self.event_search_bnt.setObjectName(u"event_search_bnt")
        sizePolicy1.setHeightForWidth(self.event_search_bnt.sizePolicy().hasHeightForWidth())
        self.event_search_bnt.setSizePolicy(sizePolicy1)
        self.event_search_bnt.setMinimumSize(QSize(137, 33))
        self.event_search_bnt.setMaximumSize(QSize(137, 33))
        self.event_search_bnt.setFont(font1)
        self.event_search_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.event_search_bnt.setStyleSheet(u"background-color: rgb(36, 39, 44);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"")

        self.horizontalLayout_16.addWidget(self.event_search_bnt)

        self.horizontalSpacer_11 = QSpacerItem(22, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_11)


        self.verticalLayout_21.addLayout(self.horizontalLayout_16)

        self.stackedWidget_2 = QStackedWidget(self.widget)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMaximumSize(QSize(480, 16777215))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_24 = QVBoxLayout(self.page)
        self.verticalLayout_24.setSpacing(7)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(8)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_9 = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)

        self.time_label = QLabel(self.page)
        self.time_label.setObjectName(u"time_label")
        font6 = QFont()
        font6.setFamilies([u"Sans"])
        font6.setPointSize(11)
        self.time_label.setFont(font6)
        self.time_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(191, 64, 64, 0);")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.time_label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)


        self.verticalLayout_23.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.time_day_start_input = QDateEdit(self.page)
        self.time_day_start_input.setObjectName(u"time_day_start_input")
        self.time_day_start_input.setMinimumSize(QSize(115, 0))
        self.time_day_start_input.setMaximumSize(QSize(105, 16777215))
        self.time_day_start_input.setFont(font1)
        self.time_day_start_input.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.time_day_start_input.setStyleSheet(u"QDateEdit {\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(13, 16, 23);\n"
"\n"
"}\n"
"QCalendarWidget {\n"
"    font-size: 10pt; /* \ud3f0\ud2b8 \ud06c\uae30\ub97c \ud06c\uac8c \uc124\uc815\ud558\uc5ec \uc804\uccb4 \ud06c\uae30 \uc99d\uac00 */\n"
"    background-color: rgb(87, 227, 137);\n"
"    alternate-background-color: rgb(87, 227, 137);\n"
"}\n"
"QCalendarWidget QWidget { /* All child widgets of QCalendarWidget */\n"
"color: rgb(255, 255, 255);\n"
"background-color: #323232;  \n"
"alternate-background-color: rgb(30, 30, 30);\n"
"border-radius: 15px;\n"
"}\n"
"QCalendarWidget QAbstractItemView {\n"
"selection-background-color: rgb(100, 100, 100);;\n"
"selection-color: white;\n"
"}\n"
"\n"
"\n"
"QToolButton#qt_calendar_prevmonth {\n"
"        qproperty-icon: url(':/ui/ui/images/left_arrow.png'); /* \uc774\uc804 \ub2ec \uc544\uc774\ucf58 */\n"
"        width: 24px;  /* \ubc84\ud2bc \ub108\ube44 */\n"
"        height: 24px; /* \ubc84\ud2bc \ub192\uc774 */\n"
"        background-color: "
                        "transparent; /* \ubc30\uacbd \ud22c\uba85 */\n"
"        border: none; /* \ud14c\ub450\ub9ac \uc5c6\uc74c */\n"
"    }\n"
"\n"
"    QToolButton#qt_calendar_nextmonth {\n"
"        qproperty-icon: url(':/ui/ui/images/right_arrow.png'); /* \ub2e4\uc74c \ub2ec \uc544\uc774\ucf58 */\n"
"        width: 24px;  /* \ubc84\ud2bc \ub108\ube44 */\n"
"        height: 24px; /* \ubc84\ud2bc \ub192\uc774 */\n"
"        background-color: transparent; /* \ubc30\uacbd \ud22c\uba85 */\n"
"        border: none; /* \ud14c\ub450\ub9ac \uc5c6\uc74c */\n"
"    }\n"
" /* \ub9c8\uc6b0\uc2a4\uac00 \ub0a0\uc9dc \uce78 \uc704\ub85c \uc774\ub3d9\ud558\uba74 \ud558\uc774\ub77c\uc774\ud2b8 */\n"
"QCalendarWidget QAbstractItemView::item:hover {\n"
"        background-color: rgba(0, 139, 41, 50); \n"
"        border: 1px solid rgba(100, 100, 100, 100); /* \uc120\ud0dd \uacbd\uacc4\uc120 */\n"
"    }")
        self.time_day_start_input.setFrame(False)
        self.time_day_start_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_day_start_input.setReadOnly(False)
        self.time_day_start_input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.time_day_start_input.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.time_day_start_input.setKeyboardTracking(True)
        self.time_day_start_input.setProperty(u"showGroupSeparator", False)
        self.time_day_start_input.setCurrentSection(QDateTimeEdit.Section.YearSection)
        self.time_day_start_input.setCalendarPopup(True)

        self.horizontalLayout_9.addWidget(self.time_day_start_input)

        self.time_hour_start_box = QComboBox(self.page)
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.setObjectName(u"time_hour_start_box")
        self.time_hour_start_box.setMinimumSize(QSize(80, 24))
        self.time_hour_start_box.setMaximumSize(QSize(68, 16777215))
        font7 = QFont()
        font7.setFamilies([u"Sans"])
        font7.setPointSize(10)
        font7.setBold(False)
        self.time_hour_start_box.setFont(font7)
        self.time_hour_start_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(13, 16, 23);\n"
"\n"
"")
        self.time_hour_start_box.setEditable(True)
        self.time_hour_start_box.setMinimumContentsLength(0)

        self.horizontalLayout_9.addWidget(self.time_hour_start_box)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)

        self.time_tilde = QLabel(self.page)
        self.time_tilde.setObjectName(u"time_tilde")
        sizePolicy.setHeightForWidth(self.time_tilde.sizePolicy().hasHeightForWidth())
        self.time_tilde.setSizePolicy(sizePolicy)
        font8 = QFont()
        font8.setFamilies([u"Sans"])
        font8.setPointSize(12)
        self.time_tilde.setFont(font8)
        self.time_tilde.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(191, 64, 64, 0);")
        self.time_tilde.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.time_tilde)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.time_day_end_input = QDateEdit(self.page)
        self.time_day_end_input.setObjectName(u"time_day_end_input")
        self.time_day_end_input.setMinimumSize(QSize(115, 0))
        self.time_day_end_input.setMaximumSize(QSize(105, 16777215))
        self.time_day_end_input.setFont(font1)
        self.time_day_end_input.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.time_day_end_input.setStyleSheet(u"QDateEdit {\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(13, 16, 23);\n"
"\n"
"}\n"
"QCalendarWidget {\n"
"    font-size: 10pt; /* \ud3f0\ud2b8 \ud06c\uae30\ub97c \ud06c\uac8c \uc124\uc815\ud558\uc5ec \uc804\uccb4 \ud06c\uae30 \uc99d\uac00 */\n"
"    background-color: rgb(87, 227, 137);\n"
"    alternate-background-color: rgb(87, 227, 137);\n"
"}\n"
"QCalendarWidget QWidget { /* All child widgets of QCalendarWidget */\n"
"color: rgb(255, 255, 255);\n"
"background-color: #323232;  \n"
"alternate-background-color: rgb(30, 30, 30);\n"
"border-radius: 15px;\n"
"}\n"
"QCalendarWidget QAbstractItemView {\n"
"selection-background-color: rgb(100, 100, 100);;\n"
"selection-color: white;\n"
"}\n"
"\n"
"\n"
"QToolButton#qt_calendar_prevmonth {\n"
"        qproperty-icon: url(':/ui/ui/images/left_arrow.png'); /* \uc774\uc804 \ub2ec \uc544\uc774\ucf58 */\n"
"        width: 24px;  /* \ubc84\ud2bc \ub108\ube44 */\n"
"        height: 24px; /* \ubc84\ud2bc \ub192\uc774 */\n"
"        background-color: "
                        "transparent; /* \ubc30\uacbd \ud22c\uba85 */\n"
"        border: none; /* \ud14c\ub450\ub9ac \uc5c6\uc74c */\n"
"    }\n"
"\n"
"    QToolButton#qt_calendar_nextmonth {\n"
"        qproperty-icon: url(':/ui/ui/images/right_arrow.png'); /* \ub2e4\uc74c \ub2ec \uc544\uc774\ucf58 */\n"
"        width: 24px;  /* \ubc84\ud2bc \ub108\ube44 */\n"
"        height: 24px; /* \ubc84\ud2bc \ub192\uc774 */\n"
"        background-color: transparent; /* \ubc30\uacbd \ud22c\uba85 */\n"
"        border: none; /* \ud14c\ub450\ub9ac \uc5c6\uc74c */\n"
"    }\n"
" /* \ub9c8\uc6b0\uc2a4\uac00 \ub0a0\uc9dc \uce78 \uc704\ub85c \uc774\ub3d9\ud558\uba74 \ud558\uc774\ub77c\uc774\ud2b8 */\n"
"QCalendarWidget QAbstractItemView::item:hover {\n"
"        background-color: rgba(0, 139, 41, 50); \n"
"        border: 1px solid rgba(100, 100, 100, 100); /* \uc120\ud0dd \uacbd\uacc4\uc120 */\n"
"    }")
        self.time_day_end_input.setWrapping(False)
        self.time_day_end_input.setFrame(False)
        self.time_day_end_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_day_end_input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.time_day_end_input.setCurrentSection(QDateTimeEdit.Section.YearSection)
        self.time_day_end_input.setCalendarPopup(True)

        self.horizontalLayout_10.addWidget(self.time_day_end_input)

        self.time_hour_end_box = QComboBox(self.page)
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.setObjectName(u"time_hour_end_box")
        self.time_hour_end_box.setMinimumSize(QSize(80, 24))
        self.time_hour_end_box.setMaximumSize(QSize(68, 16777215))
        self.time_hour_end_box.setFont(font7)
        self.time_hour_end_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.time_hour_end_box.setEditable(True)
        self.time_hour_end_box.setMinimumContentsLength(0)

        self.horizontalLayout_10.addWidget(self.time_hour_end_box)

        self.horizontalSpacer_5 = QSpacerItem(13, 23, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_10)


        self.verticalLayout_23.addLayout(self.horizontalLayout_7)


        self.verticalLayout_22.addLayout(self.verticalLayout_23)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_7 = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.event_label = QLabel(self.page)
        self.event_label.setObjectName(u"event_label")
        self.event_label.setMinimumSize(QSize(91, 0))
        self.event_label.setMaximumSize(QSize(91, 16777215))
        self.event_label.setFont(font8)
        self.event_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(191, 64, 64, 0);")
        self.event_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.event_label)

        self.event_box = QComboBox(self.page)
        self.event_box.addItem("")
        self.event_box.setObjectName(u"event_box")
        self.event_box.setFont(font7)
        self.event_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.event_box.setMinimumContentsLength(0)

        self.horizontalLayout_11.addWidget(self.event_box)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_11)

        self.horizontalSpacer_10 = QSpacerItem(38, 13, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.sort_label = QLabel(self.page)
        self.sort_label.setObjectName(u"sort_label")
        self.sort_label.setMaximumSize(QSize(70, 57))
        self.sort_label.setFont(font8)
        self.sort_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(191, 64, 64, 0);")
        self.sort_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.sort_label)

        self.sort_box = QComboBox(self.page)
        self.sort_box.addItem("")
        self.sort_box.addItem("")
        self.sort_box.setObjectName(u"sort_box")
        self.sort_box.setMaximumSize(QSize(71, 16777215))
        self.sort_box.setFont(font7)
        self.sort_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.sort_box.setMinimumContentsLength(0)

        self.horizontalLayout_6.addWidget(self.sort_box)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_4)


        self.verticalLayout_22.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_8 = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)

        self.time_video_time_speed_label = QLabel(self.page)
        self.time_video_time_speed_label.setObjectName(u"time_video_time_speed_label")
        self.time_video_time_speed_label.setMaximumSize(QSize(168, 16777215))
        self.time_video_time_speed_label.setFont(font6)
        self.time_video_time_speed_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.time_video_time_speed_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.time_video_time_speed_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.time_video_time_speed_label)

        self.time_video_time_speed_input = QDoubleSpinBox(self.page)
        self.time_video_time_speed_input.setObjectName(u"time_video_time_speed_input")
        self.time_video_time_speed_input.setMinimumSize(QSize(88, 24))
        self.time_video_time_speed_input.setMaximumSize(QSize(65, 24))
        self.time_video_time_speed_input.setStyleSheet(u"\n"
"    QDoubleSpinBox {\n"
"        subcontrol-origin: padding;\n"
"        subcontrol-position: top right;\n"
"        background: rgb(13, 16, 23);\n"
"        color: rgb(255, 255, 255);\n"
"\n"
"    }")
        self.time_video_time_speed_input.setMinimum(1.000000000000000)
        self.time_video_time_speed_input.setMaximum(10.000000000000000)
        self.time_video_time_speed_input.setSingleStep(0.200000000000000)

        self.horizontalLayout_12.addWidget(self.time_video_time_speed_input)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_12)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_6)

        self.search_bnt = QPushButton(self.page)
        self.search_bnt.setObjectName(u"search_bnt")
        self.search_bnt.setMinimumSize(QSize(61, 31))
        self.search_bnt.setMaximumSize(QSize(61, 31))
        self.search_bnt.setFont(font1)
        self.search_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.search_bnt.setStyleSheet(u"background-color: rgb(30, 195, 55);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")

        self.horizontalLayout_15.addWidget(self.search_bnt)


        self.verticalLayout_22.addLayout(self.horizontalLayout_15)


        self.verticalLayout.addLayout(self.verticalLayout_22)

        self.event_table = QTableWidget(self.page)
        if (self.event_table.columnCount() < 4):
            self.event_table.setColumnCount(4)
        font9 = QFont()
        font9.setPointSize(11)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font9);
        self.event_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font9);
        self.event_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font9);
        self.event_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font9);
        self.event_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.event_table.setObjectName(u"event_table")
        self.event_table.setMinimumSize(QSize(445, 5))
        self.event_table.setMaximumSize(QSize(445, 16777215))
        font10 = QFont()
        font10.setFamilies([u"Sans"])
        font10.setPointSize(11)
        font10.setBold(False)
        self.event_table.setFont(font10)
        self.event_table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.event_table.setStyleSheet(u"QTableWidget {\n"
"    background-color: rgb(13, 16, 23); /* \ud14c\uc774\ube14 \uc804\uccb4 \ubc30\uacbd\uc0c9 */\n"
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
"}")
        self.event_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.event_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.event_table.setTextElideMode(Qt.TextElideMode.ElideRight)
        self.event_table.setShowGrid(False)
        self.event_table.setGridStyle(Qt.PenStyle.DashDotLine)
        self.event_table.setSortingEnabled(False)
        self.event_table.setWordWrap(False)
        self.event_table.horizontalHeader().setVisible(True)
        self.event_table.horizontalHeader().setCascadingSectionResizes(False)
        self.event_table.horizontalHeader().setMinimumSectionSize(56)
        self.event_table.horizontalHeader().setDefaultSectionSize(84)
        self.event_table.horizontalHeader().setHighlightSections(False)
        self.event_table.horizontalHeader().setStretchLastSection(True)
        self.event_table.verticalHeader().setVisible(False)
        self.event_table.verticalHeader().setMinimumSectionSize(21)
        self.event_table.verticalHeader().setDefaultSectionSize(30)
        self.event_table.verticalHeader().setHighlightSections(False)
        self.event_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.event_table)


        self.verticalLayout_24.addLayout(self.verticalLayout)

        self.stackedWidget_2.addWidget(self.page)

        self.verticalLayout_21.addWidget(self.stackedWidget_2)


        self.horizontalLayout_17.addWidget(self.widget)


        self.verticalLayout_28.addLayout(self.horizontalLayout_17)


        self.verticalLayout_37.addLayout(self.verticalLayout_28)


        self.retranslateUi(Search_window)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(3)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Search_window)
    # setupUi

    def retranslateUi(self, Search_window):
        self.top_logo_2.setText("")
        self.close_bnt.setText(QCoreApplication.translate("Search_window", u"\ub2eb\uae30", None))
        self.camera_select_label.setText(QCoreApplication.translate("Search_window", u"\uc774\ubca4\ud2b8 \uac80\uc0c9 \uce74\uba54\ub77c \uc120\ud0dd", None))
        self.camera_select_all_bnt.setText(QCoreApplication.translate("Search_window", u"\ubaa8\ub450 \uc120\ud0dd", None))
        self.search_camera_undo_page_bnt_2.setText("")
        self.camera_view_name_14.setText(QCoreApplication.translate("Search_window", u"\uce74\uba54\ub77c14", None))
        self.camera_view_14.setText("")
        self.camera_view_name_13.setText(QCoreApplication.translate("Search_window", u"\uce74\uba54\ub77c13", None))
        self.camera_view_13.setText("")
        self.camera_view_name_1.setText(QCoreApplication.translate("Search_window", u"\uce74\uba54\ub77c1", None))
        self.camera_view_1.setText("")
        self.camera_view_name_7.setText(QCoreApplication.translate("Search_window", u"\uce74\uba54\ub77c7", None))
        self.camera_view_7.setText("")
        self.camera_view_name_4.setText(QCoreApplication.translate("Search_window", u"\uce74\uba54\ub77c4", None))
        self.camera_view_4.setText("")
        self.camera_view_name_15.setText(QCoreApplication.translate("Search_window", u"\uce74\uba54\ub77c15", None))
        self.camera_view_15.setText("")
        self.camera_view_name_9.setText(QCoreApplication.translate("Search_window", u"\uce74\uba54\ub77c9", None))
        self.camera_view_9.setText("")
        self.camera_view_name_11.setText(QCoreApplication.translate("Search_window", u"\uce74\uba54\ub77c11", None))
        self.camera_view_11.setText("")
        self.camera_view_name_16.setText(QCoreApplication.translate("Search_window", u"\uce74\uba54\ub77c16", None))
        self.camera_view_16.setText("")
        self.camera_view_name_8.setText(QCoreApplication.translate("Search_window", u"\uce74\uba54\ub77c8", None))
        self.camera_view_8.setText("")
        self.camera_view_name_12.setText(QCoreApplication.translate("Search_window", u"\uce74\uba54\ub77c12", None))
        self.camera_view_12.setText("")
        self.camera_view_name_3.setText(QCoreApplication.translate("Search_window", u"\uce74\uba54\ub77c3", None))
        self.camera_view_3.setText("")
        self.camera_view_name_6.setText(QCoreApplication.translate("Search_window", u"\uce74\uba54\ub77c6", None))
        self.camera_view_6.setText("")
        self.camera_view_name_10.setText(QCoreApplication.translate("Search_window", u"\uce74\uba54\ub77c10", None))
        self.camera_view_10.setText("")
        self.camera_view_name_5.setText(QCoreApplication.translate("Search_window", u"\uce74\uba54\ub77c5", None))
        self.camera_view_5.setText("")
        self.camera_view_name_2.setText(QCoreApplication.translate("Search_window", u"\uce74\uba54\ub77c2", None))
        self.camera_view_2.setText("")
        self.search_camera_next_page_bnt_2.setText("")
        self.page_undo_bnt.setText(QCoreApplication.translate("Search_window", u"\uc601\uc0c1 \ub044\uae30", None))
        self.search_viewer.setText("")
        self.par_total_result_count_label.setText(QCoreApplication.translate("Search_window", u"\ucd1d \uac80\uc0c9 \uacb0\uacfc  0 \uac74", None))
        self.camera_select_undo_bnt.setText(QCoreApplication.translate("Search_window", u"\ub4a4\ub85c\uac00\uae30", None))
        self.time_label_2.setText(QCoreApplication.translate("Search_window", u"\uc774\ubca4\ud2b8 \uc870\ud68c \uacb0\uacfc", None))
        self.event_search_bnt.setText(QCoreApplication.translate("Search_window", u"\uc774\ubca4\ud2b8 \uac80\uc0c9", None))
        self.time_label.setText(QCoreApplication.translate("Search_window", u"\ub0a0\uc9dc \ubc0f \uc2dc\uac04", None))
        self.time_day_start_input.setDisplayFormat(QCoreApplication.translate("Search_window", u"yyyy. M. d", None))
        self.time_hour_start_box.setItemText(0, QCoreApplication.translate("Search_window", u"00:00", None))
        self.time_hour_start_box.setItemText(1, QCoreApplication.translate("Search_window", u"01:00", None))
        self.time_hour_start_box.setItemText(2, QCoreApplication.translate("Search_window", u"02:00", None))
        self.time_hour_start_box.setItemText(3, QCoreApplication.translate("Search_window", u"03:00", None))
        self.time_hour_start_box.setItemText(4, QCoreApplication.translate("Search_window", u"04:00", None))
        self.time_hour_start_box.setItemText(5, QCoreApplication.translate("Search_window", u"05:00", None))
        self.time_hour_start_box.setItemText(6, QCoreApplication.translate("Search_window", u"06:00", None))
        self.time_hour_start_box.setItemText(7, QCoreApplication.translate("Search_window", u"07:00", None))
        self.time_hour_start_box.setItemText(8, QCoreApplication.translate("Search_window", u"08:00", None))
        self.time_hour_start_box.setItemText(9, QCoreApplication.translate("Search_window", u"09:00", None))
        self.time_hour_start_box.setItemText(10, QCoreApplication.translate("Search_window", u"10:00", None))
        self.time_hour_start_box.setItemText(11, QCoreApplication.translate("Search_window", u"11:00", None))
        self.time_hour_start_box.setItemText(12, QCoreApplication.translate("Search_window", u"12:00", None))
        self.time_hour_start_box.setItemText(13, QCoreApplication.translate("Search_window", u"13:00", None))
        self.time_hour_start_box.setItemText(14, QCoreApplication.translate("Search_window", u"14:00", None))
        self.time_hour_start_box.setItemText(15, QCoreApplication.translate("Search_window", u"15:00", None))
        self.time_hour_start_box.setItemText(16, QCoreApplication.translate("Search_window", u"16:00", None))
        self.time_hour_start_box.setItemText(17, QCoreApplication.translate("Search_window", u"17:00", None))
        self.time_hour_start_box.setItemText(18, QCoreApplication.translate("Search_window", u"18:00", None))
        self.time_hour_start_box.setItemText(19, QCoreApplication.translate("Search_window", u"19:00", None))
        self.time_hour_start_box.setItemText(20, QCoreApplication.translate("Search_window", u"20:00", None))
        self.time_hour_start_box.setItemText(21, QCoreApplication.translate("Search_window", u"21:00", None))
        self.time_hour_start_box.setItemText(22, QCoreApplication.translate("Search_window", u"22:00", None))
        self.time_hour_start_box.setItemText(23, QCoreApplication.translate("Search_window", u"23:00", None))

        self.time_tilde.setText(QCoreApplication.translate("Search_window", u"~", None))
        self.time_day_end_input.setDisplayFormat(QCoreApplication.translate("Search_window", u"yyyy. M. d", None))
        self.time_hour_end_box.setItemText(0, QCoreApplication.translate("Search_window", u"00:00", None))
        self.time_hour_end_box.setItemText(1, QCoreApplication.translate("Search_window", u"01:00", None))
        self.time_hour_end_box.setItemText(2, QCoreApplication.translate("Search_window", u"02:00", None))
        self.time_hour_end_box.setItemText(3, QCoreApplication.translate("Search_window", u"03:00", None))
        self.time_hour_end_box.setItemText(4, QCoreApplication.translate("Search_window", u"04:00", None))
        self.time_hour_end_box.setItemText(5, QCoreApplication.translate("Search_window", u"05:00", None))
        self.time_hour_end_box.setItemText(6, QCoreApplication.translate("Search_window", u"06:00", None))
        self.time_hour_end_box.setItemText(7, QCoreApplication.translate("Search_window", u"07:00", None))
        self.time_hour_end_box.setItemText(8, QCoreApplication.translate("Search_window", u"08:00", None))
        self.time_hour_end_box.setItemText(9, QCoreApplication.translate("Search_window", u"09:00", None))
        self.time_hour_end_box.setItemText(10, QCoreApplication.translate("Search_window", u"10:00", None))
        self.time_hour_end_box.setItemText(11, QCoreApplication.translate("Search_window", u"11:00", None))
        self.time_hour_end_box.setItemText(12, QCoreApplication.translate("Search_window", u"12:00", None))
        self.time_hour_end_box.setItemText(13, QCoreApplication.translate("Search_window", u"13:00", None))
        self.time_hour_end_box.setItemText(14, QCoreApplication.translate("Search_window", u"14:00", None))
        self.time_hour_end_box.setItemText(15, QCoreApplication.translate("Search_window", u"15:00", None))
        self.time_hour_end_box.setItemText(16, QCoreApplication.translate("Search_window", u"16:00", None))
        self.time_hour_end_box.setItemText(17, QCoreApplication.translate("Search_window", u"17:00", None))
        self.time_hour_end_box.setItemText(18, QCoreApplication.translate("Search_window", u"18:00", None))
        self.time_hour_end_box.setItemText(19, QCoreApplication.translate("Search_window", u"19:00", None))
        self.time_hour_end_box.setItemText(20, QCoreApplication.translate("Search_window", u"20:00", None))
        self.time_hour_end_box.setItemText(21, QCoreApplication.translate("Search_window", u"21:00", None))
        self.time_hour_end_box.setItemText(22, QCoreApplication.translate("Search_window", u"22:00", None))
        self.time_hour_end_box.setItemText(23, QCoreApplication.translate("Search_window", u"23:00", None))

        self.event_label.setText(QCoreApplication.translate("Search_window", u"\uc774\ubca4\ud2b8 \uc885\ub958", None))
        self.event_box.setItemText(0, QCoreApplication.translate("Search_window", u"\uc804\uccb4", None))

        self.sort_label.setText(QCoreApplication.translate("Search_window", u"\uac80\uc0c9 \uc815\ub82c", None))
        self.sort_box.setItemText(0, QCoreApplication.translate("Search_window", u"\ucd5c\uc2e0\uc21c", None))
        self.sort_box.setItemText(1, QCoreApplication.translate("Search_window", u"\uc2dc\uac04\uc21c", None))

        self.time_video_time_speed_label.setText(QCoreApplication.translate("Search_window", u"\uc601\uc0c1 \uc7ac\uc0dd \uc18d\ub3c4", None))
        self.search_bnt.setText(QCoreApplication.translate("Search_window", u"\uac80\uc0c9", None))
        ___qtablewidgetitem = self.event_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Search_window", u"\ubc88\ud638", None));
        ___qtablewidgetitem1 = self.event_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Search_window", u"\uce74\uba54\ub77c", None));
        ___qtablewidgetitem2 = self.event_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Search_window", u"\uc885\ub958", None));
        ___qtablewidgetitem3 = self.event_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Search_window", u"\uc2dc\uac04", None));
        pass
    # retranslateUi


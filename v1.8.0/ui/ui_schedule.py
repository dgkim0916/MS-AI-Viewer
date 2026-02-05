# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scheduleHJjbyq.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resourece_rc
import resourece_rc

class Ui_schedule_window(object):
    def setupUi(self, schedule_window):
        if not schedule_window.objectName():
            schedule_window.setObjectName(u"schedule_window")
        schedule_window.setWindowModality(Qt.WindowModality.ApplicationModal)
        schedule_window.resize(1252, 703)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(schedule_window.sizePolicy().hasHeightForWidth())
        schedule_window.setSizePolicy(sizePolicy)
        schedule_window.setMinimumSize(QSize(1252, 703))
        schedule_window.setMaximumSize(QSize(1252, 703))
        schedule_window.setStyleSheet(u"background-color: rgb(3, 3, 13);")
        self.horizontalLayout_2 = QHBoxLayout(schedule_window)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_3 = QWidget(schedule_window)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 9, 0, 9)
        self.top_logo_2 = QLabel(self.widget_2)
        self.top_logo_2.setObjectName(u"top_logo_2")
        self.top_logo_2.setMinimumSize(QSize(202, 32))
        self.top_logo_2.setMaximumSize(QSize(202, 32))
        font = QFont()
        font.setFamilies([u"Sans"])
        self.top_logo_2.setFont(font)
        self.top_logo_2.setPixmap(QPixmap(u":/ui/ui/images/logo.png"))
        self.top_logo_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.top_logo_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.widget_4)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy1)
        self.widget_11.setMinimumSize(QSize(60, 0))
        self.widget_11.setMaximumSize(QSize(60, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.widget_11)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)

        self.schedule_camera_undo_page_bnt = QPushButton(self.widget_11)
        self.schedule_camera_undo_page_bnt.setObjectName(u"schedule_camera_undo_page_bnt")
        self.schedule_camera_undo_page_bnt.setMinimumSize(QSize(60, 41))
        self.schedule_camera_undo_page_bnt.setMaximumSize(QSize(60, 41))
        font1 = QFont()
        font1.setPointSize(10)
        self.schedule_camera_undo_page_bnt.setFont(font1)
        self.schedule_camera_undo_page_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.schedule_camera_undo_page_bnt.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.schedule_camera_undo_page_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"Rotation: ( origin.x: 25; origin.y: 25; angle: 45);")
        icon = QIcon()
        icon.addFile(u":/ui/ui/images/ico_arrow_left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.schedule_camera_undo_page_bnt.setIcon(icon)
        self.schedule_camera_undo_page_bnt.setIconSize(QSize(31, 50))

        self.verticalLayout_7.addWidget(self.schedule_camera_undo_page_bnt)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_7.addItem(self.verticalSpacer_10)


        self.horizontalLayout_5.addWidget(self.widget_11)

        self.stackedWidget_5 = QStackedWidget(self.widget_4)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.horizontalLayout_10 = QHBoxLayout(self.page_11)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.widget_12 = QWidget(self.page_11)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_4 = QGridLayout(self.widget_12)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.search_camera_view_layout_65 = QVBoxLayout()
        self.search_camera_view_layout_65.setSpacing(0)
        self.search_camera_view_layout_65.setObjectName(u"search_camera_view_layout_65")
        self.camera_view_name_17 = QLabel(self.widget_12)
        self.camera_view_name_17.setObjectName(u"camera_view_name_17")
        sizePolicy.setHeightForWidth(self.camera_view_name_17.sizePolicy().hasHeightForWidth())
        self.camera_view_name_17.setSizePolicy(sizePolicy)
        self.camera_view_name_17.setMaximumSize(QSize(722, 20))
        font2 = QFont()
        font2.setFamilies([u"NanumSquareRound"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.camera_view_name_17.setFont(font2)
        self.camera_view_name_17.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_17.setMargin(0)
        self.camera_view_name_17.setIndent(15)

        self.search_camera_view_layout_65.addWidget(self.camera_view_name_17)

        self.camera_view_17 = QLabel(self.widget_12)
        self.camera_view_17.setObjectName(u"camera_view_17")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.camera_view_17.sizePolicy().hasHeightForWidth())
        self.camera_view_17.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"NanumBarunGothic"])
        font3.setPointSize(16)
        self.camera_view_17.setFont(font3)
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
        self.camera_view_name_18.setFont(font2)
        self.camera_view_name_18.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_18.setMargin(0)
        self.camera_view_name_18.setIndent(15)

        self.search_camera_view_layout_66.addWidget(self.camera_view_name_18)

        self.camera_view_18 = QLabel(self.widget_12)
        self.camera_view_18.setObjectName(u"camera_view_18")
        sizePolicy2.setHeightForWidth(self.camera_view_18.sizePolicy().hasHeightForWidth())
        self.camera_view_18.setSizePolicy(sizePolicy2)
        self.camera_view_18.setFont(font3)
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
        self.camera_view_name_19.setFont(font2)
        self.camera_view_name_19.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_19.setMargin(0)
        self.camera_view_name_19.setIndent(15)

        self.search_camera_view_layout_67.addWidget(self.camera_view_name_19)

        self.camera_view_19 = QLabel(self.widget_12)
        self.camera_view_19.setObjectName(u"camera_view_19")
        sizePolicy2.setHeightForWidth(self.camera_view_19.sizePolicy().hasHeightForWidth())
        self.camera_view_19.setSizePolicy(sizePolicy2)
        self.camera_view_19.setFont(font3)
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
        self.camera_view_name_20.setFont(font2)
        self.camera_view_name_20.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_20.setMargin(0)
        self.camera_view_name_20.setIndent(15)

        self.search_camera_view_layout_68.addWidget(self.camera_view_name_20)

        self.camera_view_20 = QLabel(self.widget_12)
        self.camera_view_20.setObjectName(u"camera_view_20")
        sizePolicy2.setHeightForWidth(self.camera_view_20.sizePolicy().hasHeightForWidth())
        self.camera_view_20.setSizePolicy(sizePolicy2)
        self.camera_view_20.setFont(font3)
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
        self.camera_view_name_21.setFont(font2)
        self.camera_view_name_21.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_21.setMargin(0)
        self.camera_view_name_21.setIndent(15)

        self.search_camera_view_layout_69.addWidget(self.camera_view_name_21)

        self.camera_view_21 = QLabel(self.widget_12)
        self.camera_view_21.setObjectName(u"camera_view_21")
        sizePolicy2.setHeightForWidth(self.camera_view_21.sizePolicy().hasHeightForWidth())
        self.camera_view_21.setSizePolicy(sizePolicy2)
        self.camera_view_21.setFont(font3)
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
        self.camera_view_name_22.setFont(font2)
        self.camera_view_name_22.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_22.setMargin(0)
        self.camera_view_name_22.setIndent(15)

        self.search_camera_view_layout_70.addWidget(self.camera_view_name_22)

        self.camera_view_22 = QLabel(self.widget_12)
        self.camera_view_22.setObjectName(u"camera_view_22")
        sizePolicy2.setHeightForWidth(self.camera_view_22.sizePolicy().hasHeightForWidth())
        self.camera_view_22.setSizePolicy(sizePolicy2)
        self.camera_view_22.setFont(font3)
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
        self.camera_view_name_23.setFont(font2)
        self.camera_view_name_23.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_23.setMargin(0)
        self.camera_view_name_23.setIndent(15)

        self.search_camera_view_layout_71.addWidget(self.camera_view_name_23)

        self.camera_view_23 = QLabel(self.widget_12)
        self.camera_view_23.setObjectName(u"camera_view_23")
        sizePolicy2.setHeightForWidth(self.camera_view_23.sizePolicy().hasHeightForWidth())
        self.camera_view_23.setSizePolicy(sizePolicy2)
        self.camera_view_23.setFont(font3)
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
        self.camera_view_name_24.setFont(font2)
        self.camera_view_name_24.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_24.setMargin(0)
        self.camera_view_name_24.setIndent(15)

        self.search_camera_view_layout_72.addWidget(self.camera_view_name_24)

        self.camera_view_24 = QLabel(self.widget_12)
        self.camera_view_24.setObjectName(u"camera_view_24")
        sizePolicy2.setHeightForWidth(self.camera_view_24.sizePolicy().hasHeightForWidth())
        self.camera_view_24.setSizePolicy(sizePolicy2)
        self.camera_view_24.setFont(font3)
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
        self.camera_view_name_25.setFont(font2)
        self.camera_view_name_25.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_25.setMargin(0)
        self.camera_view_name_25.setIndent(15)

        self.search_camera_view_layout_73.addWidget(self.camera_view_name_25)

        self.camera_view_25 = QLabel(self.widget_12)
        self.camera_view_25.setObjectName(u"camera_view_25")
        sizePolicy2.setHeightForWidth(self.camera_view_25.sizePolicy().hasHeightForWidth())
        self.camera_view_25.setSizePolicy(sizePolicy2)
        self.camera_view_25.setFont(font3)
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
        self.camera_view_name_26.setFont(font2)
        self.camera_view_name_26.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_26.setMargin(0)
        self.camera_view_name_26.setIndent(15)

        self.search_camera_view_layout_74.addWidget(self.camera_view_name_26)

        self.camera_view_26 = QLabel(self.widget_12)
        self.camera_view_26.setObjectName(u"camera_view_26")
        sizePolicy2.setHeightForWidth(self.camera_view_26.sizePolicy().hasHeightForWidth())
        self.camera_view_26.setSizePolicy(sizePolicy2)
        self.camera_view_26.setFont(font3)
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
        self.camera_view_name_27.setFont(font2)
        self.camera_view_name_27.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_27.setMargin(0)
        self.camera_view_name_27.setIndent(15)

        self.search_camera_view_layout_75.addWidget(self.camera_view_name_27)

        self.camera_view_27 = QLabel(self.widget_12)
        self.camera_view_27.setObjectName(u"camera_view_27")
        sizePolicy2.setHeightForWidth(self.camera_view_27.sizePolicy().hasHeightForWidth())
        self.camera_view_27.setSizePolicy(sizePolicy2)
        self.camera_view_27.setFont(font3)
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
        self.camera_view_name_28.setFont(font2)
        self.camera_view_name_28.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_28.setMargin(0)
        self.camera_view_name_28.setIndent(15)

        self.search_camera_view_layout_76.addWidget(self.camera_view_name_28)

        self.camera_view_28 = QLabel(self.widget_12)
        self.camera_view_28.setObjectName(u"camera_view_28")
        sizePolicy2.setHeightForWidth(self.camera_view_28.sizePolicy().hasHeightForWidth())
        self.camera_view_28.setSizePolicy(sizePolicy2)
        self.camera_view_28.setFont(font3)
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
        self.camera_view_name_29.setFont(font2)
        self.camera_view_name_29.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_29.setMargin(0)
        self.camera_view_name_29.setIndent(15)

        self.search_camera_view_layout_77.addWidget(self.camera_view_name_29)

        self.camera_view_29 = QLabel(self.widget_12)
        self.camera_view_29.setObjectName(u"camera_view_29")
        sizePolicy2.setHeightForWidth(self.camera_view_29.sizePolicy().hasHeightForWidth())
        self.camera_view_29.setSizePolicy(sizePolicy2)
        self.camera_view_29.setFont(font3)
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
        self.camera_view_name_30.setFont(font2)
        self.camera_view_name_30.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_30.setMargin(0)
        self.camera_view_name_30.setIndent(15)

        self.search_camera_view_layout_78.addWidget(self.camera_view_name_30)

        self.camera_view_30 = QLabel(self.widget_12)
        self.camera_view_30.setObjectName(u"camera_view_30")
        sizePolicy2.setHeightForWidth(self.camera_view_30.sizePolicy().hasHeightForWidth())
        self.camera_view_30.setSizePolicy(sizePolicy2)
        self.camera_view_30.setFont(font3)
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
        self.camera_view_name_31.setFont(font2)
        self.camera_view_name_31.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_31.setMargin(0)
        self.camera_view_name_31.setIndent(15)

        self.search_camera_view_layout_79.addWidget(self.camera_view_name_31)

        self.camera_view_31 = QLabel(self.widget_12)
        self.camera_view_31.setObjectName(u"camera_view_31")
        sizePolicy2.setHeightForWidth(self.camera_view_31.sizePolicy().hasHeightForWidth())
        self.camera_view_31.setSizePolicy(sizePolicy2)
        self.camera_view_31.setFont(font3)
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
        self.camera_view_name_32.setFont(font2)
        self.camera_view_name_32.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_32.setMargin(0)
        self.camera_view_name_32.setIndent(15)

        self.search_camera_view_layout_80.addWidget(self.camera_view_name_32)

        self.camera_view_32 = QLabel(self.widget_12)
        self.camera_view_32.setObjectName(u"camera_view_32")
        sizePolicy2.setHeightForWidth(self.camera_view_32.sizePolicy().hasHeightForWidth())
        self.camera_view_32.setSizePolicy(sizePolicy2)
        self.camera_view_32.setFont(font3)
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
        sizePolicy1.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy1)
        self.widget_13.setMinimumSize(QSize(60, 0))
        self.widget_13.setMaximumSize(QSize(60, 16777215))
        self.verticalLayout_9 = QVBoxLayout(self.widget_13)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_9.addItem(self.verticalSpacer_11)

        self.schedule_camera_next_page_bnt = QPushButton(self.widget_13)
        self.schedule_camera_next_page_bnt.setObjectName(u"schedule_camera_next_page_bnt")
        self.schedule_camera_next_page_bnt.setMinimumSize(QSize(60, 41))
        self.schedule_camera_next_page_bnt.setMaximumSize(QSize(60, 41))
        self.schedule_camera_next_page_bnt.setFont(font1)
        self.schedule_camera_next_page_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.schedule_camera_next_page_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/ui/ui/images/ico_arrow_right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.schedule_camera_next_page_bnt.setIcon(icon1)
        self.schedule_camera_next_page_bnt.setIconSize(QSize(31, 50))

        self.verticalLayout_9.addWidget(self.schedule_camera_next_page_bnt)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_9.addItem(self.verticalSpacer_12)


        self.horizontalLayout_5.addWidget(self.widget_13)


        self.verticalLayout.addWidget(self.widget_4)


        self.horizontalLayout_2.addWidget(self.widget_3)

        self.widget = QWidget(schedule_window)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(383, 709))
        self.verticalLayout_21 = QVBoxLayout(self.widget)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.event_label = QLabel(self.widget)
        self.event_label.setObjectName(u"event_label")
        self.event_label.setMaximumSize(QSize(52, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Sans"])
        font4.setPointSize(12)
        self.event_label.setFont(font4)
        self.event_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(191, 64, 64, 0);")
        self.event_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.event_label)

        self.event_box = QComboBox(self.widget)
        self.event_box.addItem("")
        self.event_box.addItem("")
        self.event_box.addItem("")
        self.event_box.addItem("")
        self.event_box.addItem("")
        self.event_box.setObjectName(u"event_box")
        font5 = QFont()
        font5.setFamilies([u"Sans"])
        font5.setPointSize(10)
        font5.setBold(False)
        self.event_box.setFont(font5)
        self.event_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.event_box.setMinimumContentsLength(0)

        self.horizontalLayout_6.addWidget(self.event_box)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.schedule_all_remove_bnt = QPushButton(self.widget)
        self.schedule_all_remove_bnt.setObjectName(u"schedule_all_remove_bnt")
        self.schedule_all_remove_bnt.setMinimumSize(QSize(61, 31))
        self.schedule_all_remove_bnt.setMaximumSize(QSize(61, 31))
        font6 = QFont()
        font6.setFamilies([u"Sans"])
        font6.setPointSize(10)
        self.schedule_all_remove_bnt.setFont(font6)
        self.schedule_all_remove_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.schedule_all_remove_bnt.setStyleSheet(u"background-color: rgb(36, 39, 44);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.schedule_all_remove_bnt)

        self.schedule_apply_bnt = QPushButton(self.widget)
        self.schedule_apply_bnt.setObjectName(u"schedule_apply_bnt")
        self.schedule_apply_bnt.setMinimumSize(QSize(61, 31))
        self.schedule_apply_bnt.setMaximumSize(QSize(61, 31))
        self.schedule_apply_bnt.setFont(font6)
        self.schedule_apply_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.schedule_apply_bnt.setStyleSheet(u"background-color: rgb(30, 195, 55);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.schedule_apply_bnt)

        self.schedule_close_bnt = QPushButton(self.widget)
        self.schedule_close_bnt.setObjectName(u"schedule_close_bnt")
        self.schedule_close_bnt.setMinimumSize(QSize(61, 31))
        self.schedule_close_bnt.setMaximumSize(QSize(61, 31))
        self.schedule_close_bnt.setFont(font6)
        self.schedule_close_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.schedule_close_bnt.setStyleSheet(u"background-color: rgb(237, 51, 59);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.schedule_close_bnt)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)


        self.verticalLayout_22.addLayout(self.horizontalLayout_8)

        self.detect_time_table_widget = QWidget(self.widget)
        self.detect_time_table_widget.setObjectName(u"detect_time_table_widget")
        sizePolicy2.setHeightForWidth(self.detect_time_table_widget.sizePolicy().hasHeightForWidth())
        self.detect_time_table_widget.setSizePolicy(sizePolicy2)
        self.detect_time_table_widget.setMinimumSize(QSize(365, 622))
        self.detect_time_table_widget.setMaximumSize(QSize(365, 622))
        self.detect_time_table_widget.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(32,39,49);\n"
"border-radius: 10px;\n"
"\n"
"\n"
"")
        self.horizontalLayout_9 = QHBoxLayout(self.detect_time_table_widget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.schedule_time_table = QTableWidget(self.detect_time_table_widget)
        if (self.schedule_time_table.columnCount() < 7):
            self.schedule_time_table.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.schedule_time_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.schedule_time_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.schedule_time_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.schedule_time_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.schedule_time_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.schedule_time_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.schedule_time_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.schedule_time_table.rowCount() < 24):
            self.schedule_time_table.setRowCount(24)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(8, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(9, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(10, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(11, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(12, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(13, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(14, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(15, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(16, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(17, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(18, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(19, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(20, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(21, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(22, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        self.schedule_time_table.setVerticalHeaderItem(23, __qtablewidgetitem30)
        self.schedule_time_table.setObjectName(u"schedule_time_table")
        self.schedule_time_table.setMinimumSize(QSize(0, 575))
        self.schedule_time_table.setMaximumSize(QSize(9999, 9999))
        self.schedule_time_table.setFont(font)
        self.schedule_time_table.setStyleSheet(u"QTableView {\n"
"\n"
"gridline-color: rgb(119, 118, 123);\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: rgb(209, 209, 209); /* \ud5e4\ub354 \ud14d\uc2a4\ud2b8 \uc0c9\uc0c1 - \ud68c\uc0c9 */\n"
"	background-color: rgb(44, 51, 60); \n"
"\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"        background-color:  rgba(30, 195, 55, 40); /* \ub4dc\ub798\uadf8 \uc2dc \uc120\ud0dd\ub41c \uc140\uc758 \ubc30\uacbd\uc0c9 */\n"
"		border: 1px solid rgba(209, 209, 209, 30);\n"
"        color: white; /* \uc120\ud0dd\ub41c \uc140\uc758 \uae00\uc790 \uc0c9 */\n"
"    }\n"
"    QTableWidget::item:hover {\n"
"        background-color: rgba(209, 209, 209, 30);; /* \ub4dc\ub798\uadf8\ud560 \ub54c \ub9c8\uc6b0\uc2a4\uac00 \uc704\uce58\ud55c \uc140\uc758 \ubc30\uacbd\uc0c9 */\n"
"    }")
        self.schedule_time_table.setProperty(u"showDropIndicator", True)
        self.schedule_time_table.setDragEnabled(False)
        self.schedule_time_table.setDragDropOverwriteMode(True)
        self.schedule_time_table.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.schedule_time_table.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.schedule_time_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.schedule_time_table.setGridStyle(Qt.PenStyle.SolidLine)
        self.schedule_time_table.setSortingEnabled(False)
        self.schedule_time_table.setRowCount(24)
        self.schedule_time_table.horizontalHeader().setCascadingSectionResizes(False)
        self.schedule_time_table.horizontalHeader().setMinimumSectionSize(3)
        self.schedule_time_table.horizontalHeader().setDefaultSectionSize(46)
        self.schedule_time_table.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.schedule_time_table.horizontalHeader().setStretchLastSection(False)
        self.schedule_time_table.verticalHeader().setVisible(True)
        self.schedule_time_table.verticalHeader().setCascadingSectionResizes(False)
        self.schedule_time_table.verticalHeader().setMinimumSectionSize(18)
        self.schedule_time_table.verticalHeader().setDefaultSectionSize(24)
        self.schedule_time_table.verticalHeader().setProperty(u"showSortIndicator", False)
        self.schedule_time_table.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_9.addWidget(self.schedule_time_table)


        self.verticalLayout_22.addWidget(self.detect_time_table_widget)


        self.verticalLayout_21.addLayout(self.verticalLayout_22)


        self.horizontalLayout_2.addWidget(self.widget)


        self.retranslateUi(schedule_window)

        self.stackedWidget_5.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(schedule_window)
    # setupUi

    def retranslateUi(self, schedule_window):
        schedule_window.setWindowTitle(QCoreApplication.translate("schedule_window", u"camera schedule", None))
        self.top_logo_2.setText("")
        self.schedule_camera_undo_page_bnt.setText("")
        self.camera_view_name_17.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c14", None))
        self.camera_view_17.setText("")
        self.camera_view_name_18.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c13", None))
        self.camera_view_18.setText("")
        self.camera_view_name_19.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c1", None))
        self.camera_view_19.setText("")
        self.camera_view_name_20.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c7", None))
        self.camera_view_20.setText("")
        self.camera_view_name_21.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c4", None))
        self.camera_view_21.setText("")
        self.camera_view_name_22.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c15", None))
        self.camera_view_22.setText("")
        self.camera_view_name_23.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c9", None))
        self.camera_view_23.setText("")
        self.camera_view_name_24.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c11", None))
        self.camera_view_24.setText("")
        self.camera_view_name_25.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c16", None))
        self.camera_view_25.setText("")
        self.camera_view_name_26.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c8", None))
        self.camera_view_26.setText("")
        self.camera_view_name_27.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c12", None))
        self.camera_view_27.setText("")
        self.camera_view_name_28.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c3", None))
        self.camera_view_28.setText("")
        self.camera_view_name_29.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c6", None))
        self.camera_view_29.setText("")
        self.camera_view_name_30.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c10", None))
        self.camera_view_30.setText("")
        self.camera_view_name_31.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c5", None))
        self.camera_view_31.setText("")
        self.camera_view_name_32.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c2", None))
        self.camera_view_32.setText("")
        self.schedule_camera_next_page_bnt.setText("")
        self.event_label.setText(QCoreApplication.translate("schedule_window", u"\uc774\ubca4\ud2b8", None))
        self.event_box.setItemText(0, QCoreApplication.translate("schedule_window", u"\uce68\uc785", None))
        self.event_box.setItemText(1, QCoreApplication.translate("schedule_window", u"\ubc30\ud68c", None))
        self.event_box.setItemText(2, QCoreApplication.translate("schedule_window", u"\uc4f0\ub7ec\uc9d0", None))
        self.event_box.setItemText(3, QCoreApplication.translate("schedule_window", u"\uc2f8\uc6c0", None))
        self.event_box.setItemText(4, QCoreApplication.translate("schedule_window", u"\ubc29\ud654", None))

        self.schedule_all_remove_bnt.setText(QCoreApplication.translate("schedule_window", u"\uc804\uccb4 \uc0ad\uc81c", None))
        self.schedule_apply_bnt.setText(QCoreApplication.translate("schedule_window", u"\uc800\uc7a5", None))
        self.schedule_close_bnt.setText(QCoreApplication.translate("schedule_window", u"\ub2eb\uae30", None))
        ___qtablewidgetitem = self.schedule_time_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("schedule_window", u"\uc77c", None));
        ___qtablewidgetitem1 = self.schedule_time_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("schedule_window", u"\uc6d4", None));
        ___qtablewidgetitem2 = self.schedule_time_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("schedule_window", u"\ud654", None));
        ___qtablewidgetitem3 = self.schedule_time_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("schedule_window", u"\uc218", None));
        ___qtablewidgetitem4 = self.schedule_time_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("schedule_window", u"\ubaa9", None));
        ___qtablewidgetitem5 = self.schedule_time_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("schedule_window", u"\uae08", None));
        ___qtablewidgetitem6 = self.schedule_time_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("schedule_window", u"\ud1a0", None));
        ___qtablewidgetitem7 = self.schedule_time_table.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("schedule_window", u"0", None));
        ___qtablewidgetitem8 = self.schedule_time_table.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("schedule_window", u"1", None));
        ___qtablewidgetitem9 = self.schedule_time_table.verticalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("schedule_window", u"2", None));
        ___qtablewidgetitem10 = self.schedule_time_table.verticalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("schedule_window", u"3", None));
        ___qtablewidgetitem11 = self.schedule_time_table.verticalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("schedule_window", u"4", None));
        ___qtablewidgetitem12 = self.schedule_time_table.verticalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("schedule_window", u"5", None));
        ___qtablewidgetitem13 = self.schedule_time_table.verticalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("schedule_window", u"6", None));
        ___qtablewidgetitem14 = self.schedule_time_table.verticalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("schedule_window", u"7", None));
        ___qtablewidgetitem15 = self.schedule_time_table.verticalHeaderItem(8)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("schedule_window", u"8", None));
        ___qtablewidgetitem16 = self.schedule_time_table.verticalHeaderItem(9)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("schedule_window", u"9", None));
        ___qtablewidgetitem17 = self.schedule_time_table.verticalHeaderItem(10)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("schedule_window", u"10", None));
        ___qtablewidgetitem18 = self.schedule_time_table.verticalHeaderItem(11)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("schedule_window", u"11", None));
        ___qtablewidgetitem19 = self.schedule_time_table.verticalHeaderItem(12)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("schedule_window", u"12", None));
        ___qtablewidgetitem20 = self.schedule_time_table.verticalHeaderItem(13)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("schedule_window", u"13", None));
        ___qtablewidgetitem21 = self.schedule_time_table.verticalHeaderItem(14)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("schedule_window", u"14", None));
        ___qtablewidgetitem22 = self.schedule_time_table.verticalHeaderItem(15)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("schedule_window", u"15", None));
        ___qtablewidgetitem23 = self.schedule_time_table.verticalHeaderItem(16)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("schedule_window", u"16", None));
        ___qtablewidgetitem24 = self.schedule_time_table.verticalHeaderItem(17)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("schedule_window", u"17", None));
        ___qtablewidgetitem25 = self.schedule_time_table.verticalHeaderItem(18)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("schedule_window", u"18", None));
        ___qtablewidgetitem26 = self.schedule_time_table.verticalHeaderItem(19)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("schedule_window", u"19", None));
        ___qtablewidgetitem27 = self.schedule_time_table.verticalHeaderItem(20)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("schedule_window", u"20", None));
        ___qtablewidgetitem28 = self.schedule_time_table.verticalHeaderItem(21)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("schedule_window", u"21", None));
        ___qtablewidgetitem29 = self.schedule_time_table.verticalHeaderItem(22)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("schedule_window", u"22", None));
        ___qtablewidgetitem30 = self.schedule_time_table.verticalHeaderItem(23)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("schedule_window", u"23", None));
    # retranslateUi


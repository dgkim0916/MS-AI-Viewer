# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ai_labelingcOVYcF.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resourece_rc

class Ui_labeling_window(object):
    def setupUi(self, labeling_window):
        if not labeling_window.objectName():
            labeling_window.setObjectName(u"labeling_window")
        labeling_window.setWindowModality(Qt.WindowModality.ApplicationModal)
        labeling_window.resize(1075, 719)
        labeling_window.setMaximumSize(QSize(1260, 16777215))
        labeling_window.setWindowTitle(u"Labeling")
        labeling_window.setStyleSheet(u"background-color: rgb(3, 3, 13);")
        self.verticalLayout_6 = QVBoxLayout(labeling_window)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.top_logo = QLabel(labeling_window)
        self.top_logo.setObjectName(u"top_logo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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

        self.self_labeling_bnt = QPushButton(labeling_window)
        self.self_labeling_bnt.setObjectName(u"self_labeling_bnt")
        self.self_labeling_bnt.setMinimumSize(QSize(115, 31))
        self.self_labeling_bnt.setMaximumSize(QSize(9999, 31))
        font1 = QFont()
        font1.setFamilies([u"NanumSquareRound"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.self_labeling_bnt.setFont(font1)
        self.self_labeling_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.self_labeling_bnt.setStyleSheet(u"\n"
"background-color: rgb(36, 39, 44);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.self_labeling_bnt)

        self.train_bnt = QPushButton(labeling_window)
        self.train_bnt.setObjectName(u"train_bnt")
        self.train_bnt.setMinimumSize(QSize(80, 31))
        self.train_bnt.setMaximumSize(QSize(80, 31))
        self.train_bnt.setFont(font1)
        self.train_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.train_bnt.setStyleSheet(u"\n"
"background-color: rgb(36, 39, 44);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.train_bnt)

        self.shutdown_bnt = QPushButton(labeling_window)
        self.shutdown_bnt.setObjectName(u"shutdown_bnt")
        self.shutdown_bnt.setMinimumSize(QSize(61, 31))
        self.shutdown_bnt.setMaximumSize(QSize(61, 31))
        font2 = QFont()
        font2.setFamilies([u"NanumSquareRound"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.shutdown_bnt.setFont(font2)
        self.shutdown_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.shutdown_bnt.setStyleSheet(u"background-color: rgb(237, 51, 59);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")

        self.horizontalLayout_6.addWidget(self.shutdown_bnt)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_2 = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_info_widget = QWidget(labeling_window)
        self.label_info_widget.setObjectName(u"label_info_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_info_widget.sizePolicy().hasHeightForWidth())
        self.label_info_widget.setSizePolicy(sizePolicy1)
        self.label_info_widget.setMinimumSize(QSize(251, 510))
        self.label_info_widget.setMaximumSize(QSize(251, 9999))
        self.verticalLayout_2 = QVBoxLayout(self.label_info_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.camera_name_label = QLabel(self.label_info_widget)
        self.camera_name_label.setObjectName(u"camera_name_label")
        sizePolicy.setHeightForWidth(self.camera_name_label.sizePolicy().hasHeightForWidth())
        self.camera_name_label.setSizePolicy(sizePolicy)
        self.camera_name_label.setMinimumSize(QSize(84, 29))
        font3 = QFont()
        font3.setFamilies([u"Sans"])
        font3.setPointSize(11)
        font3.setBold(False)
        self.camera_name_label.setFont(font3)
        self.camera_name_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.camera_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.camera_name_label)

        self.camera_name_box = QComboBox(self.label_info_widget)
        self.camera_name_box.setObjectName(u"camera_name_box")
        self.camera_name_box.setMinimumSize(QSize(110, 39))
        self.camera_name_box.setMaximumSize(QSize(145, 39))
        font4 = QFont()
        font4.setFamilies([u"Sans"])
        font4.setPointSize(11)
        self.camera_name_box.setFont(font4)
        self.camera_name_box.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.camera_name_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.camera_name_box.setCurrentText(u"")

        self.horizontalLayout.addWidget(self.camera_name_box)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.event_date_label = QLabel(self.label_info_widget)
        self.event_date_label.setObjectName(u"event_date_label")
        sizePolicy.setHeightForWidth(self.event_date_label.sizePolicy().hasHeightForWidth())
        self.event_date_label.setSizePolicy(sizePolicy)
        self.event_date_label.setMinimumSize(QSize(84, 31))
        font5 = QFont()
        font5.setFamilies([u"Sans"])
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setKerning(True)
        self.event_date_label.setFont(font5)
        self.event_date_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.event_date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.event_date_label)

        self.event_date_box = QComboBox(self.label_info_widget)
        self.event_date_box.setObjectName(u"event_date_box")
        self.event_date_box.setMinimumSize(QSize(120, 39))
        self.event_date_box.setMaximumSize(QSize(120, 39))
        self.event_date_box.setFont(font4)
        self.event_date_box.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.event_date_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.event_date_box.setCurrentText(u"")

        self.horizontalLayout_3.addWidget(self.event_date_box)

        self.label_refresh_bnt = QPushButton(self.label_info_widget)
        self.label_refresh_bnt.setObjectName(u"label_refresh_bnt")
        self.label_refresh_bnt.setMinimumSize(QSize(28, 30))
        self.label_refresh_bnt.setMaximumSize(QSize(37, 52))
        font6 = QFont()
        font6.setFamilies([u"Sans"])
        font6.setPointSize(10)
        self.label_refresh_bnt.setFont(font6)
        self.label_refresh_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_refresh_bnt.setStyleSheet(u"background-color: rgb(20, 20, 20);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(20, 20, 20);")
        icon = QIcon()
        icon.addFile(u":/ui/ui/images/ico_refresh.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.label_refresh_bnt.setIcon(icon)
        self.label_refresh_bnt.setIconSize(QSize(31, 50))

        self.horizontalLayout_3.addWidget(self.label_refresh_bnt)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_list_table = QTableWidget(self.label_info_widget)
        if (self.label_list_table.columnCount() < 1):
            self.label_list_table.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.label_list_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.label_list_table.rowCount() < 10):
            self.label_list_table.setRowCount(10)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.label_list_table.setVerticalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.label_list_table.setVerticalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.label_list_table.setVerticalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.label_list_table.setVerticalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.label_list_table.setVerticalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.label_list_table.setVerticalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.label_list_table.setVerticalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.label_list_table.setVerticalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.label_list_table.setVerticalHeaderItem(9, __qtablewidgetitem9)
        self.label_list_table.setObjectName(u"label_list_table")
        self.label_list_table.setMinimumSize(QSize(181, 1))
        self.label_list_table.setMaximumSize(QSize(401, 16777215))
        font7 = QFont()
        font7.setFamilies([u"Sans"])
        font7.setPointSize(10)
        font7.setBold(False)
        self.label_list_table.setFont(font7)
        self.label_list_table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.label_list_table.setStyleSheet(u"QTableWidget {\n"
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
"}\n"
"")
        self.label_list_table.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.label_list_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.label_list_table.setTabKeyNavigation(False)
        self.label_list_table.setDragEnabled(False)
        self.label_list_table.setDragDropOverwriteMode(False)
        self.label_list_table.setSelectionMode(QAbstractItemView.SelectionMode.ContiguousSelection)
        self.label_list_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.label_list_table.setShowGrid(False)
        self.label_list_table.setGridStyle(Qt.PenStyle.NoPen)
        self.label_list_table.setWordWrap(False)
        self.label_list_table.setCornerButtonEnabled(False)
        self.label_list_table.horizontalHeader().setCascadingSectionResizes(False)
        self.label_list_table.horizontalHeader().setMinimumSectionSize(5)
        self.label_list_table.horizontalHeader().setDefaultSectionSize(18)
        self.label_list_table.horizontalHeader().setHighlightSections(False)
        self.label_list_table.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.label_list_table.horizontalHeader().setStretchLastSection(True)
        self.label_list_table.verticalHeader().setVisible(False)
        self.label_list_table.verticalHeader().setCascadingSectionResizes(False)
        self.label_list_table.verticalHeader().setHighlightSections(False)
        self.label_list_table.verticalHeader().setProperty(u"showSortIndicator", False)
        self.label_list_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.label_list_table)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addWidget(self.label_info_widget)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_class_widget = QWidget(labeling_window)
        self.label_class_widget.setObjectName(u"label_class_widget")
        self.label_class_widget.setMinimumSize(QSize(0, 48))
        self.label_class_widget.setMaximumSize(QSize(979, 48))
        self.verticalLayout_5 = QVBoxLayout(self.label_class_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.cls_1 = QPushButton(self.label_class_widget)
        self.cls_1.setObjectName(u"cls_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cls_1.sizePolicy().hasHeightForWidth())
        self.cls_1.setSizePolicy(sizePolicy2)
        self.cls_1.setMinimumSize(QSize(55, 25))
        self.cls_1.setMaximumSize(QSize(55, 25))
        self.cls_1.setFont(font6)
        self.cls_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cls_1.setStyleSheet(u"background-color: rgb(36, 39, 44);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 9px;\n"
"border: 1px solid rgba(255, 255, 255, 100);\n"
"")

        self.horizontalLayout_7.addWidget(self.cls_1)

        self.horizontalSpacer_2 = QSpacerItem(562, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.label_del_bnt = QPushButton(self.label_class_widget)
        self.label_del_bnt.setObjectName(u"label_del_bnt")
        sizePolicy2.setHeightForWidth(self.label_del_bnt.sizePolicy().hasHeightForWidth())
        self.label_del_bnt.setSizePolicy(sizePolicy2)
        self.label_del_bnt.setMinimumSize(QSize(102, 25))
        self.label_del_bnt.setMaximumSize(QSize(9999, 25))
        self.label_del_bnt.setFont(font6)
        self.label_del_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_del_bnt.setStyleSheet(u"border-radius: 9px;\n"
"background-color: rgb(255, 49, 38);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.label_del_bnt)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)


        self.verticalLayout_3.addWidget(self.label_class_widget)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_4 = QSpacerItem(368, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.img_cur_num = QLabel(labeling_window)
        self.img_cur_num.setObjectName(u"img_cur_num")
        self.img_cur_num.setMaximumSize(QSize(20, 17))
        self.img_cur_num.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.img_cur_num.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.img_cur_num)

        self.img_counter_bar = QLabel(labeling_window)
        self.img_counter_bar.setObjectName(u"img_counter_bar")
        self.img_counter_bar.setMaximumSize(QSize(20, 17))
        self.img_counter_bar.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.img_counter_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.img_counter_bar)

        self.img_total_num = QLabel(labeling_window)
        self.img_total_num.setObjectName(u"img_total_num")
        self.img_total_num.setMaximumSize(QSize(20, 17))
        self.img_total_num.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.img_total_num.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.img_total_num)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_13)

        self.horizontalSpacer_5 = QSpacerItem(368, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.label_image_viewer = QLabel(labeling_window)
        self.label_image_viewer.setObjectName(u"label_image_viewer")
        sizePolicy2.setHeightForWidth(self.label_image_viewer.sizePolicy().hasHeightForWidth())
        self.label_image_viewer.setSizePolicy(sizePolicy2)
        self.label_image_viewer.setMinimumSize(QSize(640, 460))
        self.label_image_viewer.setMaximumSize(QSize(9999, 9999))
        self.label_image_viewer.setFont(font)
        self.label_image_viewer.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"border-radius: 10px ;")
        self.label_image_viewer.setPixmap(QPixmap(u":/ui/ui/images/logo.png"))
        self.label_image_viewer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_image_viewer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(940, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_save_bnt = QPushButton(labeling_window)
        self.label_save_bnt.setObjectName(u"label_save_bnt")
        sizePolicy.setHeightForWidth(self.label_save_bnt.sizePolicy().hasHeightForWidth())
        self.label_save_bnt.setSizePolicy(sizePolicy)
        self.label_save_bnt.setMinimumSize(QSize(76, 39))
        self.label_save_bnt.setMaximumSize(QSize(76, 39))
        self.label_save_bnt.setFont(font6)
        self.label_save_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_save_bnt.setStyleSheet(u"background-color: rgb(30, 195, 55);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 19px;\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.label_save_bnt)

        self.label_data_del_bnt = QPushButton(labeling_window)
        self.label_data_del_bnt.setObjectName(u"label_data_del_bnt")
        sizePolicy.setHeightForWidth(self.label_data_del_bnt.sizePolicy().hasHeightForWidth())
        self.label_data_del_bnt.setSizePolicy(sizePolicy)
        self.label_data_del_bnt.setMinimumSize(QSize(76, 39))
        self.label_data_del_bnt.setMaximumSize(QSize(76, 39))
        self.label_data_del_bnt.setFont(font6)
        self.label_data_del_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_data_del_bnt.setStyleSheet(u"background-color: rgb(255, 49, 38);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 19px;\n"
"")

        self.horizontalLayout_4.addWidget(self.label_data_del_bnt)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.retranslateUi(labeling_window)

        QMetaObject.connectSlotsByName(labeling_window)
    # setupUi

    def retranslateUi(self, labeling_window):
        self.top_logo.setText("")
        self.self_labeling_bnt.setText(QCoreApplication.translate("labeling_window", u"\uc790\ub3d9 \ub77c\ubca8\ub9c1 \uc2dc\uc791", None))
        self.train_bnt.setText(QCoreApplication.translate("labeling_window", u"\ud559\uc2b5 \uc2dc\uc791", None))
        self.shutdown_bnt.setText(QCoreApplication.translate("labeling_window", u"\ub2eb\uae30", None))
        self.camera_name_label.setText(QCoreApplication.translate("labeling_window", u"\uce74\uba54\ub77c \ubc88\ud638", None))
        self.event_date_label.setText(QCoreApplication.translate("labeling_window", u"\uc774\ubca4\ud2b8 \ub0a0\uc9dc", None))
        self.label_refresh_bnt.setText("")
        ___qtablewidgetitem = self.label_list_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("labeling_window", u"\uc774\ubca4\ud2b8 \ubaa9\ub85d", None));
        ___qtablewidgetitem1 = self.label_list_table.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("labeling_window", u"New Row", None));
        ___qtablewidgetitem2 = self.label_list_table.verticalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("labeling_window", u"2 ", None));
        ___qtablewidgetitem3 = self.label_list_table.verticalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("labeling_window", u"New Row", None));
        ___qtablewidgetitem4 = self.label_list_table.verticalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("labeling_window", u"New Row", None));
        ___qtablewidgetitem5 = self.label_list_table.verticalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("labeling_window", u"New Row", None));
        ___qtablewidgetitem6 = self.label_list_table.verticalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("labeling_window", u"New Row", None));
        ___qtablewidgetitem7 = self.label_list_table.verticalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("labeling_window", u"New Row", None));
        ___qtablewidgetitem8 = self.label_list_table.verticalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("labeling_window", u"New Row", None));
        ___qtablewidgetitem9 = self.label_list_table.verticalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("labeling_window", u"New Row", None));
        self.cls_1.setText(QCoreApplication.translate("labeling_window", u"\uc0ac\ub78c1", None))
        self.label_del_bnt.setText(QCoreApplication.translate("labeling_window", u"\ub77c\ubca8 \ubaa8\ub450 \uc0ad\uc81c", None))
        self.img_cur_num.setText(QCoreApplication.translate("labeling_window", u"0", None))
        self.img_counter_bar.setText(QCoreApplication.translate("labeling_window", u"/", None))
        self.img_total_num.setText(QCoreApplication.translate("labeling_window", u"0", None))
        self.label_image_viewer.setText("")
        self.label_save_bnt.setText(QCoreApplication.translate("labeling_window", u"\uc800\uc7a5", None))
        self.label_data_del_bnt.setText(QCoreApplication.translate("labeling_window", u"\uc0ad\uc81c", None))
        pass
    # retranslateUi


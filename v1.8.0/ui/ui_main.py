# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainnoHMFr.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)
import resourece_rc
import resourece_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(1551, 875)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(3840, 2160))
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        icon = QIcon()
        icon.addFile(u":/ui/ui/images/icon2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(9, 9, 9);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_58 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.top_logo = QLabel(self.centralwidget)
        self.top_logo.setObjectName(u"top_logo")
        self.top_logo.setMinimumSize(QSize(240, 38))
        self.top_logo.setMaximumSize(QSize(240, 38))
        font = QFont()
        font.setFamilies([u"Sans"])
        self.top_logo.setFont(font)
        self.top_logo.setPixmap(QPixmap(u":/ui/ui/images/logo.png"))
        self.top_logo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.top_logo)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verson_label = QLabel(self.centralwidget)
        self.verson_label.setObjectName(u"verson_label")
        self.verson_label.setMaximumSize(QSize(16777215, 21))
        font1 = QFont()
        font1.setFamilies([u"Sans"])
        font1.setPointSize(10)
        self.verson_label.setFont(font1)
        self.verson_label.setStyleSheet(u"color: rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.verson_label)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.server_icon = QLabel(self.centralwidget)
        self.server_icon.setObjectName(u"server_icon")
        self.server_icon.setMaximumSize(QSize(23, 23))
        self.server_icon.setFont(font)
        self.server_icon.setPixmap(QPixmap(u":/newPrefix/images/ico_server.svg"))
        self.server_icon.setScaledContents(True)

        self.horizontalLayout.addWidget(self.server_icon)

        self.horizontalSpacer_2 = QSpacerItem(37, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.shutdown_bnt = QPushButton(self.centralwidget)
        self.shutdown_bnt.setObjectName(u"shutdown_bnt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.shutdown_bnt.sizePolicy().hasHeightForWidth())
        self.shutdown_bnt.setSizePolicy(sizePolicy1)
        self.shutdown_bnt.setMinimumSize(QSize(76, 39))
        self.shutdown_bnt.setMaximumSize(QSize(76, 39))
        self.shutdown_bnt.setFont(font1)
        self.shutdown_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.shutdown_bnt.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.05 rgba(46, 49, 54, 255),\n"
"    stop:0.30 rgba(37, 40, 44, 255)\n"
");\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 19px;\n"
"")

        self.horizontalLayout.addWidget(self.shutdown_bnt)


        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_25 = QVBoxLayout(self.page)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(410, 720))
        self.widget.setMaximumSize(QSize(410, 16777215))
        self.widget.setStyleSheet(u"background-color: rgb(16, 16, 16);")
        self.verticalLayout_10 = QVBoxLayout(self.widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(222, 221, 218);")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.nvr_add_bnt = QPushButton(self.widget_4)
        self.nvr_add_bnt.setObjectName(u"nvr_add_bnt")
        self.nvr_add_bnt.setMinimumSize(QSize(35, 35))
        self.nvr_add_bnt.setMaximumSize(QSize(35, 35))
        self.nvr_add_bnt.setFont(font1)
        self.nvr_add_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nvr_add_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/ui/ui/images/ico_add_circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.nvr_add_bnt.setIcon(icon1)
        self.nvr_add_bnt.setIconSize(QSize(31, 50))

        self.verticalLayout_3.addWidget(self.nvr_add_bnt)

        self.nvr_del_bnt = QPushButton(self.widget_4)
        self.nvr_del_bnt.setObjectName(u"nvr_del_bnt")
        self.nvr_del_bnt.setMinimumSize(QSize(35, 35))
        self.nvr_del_bnt.setMaximumSize(QSize(35, 35))
        self.nvr_del_bnt.setFont(font1)
        self.nvr_del_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nvr_del_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/ui/ui/images/ico_delete.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.nvr_del_bnt.setIcon(icon2)
        self.nvr_del_bnt.setIconSize(QSize(31, 50))

        self.verticalLayout_3.addWidget(self.nvr_del_bnt)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.nvr_list_table = QTableWidget(self.widget_4)
        if (self.nvr_list_table.columnCount() < 3):
            self.nvr_list_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.nvr_list_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.nvr_list_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.nvr_list_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.nvr_list_table.rowCount() < 3):
            self.nvr_list_table.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.nvr_list_table.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.nvr_list_table.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.nvr_list_table.setItem(0, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.nvr_list_table.setItem(0, 2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.nvr_list_table.setItem(1, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.nvr_list_table.setItem(1, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.nvr_list_table.setItem(1, 2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.nvr_list_table.setItem(2, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.nvr_list_table.setItem(2, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.nvr_list_table.setItem(2, 2, __qtablewidgetitem12)
        self.nvr_list_table.setObjectName(u"nvr_list_table")
        self.nvr_list_table.setMinimumSize(QSize(328, 300))
        self.nvr_list_table.setStyleSheet(u"\n"
"QTableWidget {\n"
"    background-color: rgb(16, 16, 16); /* \ud14c\uc774\ube14 \uc804\uccb4 \ubc30\uacbd\uc0c9 */\n"
"    color: rgb(179,179,179);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: rgb(209, 209, 209); /* \ud5e4\ub354 \ud14d\uc2a4\ud2b8 \uc0c9\uc0c1 - \ud68c\uc0c9 */\n"
"	background-color: rgb(7, 7, 16); \n"
"\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    color: rgb(179,179,179); /* \uae30\ubcf8 \uc0c1\ud0dc\uc5d0\uc11c\uc758 \ud14d\uc2a4\ud2b8 \uc0c9\uc0c1 - \ud770\uc0c9 */\n"
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
        self.nvr_list_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.nvr_list_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.nvr_list_table.setShowGrid(True)
        self.nvr_list_table.horizontalHeader().setVisible(True)
        self.nvr_list_table.horizontalHeader().setCascadingSectionResizes(True)
        self.nvr_list_table.horizontalHeader().setMinimumSectionSize(10)
        self.nvr_list_table.horizontalHeader().setDefaultSectionSize(100)
        self.nvr_list_table.horizontalHeader().setHighlightSections(False)
        self.nvr_list_table.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.nvr_list_table.horizontalHeader().setStretchLastSection(True)
        self.nvr_list_table.verticalHeader().setVisible(False)
        self.nvr_list_table.verticalHeader().setCascadingSectionResizes(False)
        self.nvr_list_table.verticalHeader().setMinimumSectionSize(21)
        self.nvr_list_table.verticalHeader().setDefaultSectionSize(33)
        self.nvr_list_table.verticalHeader().setProperty(u"showSortIndicator", False)

        self.horizontalLayout_3.addWidget(self.nvr_list_table)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_10.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 360))
        self.verticalLayout_9 = QVBoxLayout(self.widget_3)
        self.verticalLayout_9.setSpacing(9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(56, 0))
        font3 = QFont()
        font3.setPointSize(13)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: rgb(179,179,179);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(38)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.nvr_name_label = QLabel(self.widget_3)
        self.nvr_name_label.setObjectName(u"nvr_name_label")
        self.nvr_name_label.setMinimumSize(QSize(29, 22))
        self.nvr_name_label.setMaximumSize(QSize(999, 999))
        font4 = QFont()
        font4.setFamilies([u"Sans"])
        font4.setPointSize(10)
        font4.setBold(False)
        self.nvr_name_label.setFont(font4)
        self.nvr_name_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.nvr_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.nvr_name_label)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.nvr_name_input = QLineEdit(self.widget_3)
        self.nvr_name_input.setObjectName(u"nvr_name_input")
        self.nvr_name_input.setMinimumSize(QSize(252, 17))
        self.nvr_name_input.setMaximumSize(QSize(999, 999))
        self.nvr_name_input.setFont(font4)
        self.nvr_name_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.nvr_name_input.setStyleSheet(u"qproperty-frame: false;\n"
"font-size:10pt;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_4.addWidget(self.nvr_name_input)

        self.nvr_name_input_line = QFrame(self.widget_3)
        self.nvr_name_input_line.setObjectName(u"nvr_name_input_line")
        self.nvr_name_input_line.setMinimumSize(QSize(0, 3))
        self.nvr_name_input_line.setMaximumSize(QSize(999, 3))
        font5 = QFont()
        font5.setFamilies([u"Sans"])
        font5.setPointSize(5)
        font5.setStrikeOut(False)
        self.nvr_name_input_line.setFont(font5)
        self.nvr_name_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.nvr_name_input_line.setAutoFillBackground(False)
        self.nvr_name_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.nvr_name_input_line.setFrameShape(QFrame.Shape.HLine)
        self.nvr_name_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.nvr_name_input_line)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(39)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.nvr_ip_label = QLabel(self.widget_3)
        self.nvr_ip_label.setObjectName(u"nvr_ip_label")
        self.nvr_ip_label.setMinimumSize(QSize(29, 22))
        self.nvr_ip_label.setMaximumSize(QSize(999, 999))
        self.nvr_ip_label.setFont(font4)
        self.nvr_ip_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.nvr_ip_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.nvr_ip_label)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.nvr_ip_input = QLineEdit(self.widget_3)
        self.nvr_ip_input.setObjectName(u"nvr_ip_input")
        self.nvr_ip_input.setMinimumSize(QSize(252, 17))
        self.nvr_ip_input.setMaximumSize(QSize(999, 999))
        self.nvr_ip_input.setFont(font4)
        self.nvr_ip_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.nvr_ip_input.setStyleSheet(u"qproperty-frame: false;\n"
"font-size:10pt;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_5.addWidget(self.nvr_ip_input)

        self.nvr_ip_input_line = QFrame(self.widget_3)
        self.nvr_ip_input_line.setObjectName(u"nvr_ip_input_line")
        self.nvr_ip_input_line.setMinimumSize(QSize(0, 3))
        self.nvr_ip_input_line.setMaximumSize(QSize(999, 3))
        self.nvr_ip_input_line.setFont(font5)
        self.nvr_ip_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.nvr_ip_input_line.setAutoFillBackground(False)
        self.nvr_ip_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.nvr_ip_input_line.setFrameShape(QFrame.Shape.HLine)
        self.nvr_ip_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.nvr_ip_input_line)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(39)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.nvr_port_label = QLabel(self.widget_3)
        self.nvr_port_label.setObjectName(u"nvr_port_label")
        self.nvr_port_label.setMinimumSize(QSize(29, 22))
        self.nvr_port_label.setMaximumSize(QSize(999, 999))
        self.nvr_port_label.setFont(font4)
        self.nvr_port_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.nvr_port_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.nvr_port_label)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.nvr_port_input = QLineEdit(self.widget_3)
        self.nvr_port_input.setObjectName(u"nvr_port_input")
        self.nvr_port_input.setMinimumSize(QSize(252, 17))
        self.nvr_port_input.setMaximumSize(QSize(999, 999))
        self.nvr_port_input.setFont(font4)
        self.nvr_port_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.nvr_port_input.setStyleSheet(u"qproperty-frame: false;\n"
"font-size:10pt;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_6.addWidget(self.nvr_port_input)

        self.nvr_port_input_line = QFrame(self.widget_3)
        self.nvr_port_input_line.setObjectName(u"nvr_port_input_line")
        self.nvr_port_input_line.setMinimumSize(QSize(0, 3))
        self.nvr_port_input_line.setMaximumSize(QSize(999, 3))
        self.nvr_port_input_line.setFont(font5)
        self.nvr_port_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.nvr_port_input_line.setAutoFillBackground(False)
        self.nvr_port_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.nvr_port_input_line.setFrameShape(QFrame.Shape.HLine)
        self.nvr_port_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.nvr_port_input_line)


        self.horizontalLayout_7.addLayout(self.verticalLayout_6)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.nvr_http_port_label = QLabel(self.widget_3)
        self.nvr_http_port_label.setObjectName(u"nvr_http_port_label")
        self.nvr_http_port_label.setMinimumSize(QSize(29, 22))
        self.nvr_http_port_label.setMaximumSize(QSize(999, 999))
        self.nvr_http_port_label.setFont(font4)
        self.nvr_http_port_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.nvr_http_port_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.nvr_http_port_label)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.nvr_http_port_input = QLineEdit(self.widget_3)
        self.nvr_http_port_input.setObjectName(u"nvr_http_port_input")
        self.nvr_http_port_input.setMinimumSize(QSize(252, 17))
        self.nvr_http_port_input.setMaximumSize(QSize(999, 999))
        self.nvr_http_port_input.setFont(font4)
        self.nvr_http_port_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.nvr_http_port_input.setStyleSheet(u"qproperty-frame: false;\n"
"font-size:10pt;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_7.addWidget(self.nvr_http_port_input)

        self.nvr_http_port_input_line = QFrame(self.widget_3)
        self.nvr_http_port_input_line.setObjectName(u"nvr_http_port_input_line")
        self.nvr_http_port_input_line.setMinimumSize(QSize(0, 3))
        self.nvr_http_port_input_line.setMaximumSize(QSize(999, 3))
        self.nvr_http_port_input_line.setFont(font5)
        self.nvr_http_port_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.nvr_http_port_input_line.setAutoFillBackground(False)
        self.nvr_http_port_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.nvr_http_port_input_line.setFrameShape(QFrame.Shape.HLine)
        self.nvr_http_port_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.nvr_http_port_input_line)


        self.horizontalLayout_8.addLayout(self.verticalLayout_7)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(33)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.nvr_id_label = QLabel(self.widget_3)
        self.nvr_id_label.setObjectName(u"nvr_id_label")
        self.nvr_id_label.setMinimumSize(QSize(29, 22))
        self.nvr_id_label.setMaximumSize(QSize(999, 999))
        self.nvr_id_label.setFont(font4)
        self.nvr_id_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.nvr_id_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.nvr_id_label)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.nvr_id_input = QLineEdit(self.widget_3)
        self.nvr_id_input.setObjectName(u"nvr_id_input")
        self.nvr_id_input.setMinimumSize(QSize(252, 17))
        self.nvr_id_input.setMaximumSize(QSize(999, 999))
        self.nvr_id_input.setFont(font4)
        self.nvr_id_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.nvr_id_input.setStyleSheet(u"qproperty-frame: false;\n"
"font-size:10pt;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_8.addWidget(self.nvr_id_input)

        self.nvr_id_input_line = QFrame(self.widget_3)
        self.nvr_id_input_line.setObjectName(u"nvr_id_input_line")
        self.nvr_id_input_line.setMinimumSize(QSize(0, 3))
        self.nvr_id_input_line.setMaximumSize(QSize(999, 3))
        self.nvr_id_input_line.setFont(font5)
        self.nvr_id_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.nvr_id_input_line.setAutoFillBackground(False)
        self.nvr_id_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.nvr_id_input_line.setFrameShape(QFrame.Shape.HLine)
        self.nvr_id_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.nvr_id_input_line)


        self.horizontalLayout_9.addLayout(self.verticalLayout_8)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(19)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.nvr_passward_label = QLabel(self.widget_3)
        self.nvr_passward_label.setObjectName(u"nvr_passward_label")
        self.nvr_passward_label.setMinimumSize(QSize(29, 22))
        self.nvr_passward_label.setMaximumSize(QSize(999, 999))
        self.nvr_passward_label.setFont(font4)
        self.nvr_passward_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.nvr_passward_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.nvr_passward_label)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.nvr_passward_input = QLineEdit(self.widget_3)
        self.nvr_passward_input.setObjectName(u"nvr_passward_input")
        self.nvr_passward_input.setMinimumSize(QSize(252, 17))
        self.nvr_passward_input.setMaximumSize(QSize(999, 999))
        self.nvr_passward_input.setFont(font4)
        self.nvr_passward_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.nvr_passward_input.setStyleSheet(u"qproperty-frame: false;\n"
"font-size:10pt;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.nvr_passward_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_12.addWidget(self.nvr_passward_input)

        self.nvr_passward_input_line = QFrame(self.widget_3)
        self.nvr_passward_input_line.setObjectName(u"nvr_passward_input_line")
        self.nvr_passward_input_line.setMinimumSize(QSize(0, 3))
        self.nvr_passward_input_line.setMaximumSize(QSize(999, 3))
        self.nvr_passward_input_line.setFont(font5)
        self.nvr_passward_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.nvr_passward_input_line.setAutoFillBackground(False)
        self.nvr_passward_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.nvr_passward_input_line.setFrameShape(QFrame.Shape.HLine)
        self.nvr_passward_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.nvr_passward_input_line)


        self.horizontalLayout_10.addLayout(self.verticalLayout_12)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.nvr_save_bnt = QPushButton(self.widget_3)
        self.nvr_save_bnt.setObjectName(u"nvr_save_bnt")
        sizePolicy.setHeightForWidth(self.nvr_save_bnt.sizePolicy().hasHeightForWidth())
        self.nvr_save_bnt.setSizePolicy(sizePolicy)
        self.nvr_save_bnt.setMinimumSize(QSize(76, 39))
        self.nvr_save_bnt.setMaximumSize(QSize(76, 39))
        self.nvr_save_bnt.setFont(font1)
        self.nvr_save_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nvr_save_bnt.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.0 rgba(112, 210, 112, 255),\n"
"    stop:0.3 rgba(0, 196, 0, 255)\n"
");\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"")

        self.horizontalLayout_11.addWidget(self.nvr_save_bnt)


        self.verticalLayout_9.addLayout(self.horizontalLayout_11)


        self.verticalLayout_10.addWidget(self.widget_3)


        self.horizontalLayout_22.addWidget(self.widget)

        self.widget_5 = QWidget(self.page)
        self.widget_5.setObjectName(u"widget_5")
        font6 = QFont()
        font6.setPointSize(11)
        font6.setHintingPreference(QFont.PreferDefaultHinting)
        self.widget_5.setFont(font6)
        self.widget_5.setStyleSheet(u"background-color: rgb(16, 16, 16);")
        self.verticalLayout_13 = QVBoxLayout(self.widget_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(32, 32))
        self.label_3.setPixmap(QPixmap(u":/ui/ui/images/search_ico.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.label_3)

        self.nvr_search_input = QLineEdit(self.widget_5)
        self.nvr_search_input.setObjectName(u"nvr_search_input")
        self.nvr_search_input.setMinimumSize(QSize(252, 17))
        self.nvr_search_input.setMaximumSize(QSize(999999, 27))
        self.nvr_search_input.setFont(font4)
        self.nvr_search_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.nvr_search_input.setStyleSheet(u"\n"
"\n"
"QLineEdit {\n"
"qproperty-frame: false;\n"
"font-size:10pt;\n"
"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid #555;\n"
"border-radius: 6px;\n"
" padding: 5px;\n"
"            }\n"
"            \n"
"            QLineEdit::placeholder {\n"
"                color: rgba(255, 255, 255, 120); /* \ubc18\ud22c\uba85 \ud770\uc0c9 */\n"
"            }")

        self.horizontalLayout_12.addWidget(self.nvr_search_input)


        self.verticalLayout_13.addLayout(self.horizontalLayout_12)

        self.nvr_server_tree_list = QTreeWidget(self.widget_5)
        __qtreewidgetitem = QTreeWidgetItem(self.nvr_server_tree_list)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.nvr_server_tree_list)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        self.nvr_server_tree_list.setObjectName(u"nvr_server_tree_list")
        self.nvr_server_tree_list.setStyleSheet(u"/* QTreeWidget \ub610\ub294 QTreeView\uc5d0 \uc801\uc6a9 */\n"
"QTreeWidget {\n"
"    background-color: black;  /* \uc804\uccb4 \ubc30\uacbd\uc0c9 */\n"
"    color: #E0E0E0;             /* \uae30\ubcf8 \uae00\uc790\uc0c9 */\n"
"    border: none;             /* \ud14c\ub450\ub9ac \uc5c6\uc74c */\n"
"    show-decoration-selected: 1;\n"
"\n"
"    /* --- \ucd94\uac00: \uc2dc\uc2a4\ud15c \uae30\ubcf8 \uc120\ud0dd \uc2a4\ud0c0\uc77c \ub36e\uc5b4\uc4f0\uae30 --- */\n"
"    /*selection-background-color: #4a4a4a; /* (\ud544\uc218) item:selected\uc640 \ub3d9\uc77c\ud558\uac8c */\n"
"    selection-background-color: rgb(32,39,49); /* \uc120\ud0dd\ub41c \uc140\uc758 \ubc30\uacbd\uc0c9 */\n"
"    selection-color: #E0E0E0;            /* (\ud544\uc218) \uc120\ud0dd \uc2dc \ud14d\uc2a4\ud2b8 \uc0c9\uc0c1 */\n"
"}\n"
"\n"
"/* --- \ud56d\ubaa9(Item) \uc2a4\ud0c0\uc77c (\ud14d\uc2a4\ud2b8 + \uc544\uc774\ucf58 \uc601\uc5ed) --- */\n"
"\n"
"QTreeWidget::item {\n"
"    padding: 5px; /* \ud56d\ubaa9 \uac04 \uc5ec\ubc31 */\n"
"    /*b"
                        "order-radius: 4px; /* \ud638\ubc84 \uc2dc \ub465\uadfc \ubaa8\uc11c\ub9ac */\n"
"}\n"
"\n"
"/* (\uc120\ud0dd) \ud074\ub9ad \uc2dc \ub098\ud0c0\ub098\ub294 \uc810\uc120 \ud3ec\ucee4\uc2a4 \ud14c\ub450\ub9ac \uc81c\uac70 */\n"
"QTreeWidget::item:focus {\n"
"    outline: none;\n"
"    border: 0px;\n"
"}\n"
"\n"
"/* \ud56d\ubaa9\uc5d0 \ub9c8\uc6b0\uc2a4\ub97c \uc62c\ub838\uc744 \ub54c */\n"
"QTreeWidget::item:hover {\n"
"    background-color: #2a2a2a; /* \uc0b4\uc9dd \ubc1d\uc740 \ud68c\uc0c9 */\n"
"}\n"
"\n"
"/* \ud56d\ubaa9\uc744 \uc120\ud0dd\ud588\uc744 \ub54c */\n"
"QTreeWidget::item:selected {\n"
"    background-color: rgb(32,39,49); /* \uc120\ud0dd\ub41c \ud56d\ubaa9 \ubc30\uacbd\uc0c9 */\n"
"    \n"
"    /* * (\uc120\ud0dd \uc0ac\ud56d) \uc5ec\uae30\uc5d0 color\ub97c \uba85\uc2dc\ud574\ub3c4 \uc88b\uc9c0\ub9cc,\n"
"     * QWidget\uc758 selection-color\uac00 \uc774\ubbf8 \ucc98\ub9ac\ud574\uc90d\ub2c8\ub2e4.\n"
"     */\n"
"     color: #E0E0E0; \n"
"}\n"
"\n"
"\n"
"/* --- \uc2a4\ud06c\ub864\ubc14 (\uae30\uc874"
                        "\uacfc \ub3d9\uc77c) --- */\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #999999;\n"
"    background: #b3b3b3c6;\n"
"    width: 8px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #2f2f2f; \n"
"    min-height: 10px;\n"
"    width: 8px;\n"
"}\n"
"\n"
"\n"
"/* --- \ud5e4\ub4dc(Branch) \uc2a4\ud0c0\uc77c (\uae30\uc874\uacfc \ub3d9\uc77c) --- */\n"
"QTreeWidget::branch {\n"
"    background: transparent;\n"
"    border-image: none;\n"
"    image: none;\n"
"    /* 'color: white;'\ub294 \uc5ec\uae30\uc11c \uc758\ubbf8\uac00 \uc5c6\uc73c\ubbc0\ub85c \uc81c\uac70\ud574\ub3c4 \ub429\ub2c8\ub2e4. */\n"
"}\n"
"\n"
"QTreeWidget::branch:closed:has-children {\n"
"    image: url(:/ui/ui/images/ico_right.svg)\n"
"}\n"
"\n"
"QTreeWidget::branch:open:has-children {\n"
"    image: url(:/ui/ui/images/down_arrow.png)\n"
"}")
        self.nvr_server_tree_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.nvr_server_tree_list.setDragEnabled(True)
        self.nvr_server_tree_list.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.nvr_server_tree_list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.nvr_server_tree_list.setRootIsDecorated(True)
        self.nvr_server_tree_list.setUniformRowHeights(False)
        self.nvr_server_tree_list.setSortingEnabled(False)
        self.nvr_server_tree_list.setAnimated(True)
        self.nvr_server_tree_list.setAllColumnsShowFocus(True)
        self.nvr_server_tree_list.setWordWrap(True)
        self.nvr_server_tree_list.setHeaderHidden(True)
        self.nvr_server_tree_list.setExpandsOnDoubleClick(False)
        self.nvr_server_tree_list.setColumnCount(1)
        self.nvr_server_tree_list.header().setHighlightSections(False)

        self.verticalLayout_13.addWidget(self.nvr_server_tree_list)


        self.horizontalLayout_22.addWidget(self.widget_5)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.widget_2 = QWidget(self.page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 400))
        self.widget_2.setStyleSheet(u"background-color: rgb(16, 16, 16);")
        self.verticalLayout_18 = QVBoxLayout(self.widget_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(222, 221, 218);")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.server_list_setting_bnt = QPushButton(self.widget_2)
        self.server_list_setting_bnt.setObjectName(u"server_list_setting_bnt")
        self.server_list_setting_bnt.setMinimumSize(QSize(35, 35))
        self.server_list_setting_bnt.setMaximumSize(QSize(35, 35))
        self.server_list_setting_bnt.setFont(font1)
        self.server_list_setting_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.server_list_setting_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/ui/ui/images/ico_setting.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.server_list_setting_bnt.setIcon(icon3)
        self.server_list_setting_bnt.setIconSize(QSize(35, 35))

        self.horizontalLayout_13.addWidget(self.server_list_setting_bnt)


        self.verticalLayout_18.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(11)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.ai_server_add_bnt = QPushButton(self.widget_2)
        self.ai_server_add_bnt.setObjectName(u"ai_server_add_bnt")
        self.ai_server_add_bnt.setMinimumSize(QSize(35, 35))
        self.ai_server_add_bnt.setMaximumSize(QSize(35, 35))
        self.ai_server_add_bnt.setFont(font1)
        self.ai_server_add_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ai_server_add_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.ai_server_add_bnt.setIcon(icon1)
        self.ai_server_add_bnt.setIconSize(QSize(31, 50))

        self.verticalLayout_14.addWidget(self.ai_server_add_bnt)

        self.ai_server_del_bnt = QPushButton(self.widget_2)
        self.ai_server_del_bnt.setObjectName(u"ai_server_del_bnt")
        self.ai_server_del_bnt.setMinimumSize(QSize(35, 35))
        self.ai_server_del_bnt.setMaximumSize(QSize(35, 35))
        self.ai_server_del_bnt.setFont(font1)
        self.ai_server_del_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ai_server_del_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.ai_server_del_bnt.setIcon(icon2)
        self.ai_server_del_bnt.setIconSize(QSize(31, 50))

        self.verticalLayout_14.addWidget(self.ai_server_del_bnt)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)


        self.horizontalLayout_14.addLayout(self.verticalLayout_14)

        self.ai_server_table = QTableWidget(self.widget_2)
        if (self.ai_server_table.columnCount() < 3):
            self.ai_server_table.setColumnCount(3)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.ai_server_table.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.ai_server_table.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.ai_server_table.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        if (self.ai_server_table.rowCount() < 3):
            self.ai_server_table.setRowCount(3)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.ai_server_table.setVerticalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.ai_server_table.setItem(0, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.ai_server_table.setItem(0, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.ai_server_table.setItem(0, 2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.ai_server_table.setItem(1, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.ai_server_table.setItem(1, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.ai_server_table.setItem(1, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.ai_server_table.setItem(2, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.ai_server_table.setItem(2, 1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.ai_server_table.setItem(2, 2, __qtablewidgetitem25)
        self.ai_server_table.setObjectName(u"ai_server_table")
        self.ai_server_table.setMinimumSize(QSize(360, 300))
        self.ai_server_table.setMaximumSize(QSize(328, 16777215))
        self.ai_server_table.setStyleSheet(u"\n"
"QTableWidget {\n"
"    background-color: rgb(16, 16, 16); /* \ud14c\uc774\ube14 \uc804\uccb4 \ubc30\uacbd\uc0c9 */\n"
"    color: rgb(179,179,179);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: rgb(209, 209, 209); /* \ud5e4\ub354 \ud14d\uc2a4\ud2b8 \uc0c9\uc0c1 - \ud68c\uc0c9 */\n"
"	background-color: rgb(7, 7, 16); \n"
"\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    color: rgb(179,179,179); /* \uae30\ubcf8 \uc0c1\ud0dc\uc5d0\uc11c\uc758 \ud14d\uc2a4\ud2b8 \uc0c9\uc0c1 - \ud770\uc0c9 */\n"
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
        self.ai_server_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ai_server_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.ai_server_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ai_server_table.setShowGrid(True)
        self.ai_server_table.horizontalHeader().setVisible(True)
        self.ai_server_table.horizontalHeader().setCascadingSectionResizes(True)
        self.ai_server_table.horizontalHeader().setMinimumSectionSize(30)
        self.ai_server_table.horizontalHeader().setDefaultSectionSize(100)
        self.ai_server_table.horizontalHeader().setHighlightSections(False)
        self.ai_server_table.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.ai_server_table.horizontalHeader().setStretchLastSection(True)
        self.ai_server_table.verticalHeader().setVisible(False)
        self.ai_server_table.verticalHeader().setCascadingSectionResizes(False)
        self.ai_server_table.verticalHeader().setMinimumSectionSize(21)
        self.ai_server_table.verticalHeader().setDefaultSectionSize(33)
        self.ai_server_table.verticalHeader().setHighlightSections(False)
        self.ai_server_table.verticalHeader().setProperty(u"showSortIndicator", False)

        self.horizontalLayout_14.addWidget(self.ai_server_table)

        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(16777215, 322))
        self.verticalLayout_15 = QVBoxLayout(self.widget_7)
        self.verticalLayout_15.setSpacing(12)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(22, 22, 22, 22)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(38)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.ai_server_name_label = QLabel(self.widget_7)
        self.ai_server_name_label.setObjectName(u"ai_server_name_label")
        self.ai_server_name_label.setMinimumSize(QSize(29, 22))
        self.ai_server_name_label.setMaximumSize(QSize(999, 999))
        self.ai_server_name_label.setFont(font4)
        self.ai_server_name_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.ai_server_name_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.ai_server_name_label)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.ai_server_name_input = QLineEdit(self.widget_7)
        self.ai_server_name_input.setObjectName(u"ai_server_name_input")
        self.ai_server_name_input.setMinimumSize(QSize(252, 17))
        self.ai_server_name_input.setMaximumSize(QSize(999, 999))
        self.ai_server_name_input.setFont(font4)
        self.ai_server_name_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ai_server_name_input.setStyleSheet(u"qproperty-frame: false;\n"
"font-size:10pt;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_16.addWidget(self.ai_server_name_input)

        self.ai_server_name_input_line = QFrame(self.widget_7)
        self.ai_server_name_input_line.setObjectName(u"ai_server_name_input_line")
        self.ai_server_name_input_line.setMinimumSize(QSize(0, 3))
        self.ai_server_name_input_line.setMaximumSize(QSize(999, 3))
        self.ai_server_name_input_line.setFont(font5)
        self.ai_server_name_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.ai_server_name_input_line.setAutoFillBackground(False)
        self.ai_server_name_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.ai_server_name_input_line.setFrameShape(QFrame.Shape.HLine)
        self.ai_server_name_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_16.addWidget(self.ai_server_name_input_line)


        self.horizontalLayout_15.addLayout(self.verticalLayout_16)


        self.verticalLayout_15.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(39)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.ai_server_ip_label = QLabel(self.widget_7)
        self.ai_server_ip_label.setObjectName(u"ai_server_ip_label")
        self.ai_server_ip_label.setMinimumSize(QSize(29, 22))
        self.ai_server_ip_label.setMaximumSize(QSize(999, 999))
        self.ai_server_ip_label.setFont(font4)
        self.ai_server_ip_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.ai_server_ip_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.ai_server_ip_label)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.ai_server_ip_input = QLineEdit(self.widget_7)
        self.ai_server_ip_input.setObjectName(u"ai_server_ip_input")
        self.ai_server_ip_input.setMinimumSize(QSize(252, 17))
        self.ai_server_ip_input.setMaximumSize(QSize(999, 999))
        self.ai_server_ip_input.setFont(font4)
        self.ai_server_ip_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ai_server_ip_input.setStyleSheet(u"qproperty-frame: false;\n"
"font-size:10pt;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_17.addWidget(self.ai_server_ip_input)

        self.ai_server_ip_input_line = QFrame(self.widget_7)
        self.ai_server_ip_input_line.setObjectName(u"ai_server_ip_input_line")
        self.ai_server_ip_input_line.setMinimumSize(QSize(0, 3))
        self.ai_server_ip_input_line.setMaximumSize(QSize(999, 3))
        self.ai_server_ip_input_line.setFont(font5)
        self.ai_server_ip_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.ai_server_ip_input_line.setAutoFillBackground(False)
        self.ai_server_ip_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.ai_server_ip_input_line.setFrameShape(QFrame.Shape.HLine)
        self.ai_server_ip_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_17.addWidget(self.ai_server_ip_input_line)


        self.horizontalLayout_16.addLayout(self.verticalLayout_17)


        self.verticalLayout_15.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(39)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.ai_server_port_label = QLabel(self.widget_7)
        self.ai_server_port_label.setObjectName(u"ai_server_port_label")
        self.ai_server_port_label.setMinimumSize(QSize(29, 22))
        self.ai_server_port_label.setMaximumSize(QSize(999, 999))
        self.ai_server_port_label.setFont(font4)
        self.ai_server_port_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.ai_server_port_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.ai_server_port_label)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.ai_server_port_input = QLineEdit(self.widget_7)
        self.ai_server_port_input.setObjectName(u"ai_server_port_input")
        self.ai_server_port_input.setMinimumSize(QSize(252, 17))
        self.ai_server_port_input.setMaximumSize(QSize(999, 999))
        self.ai_server_port_input.setFont(font4)
        self.ai_server_port_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ai_server_port_input.setStyleSheet(u"qproperty-frame: false;\n"
"font-size:10pt;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_19.addWidget(self.ai_server_port_input)

        self.ai_server_port_input_line = QFrame(self.widget_7)
        self.ai_server_port_input_line.setObjectName(u"ai_server_port_input_line")
        self.ai_server_port_input_line.setMinimumSize(QSize(0, 3))
        self.ai_server_port_input_line.setMaximumSize(QSize(999, 3))
        self.ai_server_port_input_line.setFont(font5)
        self.ai_server_port_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.ai_server_port_input_line.setAutoFillBackground(False)
        self.ai_server_port_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.ai_server_port_input_line.setFrameShape(QFrame.Shape.HLine)
        self.ai_server_port_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_19.addWidget(self.ai_server_port_input_line)


        self.horizontalLayout_17.addLayout(self.verticalLayout_19)


        self.verticalLayout_15.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(24)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.ai_server_id_label = QLabel(self.widget_7)
        self.ai_server_id_label.setObjectName(u"ai_server_id_label")
        self.ai_server_id_label.setMinimumSize(QSize(44, 22))
        self.ai_server_id_label.setMaximumSize(QSize(999, 999))
        self.ai_server_id_label.setFont(font4)
        self.ai_server_id_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.ai_server_id_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.ai_server_id_label)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.ai_server_id_input = QLineEdit(self.widget_7)
        self.ai_server_id_input.setObjectName(u"ai_server_id_input")
        self.ai_server_id_input.setMinimumSize(QSize(252, 17))
        self.ai_server_id_input.setMaximumSize(QSize(999, 999))
        self.ai_server_id_input.setFont(font4)
        self.ai_server_id_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ai_server_id_input.setStyleSheet(u"qproperty-frame: false;\n"
"font-size:10pt;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_20.addWidget(self.ai_server_id_input)

        self.ai_server_id_input_line = QFrame(self.widget_7)
        self.ai_server_id_input_line.setObjectName(u"ai_server_id_input_line")
        self.ai_server_id_input_line.setMinimumSize(QSize(0, 3))
        self.ai_server_id_input_line.setMaximumSize(QSize(999, 3))
        self.ai_server_id_input_line.setFont(font5)
        self.ai_server_id_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.ai_server_id_input_line.setAutoFillBackground(False)
        self.ai_server_id_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.ai_server_id_input_line.setFrameShape(QFrame.Shape.HLine)
        self.ai_server_id_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_20.addWidget(self.ai_server_id_input_line)


        self.horizontalLayout_19.addLayout(self.verticalLayout_20)


        self.verticalLayout_15.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(19)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.ai_server_passward_label = QLabel(self.widget_7)
        self.ai_server_passward_label.setObjectName(u"ai_server_passward_label")
        self.ai_server_passward_label.setMinimumSize(QSize(50, 22))
        self.ai_server_passward_label.setMaximumSize(QSize(999, 999))
        self.ai_server_passward_label.setFont(font4)
        self.ai_server_passward_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.ai_server_passward_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.ai_server_passward_label)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.ai_server_passward_input = QLineEdit(self.widget_7)
        self.ai_server_passward_input.setObjectName(u"ai_server_passward_input")
        self.ai_server_passward_input.setMinimumSize(QSize(252, 17))
        self.ai_server_passward_input.setMaximumSize(QSize(999, 999))
        self.ai_server_passward_input.setFont(font4)
        self.ai_server_passward_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ai_server_passward_input.setStyleSheet(u"qproperty-frame: false;\n"
"font-size:10pt;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.ai_server_passward_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_21.addWidget(self.ai_server_passward_input)

        self.ai_server_passward_input_line = QFrame(self.widget_7)
        self.ai_server_passward_input_line.setObjectName(u"ai_server_passward_input_line")
        self.ai_server_passward_input_line.setMinimumSize(QSize(0, 3))
        self.ai_server_passward_input_line.setMaximumSize(QSize(999, 3))
        self.ai_server_passward_input_line.setFont(font5)
        self.ai_server_passward_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.ai_server_passward_input_line.setAutoFillBackground(False)
        self.ai_server_passward_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.ai_server_passward_input_line.setFrameShape(QFrame.Shape.HLine)
        self.ai_server_passward_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_21.addWidget(self.ai_server_passward_input_line)


        self.horizontalLayout_20.addLayout(self.verticalLayout_21)


        self.verticalLayout_15.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_7)

        self.ai_server_save_bnt = QPushButton(self.widget_7)
        self.ai_server_save_bnt.setObjectName(u"ai_server_save_bnt")
        sizePolicy.setHeightForWidth(self.ai_server_save_bnt.sizePolicy().hasHeightForWidth())
        self.ai_server_save_bnt.setSizePolicy(sizePolicy)
        self.ai_server_save_bnt.setMinimumSize(QSize(76, 39))
        self.ai_server_save_bnt.setMaximumSize(QSize(76, 39))
        self.ai_server_save_bnt.setFont(font1)
        self.ai_server_save_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ai_server_save_bnt.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.0 rgba(112, 210, 112, 255),\n"
"    stop:0.3 rgba(0, 196, 0, 255)\n"
");\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"")

        self.horizontalLayout_21.addWidget(self.ai_server_save_bnt)


        self.verticalLayout_15.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_14.addWidget(self.widget_7)


        self.verticalLayout_18.addLayout(self.horizontalLayout_14)


        self.verticalLayout_23.addWidget(self.widget_2)

        self.widget_6 = QWidget(self.page)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"background-color: rgb(16, 16, 16);")
        self.verticalLayout_22 = QVBoxLayout(self.widget_6)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_5 = QLabel(self.widget_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(32, 32))
        self.label_5.setPixmap(QPixmap(u":/ui/ui/images/search_ico.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_5)

        self.ai_server_camera_search_input = QLineEdit(self.widget_6)
        self.ai_server_camera_search_input.setObjectName(u"ai_server_camera_search_input")
        self.ai_server_camera_search_input.setMinimumSize(QSize(252, 17))
        self.ai_server_camera_search_input.setMaximumSize(QSize(999999, 27))
        self.ai_server_camera_search_input.setFont(font4)
        self.ai_server_camera_search_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ai_server_camera_search_input.setStyleSheet(u"\n"
"\n"
"QLineEdit {\n"
"qproperty-frame: false;\n"
"font-size:10pt;\n"
"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid #555;\n"
"border-radius: 6px;\n"
" padding: 5px;\n"
"            }\n"
"            \n"
"            QLineEdit::placeholder {\n"
"                color: rgba(255, 255, 255, 120); /* \ubc18\ud22c\uba85 \ud770\uc0c9 */\n"
"            }")

        self.horizontalLayout_18.addWidget(self.ai_server_camera_search_input)


        self.verticalLayout_24.addLayout(self.horizontalLayout_18)

        self.ai_server_info_table = QTableWidget(self.widget_6)
        if (self.ai_server_info_table.columnCount() < 5):
            self.ai_server_info_table.setColumnCount(5)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.ai_server_info_table.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.ai_server_info_table.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.ai_server_info_table.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.ai_server_info_table.setHorizontalHeaderItem(3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.ai_server_info_table.setHorizontalHeaderItem(4, __qtablewidgetitem30)
        if (self.ai_server_info_table.rowCount() < 2):
            self.ai_server_info_table.setRowCount(2)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.ai_server_info_table.setItem(0, 0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.ai_server_info_table.setItem(0, 1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.ai_server_info_table.setItem(0, 2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.ai_server_info_table.setItem(0, 3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.ai_server_info_table.setItem(0, 4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.ai_server_info_table.setItem(1, 0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.ai_server_info_table.setItem(1, 1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.ai_server_info_table.setItem(1, 2, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.ai_server_info_table.setItem(1, 3, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.ai_server_info_table.setItem(1, 4, __qtablewidgetitem40)
        self.ai_server_info_table.setObjectName(u"ai_server_info_table")
        self.ai_server_info_table.setMinimumSize(QSize(328, 120))
        self.ai_server_info_table.setStyleSheet(u"\n"
"QTableWidget {\n"
"    background-color: rgb(16, 16, 16); /* \ud14c\uc774\ube14 \uc804\uccb4 \ubc30\uacbd\uc0c9 */\n"
"    color: rgb(179,179,179);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: rgb(209, 209, 209); /* \ud5e4\ub354 \ud14d\uc2a4\ud2b8 \uc0c9\uc0c1 - \ud68c\uc0c9 */\n"
"	background-color: rgb(7, 7, 16); \n"
"\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    color: rgb(179,179,179); /* \uae30\ubcf8 \uc0c1\ud0dc\uc5d0\uc11c\uc758 \ud14d\uc2a4\ud2b8 \uc0c9\uc0c1 - \ud770\uc0c9 */\n"
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
        self.ai_server_info_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ai_server_info_table.setDragDropOverwriteMode(False)
        self.ai_server_info_table.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.ai_server_info_table.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.ai_server_info_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ai_server_info_table.setShowGrid(True)
        self.ai_server_info_table.horizontalHeader().setVisible(True)
        self.ai_server_info_table.horizontalHeader().setCascadingSectionResizes(True)
        self.ai_server_info_table.horizontalHeader().setMinimumSectionSize(30)
        self.ai_server_info_table.horizontalHeader().setDefaultSectionSize(100)
        self.ai_server_info_table.horizontalHeader().setHighlightSections(False)
        self.ai_server_info_table.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.ai_server_info_table.horizontalHeader().setStretchLastSection(True)
        self.ai_server_info_table.verticalHeader().setVisible(False)
        self.ai_server_info_table.verticalHeader().setCascadingSectionResizes(False)
        self.ai_server_info_table.verticalHeader().setMinimumSectionSize(21)
        self.ai_server_info_table.verticalHeader().setDefaultSectionSize(33)
        self.ai_server_info_table.verticalHeader().setHighlightSections(False)
        self.ai_server_info_table.verticalHeader().setProperty(u"showSortIndicator", False)

        self.verticalLayout_24.addWidget(self.ai_server_info_table)


        self.verticalLayout_22.addLayout(self.verticalLayout_24)


        self.verticalLayout_23.addWidget(self.widget_6)


        self.horizontalLayout_22.addLayout(self.verticalLayout_23)


        self.verticalLayout_25.addLayout(self.horizontalLayout_22)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_69 = QVBoxLayout(self.page_2)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.camera_info_side_widget = QWidget(self.page_2)
        self.camera_info_side_widget.setObjectName(u"camera_info_side_widget")
        self.camera_info_side_widget.setMaximumSize(QSize(335, 16777215))
        self.verticalLayout_26 = QVBoxLayout(self.camera_info_side_widget)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.camera_list_table = QTableWidget(self.camera_info_side_widget)
        if (self.camera_list_table.columnCount() < 4):
            self.camera_list_table.setColumnCount(4)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.camera_list_table.setHorizontalHeaderItem(0, __qtablewidgetitem41)
        font7 = QFont()
        font7.setFamilies([u"Ubuntu Light"])
        font7.setPointSize(10)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setFont(font7);
        self.camera_list_table.setHorizontalHeaderItem(1, __qtablewidgetitem42)
        font8 = QFont()
        font8.setFamilies([u"Ubuntu Light"])
        font8.setPointSize(10)
        font8.setBold(False)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setFont(font8);
        self.camera_list_table.setHorizontalHeaderItem(2, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.camera_list_table.setHorizontalHeaderItem(3, __qtablewidgetitem44)
        self.camera_list_table.setObjectName(u"camera_list_table")
        self.camera_list_table.setMinimumSize(QSize(319, 100))
        self.camera_list_table.setMaximumSize(QSize(319, 16777215))
        self.camera_list_table.setFont(font4)
        self.camera_list_table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.camera_list_table.setStyleSheet(u"\n"
"QTableWidget {\n"
"    background-color: rgb(16, 16, 16); /* \ud14c\uc774\ube14 \uc804\uccb4 \ubc30\uacbd\uc0c9 */\n"
"    color: rgb(179,179,179);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: rgb(209, 209, 209); /* \ud5e4\ub354 \ud14d\uc2a4\ud2b8 \uc0c9\uc0c1 - \ud68c\uc0c9 */\n"
"	background-color: rgb(7, 7, 16); \n"
"\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    color: rgb(179,179,179); /* \uae30\ubcf8 \uc0c1\ud0dc\uc5d0\uc11c\uc758 \ud14d\uc2a4\ud2b8 \uc0c9\uc0c1 - \ud770\uc0c9 */\n"
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
        self.camera_list_table.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.camera_list_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.camera_list_table.setTabKeyNavigation(False)
        self.camera_list_table.setDragDropOverwriteMode(False)
        self.camera_list_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.camera_list_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.camera_list_table.setShowGrid(False)
        self.camera_list_table.setGridStyle(Qt.PenStyle.NoPen)
        self.camera_list_table.setWordWrap(False)
        self.camera_list_table.setCornerButtonEnabled(False)
        self.camera_list_table.horizontalHeader().setVisible(True)
        self.camera_list_table.horizontalHeader().setCascadingSectionResizes(False)
        self.camera_list_table.horizontalHeader().setMinimumSectionSize(5)
        self.camera_list_table.horizontalHeader().setDefaultSectionSize(69)
        self.camera_list_table.horizontalHeader().setHighlightSections(False)
        self.camera_list_table.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.camera_list_table.horizontalHeader().setStretchLastSection(True)
        self.camera_list_table.verticalHeader().setVisible(False)
        self.camera_list_table.verticalHeader().setCascadingSectionResizes(False)
        self.camera_list_table.verticalHeader().setMinimumSectionSize(21)
        self.camera_list_table.verticalHeader().setDefaultSectionSize(30)
        self.camera_list_table.verticalHeader().setHighlightSections(False)
        self.camera_list_table.verticalHeader().setProperty(u"showSortIndicator", False)
        self.camera_list_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_27.addWidget(self.camera_list_table)


        self.verticalLayout_26.addLayout(self.verticalLayout_27)


        self.horizontalLayout_32.addWidget(self.camera_info_side_widget)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.tab_layout = QHBoxLayout()
        self.tab_layout.setObjectName(u"tab_layout")
        self.tab_backgournd = QWidget(self.page_2)
        self.tab_backgournd.setObjectName(u"tab_backgournd")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tab_backgournd.sizePolicy().hasHeightForWidth())
        self.tab_backgournd.setSizePolicy(sizePolicy2)
        self.tab_backgournd.setMinimumSize(QSize(1, 50))
        self.tab_backgournd.setMaximumSize(QSize(12345, 50))
        self.tab_backgournd.setStyleSheet(u"background-color: rgb(16, 16, 16);\n"
"\n"
"border-right: 1px solid rgb(119, 118, 123);\n"
"border-bottom-right-radius:20px solid rgb(119, 118, 123);\n"
"\n"
"border-bottom:1px solid rgb(119, 118, 123);\n"
"")
        self.horizontalLayout_23 = QHBoxLayout(self.tab_backgournd)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.camera_bnt = QPushButton(self.tab_backgournd)
        self.camera_bnt.setObjectName(u"camera_bnt")
        self.camera_bnt.setMinimumSize(QSize(163, 28))
        self.camera_bnt.setMaximumSize(QSize(163, 28))
        font9 = QFont()
        font9.setFamilies([u"Sans"])
        font9.setPointSize(13)
        self.camera_bnt.setFont(font9)
        self.camera_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.camera_bnt.setStyleSheet(u"\n"
"\n"
"\n"
"QPushButton {\n"
"\n"
"background-color: rgba(191, 64, 64, 0);\n"
"\n"
"    padding: 0px; /* \ud328\ub529\ub3c4 0\uc73c\ub85c \uc124\uc815 */\n"
"    outline: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgba(0, 0, 0, 0);\n"
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

        self.horizontalLayout_31.addWidget(self.camera_bnt)

        self.tab_partion_5 = QLabel(self.tab_backgournd)
        self.tab_partion_5.setObjectName(u"tab_partion_5")
        sizePolicy2.setHeightForWidth(self.tab_partion_5.sizePolicy().hasHeightForWidth())
        self.tab_partion_5.setSizePolicy(sizePolicy2)
        self.tab_partion_5.setMinimumSize(QSize(3, 0))
        font10 = QFont()
        font10.setFamilies([u"Sans"])
        font10.setPointSize(14)
        self.tab_partion_5.setFont(font10)
        self.tab_partion_5.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"background-color: rgba(191, 64, 64, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0 0, 0);")
        self.tab_partion_5.setTextFormat(Qt.TextFormat.PlainText)
        self.tab_partion_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_31.addWidget(self.tab_partion_5)

        self.setting_bnt = QPushButton(self.tab_backgournd)
        self.setting_bnt.setObjectName(u"setting_bnt")
        self.setting_bnt.setMinimumSize(QSize(163, 28))
        self.setting_bnt.setMaximumSize(QSize(163, 28))
        self.setting_bnt.setFont(font9)
        self.setting_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setting_bnt.setStyleSheet(u"\n"
"\n"
"\n"
"QPushButton {\n"
"\n"
"background-color: rgba(191, 64, 64, 0);\n"
"\n"
"    padding: 0px; /* \ud328\ub529\ub3c4 0\uc73c\ub85c \uc124\uc815 */\n"
"    outline: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgba(0, 0, 0, 0);\n"
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

        self.horizontalLayout_31.addWidget(self.setting_bnt)

        self.tab_partion_4 = QLabel(self.tab_backgournd)
        self.tab_partion_4.setObjectName(u"tab_partion_4")
        sizePolicy2.setHeightForWidth(self.tab_partion_4.sizePolicy().hasHeightForWidth())
        self.tab_partion_4.setSizePolicy(sizePolicy2)
        self.tab_partion_4.setMinimumSize(QSize(3, 0))
        self.tab_partion_4.setFont(font10)
        self.tab_partion_4.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"background-color: rgba(191, 64, 64, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0 0, 0);")
        self.tab_partion_4.setTextFormat(Qt.TextFormat.PlainText)
        self.tab_partion_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_31.addWidget(self.tab_partion_4)

        self.admin_bnt = QPushButton(self.tab_backgournd)
        self.admin_bnt.setObjectName(u"admin_bnt")
        self.admin_bnt.setMinimumSize(QSize(163, 28))
        self.admin_bnt.setMaximumSize(QSize(163, 28))
        self.admin_bnt.setFont(font9)
        self.admin_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.admin_bnt.setStyleSheet(u"\n"
"\n"
"\n"
"QPushButton {\n"
"\n"
"background-color: rgba(191, 64, 64, 0);\n"
"\n"
"    padding: 0px; /* \ud328\ub529\ub3c4 0\uc73c\ub85c \uc124\uc815 */\n"
"    outline: none;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid rgba(0, 0, 0, 0);\n"
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

        self.horizontalLayout_31.addWidget(self.admin_bnt)


        self.horizontalLayout_23.addLayout(self.horizontalLayout_31)


        self.tab_layout.addWidget(self.tab_backgournd)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.tab_layout.addItem(self.horizontalSpacer_18)

        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalSpacer_17 = QSpacerItem(20, 11, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_55.addItem(self.verticalSpacer_17)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setSpacing(9)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.search_memu_bnt = QPushButton(self.page_2)
        self.search_memu_bnt.setObjectName(u"search_memu_bnt")
        self.search_memu_bnt.setMinimumSize(QSize(35, 35))
        self.search_memu_bnt.setMaximumSize(QSize(35, 35))
        self.search_memu_bnt.setFont(font1)
        self.search_memu_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.search_memu_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/ui/ui/images/search_ico.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_memu_bnt.setIcon(icon4)
        self.search_memu_bnt.setIconSize(QSize(35, 35))

        self.horizontalLayout_36.addWidget(self.search_memu_bnt)

        self.labeling_bnt = QPushButton(self.page_2)
        self.labeling_bnt.setObjectName(u"labeling_bnt")
        self.labeling_bnt.setMinimumSize(QSize(35, 35))
        self.labeling_bnt.setMaximumSize(QSize(35, 35))
        self.labeling_bnt.setFont(font1)
        self.labeling_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.labeling_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/ui/ui/images/ico_ai_setting.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.labeling_bnt.setIcon(icon5)
        self.labeling_bnt.setIconSize(QSize(35, 35))

        self.horizontalLayout_36.addWidget(self.labeling_bnt)

        self.camera_schedule_bnt = QPushButton(self.page_2)
        self.camera_schedule_bnt.setObjectName(u"camera_schedule_bnt")
        self.camera_schedule_bnt.setMinimumSize(QSize(35, 35))
        self.camera_schedule_bnt.setMaximumSize(QSize(35, 35))
        self.camera_schedule_bnt.setFont(font1)
        self.camera_schedule_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.camera_schedule_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/ui/ui/images/ico_timer.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.camera_schedule_bnt.setIcon(icon6)
        self.camera_schedule_bnt.setIconSize(QSize(35, 35))

        self.horizontalLayout_36.addWidget(self.camera_schedule_bnt)


        self.verticalLayout_55.addLayout(self.horizontalLayout_36)


        self.tab_layout.addLayout(self.verticalLayout_55)


        self.verticalLayout_28.addLayout(self.tab_layout)

        self.stackedWidget_2 = QStackedWidget(self.page_2)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy3)
        self.stackedWidget_2.setMinimumSize(QSize(790, 499))
        self.stackedWidget_2.setStyleSheet(u"QScrollBar:vertical {\n"
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
        self.camera_page = QWidget()
        self.camera_page.setObjectName(u"camera_page")
        self.verticalLayout_47 = QVBoxLayout(self.camera_page)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.widget_8 = QWidget(self.camera_page)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(301, 351))
        self.widget_8.setMaximumSize(QSize(350, 9999))
        self.verticalLayout_29 = QVBoxLayout(self.widget_8)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.camera_page_camera_name_label = QLabel(self.widget_8)
        self.camera_page_camera_name_label.setObjectName(u"camera_page_camera_name_label")
        sizePolicy2.setHeightForWidth(self.camera_page_camera_name_label.sizePolicy().hasHeightForWidth())
        self.camera_page_camera_name_label.setSizePolicy(sizePolicy2)
        self.camera_page_camera_name_label.setMinimumSize(QSize(93, 31))
        font11 = QFont()
        font11.setFamilies([u"Sans"])
        font11.setPointSize(12)
        font11.setBold(True)
        self.camera_page_camera_name_label.setFont(font11)
        self.camera_page_camera_name_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.camera_page_camera_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_40.addWidget(self.camera_page_camera_name_label)

        self.camera_page_name_box = QComboBox(self.widget_8)
        self.camera_page_name_box.setObjectName(u"camera_page_name_box")
        self.camera_page_name_box.setMinimumSize(QSize(141, 39))
        self.camera_page_name_box.setMaximumSize(QSize(145, 39))
        font12 = QFont()
        font12.setFamilies([u"Sans"])
        font12.setPointSize(11)
        self.camera_page_name_box.setFont(font12)
        self.camera_page_name_box.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.camera_page_name_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.camera_page_name_box.setCurrentText(u"")
        self.camera_page_name_box.setMaxVisibleItems(16)

        self.horizontalLayout_40.addWidget(self.camera_page_name_box)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_10)


        self.verticalLayout_30.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.camera_page_camera_event_label = QLabel(self.widget_8)
        self.camera_page_camera_event_label.setObjectName(u"camera_page_camera_event_label")
        sizePolicy2.setHeightForWidth(self.camera_page_camera_event_label.sizePolicy().hasHeightForWidth())
        self.camera_page_camera_event_label.setSizePolicy(sizePolicy2)
        self.camera_page_camera_event_label.setMinimumSize(QSize(93, 31))
        self.camera_page_camera_event_label.setFont(font11)
        self.camera_page_camera_event_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.camera_page_camera_event_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_48.addWidget(self.camera_page_camera_event_label)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.camera_page_camera_event_box = QComboBox(self.widget_8)
        self.camera_page_camera_event_box.addItem("")
        self.camera_page_camera_event_box.addItem("")
        self.camera_page_camera_event_box.addItem("")
        self.camera_page_camera_event_box.addItem("")
        self.camera_page_camera_event_box.setObjectName(u"camera_page_camera_event_box")
        sizePolicy2.setHeightForWidth(self.camera_page_camera_event_box.sizePolicy().hasHeightForWidth())
        self.camera_page_camera_event_box.setSizePolicy(sizePolicy2)
        self.camera_page_camera_event_box.setMinimumSize(QSize(141, 39))
        self.camera_page_camera_event_box.setMaximumSize(QSize(141, 39))
        font13 = QFont()
        font13.setFamilies([u"Sans"])
        font13.setPointSize(11)
        font13.setBold(False)
        self.camera_page_camera_event_box.setFont(font13)
        self.camera_page_camera_event_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.camera_page_camera_event_box.setMaxVisibleItems(16)
        self.camera_page_camera_event_box.setMinimumContentsLength(0)

        self.horizontalLayout_49.addWidget(self.camera_page_camera_event_box)

        self.camera_page_detect_add_bnt = QPushButton(self.widget_8)
        self.camera_page_detect_add_bnt.setObjectName(u"camera_page_detect_add_bnt")
        sizePolicy2.setHeightForWidth(self.camera_page_detect_add_bnt.sizePolicy().hasHeightForWidth())
        self.camera_page_detect_add_bnt.setSizePolicy(sizePolicy2)
        self.camera_page_detect_add_bnt.setMinimumSize(QSize(31, 31))
        self.camera_page_detect_add_bnt.setFont(font1)
        self.camera_page_detect_add_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.camera_page_detect_add_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.camera_page_detect_add_bnt.setIcon(icon1)
        self.camera_page_detect_add_bnt.setIconSize(QSize(31, 50))

        self.horizontalLayout_49.addWidget(self.camera_page_detect_add_bnt)


        self.horizontalLayout_48.addLayout(self.horizontalLayout_49)


        self.horizontalLayout_41.addLayout(self.horizontalLayout_48)

        self.horizontalSpacer_31 = QSpacerItem(46, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_31)


        self.verticalLayout_30.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setSpacing(6)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.camera_page_detect_area_table = QTableWidget(self.widget_8)
        if (self.camera_page_detect_area_table.columnCount() < 1):
            self.camera_page_detect_area_table.setColumnCount(1)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.camera_page_detect_area_table.setHorizontalHeaderItem(0, __qtablewidgetitem45)
        self.camera_page_detect_area_table.setObjectName(u"camera_page_detect_area_table")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.camera_page_detect_area_table.sizePolicy().hasHeightForWidth())
        self.camera_page_detect_area_table.setSizePolicy(sizePolicy4)
        self.camera_page_detect_area_table.setMinimumSize(QSize(231, 273))
        self.camera_page_detect_area_table.setMaximumSize(QSize(231, 9999))
        self.camera_page_detect_area_table.setFont(font)
        self.camera_page_detect_area_table.setStyleSheet(u"QTableWidget {\n"
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
        self.camera_page_detect_area_table.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.camera_page_detect_area_table.setDragDropOverwriteMode(False)
        self.camera_page_detect_area_table.setAlternatingRowColors(False)
        self.camera_page_detect_area_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.camera_page_detect_area_table.setShowGrid(False)
        self.camera_page_detect_area_table.setGridStyle(Qt.PenStyle.NoPen)
        self.camera_page_detect_area_table.setWordWrap(False)
        self.camera_page_detect_area_table.setCornerButtonEnabled(False)
        self.camera_page_detect_area_table.horizontalHeader().setHighlightSections(False)
        self.camera_page_detect_area_table.horizontalHeader().setStretchLastSection(True)
        self.camera_page_detect_area_table.verticalHeader().setVisible(False)
        self.camera_page_detect_area_table.verticalHeader().setHighlightSections(False)

        self.verticalLayout_31.addWidget(self.camera_page_detect_area_table)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalSpacer_33 = QSpacerItem(166, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_33)

        self.camera_page_object_setting_bnt = QPushButton(self.widget_8)
        self.camera_page_object_setting_bnt.setObjectName(u"camera_page_object_setting_bnt")
        sizePolicy2.setHeightForWidth(self.camera_page_object_setting_bnt.sizePolicy().hasHeightForWidth())
        self.camera_page_object_setting_bnt.setSizePolicy(sizePolicy2)
        self.camera_page_object_setting_bnt.setMinimumSize(QSize(100, 30))
        self.camera_page_object_setting_bnt.setMaximumSize(QSize(100, 30))
        self.camera_page_object_setting_bnt.setFont(font1)
        self.camera_page_object_setting_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.camera_page_object_setting_bnt.setStyleSheet(u"background-color: rgb(36, 39, 44);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"\n"
"")

        self.horizontalLayout_51.addWidget(self.camera_page_object_setting_bnt)

        self.camera_page_detect_area_del_bnt = QPushButton(self.widget_8)
        self.camera_page_detect_area_del_bnt.setObjectName(u"camera_page_detect_area_del_bnt")
        sizePolicy2.setHeightForWidth(self.camera_page_detect_area_del_bnt.sizePolicy().hasHeightForWidth())
        self.camera_page_detect_area_del_bnt.setSizePolicy(sizePolicy2)
        self.camera_page_detect_area_del_bnt.setMinimumSize(QSize(61, 31))
        self.camera_page_detect_area_del_bnt.setMaximumSize(QSize(61, 31))
        self.camera_page_detect_area_del_bnt.setFont(font1)
        self.camera_page_detect_area_del_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.camera_page_detect_area_del_bnt.setStyleSheet(u"background-color: rgb(255, 49, 38);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"")

        self.horizontalLayout_51.addWidget(self.camera_page_detect_area_del_bnt)


        self.verticalLayout_31.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalSpacer_14 = QSpacerItem(129, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_14)

        self.camera_page_ai_bnt = QPushButton(self.widget_8)
        self.camera_page_ai_bnt.setObjectName(u"camera_page_ai_bnt")
        sizePolicy2.setHeightForWidth(self.camera_page_ai_bnt.sizePolicy().hasHeightForWidth())
        self.camera_page_ai_bnt.setSizePolicy(sizePolicy2)
        self.camera_page_ai_bnt.setMinimumSize(QSize(122, 33))
        self.camera_page_ai_bnt.setFont(font1)
        self.camera_page_ai_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.camera_page_ai_bnt.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.0 rgba(112, 210, 112, 255),\n"
"    stop:0.3 rgba(0, 196, 0, 255)\n"
");\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"\n"
"")

        self.horizontalLayout_52.addWidget(self.camera_page_ai_bnt)


        self.verticalLayout_31.addLayout(self.horizontalLayout_52)


        self.horizontalLayout_50.addLayout(self.verticalLayout_31)

        self.horizontalSpacer_44 = QSpacerItem(63, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_44)


        self.verticalLayout_30.addLayout(self.horizontalLayout_50)

        self.verticalSpacer_7 = QSpacerItem(20, 270, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_30.addItem(self.verticalSpacer_7)


        self.verticalLayout_29.addLayout(self.verticalLayout_30)


        self.horizontalLayout_24.addWidget(self.widget_8)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.widget_9 = QWidget(self.camera_page)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 0))
        self.widget_9.setMaximumSize(QSize(16777215, 25))
        self.verticalLayout_33 = QVBoxLayout(self.widget_9)
        self.verticalLayout_33.setSpacing(6)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.camera_page_block_label = QLabel(self.widget_9)
        self.camera_page_block_label.setObjectName(u"camera_page_block_label")
        sizePolicy2.setHeightForWidth(self.camera_page_block_label.sizePolicy().hasHeightForWidth())
        self.camera_page_block_label.setSizePolicy(sizePolicy2)
        self.camera_page_block_label.setMinimumSize(QSize(63, 21))
        self.camera_page_block_label.setMaximumSize(QSize(260, 21))
        self.camera_page_block_label.setFont(font12)
        self.camera_page_block_label.setStyleSheet(u"color: rgb(242, 18, 94);")
        self.camera_page_block_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_63.addWidget(self.camera_page_block_label)


        self.horizontalLayout_54.addLayout(self.horizontalLayout_63)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_45)

        self.camera_page_ai_active_icon = QLabel(self.widget_9)
        self.camera_page_ai_active_icon.setObjectName(u"camera_page_ai_active_icon")
        sizePolicy2.setHeightForWidth(self.camera_page_ai_active_icon.sizePolicy().hasHeightForWidth())
        self.camera_page_ai_active_icon.setSizePolicy(sizePolicy2)
        self.camera_page_ai_active_icon.setMinimumSize(QSize(21, 21))
        self.camera_page_ai_active_icon.setMaximumSize(QSize(21, 21))
        self.camera_page_ai_active_icon.setFont(font)
        self.camera_page_ai_active_icon.setStyleSheet(u"color: rgb(242, 18, 94);")
        self.camera_page_ai_active_icon.setPixmap(QPixmap(u":/ui/ui/images/ico_analysis_on.svg"))
        self.camera_page_ai_active_icon.setScaledContents(True)

        self.horizontalLayout_54.addWidget(self.camera_page_ai_active_icon)

        self.camera_page_ai_active_label = QLabel(self.widget_9)
        self.camera_page_ai_active_label.setObjectName(u"camera_page_ai_active_label")
        sizePolicy2.setHeightForWidth(self.camera_page_ai_active_label.sizePolicy().hasHeightForWidth())
        self.camera_page_ai_active_label.setSizePolicy(sizePolicy2)
        self.camera_page_ai_active_label.setMinimumSize(QSize(130, 21))
        self.camera_page_ai_active_label.setMaximumSize(QSize(130, 21))
        self.camera_page_ai_active_label.setFont(font12)
        self.camera_page_ai_active_label.setStyleSheet(u"color: rgb(242, 18, 94);")

        self.horizontalLayout_54.addWidget(self.camera_page_ai_active_label)


        self.verticalLayout_33.addLayout(self.horizontalLayout_54)


        self.verticalLayout_32.addWidget(self.widget_9)

        self.ai_camera_page_verticalLayout = QVBoxLayout()
        self.ai_camera_page_verticalLayout.setSpacing(0)
        self.ai_camera_page_verticalLayout.setObjectName(u"ai_camera_page_verticalLayout")
        self.verticalSpacer_26 = QSpacerItem(20, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.ai_camera_page_verticalLayout.addItem(self.verticalSpacer_26)

        self.camera_page_viewer = QLabel(self.camera_page)
        self.camera_page_viewer.setObjectName(u"camera_page_viewer")
        sizePolicy3.setHeightForWidth(self.camera_page_viewer.sizePolicy().hasHeightForWidth())
        self.camera_page_viewer.setSizePolicy(sizePolicy3)
        self.camera_page_viewer.setMinimumSize(QSize(325, 360))
        self.camera_page_viewer.setMaximumSize(QSize(9999, 9999))
        self.camera_page_viewer.setFont(font12)
        self.camera_page_viewer.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.camera_page_viewer.setScaledContents(False)

        self.ai_camera_page_verticalLayout.addWidget(self.camera_page_viewer)


        self.verticalLayout_32.addLayout(self.ai_camera_page_verticalLayout)


        self.horizontalLayout_53.addLayout(self.verticalLayout_32)


        self.horizontalLayout_24.addLayout(self.horizontalLayout_53)


        self.verticalLayout_47.addLayout(self.horizontalLayout_24)

        self.stackedWidget_2.addWidget(self.camera_page)
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.verticalLayout_53 = QVBoxLayout(self.setting_page)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.setting_scrollArea = QScrollArea(self.setting_page)
        self.setting_scrollArea.setObjectName(u"setting_scrollArea")
        self.setting_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1148, 702))
        self.verticalLayout_34 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.widget_13 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_51 = QVBoxLayout(self.widget_13)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalSpacer_51 = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_51)

        self.setting_detect_info_label = QLabel(self.widget_13)
        self.setting_detect_info_label.setObjectName(u"setting_detect_info_label")
        self.setting_detect_info_label.setMinimumSize(QSize(197, 28))
        self.setting_detect_info_label.setMaximumSize(QSize(9999, 28))
        font14 = QFont()
        font14.setFamilies([u"Sans"])
        font14.setPointSize(11)
        font14.setBold(True)
        self.setting_detect_info_label.setFont(font14)
        self.setting_detect_info_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_detect_info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_61.addWidget(self.setting_detect_info_label)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_32)


        self.verticalLayout_51.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalSpacer_34 = QSpacerItem(232, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_76.addItem(self.horizontalSpacer_34)

        self.setting_detect_bbox_active_label = QLabel(self.widget_13)
        self.setting_detect_bbox_active_label.setObjectName(u"setting_detect_bbox_active_label")
        self.setting_detect_bbox_active_label.setMinimumSize(QSize(91, 28))
        self.setting_detect_bbox_active_label.setMaximumSize(QSize(91, 28))
        self.setting_detect_bbox_active_label.setFont(font12)
        self.setting_detect_bbox_active_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_detect_bbox_active_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_76.addWidget(self.setting_detect_bbox_active_label)

        self.setting_detect_bbox_active_bnt = QPushButton(self.widget_13)
        self.setting_detect_bbox_active_bnt.setObjectName(u"setting_detect_bbox_active_bnt")
        self.setting_detect_bbox_active_bnt.setMinimumSize(QSize(61, 25))
        self.setting_detect_bbox_active_bnt.setMaximumSize(QSize(61, 25))
        self.setting_detect_bbox_active_bnt.setStyleSheet(u"QPushButton {\n"
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
        icon7 = QIcon()
        icon7.addFile(u":/ui/ui/images/icon-switch-off.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/ui/ui/images/icon-switch-on.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon7.addFile(u":/ui/ui/images/icon-switch-off.png", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        icon7.addFile(u":/ui/ui/images/icon-switch-on.png", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.setting_detect_bbox_active_bnt.setIcon(icon7)
        self.setting_detect_bbox_active_bnt.setIconSize(QSize(55, 103))
        self.setting_detect_bbox_active_bnt.setCheckable(True)

        self.horizontalLayout_76.addWidget(self.setting_detect_bbox_active_bnt)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_76.addItem(self.horizontalSpacer_35)


        self.verticalLayout_51.addLayout(self.horizontalLayout_76)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalSpacer_107 = QSpacerItem(232, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_77.addItem(self.horizontalSpacer_107)

        self.setting_detect_label_active_label = QLabel(self.widget_13)
        self.setting_detect_label_active_label.setObjectName(u"setting_detect_label_active_label")
        self.setting_detect_label_active_label.setMinimumSize(QSize(91, 28))
        self.setting_detect_label_active_label.setMaximumSize(QSize(91, 28))
        self.setting_detect_label_active_label.setFont(font12)
        self.setting_detect_label_active_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_detect_label_active_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_77.addWidget(self.setting_detect_label_active_label)

        self.setting_detect_label_active_bnt = QPushButton(self.widget_13)
        self.setting_detect_label_active_bnt.setObjectName(u"setting_detect_label_active_bnt")
        self.setting_detect_label_active_bnt.setMinimumSize(QSize(61, 25))
        self.setting_detect_label_active_bnt.setMaximumSize(QSize(61, 25))
        self.setting_detect_label_active_bnt.setStyleSheet(u"QPushButton {\n"
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
        self.setting_detect_label_active_bnt.setIcon(icon7)
        self.setting_detect_label_active_bnt.setIconSize(QSize(55, 103))
        self.setting_detect_label_active_bnt.setCheckable(True)

        self.horizontalLayout_77.addWidget(self.setting_detect_label_active_bnt)

        self.horizontalSpacer_108 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_77.addItem(self.horizontalSpacer_108)


        self.verticalLayout_51.addLayout(self.horizontalLayout_77)

        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalSpacer_109 = QSpacerItem(216, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_78.addItem(self.horizontalSpacer_109)

        self.setting_detect_roi_active_label = QLabel(self.widget_13)
        self.setting_detect_roi_active_label.setObjectName(u"setting_detect_roi_active_label")
        self.setting_detect_roi_active_label.setMinimumSize(QSize(107, 28))
        self.setting_detect_roi_active_label.setMaximumSize(QSize(117, 28))
        self.setting_detect_roi_active_label.setFont(font12)
        self.setting_detect_roi_active_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_detect_roi_active_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_78.addWidget(self.setting_detect_roi_active_label)

        self.setting_detect_roi_active_bnt = QPushButton(self.widget_13)
        self.setting_detect_roi_active_bnt.setObjectName(u"setting_detect_roi_active_bnt")
        self.setting_detect_roi_active_bnt.setMinimumSize(QSize(61, 25))
        self.setting_detect_roi_active_bnt.setMaximumSize(QSize(61, 25))
        self.setting_detect_roi_active_bnt.setStyleSheet(u"QPushButton {\n"
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
        self.setting_detect_roi_active_bnt.setIcon(icon7)
        self.setting_detect_roi_active_bnt.setIconSize(QSize(55, 103))
        self.setting_detect_roi_active_bnt.setCheckable(True)

        self.horizontalLayout_78.addWidget(self.setting_detect_roi_active_bnt)

        self.horizontalSpacer_110 = QSpacerItem(38, 25, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_78.addItem(self.horizontalSpacer_110)


        self.verticalLayout_51.addLayout(self.horizontalLayout_78)


        self.verticalLayout_36.addWidget(self.widget_13)

        self.setting_partion_4 = QFrame(self.scrollAreaWidgetContents_2)
        self.setting_partion_4.setObjectName(u"setting_partion_4")
        sizePolicy2.setHeightForWidth(self.setting_partion_4.sizePolicy().hasHeightForWidth())
        self.setting_partion_4.setSizePolicy(sizePolicy2)
        self.setting_partion_4.setMinimumSize(QSize(246, 3))
        self.setting_partion_4.setMaximumSize(QSize(434, 3))
        self.setting_partion_4.setFont(font5)
        self.setting_partion_4.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setting_partion_4.setAutoFillBackground(False)
        self.setting_partion_4.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.setting_partion_4.setFrameShape(QFrame.Shape.HLine)
        self.setting_partion_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_36.addWidget(self.setting_partion_4)

        self.setting_self_labeling_widget = QWidget(self.scrollAreaWidgetContents_2)
        self.setting_self_labeling_widget.setObjectName(u"setting_self_labeling_widget")
        self.verticalLayout_52 = QVBoxLayout(self.setting_self_labeling_widget)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalSpacer_52 = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_79.addItem(self.horizontalSpacer_52)

        self.setting_label_4 = QLabel(self.setting_self_labeling_widget)
        self.setting_label_4.setObjectName(u"setting_label_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.setting_label_4.sizePolicy().hasHeightForWidth())
        self.setting_label_4.setSizePolicy(sizePolicy5)
        self.setting_label_4.setMinimumSize(QSize(122, 22))
        self.setting_label_4.setMaximumSize(QSize(208, 22))
        self.setting_label_4.setFont(font14)
        self.setting_label_4.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_79.addWidget(self.setting_label_4)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_79.addItem(self.horizontalSpacer_36)


        self.verticalLayout_52.addLayout(self.horizontalLayout_79)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalSpacer_69 = QSpacerItem(36, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_80.addItem(self.horizontalSpacer_69)

        self.setting_ai_weight_label = QLabel(self.setting_self_labeling_widget)
        self.setting_ai_weight_label.setObjectName(u"setting_ai_weight_label")
        sizePolicy2.setHeightForWidth(self.setting_ai_weight_label.sizePolicy().hasHeightForWidth())
        self.setting_ai_weight_label.setSizePolicy(sizePolicy2)
        self.setting_ai_weight_label.setMinimumSize(QSize(176, 28))
        self.setting_ai_weight_label.setMaximumSize(QSize(9999, 28))
        self.setting_ai_weight_label.setFont(font12)
        self.setting_ai_weight_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_ai_weight_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_80.addWidget(self.setting_ai_weight_label)

        self.horizontalSpacer_111 = QSpacerItem(59, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_80.addItem(self.horizontalSpacer_111)

        self.setting_setting_ai_weight_box = QComboBox(self.setting_self_labeling_widget)
        self.setting_setting_ai_weight_box.addItem("")
        self.setting_setting_ai_weight_box.setObjectName(u"setting_setting_ai_weight_box")
        sizePolicy2.setHeightForWidth(self.setting_setting_ai_weight_box.sizePolicy().hasHeightForWidth())
        self.setting_setting_ai_weight_box.setSizePolicy(sizePolicy2)
        self.setting_setting_ai_weight_box.setMinimumSize(QSize(105, 31))
        self.setting_setting_ai_weight_box.setMaximumSize(QSize(105, 31))
        self.setting_setting_ai_weight_box.setFont(font4)
        self.setting_setting_ai_weight_box.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.setting_setting_ai_weight_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.setting_setting_ai_weight_box.setCurrentText(u"1234-12-12")
        self.setting_setting_ai_weight_box.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)

        self.horizontalLayout_80.addWidget(self.setting_setting_ai_weight_box)

        self.horizontalSpacer_112 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_80.addItem(self.horizontalSpacer_112)


        self.verticalLayout_52.addLayout(self.horizontalLayout_80)

        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalSpacer_113 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_113)

        self.setting_self_training_auto_labeling_label = QLabel(self.setting_self_labeling_widget)
        self.setting_self_training_auto_labeling_label.setObjectName(u"setting_self_training_auto_labeling_label")
        sizePolicy2.setHeightForWidth(self.setting_self_training_auto_labeling_label.sizePolicy().hasHeightForWidth())
        self.setting_self_training_auto_labeling_label.setSizePolicy(sizePolicy2)
        self.setting_self_training_auto_labeling_label.setMinimumSize(QSize(1, 28))
        self.setting_self_training_auto_labeling_label.setMaximumSize(QSize(194, 28))
        self.setting_self_training_auto_labeling_label.setFont(font12)
        self.setting_self_training_auto_labeling_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_self_training_auto_labeling_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_81.addWidget(self.setting_self_training_auto_labeling_label)

        self.horizontalSpacer_114 = QSpacerItem(92, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_114)

        self.setting_self_training_auto_labeling_bnt = QPushButton(self.setting_self_labeling_widget)
        self.setting_self_training_auto_labeling_bnt.setObjectName(u"setting_self_training_auto_labeling_bnt")
        sizePolicy2.setHeightForWidth(self.setting_self_training_auto_labeling_bnt.sizePolicy().hasHeightForWidth())
        self.setting_self_training_auto_labeling_bnt.setSizePolicy(sizePolicy2)
        self.setting_self_training_auto_labeling_bnt.setMinimumSize(QSize(61, 25))
        self.setting_self_training_auto_labeling_bnt.setMaximumSize(QSize(187, 25))
        self.setting_self_training_auto_labeling_bnt.setStyleSheet(u"QPushButton {\n"
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
        self.setting_self_training_auto_labeling_bnt.setIcon(icon7)
        self.setting_self_training_auto_labeling_bnt.setIconSize(QSize(55, 103))
        self.setting_self_training_auto_labeling_bnt.setCheckable(True)

        self.horizontalLayout_81.addWidget(self.setting_self_training_auto_labeling_bnt)

        self.horizontalSpacer_115 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_115)


        self.verticalLayout_52.addLayout(self.horizontalLayout_81)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalSpacer_135 = QSpacerItem(199, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_135)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(9)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.setting_auto_label_time_start_box = QComboBox(self.setting_self_labeling_widget)
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.setObjectName(u"setting_auto_label_time_start_box")
        sizePolicy2.setHeightForWidth(self.setting_auto_label_time_start_box.sizePolicy().hasHeightForWidth())
        self.setting_auto_label_time_start_box.setSizePolicy(sizePolicy2)
        self.setting_auto_label_time_start_box.setMinimumSize(QSize(80, 24))
        self.setting_auto_label_time_start_box.setMaximumSize(QSize(68, 24))
        self.setting_auto_label_time_start_box.setFont(font4)
        self.setting_auto_label_time_start_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(13, 16, 23);\n"
"\n"
"")
        self.setting_auto_label_time_start_box.setEditable(True)
        self.setting_auto_label_time_start_box.setMinimumContentsLength(0)

        self.horizontalLayout_27.addWidget(self.setting_auto_label_time_start_box)

        self.time_tilde_2 = QLabel(self.setting_self_labeling_widget)
        self.time_tilde_2.setObjectName(u"time_tilde_2")
        sizePolicy2.setHeightForWidth(self.time_tilde_2.sizePolicy().hasHeightForWidth())
        self.time_tilde_2.setSizePolicy(sizePolicy2)
        font15 = QFont()
        font15.setFamilies([u"Sans"])
        font15.setPointSize(12)
        self.time_tilde_2.setFont(font15)
        self.time_tilde_2.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(191, 64, 64, 0);")
        self.time_tilde_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_27.addWidget(self.time_tilde_2)

        self.setting_auto_label_time_end_box = QComboBox(self.setting_self_labeling_widget)
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.setObjectName(u"setting_auto_label_time_end_box")
        sizePolicy2.setHeightForWidth(self.setting_auto_label_time_end_box.sizePolicy().hasHeightForWidth())
        self.setting_auto_label_time_end_box.setSizePolicy(sizePolicy2)
        self.setting_auto_label_time_end_box.setMinimumSize(QSize(80, 24))
        self.setting_auto_label_time_end_box.setMaximumSize(QSize(68, 24))
        self.setting_auto_label_time_end_box.setFont(font4)
        self.setting_auto_label_time_end_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(13, 16, 23);\n"
"\n"
"")
        self.setting_auto_label_time_end_box.setEditable(True)
        self.setting_auto_label_time_end_box.setMinimumContentsLength(0)

        self.horizontalLayout_27.addWidget(self.setting_auto_label_time_end_box)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_27)

        self.horizontalSpacer_136 = QSpacerItem(11, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_136)


        self.verticalLayout_52.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalSpacer_116 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_116)

        self.setting_page_email_info_label_10 = QLabel(self.setting_self_labeling_widget)
        self.setting_page_email_info_label_10.setObjectName(u"setting_page_email_info_label_10")
        sizePolicy2.setHeightForWidth(self.setting_page_email_info_label_10.sizePolicy().hasHeightForWidth())
        self.setting_page_email_info_label_10.setSizePolicy(sizePolicy2)
        self.setting_page_email_info_label_10.setMinimumSize(QSize(12, 21))
        self.setting_page_email_info_label_10.setMaximumSize(QSize(9999, 21))
        self.setting_page_email_info_label_10.setFont(font1)
        self.setting_page_email_info_label_10.setStyleSheet(u"color: rgb(242, 18, 94);")

        self.horizontalLayout_28.addWidget(self.setting_page_email_info_label_10)

        self.horizontalSpacer_117 = QSpacerItem(4, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_117)


        self.verticalLayout_52.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalSpacer_118 = QSpacerItem(41, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_82.addItem(self.horizontalSpacer_118)

        self.setting_self_training_zeroshot_label = QLabel(self.setting_self_labeling_widget)
        self.setting_self_training_zeroshot_label.setObjectName(u"setting_self_training_zeroshot_label")
        sizePolicy2.setHeightForWidth(self.setting_self_training_zeroshot_label.sizePolicy().hasHeightForWidth())
        self.setting_self_training_zeroshot_label.setSizePolicy(sizePolicy2)
        self.setting_self_training_zeroshot_label.setMinimumSize(QSize(9, 28))
        self.setting_self_training_zeroshot_label.setMaximumSize(QSize(300, 28))
        self.setting_self_training_zeroshot_label.setFont(font12)
        self.setting_self_training_zeroshot_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_self_training_zeroshot_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_82.addWidget(self.setting_self_training_zeroshot_label)

        self.horizontalSpacer_119 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_82.addItem(self.horizontalSpacer_119)

        self.setting_self_training_zeroshot_bnt = QPushButton(self.setting_self_labeling_widget)
        self.setting_self_training_zeroshot_bnt.setObjectName(u"setting_self_training_zeroshot_bnt")
        sizePolicy2.setHeightForWidth(self.setting_self_training_zeroshot_bnt.sizePolicy().hasHeightForWidth())
        self.setting_self_training_zeroshot_bnt.setSizePolicy(sizePolicy2)
        self.setting_self_training_zeroshot_bnt.setMinimumSize(QSize(61, 25))
        self.setting_self_training_zeroshot_bnt.setMaximumSize(QSize(151, 25))
        self.setting_self_training_zeroshot_bnt.setStyleSheet(u"QPushButton {\n"
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
        self.setting_self_training_zeroshot_bnt.setIcon(icon7)
        self.setting_self_training_zeroshot_bnt.setIconSize(QSize(55, 103))
        self.setting_self_training_zeroshot_bnt.setCheckable(True)

        self.horizontalLayout_82.addWidget(self.setting_self_training_zeroshot_bnt)

        self.horizontalSpacer_120 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_82.addItem(self.horizontalSpacer_120)


        self.verticalLayout_52.addLayout(self.horizontalLayout_82)

        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalSpacer_121 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_83.addItem(self.horizontalSpacer_121)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.setting_page_email_info_label_9 = QLabel(self.setting_self_labeling_widget)
        self.setting_page_email_info_label_9.setObjectName(u"setting_page_email_info_label_9")
        sizePolicy2.setHeightForWidth(self.setting_page_email_info_label_9.sizePolicy().hasHeightForWidth())
        self.setting_page_email_info_label_9.setSizePolicy(sizePolicy2)
        self.setting_page_email_info_label_9.setMinimumSize(QSize(12, 21))
        self.setting_page_email_info_label_9.setMaximumSize(QSize(9999, 21))
        self.setting_page_email_info_label_9.setFont(font1)
        self.setting_page_email_info_label_9.setStyleSheet(u"color: rgb(242, 18, 94);")

        self.verticalLayout_37.addWidget(self.setting_page_email_info_label_9)

        self.setting_page_email_info_label_11 = QLabel(self.setting_self_labeling_widget)
        self.setting_page_email_info_label_11.setObjectName(u"setting_page_email_info_label_11")
        sizePolicy2.setHeightForWidth(self.setting_page_email_info_label_11.sizePolicy().hasHeightForWidth())
        self.setting_page_email_info_label_11.setSizePolicy(sizePolicy2)
        self.setting_page_email_info_label_11.setMinimumSize(QSize(12, 21))
        self.setting_page_email_info_label_11.setMaximumSize(QSize(9999, 21))
        self.setting_page_email_info_label_11.setFont(font1)
        self.setting_page_email_info_label_11.setStyleSheet(u"color: rgb(242, 18, 94);")

        self.verticalLayout_37.addWidget(self.setting_page_email_info_label_11)


        self.horizontalLayout_83.addLayout(self.verticalLayout_37)

        self.horizontalSpacer_122 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_83.addItem(self.horizontalSpacer_122)


        self.verticalLayout_52.addLayout(self.horizontalLayout_83)

        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalSpacer_123 = QSpacerItem(338, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_84.addItem(self.horizontalSpacer_123)

        self.setting_ai_setting_save_bnt = QPushButton(self.setting_self_labeling_widget)
        self.setting_ai_setting_save_bnt.setObjectName(u"setting_ai_setting_save_bnt")
        sizePolicy.setHeightForWidth(self.setting_ai_setting_save_bnt.sizePolicy().hasHeightForWidth())
        self.setting_ai_setting_save_bnt.setSizePolicy(sizePolicy)
        self.setting_ai_setting_save_bnt.setMinimumSize(QSize(71, 41))
        self.setting_ai_setting_save_bnt.setMaximumSize(QSize(71, 41))
        self.setting_ai_setting_save_bnt.setFont(font1)
        self.setting_ai_setting_save_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setting_ai_setting_save_bnt.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.0 rgba(112, 210, 112, 255),\n"
"    stop:0.3 rgba(0, 196, 0, 255)\n"
");\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 19px;\n"
"\n"
"")

        self.horizontalLayout_84.addWidget(self.setting_ai_setting_save_bnt)

        self.horizontalSpacer_124 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_84.addItem(self.horizontalSpacer_124)


        self.verticalLayout_52.addLayout(self.horizontalLayout_84)

        self.setting_partion_5 = QFrame(self.setting_self_labeling_widget)
        self.setting_partion_5.setObjectName(u"setting_partion_5")
        sizePolicy2.setHeightForWidth(self.setting_partion_5.sizePolicy().hasHeightForWidth())
        self.setting_partion_5.setSizePolicy(sizePolicy2)
        self.setting_partion_5.setMinimumSize(QSize(246, 3))
        self.setting_partion_5.setMaximumSize(QSize(434, 3))
        self.setting_partion_5.setFont(font5)
        self.setting_partion_5.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setting_partion_5.setAutoFillBackground(False)
        self.setting_partion_5.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.setting_partion_5.setFrameShape(QFrame.Shape.HLine)
        self.setting_partion_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_52.addWidget(self.setting_partion_5)


        self.verticalLayout_36.addWidget(self.setting_self_labeling_widget)


        self.verticalLayout_35.addLayout(self.verticalLayout_36)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_5)


        self.horizontalLayout_25.addLayout(self.verticalLayout_35)

        self.horizontalSpacer_6 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_6)


        self.verticalLayout_34.addLayout(self.horizontalLayout_25)

        self.setting_scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_53.addWidget(self.setting_scrollArea)

        self.stackedWidget_2.addWidget(self.setting_page)
        self.admin_page = QWidget()
        self.admin_page.setObjectName(u"admin_page")
        self.verticalLayout_41 = QVBoxLayout(self.admin_page)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_42.addItem(self.verticalSpacer_14)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_37)

        self.admin_pw_label = QLabel(self.admin_page)
        self.admin_pw_label.setObjectName(u"admin_pw_label")
        self.admin_pw_label.setMinimumSize(QSize(115, 46))
        self.admin_pw_label.setMaximumSize(QSize(115, 46))
        self.admin_pw_label.setFont(font15)
        self.admin_pw_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.admin_pw_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.admin_pw_label)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(-1, -1, -1, 0)
        self.admin_pw_input = QLineEdit(self.admin_page)
        self.admin_pw_input.setObjectName(u"admin_pw_input")
        self.admin_pw_input.setMinimumSize(QSize(221, 21))
        self.admin_pw_input.setMaximumSize(QSize(221, 21))
        self.admin_pw_input.setFont(font1)
        self.admin_pw_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.admin_pw_input.setStyleSheet(u"qproperty-frame: false;\n"
"font-size:10pt;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.admin_pw_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_43.addWidget(self.admin_pw_input)

        self.admin_pw_input_line = QFrame(self.admin_page)
        self.admin_pw_input_line.setObjectName(u"admin_pw_input_line")
        self.admin_pw_input_line.setMinimumSize(QSize(221, 3))
        self.admin_pw_input_line.setMaximumSize(QSize(221, 3))
        self.admin_pw_input_line.setFont(font5)
        self.admin_pw_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.admin_pw_input_line.setAutoFillBackground(False)
        self.admin_pw_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.admin_pw_input_line.setFrameShape(QFrame.Shape.HLine)
        self.admin_pw_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_43.addWidget(self.admin_pw_input_line)


        self.horizontalLayout_38.addLayout(self.verticalLayout_43)

        self.admin_page_bnt = QPushButton(self.admin_page)
        self.admin_page_bnt.setObjectName(u"admin_page_bnt")
        self.admin_page_bnt.setMinimumSize(QSize(71, 41))
        self.admin_page_bnt.setMaximumSize(QSize(71, 41))
        self.admin_page_bnt.setFont(font1)
        self.admin_page_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.admin_page_bnt.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.0 rgba(112, 210, 112, 255),\n"
"    stop:0.3 rgba(0, 196, 0, 255)\n"
");\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")

        self.horizontalLayout_38.addWidget(self.admin_page_bnt)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_38)


        self.verticalLayout_42.addLayout(self.horizontalLayout_38)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_42.addItem(self.verticalSpacer_15)


        self.verticalLayout_41.addLayout(self.verticalLayout_42)

        self.stackedWidget_2.addWidget(self.admin_page)
        self.admin_page_2 = QWidget()
        self.admin_page_2.setObjectName(u"admin_page_2")
        self.horizontalLayout_47 = QHBoxLayout(self.admin_page_2)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.widget_11 = QWidget(self.admin_page_2)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_50 = QVBoxLayout(self.widget_11)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.admin_license_bnt = QPushButton(self.widget_11)
        self.admin_license_bnt.setObjectName(u"admin_license_bnt")
        sizePolicy3.setHeightForWidth(self.admin_license_bnt.sizePolicy().hasHeightForWidth())
        self.admin_license_bnt.setSizePolicy(sizePolicy3)
        self.admin_license_bnt.setMinimumSize(QSize(171, 41))
        self.admin_license_bnt.setMaximumSize(QSize(171, 41))
        self.admin_license_bnt.setFont(font12)
        self.admin_license_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.admin_license_bnt.setStyleSheet(u"border-radius: 20px;\n"
"border: 1px solid rgb(179,179,179);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(3, 3, 13);\n"
"")
        self.admin_license_bnt.setCheckable(True)
        self.admin_license_bnt.setChecked(False)
        self.admin_license_bnt.setAutoExclusive(True)

        self.verticalLayout_48.addWidget(self.admin_license_bnt)

        self.admin_fn_permission_bnt = QPushButton(self.widget_11)
        self.admin_fn_permission_bnt.setObjectName(u"admin_fn_permission_bnt")
        sizePolicy3.setHeightForWidth(self.admin_fn_permission_bnt.sizePolicy().hasHeightForWidth())
        self.admin_fn_permission_bnt.setSizePolicy(sizePolicy3)
        self.admin_fn_permission_bnt.setMinimumSize(QSize(171, 41))
        self.admin_fn_permission_bnt.setMaximumSize(QSize(171, 41))
        self.admin_fn_permission_bnt.setFont(font12)
        self.admin_fn_permission_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.admin_fn_permission_bnt.setStyleSheet(u"border-radius: 20px;\n"
"border: 1px solid rgb(179,179,179);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(3, 3, 13);\n"
"")
        self.admin_fn_permission_bnt.setCheckable(True)
        self.admin_fn_permission_bnt.setChecked(False)
        self.admin_fn_permission_bnt.setAutoExclusive(True)

        self.verticalLayout_48.addWidget(self.admin_fn_permission_bnt)


        self.verticalLayout_49.addLayout(self.verticalLayout_48)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_49.addItem(self.verticalSpacer_23)


        self.verticalLayout_50.addLayout(self.verticalLayout_49)


        self.horizontalLayout_47.addWidget(self.widget_11)

        self.stackedWidget_3 = QStackedWidget(self.admin_page_2)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: rgb(13, 16, 23);\n"
"")
        self.license_page = QWidget()
        self.license_page.setObjectName(u"license_page")
        self.horizontalLayout_35 = QHBoxLayout(self.license_page)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setSpacing(20)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.horizontalLayout_95 = QHBoxLayout()
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalSpacer_133 = QSpacerItem(36, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_95.addItem(self.horizontalSpacer_133)

        self.horizontalLayout_96 = QHBoxLayout()
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.license_camera_allow_num_label = QLabel(self.license_page)
        self.license_camera_allow_num_label.setObjectName(u"license_camera_allow_num_label")
        sizePolicy5.setHeightForWidth(self.license_camera_allow_num_label.sizePolicy().hasHeightForWidth())
        self.license_camera_allow_num_label.setSizePolicy(sizePolicy5)
        self.license_camera_allow_num_label.setMinimumSize(QSize(166, 27))
        self.license_camera_allow_num_label.setMaximumSize(QSize(166, 27))
        self.license_camera_allow_num_label.setFont(font12)
        self.license_camera_allow_num_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.license_camera_allow_num_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_96.addWidget(self.license_camera_allow_num_label)

        self.verticalLayout_60 = QVBoxLayout()
        self.verticalLayout_60.setSpacing(1)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.license_camera_allow_num_input = QLineEdit(self.license_page)
        self.license_camera_allow_num_input.setObjectName(u"license_camera_allow_num_input")
        sizePolicy2.setHeightForWidth(self.license_camera_allow_num_input.sizePolicy().hasHeightForWidth())
        self.license_camera_allow_num_input.setSizePolicy(sizePolicy2)
        self.license_camera_allow_num_input.setMinimumSize(QSize(94, 19))
        self.license_camera_allow_num_input.setMaximumSize(QSize(94, 19))
        self.license_camera_allow_num_input.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.license_camera_allow_num_input.setEchoMode(QLineEdit.EchoMode.Normal)
        self.license_camera_allow_num_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_60.addWidget(self.license_camera_allow_num_input)

        self.license_camera_allow_num_input_line = QFrame(self.license_page)
        self.license_camera_allow_num_input_line.setObjectName(u"license_camera_allow_num_input_line")
        sizePolicy2.setHeightForWidth(self.license_camera_allow_num_input_line.sizePolicy().hasHeightForWidth())
        self.license_camera_allow_num_input_line.setSizePolicy(sizePolicy2)
        self.license_camera_allow_num_input_line.setMinimumSize(QSize(94, 3))
        self.license_camera_allow_num_input_line.setMaximumSize(QSize(94, 3))
        self.license_camera_allow_num_input_line.setFont(font5)
        self.license_camera_allow_num_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.license_camera_allow_num_input_line.setAutoFillBackground(False)
        self.license_camera_allow_num_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.license_camera_allow_num_input_line.setFrameShape(QFrame.Shape.HLine)
        self.license_camera_allow_num_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_60.addWidget(self.license_camera_allow_num_input_line)


        self.horizontalLayout_96.addLayout(self.verticalLayout_60)


        self.horizontalLayout_95.addLayout(self.horizontalLayout_96)

        self.horizontalSpacer_134 = QSpacerItem(40, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_95.addItem(self.horizontalSpacer_134)


        self.verticalLayout_46.addLayout(self.horizontalLayout_95)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalSpacer_42 = QSpacerItem(259, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_42)

        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setSpacing(3)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.non_active_license_label = QLabel(self.license_page)
        self.non_active_license_label.setObjectName(u"non_active_license_label")
        self.non_active_license_label.setMinimumSize(QSize(171, 31))
        self.non_active_license_label.setMaximumSize(QSize(171, 31))
        font16 = QFont()
        font16.setFamilies([u"Ubuntu Light"])
        font16.setPointSize(11)
        font16.setBold(True)
        self.non_active_license_label.setFont(font16)
        self.non_active_license_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: rgb(32,39,49);\n"
"\n"
"")
        self.non_active_license_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_45.addWidget(self.non_active_license_label)

        self.widget_12 = QWidget(self.license_page)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(171, 0))
        self.widget_12.setMaximumSize(QSize(171, 16777215))
        self.widget_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: rgb(32,39,49);\n"
"\n"
"")
        self.verticalLayout_61 = QVBoxLayout(self.widget_12)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.non_active_license_list = QListWidget(self.widget_12)
        QListWidgetItem(self.non_active_license_list)
        QListWidgetItem(self.non_active_license_list)
        QListWidgetItem(self.non_active_license_list)
        QListWidgetItem(self.non_active_license_list)
        QListWidgetItem(self.non_active_license_list)
        self.non_active_license_list.setObjectName(u"non_active_license_list")
        self.non_active_license_list.setMinimumSize(QSize(156, 397))
        self.non_active_license_list.setMaximumSize(QSize(156, 16777215))
        font17 = QFont()
        font17.setPointSize(11)
        font17.setBold(False)
        font17.setItalic(False)
        font17.setUnderline(False)
        font17.setStrikeOut(False)
        font17.setKerning(True)
        self.non_active_license_list.setFont(font17)
        self.non_active_license_list.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.non_active_license_list.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.non_active_license_list.setAcceptDrops(True)
        self.non_active_license_list.setStyleSheet(u"QListWidget::item {\n"
"    padding: 3px;\n"
"}\n"
"QListWidget::item:selected {\n"
"    background-color: rgba(19, 193, 13, 200);\n"
"    border: 2px solid green;\n"
"    border-radius: 5px; /* \ub465\uadfc \ud14c\ub450\ub9ac \ucd94\uac00 */\n"
"}\n"
"")
        self.non_active_license_list.setFrameShape(QFrame.Shape.NoFrame)
        self.non_active_license_list.setLineWidth(1)
        self.non_active_license_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.non_active_license_list.setTabKeyNavigation(False)
        self.non_active_license_list.setProperty(u"showDropIndicator", True)
        self.non_active_license_list.setDragEnabled(True)
        self.non_active_license_list.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.non_active_license_list.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.non_active_license_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.non_active_license_list.setTextElideMode(Qt.TextElideMode.ElideLeft)
        self.non_active_license_list.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.non_active_license_list.setMovement(QListView.Movement.Static)
        self.non_active_license_list.setFlow(QListView.Flow.TopToBottom)
        self.non_active_license_list.setProperty(u"isWrapping", False)
        self.non_active_license_list.setResizeMode(QListView.ResizeMode.Fixed)
        self.non_active_license_list.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.non_active_license_list.setSpacing(1)
        self.non_active_license_list.setModelColumn(0)
        self.non_active_license_list.setUniformItemSizes(True)
        self.non_active_license_list.setWordWrap(False)
        self.non_active_license_list.setSelectionRectVisible(True)

        self.verticalLayout_61.addWidget(self.non_active_license_list)


        self.verticalLayout_45.addWidget(self.widget_12)


        self.horizontalLayout_42.addLayout(self.verticalLayout_45)

        self.verticalLayout_63 = QVBoxLayout()
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_63.addItem(self.verticalSpacer_16)

        self.license_add_bnt = QPushButton(self.license_page)
        self.license_add_bnt.setObjectName(u"license_add_bnt")
        self.license_add_bnt.setMinimumSize(QSize(41, 41))
        self.license_add_bnt.setMaximumSize(QSize(41, 41))
        font18 = QFont()
        font18.setPointSize(10)
        self.license_add_bnt.setFont(font18)
        self.license_add_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.license_add_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/ui/ui/images/ico_arrow_right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.license_add_bnt.setIcon(icon8)
        self.license_add_bnt.setIconSize(QSize(31, 50))

        self.verticalLayout_63.addWidget(self.license_add_bnt)

        self.license_remove_bnt = QPushButton(self.license_page)
        self.license_remove_bnt.setObjectName(u"license_remove_bnt")
        self.license_remove_bnt.setMinimumSize(QSize(41, 41))
        self.license_remove_bnt.setMaximumSize(QSize(41, 41))
        self.license_remove_bnt.setFont(font18)
        self.license_remove_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.license_remove_bnt.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.license_remove_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"Rotation: ( origin.x: 25; origin.y: 25; angle: 45);")
        icon9 = QIcon()
        icon9.addFile(u":/ui/ui/images/ico_arrow_left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.license_remove_bnt.setIcon(icon9)
        self.license_remove_bnt.setIconSize(QSize(31, 50))

        self.verticalLayout_63.addWidget(self.license_remove_bnt)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_63.addItem(self.verticalSpacer_18)


        self.horizontalLayout_42.addLayout(self.verticalLayout_63)

        self.verticalLayout_64 = QVBoxLayout()
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.active_license_label = QLabel(self.license_page)
        self.active_license_label.setObjectName(u"active_license_label")
        self.active_license_label.setMinimumSize(QSize(171, 31))
        self.active_license_label.setMaximumSize(QSize(171, 31))
        self.active_license_label.setFont(font16)
        self.active_license_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: rgb(32,39,49);\n"
"\n"
"")
        self.active_license_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_64.addWidget(self.active_license_label)

        self.widget_16 = QWidget(self.license_page)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(171, 0))
        self.widget_16.setMaximumSize(QSize(171, 16777215))
        self.widget_16.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: rgb(32,39,49);\n"
"\n"
"")
        self.verticalLayout_65 = QVBoxLayout(self.widget_16)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.active_license_list = QListWidget(self.widget_16)
        QListWidgetItem(self.active_license_list)
        QListWidgetItem(self.active_license_list)
        QListWidgetItem(self.active_license_list)
        QListWidgetItem(self.active_license_list)
        self.active_license_list.setObjectName(u"active_license_list")
        self.active_license_list.setMinimumSize(QSize(156, 397))
        self.active_license_list.setMaximumSize(QSize(156, 16777215))
        self.active_license_list.setFont(font17)
        self.active_license_list.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.active_license_list.setAcceptDrops(True)
        self.active_license_list.setStyleSheet(u"QListWidget::item {\n"
"    padding: 3px;\n"
"}\n"
"QListWidget::item:selected {\n"
"    background-color: rgba(19, 193, 13, 200);\n"
"    border: 2px solid green;\n"
"    border-radius: 5px; /* \ub465\uadfc \ud14c\ub450\ub9ac \ucd94\uac00 */\n"
"}\n"
"")
        self.active_license_list.setFrameShape(QFrame.Shape.NoFrame)
        self.active_license_list.setLineWidth(1)
        self.active_license_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.active_license_list.setTabKeyNavigation(False)
        self.active_license_list.setProperty(u"showDropIndicator", False)
        self.active_license_list.setDragEnabled(True)
        self.active_license_list.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.active_license_list.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.active_license_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.active_license_list.setTextElideMode(Qt.TextElideMode.ElideLeft)
        self.active_license_list.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.active_license_list.setMovement(QListView.Movement.Static)
        self.active_license_list.setFlow(QListView.Flow.TopToBottom)
        self.active_license_list.setProperty(u"isWrapping", False)
        self.active_license_list.setResizeMode(QListView.ResizeMode.Fixed)
        self.active_license_list.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.active_license_list.setSpacing(1)
        self.active_license_list.setModelColumn(0)
        self.active_license_list.setUniformItemSizes(True)
        self.active_license_list.setWordWrap(False)
        self.active_license_list.setSelectionRectVisible(True)

        self.verticalLayout_65.addWidget(self.active_license_list)


        self.verticalLayout_64.addWidget(self.widget_16)


        self.horizontalLayout_42.addLayout(self.verticalLayout_64)


        self.verticalLayout_44.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_39)

        self.license_save_bnt = QPushButton(self.license_page)
        self.license_save_bnt.setObjectName(u"license_save_bnt")
        sizePolicy3.setHeightForWidth(self.license_save_bnt.sizePolicy().hasHeightForWidth())
        self.license_save_bnt.setSizePolicy(sizePolicy3)
        self.license_save_bnt.setMinimumSize(QSize(71, 41))
        self.license_save_bnt.setMaximumSize(QSize(71, 41))
        self.license_save_bnt.setFont(font18)
        self.license_save_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.license_save_bnt.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.0 rgba(112, 210, 112, 255),\n"
"    stop:0.3 rgba(0, 196, 0, 255)\n"
");\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"\n"
"")

        self.horizontalLayout_43.addWidget(self.license_save_bnt)


        self.verticalLayout_44.addLayout(self.horizontalLayout_43)


        self.horizontalLayout_46.addLayout(self.verticalLayout_44)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_43)


        self.verticalLayout_46.addLayout(self.horizontalLayout_46)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_22)


        self.horizontalLayout_35.addLayout(self.verticalLayout_46)

        self.stackedWidget_3.addWidget(self.license_page)
        self.fn_permission_page = QWidget()
        self.fn_permission_page.setObjectName(u"fn_permission_page")
        self.verticalLayout_66 = QVBoxLayout(self.fn_permission_page)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_67 = QVBoxLayout()
        self.verticalLayout_67.setSpacing(9)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_67.addItem(self.verticalSpacer_20)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalSpacer_46 = QSpacerItem(43, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_46)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setSpacing(17)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.admin_self_labeling_fn_active_label = QLabel(self.fn_permission_page)
        self.admin_self_labeling_fn_active_label.setObjectName(u"admin_self_labeling_fn_active_label")
        self.admin_self_labeling_fn_active_label.setMinimumSize(QSize(160, 25))
        self.admin_self_labeling_fn_active_label.setMaximumSize(QSize(167, 25))
        self.admin_self_labeling_fn_active_label.setFont(font12)
        self.admin_self_labeling_fn_active_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.admin_self_labeling_fn_active_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_39.addWidget(self.admin_self_labeling_fn_active_label)

        self.admin_self_labeling_fn_active_bnt = QPushButton(self.fn_permission_page)
        self.admin_self_labeling_fn_active_bnt.setObjectName(u"admin_self_labeling_fn_active_bnt")
        self.admin_self_labeling_fn_active_bnt.setMinimumSize(QSize(61, 25))
        self.admin_self_labeling_fn_active_bnt.setMaximumSize(QSize(61, 25))
        icon10 = QIcon()
        icon10.addFile(u":/ui/ui/images/icon-switch-off.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/ui/ui/images/icon-switch-on.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.admin_self_labeling_fn_active_bnt.setIcon(icon10)
        self.admin_self_labeling_fn_active_bnt.setIconSize(QSize(55, 103))
        self.admin_self_labeling_fn_active_bnt.setCheckable(True)

        self.horizontalLayout_39.addWidget(self.admin_self_labeling_fn_active_bnt)


        self.horizontalLayout_37.addLayout(self.horizontalLayout_39)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_47)


        self.verticalLayout_67.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalSpacer_48 = QSpacerItem(267, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_48)

        self.admin_fn_save_bnt = QPushButton(self.fn_permission_page)
        self.admin_fn_save_bnt.setObjectName(u"admin_fn_save_bnt")
        sizePolicy3.setHeightForWidth(self.admin_fn_save_bnt.sizePolicy().hasHeightForWidth())
        self.admin_fn_save_bnt.setSizePolicy(sizePolicy3)
        self.admin_fn_save_bnt.setMinimumSize(QSize(71, 41))
        self.admin_fn_save_bnt.setMaximumSize(QSize(71, 41))
        self.admin_fn_save_bnt.setFont(font18)
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

        self.horizontalLayout_57.addWidget(self.admin_fn_save_bnt)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_49)


        self.verticalLayout_67.addLayout(self.horizontalLayout_57)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_67.addItem(self.verticalSpacer_19)


        self.verticalLayout_66.addLayout(self.verticalLayout_67)

        self.stackedWidget_3.addWidget(self.fn_permission_page)

        self.horizontalLayout_47.addWidget(self.stackedWidget_3)

        self.stackedWidget_2.addWidget(self.admin_page_2)

        self.verticalLayout_28.addWidget(self.stackedWidget_2)


        self.horizontalLayout_32.addLayout(self.verticalLayout_28)


        self.verticalLayout_69.addLayout(self.horizontalLayout_32)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_11.addWidget(self.stackedWidget)


        self.horizontalLayout_58.addLayout(self.verticalLayout_11)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)
        self.setting_setting_ai_weight_box.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MS-AI 1000", None))
        self.top_logo.setText("")
        self.verson_label.setText(QCoreApplication.translate("MainWindow", u"MS-AI1000 1.7.0", None))
        self.server_icon.setText("")
        self.shutdown_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc774\uc804", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"NVR \uc815\ubcf4", None))
        self.nvr_add_bnt.setText("")
        self.nvr_del_bnt.setText("")
        ___qtablewidgetitem = self.nvr_list_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\ubc88\ud638", None));
        ___qtablewidgetitem1 = self.nvr_list_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NVR \uc774\ub984", None));
        ___qtablewidgetitem2 = self.nvr_list_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\uc18c", None));
        ___qtablewidgetitem3 = self.nvr_list_table.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"2", None));

        __sortingEnabled = self.nvr_list_table.isSortingEnabled()
        self.nvr_list_table.setSortingEnabled(False)
        ___qtablewidgetitem4 = self.nvr_list_table.item(0, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"nvr2", None));
        ___qtablewidgetitem5 = self.nvr_list_table.item(0, 2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"192.123.123.123", None));
        ___qtablewidgetitem6 = self.nvr_list_table.item(1, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"nvr3", None));
        ___qtablewidgetitem7 = self.nvr_list_table.item(1, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"192.123.123.123", None));
        ___qtablewidgetitem8 = self.nvr_list_table.item(2, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"nvr4", None));
        ___qtablewidgetitem9 = self.nvr_list_table.item(2, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"192.123.123.123", None));
        self.nvr_list_table.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc18d\uc131", None))
        self.nvr_name_label.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub984", None))
        self.nvr_name_input.setText("")
        self.nvr_ip_label.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\uc18c", None))
        self.nvr_ip_input.setText("")
        self.nvr_port_label.setText(QCoreApplication.translate("MainWindow", u"\ud3ec\ud2b8", None))
        self.nvr_port_input.setText(QCoreApplication.translate("MainWindow", u"8081", None))
        self.nvr_http_port_label.setText(QCoreApplication.translate("MainWindow", u"HTTP \ud3ec\ud2b8", None))
        self.nvr_http_port_input.setText(QCoreApplication.translate("MainWindow", u"80", None))
        self.nvr_id_label.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\uc790", None))
        self.nvr_id_input.setText("")
        self.nvr_passward_label.setText(QCoreApplication.translate("MainWindow", u"\ube44\ubc00\ubc88\ud638", None))
        self.nvr_passward_input.setText("")
        self.nvr_save_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
        self.label_3.setText("")
#if QT_CONFIG(statustip)
        self.nvr_search_input.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.nvr_search_input.setText(QCoreApplication.translate("MainWindow", u"\uce74\uba54\ub77c \uac80\uc0c9....", None))
        self.nvr_search_input.setPlaceholderText("")
        ___qtreewidgetitem = self.nvr_server_tree_list.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\uc774\ub984", None));

        __sortingEnabled1 = self.nvr_server_tree_list.isSortingEnabled()
        self.nvr_server_tree_list.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.nvr_server_tree_list.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"192.123.123.123", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"\uce74\uba54\ub77c1", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"\uce74\uba54\ub77c2", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"\uce74\uba54\ub77c3", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem1.child(3)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"\uce74\uba54\ub77c4", None));
        ___qtreewidgetitem6 = self.nvr_server_tree_list.topLevelItem(1)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"192.123.123.001", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem6.child(0)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"\uce74\uba54\ub77c1", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem6.child(1)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"\uce74\uba54\ub77c2", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem6.child(2)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"\uce74\uba54\ub77c3", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem6.child(3)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"\uce74\uba54\ub77c4", None));
        self.nvr_server_tree_list.setSortingEnabled(__sortingEnabled1)

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \uc11c\ubc84 \uc815\ubcf4", None))
        self.server_list_setting_bnt.setText("")
        self.ai_server_add_bnt.setText("")
        self.ai_server_del_bnt.setText("")
        ___qtablewidgetitem10 = self.ai_server_table.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\ubc88\ud638", None));
        ___qtablewidgetitem11 = self.ai_server_table.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub984", None));
        ___qtablewidgetitem12 = self.ai_server_table.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\uc18c", None));
        ___qtablewidgetitem13 = self.ai_server_table.verticalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"2", None));

        __sortingEnabled2 = self.ai_server_table.isSortingEnabled()
        self.ai_server_table.setSortingEnabled(False)
        ___qtablewidgetitem14 = self.ai_server_table.item(0, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem15 = self.ai_server_table.item(0, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"server1", None));
        ___qtablewidgetitem16 = self.ai_server_table.item(0, 2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"192.123.123.123", None));
        ___qtablewidgetitem17 = self.ai_server_table.item(1, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem18 = self.ai_server_table.item(1, 1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"server2", None));
        ___qtablewidgetitem19 = self.ai_server_table.item(1, 2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"192.123.123.123", None));
        ___qtablewidgetitem20 = self.ai_server_table.item(2, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem21 = self.ai_server_table.item(2, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"server3", None));
        ___qtablewidgetitem22 = self.ai_server_table.item(2, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"192.123.123.123", None));
        self.ai_server_table.setSortingEnabled(__sortingEnabled2)

        self.ai_server_name_label.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub984", None))
        self.ai_server_name_input.setText("")
        self.ai_server_ip_label.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\uc18c", None))
        self.ai_server_ip_input.setText("")
        self.ai_server_port_label.setText(QCoreApplication.translate("MainWindow", u"\ud3ec\ud2b8", None))
        self.ai_server_port_input.setText(QCoreApplication.translate("MainWindow", u"65432", None))
        self.ai_server_id_label.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\uc790", None))
        self.ai_server_id_input.setText("")
        self.ai_server_passward_label.setText(QCoreApplication.translate("MainWindow", u"\ube44\ubc00\ubc88\ud638", None))
        self.ai_server_passward_input.setText("")
        self.ai_server_save_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
        self.label_5.setText("")
#if QT_CONFIG(statustip)
        self.ai_server_camera_search_input.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.ai_server_camera_search_input.setText(QCoreApplication.translate("MainWindow", u"\uce74\uba54\ub77c \uac80\uc0c9....", None))
        self.ai_server_camera_search_input.setPlaceholderText("")
        ___qtablewidgetitem23 = self.ai_server_info_table.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\ubc88\ud638", None));
        ___qtablewidgetitem24 = self.ai_server_info_table.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\uce74\uba54\ub77c \uc774\ub984", None));
        ___qtablewidgetitem25 = self.ai_server_info_table.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\uce74\uba54\ub77c \uc8fc\uc18c", None));
        ___qtablewidgetitem26 = self.ai_server_info_table.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"NVR \uc774\ub984", None));
        ___qtablewidgetitem27 = self.ai_server_info_table.horizontalHeaderItem(4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"NVR \uc8fc\uc18c", None));

        __sortingEnabled3 = self.ai_server_info_table.isSortingEnabled()
        self.ai_server_info_table.setSortingEnabled(False)
        ___qtablewidgetitem28 = self.ai_server_info_table.item(0, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem29 = self.ai_server_info_table.item(0, 1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\uce74\uba54\ub77c1", None));
        ___qtablewidgetitem30 = self.ai_server_info_table.item(0, 2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"192.123.123.123", None));
        ___qtablewidgetitem31 = self.ai_server_info_table.item(0, 3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"NVR1", None));
        ___qtablewidgetitem32 = self.ai_server_info_table.item(0, 4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"172.123.123.123", None));
        ___qtablewidgetitem33 = self.ai_server_info_table.item(1, 0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem34 = self.ai_server_info_table.item(1, 1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\uce74\uba54\ub77c2", None));
        ___qtablewidgetitem35 = self.ai_server_info_table.item(1, 2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"192.123.123.123", None));
        ___qtablewidgetitem36 = self.ai_server_info_table.item(1, 3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"NVR2", None));
        ___qtablewidgetitem37 = self.ai_server_info_table.item(1, 4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"173.123.123.123", None));
        self.ai_server_info_table.setSortingEnabled(__sortingEnabled3)

        ___qtablewidgetitem38 = self.camera_list_table.horizontalHeaderItem(1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem39 = self.camera_list_table.horizontalHeaderItem(2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Addrees", None));
        ___qtablewidgetitem40 = self.camera_list_table.horizontalHeaderItem(3)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"NVR", None));
        self.camera_bnt.setText(QCoreApplication.translate("MainWindow", u"AI Camera", None))
        self.tab_partion_5.setText(QCoreApplication.translate("MainWindow", u"|", None))
        self.setting_bnt.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.tab_partion_4.setText(QCoreApplication.translate("MainWindow", u"|", None))
        self.admin_bnt.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.search_memu_bnt.setText("")
        self.labeling_bnt.setText("")
        self.camera_schedule_bnt.setText("")
        self.camera_page_camera_name_label.setText(QCoreApplication.translate("MainWindow", u"\uce74\uba54\ub77c \uc774\ub984", None))
        self.camera_page_camera_event_label.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubca4\ud2b8 \uc885\ub958", None))
        self.camera_page_camera_event_box.setItemText(0, QCoreApplication.translate("MainWindow", u"\uce68\uc785", None))
        self.camera_page_camera_event_box.setItemText(1, QCoreApplication.translate("MainWindow", u"\ubc30\ud68c", None))
        self.camera_page_camera_event_box.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc4f0\ub7ec\uc9d0", None))
        self.camera_page_camera_event_box.setItemText(3, QCoreApplication.translate("MainWindow", u"\ubc29\ud654", None))

        self.camera_page_detect_add_bnt.setText("")
        ___qtablewidgetitem41 = self.camera_page_detect_area_table.horizontalHeaderItem(0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"\uac10\uc9c0 \uc601\uc5ed \ub9ac\uc2a4\ud2b8", None));
        self.camera_page_object_setting_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \ubd84\uc11d \uc124\uc815", None))
        self.camera_page_detect_area_del_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.camera_page_ai_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \ubd84\uc11d \uc2dc\uc791", None))
        self.camera_page_block_label.setText(QCoreApplication.translate("MainWindow", u"\u203b\uc6b4\uc601 \uc815\ucc45\uc0c1 LIVE \ud654\uba74\uc744 \ucc28\ub2e8\ud569\ub2c8\ub2e4.", None))
        self.camera_page_ai_active_icon.setText("")
        self.camera_page_ai_active_label.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \ubd84\uc11d \uc9c4\ud589\uc911", None))
        self.camera_page_viewer.setText("")
        self.setting_detect_info_label.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \uac80\ucd9c \uc815\ubcf4 \ud45c\uc2dc \uc124\uc815", None))
        self.setting_detect_bbox_active_label.setText(QCoreApplication.translate("MainWindow", u"BBox \ud65c\uc131\ud654", None))
        self.setting_detect_bbox_active_bnt.setText("")
        self.setting_detect_label_active_label.setText(QCoreApplication.translate("MainWindow", u"Label \ud65c\uc131\ud654", None))
        self.setting_detect_label_active_bnt.setText("")
        self.setting_detect_roi_active_label.setText(QCoreApplication.translate("MainWindow", u"\uad00\uc2ec\uc601\uc5ed \ud65c\uc131\ud654", None))
        self.setting_detect_roi_active_bnt.setText("")
        self.setting_label_4.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 AI \uc5d4\uc9c4 \uc124\uc815", None))
        self.setting_ai_weight_label.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \uac1d\uccb4 \uc778\uc2dd \ubaa8\ub378 \uc120\ud14d", None))
        self.setting_setting_ai_weight_box.setItemText(0, QCoreApplication.translate("MainWindow", u"1234-12-12", None))

        self.setting_setting_ai_weight_box.setPlaceholderText("")
        self.setting_self_training_auto_labeling_label.setText(QCoreApplication.translate("MainWindow", u"Self Auto Labeling \ud65c\uc131\ud654", None))
        self.setting_self_training_auto_labeling_bnt.setText("")
        self.setting_auto_label_time_start_box.setItemText(0, QCoreApplication.translate("MainWindow", u"00:00", None))
        self.setting_auto_label_time_start_box.setItemText(1, QCoreApplication.translate("MainWindow", u"01:00", None))
        self.setting_auto_label_time_start_box.setItemText(2, QCoreApplication.translate("MainWindow", u"02:00", None))
        self.setting_auto_label_time_start_box.setItemText(3, QCoreApplication.translate("MainWindow", u"03:00", None))
        self.setting_auto_label_time_start_box.setItemText(4, QCoreApplication.translate("MainWindow", u"04:00", None))
        self.setting_auto_label_time_start_box.setItemText(5, QCoreApplication.translate("MainWindow", u"05:00", None))
        self.setting_auto_label_time_start_box.setItemText(6, QCoreApplication.translate("MainWindow", u"06:00", None))
        self.setting_auto_label_time_start_box.setItemText(7, QCoreApplication.translate("MainWindow", u"07:00", None))
        self.setting_auto_label_time_start_box.setItemText(8, QCoreApplication.translate("MainWindow", u"08:00", None))
        self.setting_auto_label_time_start_box.setItemText(9, QCoreApplication.translate("MainWindow", u"09:00", None))
        self.setting_auto_label_time_start_box.setItemText(10, QCoreApplication.translate("MainWindow", u"10:00", None))
        self.setting_auto_label_time_start_box.setItemText(11, QCoreApplication.translate("MainWindow", u"11:00", None))
        self.setting_auto_label_time_start_box.setItemText(12, QCoreApplication.translate("MainWindow", u"12:00", None))
        self.setting_auto_label_time_start_box.setItemText(13, QCoreApplication.translate("MainWindow", u"13:00", None))
        self.setting_auto_label_time_start_box.setItemText(14, QCoreApplication.translate("MainWindow", u"14:00", None))
        self.setting_auto_label_time_start_box.setItemText(15, QCoreApplication.translate("MainWindow", u"15:00", None))
        self.setting_auto_label_time_start_box.setItemText(16, QCoreApplication.translate("MainWindow", u"16:00", None))
        self.setting_auto_label_time_start_box.setItemText(17, QCoreApplication.translate("MainWindow", u"17:00", None))
        self.setting_auto_label_time_start_box.setItemText(18, QCoreApplication.translate("MainWindow", u"18:00", None))
        self.setting_auto_label_time_start_box.setItemText(19, QCoreApplication.translate("MainWindow", u"19:00", None))
        self.setting_auto_label_time_start_box.setItemText(20, QCoreApplication.translate("MainWindow", u"20:00", None))
        self.setting_auto_label_time_start_box.setItemText(21, QCoreApplication.translate("MainWindow", u"21:00", None))
        self.setting_auto_label_time_start_box.setItemText(22, QCoreApplication.translate("MainWindow", u"22:00", None))
        self.setting_auto_label_time_start_box.setItemText(23, QCoreApplication.translate("MainWindow", u"23:00", None))

        self.time_tilde_2.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.setting_auto_label_time_end_box.setItemText(0, QCoreApplication.translate("MainWindow", u"00:00", None))
        self.setting_auto_label_time_end_box.setItemText(1, QCoreApplication.translate("MainWindow", u"01:00", None))
        self.setting_auto_label_time_end_box.setItemText(2, QCoreApplication.translate("MainWindow", u"02:00", None))
        self.setting_auto_label_time_end_box.setItemText(3, QCoreApplication.translate("MainWindow", u"03:00", None))
        self.setting_auto_label_time_end_box.setItemText(4, QCoreApplication.translate("MainWindow", u"04:00", None))
        self.setting_auto_label_time_end_box.setItemText(5, QCoreApplication.translate("MainWindow", u"05:00", None))
        self.setting_auto_label_time_end_box.setItemText(6, QCoreApplication.translate("MainWindow", u"06:00", None))
        self.setting_auto_label_time_end_box.setItemText(7, QCoreApplication.translate("MainWindow", u"07:00", None))
        self.setting_auto_label_time_end_box.setItemText(8, QCoreApplication.translate("MainWindow", u"08:00", None))
        self.setting_auto_label_time_end_box.setItemText(9, QCoreApplication.translate("MainWindow", u"09:00", None))
        self.setting_auto_label_time_end_box.setItemText(10, QCoreApplication.translate("MainWindow", u"10:00", None))
        self.setting_auto_label_time_end_box.setItemText(11, QCoreApplication.translate("MainWindow", u"11:00", None))
        self.setting_auto_label_time_end_box.setItemText(12, QCoreApplication.translate("MainWindow", u"12:00", None))
        self.setting_auto_label_time_end_box.setItemText(13, QCoreApplication.translate("MainWindow", u"13:00", None))
        self.setting_auto_label_time_end_box.setItemText(14, QCoreApplication.translate("MainWindow", u"14:00", None))
        self.setting_auto_label_time_end_box.setItemText(15, QCoreApplication.translate("MainWindow", u"15:00", None))
        self.setting_auto_label_time_end_box.setItemText(16, QCoreApplication.translate("MainWindow", u"16:00", None))
        self.setting_auto_label_time_end_box.setItemText(17, QCoreApplication.translate("MainWindow", u"17:00", None))
        self.setting_auto_label_time_end_box.setItemText(18, QCoreApplication.translate("MainWindow", u"18:00", None))
        self.setting_auto_label_time_end_box.setItemText(19, QCoreApplication.translate("MainWindow", u"19:00", None))
        self.setting_auto_label_time_end_box.setItemText(20, QCoreApplication.translate("MainWindow", u"20:00", None))
        self.setting_auto_label_time_end_box.setItemText(21, QCoreApplication.translate("MainWindow", u"21:00", None))
        self.setting_auto_label_time_end_box.setItemText(22, QCoreApplication.translate("MainWindow", u"22:00", None))
        self.setting_auto_label_time_end_box.setItemText(23, QCoreApplication.translate("MainWindow", u"23:00", None))

        self.setting_page_email_info_label_10.setText(QCoreApplication.translate("MainWindow", u"\u203bSelf Auto Labeling \ud65c\uc131\ud654\uc2dc \uc9c0\uc815\ub41c \uc2dc\uac04\uc5d0 \uc790\ub3d9\uc73c\ub85c Labeling\uc744 \uc2dc\uc791\ud569\ub2c8\ub2e4.", None))
        self.setting_self_training_zeroshot_label.setText(QCoreApplication.translate("MainWindow", u"AI Labeling Assistance \ud65c\uc131\ud654", None))
        self.setting_self_training_zeroshot_bnt.setText("")
        self.setting_page_email_info_label_9.setText(QCoreApplication.translate("MainWindow", u"\u203bAI Labeling Assistance \uc740 \uc0c8\ub85c\uc6b4 \ud658\uacbd\uc5d0\uc11c  \ucd08\uae30  \ubaa8\ub378 \ud559\uc2b5 \uc131\ub2a5 \uac1c\uc120\uc744 \ub3c4\uc640\uc90d\ub2c8\ub2e4.", None))
        self.setting_page_email_info_label_11.setText(QCoreApplication.translate("MainWindow", u"  (\uc8fc\uc758 : AI Labeling \uc18c\uc694 \uc2dc\uac04 \uc99d\uac00)", None))
        self.setting_ai_setting_save_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
        self.admin_pw_label.setText(QCoreApplication.translate("MainWindow", u"\uad00\ub9ac\uc790 \ube44\ubc00\ubc88\ud638", None))
        self.admin_pw_input.setText(QCoreApplication.translate("MainWindow", u"asdsad", None))
        self.admin_page_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc785\ub825", None))
        self.admin_license_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \ub77c\uc774\uc13c\uc2a4 \uc124\uc815", None))
        self.admin_fn_permission_bnt.setText(QCoreApplication.translate("MainWindow", u"\uae30\ub2a5 \uad8c\ud55c \uc124\uc815", None))
        self.license_camera_allow_num_label.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \uad6c\ub3d9 \uce74\uba54\ub77c \ud5c8\uc6a9 \uc218", None))
        self.license_camera_allow_num_input.setText("")
        self.non_active_license_label.setText(QCoreApplication.translate("MainWindow", u"\ube44\ud65c\uc131 \ub77c\uc774\uc13c\uc2a4", None))

        __sortingEnabled4 = self.non_active_license_list.isSortingEnabled()
        self.non_active_license_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.non_active_license_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\uce68\uc785", None));
        ___qlistwidgetitem1 = self.non_active_license_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\ubc30\ud68c", None));
        ___qlistwidgetitem2 = self.non_active_license_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\ubc29\ud654", None));
        ___qlistwidgetitem3 = self.non_active_license_list.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\uc4f0\ub7ec\uc9d0", None));
        ___qlistwidgetitem4 = self.non_active_license_list.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\uc2f8\uc6c0", None));
        self.non_active_license_list.setSortingEnabled(__sortingEnabled4)

        self.license_add_bnt.setText("")
        self.license_remove_bnt.setText("")
        self.active_license_label.setText(QCoreApplication.translate("MainWindow", u"\ud65c\uc131 \ub77c\uc774\uc13c\uc2a4", None))

        __sortingEnabled5 = self.active_license_list.isSortingEnabled()
        self.active_license_list.setSortingEnabled(False)
        ___qlistwidgetitem5 = self.active_license_list.item(0)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem6 = self.active_license_list.item(1)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem7 = self.active_license_list.item(2)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem8 = self.active_license_list.item(3)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.active_license_list.setSortingEnabled(__sortingEnabled5)

        self.license_save_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
        self.admin_self_labeling_fn_active_label.setText(QCoreApplication.translate("MainWindow", u"\uc790\uac00\ud559\uc2b5 \uae30\ub2a5 \ud65c\uc131\ud654", None))
        self.admin_self_labeling_fn_active_bnt.setText("")
        self.admin_fn_save_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
    # retranslateUi


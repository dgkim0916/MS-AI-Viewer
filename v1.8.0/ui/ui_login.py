# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginatyNcb.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resourece_rc
import resourece_rc

class Ui_login_windows(object):
    def setupUi(self, login_windows):
        if not login_windows.objectName():
            login_windows.setObjectName(u"login_windows")
        login_windows.resize(640, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login_windows.sizePolicy().hasHeightForWidth())
        login_windows.setSizePolicy(sizePolicy)
        login_windows.setMinimumSize(QSize(640, 650))
        login_windows.setMaximumSize(QSize(1280, 720))
        icon = QIcon()
        icon.addFile(u":/ui/ui/images/icon2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        login_windows.setWindowIcon(icon)
        login_windows.setAutoFillBackground(False)
        login_windows.setStyleSheet(u"background-color: rgb(9, 9, 9);")
        self.verticalLayout_10 = QVBoxLayout(login_windows)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.widget = QWidget(login_windows)
        self.widget.setObjectName(u"widget")
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(u"background-color: rgb(32, 32, 32);\n"
"border-radius: 20px")
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(13)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.logo = QLabel(self.widget)
        self.logo.setObjectName(u"logo")
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setPixmap(QPixmap(u":/ui/ui/images/logo.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.logo)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.id_input = QLineEdit(self.widget)
        self.id_input.setObjectName(u"id_input")
        sizePolicy.setHeightForWidth(self.id_input.sizePolicy().hasHeightForWidth())
        self.id_input.setSizePolicy(sizePolicy)
        self.id_input.setMinimumSize(QSize(300, 0))
        font1 = QFont()
        font1.setPointSize(11)
        self.id_input.setFont(font1)
        self.id_input.setStyleSheet(u"font-size:11pt;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.id_input)

        self.id_line = QFrame(self.widget)
        self.id_line.setObjectName(u"id_line")
        sizePolicy.setHeightForWidth(self.id_line.sizePolicy().hasHeightForWidth())
        self.id_line.setSizePolicy(sizePolicy)
        self.id_line.setMaximumSize(QSize(16777215, 1))
        font2 = QFont()
        font2.setPointSize(5)
        font2.setStrikeOut(False)
        self.id_line.setFont(font2)
        self.id_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.id_line.setAutoFillBackground(False)
        self.id_line.setStyleSheet(u"background-color: rgb(45, 45, 45)")
        self.id_line.setFrameShape(QFrame.Shape.HLine)
        self.id_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.id_line)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pw_input = QLineEdit(self.widget)
        self.pw_input.setObjectName(u"pw_input")
        sizePolicy.setHeightForWidth(self.pw_input.sizePolicy().hasHeightForWidth())
        self.pw_input.setSizePolicy(sizePolicy)
        self.pw_input.setMinimumSize(QSize(300, 0))
        font3 = QFont()
        font3.setPointSize(14)
        self.pw_input.setFont(font3)
        self.pw_input.setStyleSheet(u"font-size:14pt;\n"
"color: rgb(255, 255, 255);")
        self.pw_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.pw_input.setCursorPosition(0)

        self.verticalLayout_2.addWidget(self.pw_input)

        self.pw_line = QFrame(self.widget)
        self.pw_line.setObjectName(u"pw_line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pw_line.sizePolicy().hasHeightForWidth())
        self.pw_line.setSizePolicy(sizePolicy1)
        self.pw_line.setMaximumSize(QSize(16777215, 1))
        self.pw_line.setFont(font2)
        self.pw_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.pw_line.setAutoFillBackground(False)
        self.pw_line.setStyleSheet(u"background-color: rgb(45, 45, 45)")
        self.pw_line.setFrameShape(QFrame.Shape.HLine)
        self.pw_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.pw_line)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.login_bn = QPushButton(self.widget)
        self.login_bn.setObjectName(u"login_bn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.login_bn.sizePolicy().hasHeightForWidth())
        self.login_bn.setSizePolicy(sizePolicy2)
        self.login_bn.setMinimumSize(QSize(0, 40))
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(False)
        self.login_bn.setFont(font4)
        self.login_bn.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.05 rgba(46, 49, 54, 255),\n"
"    stop:0.30 rgba(37, 40, 44, 255)\n"
");\n"
"border-radius: 10px;\n"
"color: rgb(252, 252, 252);")

        self.verticalLayout_6.addWidget(self.login_bn)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.horizontalLayout_5.addWidget(self.widget)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)


        self.retranslateUi(login_windows)

        QMetaObject.connectSlotsByName(login_windows)
    # setupUi

    def retranslateUi(self, login_windows):
        login_windows.setWindowTitle(QCoreApplication.translate("login_windows", u"login", None))
        self.logo.setText("")
        self.label_5.setText(QCoreApplication.translate("login_windows", u"\uc544\uc774\ub514", None))
        self.id_input.setText("")
        self.label_6.setText(QCoreApplication.translate("login_windows", u"\ube44\ubc00\ubc88\ud638", None))
        self.pw_input.setText("")
        self.login_bn.setText(QCoreApplication.translate("login_windows", u"\ub85c\uadf8\uc778", None))
    # retranslateUi


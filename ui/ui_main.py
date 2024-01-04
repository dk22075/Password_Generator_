# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(618, 381)
        icon = QIcon()
        icon.addFile(u":/icons/keyicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #E6E6FA;\n"
"    color: black;\n"
"    font-family: Verdana;\n"
"    font-size: 16pt;\n"
"    margin: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(460, 10, 151, 361))
        self.layout_characters = QVBoxLayout(self.verticalLayoutWidget_2)
        self.layout_characters.setObjectName(u"layout_characters")
        self.layout_characters.setContentsMargins(0, 0, 0, 0)
        self.button_upper = QPushButton(self.verticalLayoutWidget_2)
        self.button_upper.setObjectName(u"button_upper")
        self.button_upper.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_upper.setStyleSheet(u"QPushButton:hover {\n"
"    border-color: #9370DB;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #b39edd;\n"
"    border-color:	#4B0082;\n"
"}")
        self.button_upper.setCheckable(True)
        self.button_upper.setChecked(True)

        self.layout_characters.addWidget(self.button_upper)

        self.button_lower = QPushButton(self.verticalLayoutWidget_2)
        self.button_lower.setObjectName(u"button_lower")
        self.button_lower.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_lower.setStyleSheet(u"QPushButton:hover {\n"
"    border-color: #9370DB;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #b39edd;\n"
"    border-color:	#4B0082;\n"
"}")
        self.button_lower.setCheckable(True)
        self.button_lower.setChecked(True)

        self.layout_characters.addWidget(self.button_lower)

        self.button_digits = QPushButton(self.verticalLayoutWidget_2)
        self.button_digits.setObjectName(u"button_digits")
        self.button_digits.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_digits.setStyleSheet(u"QPushButton:hover {\n"
"    border-color: #9370DB;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #b39edd;\n"
"    border-color:	#4B0082;\n"
"}")
        self.button_digits.setCheckable(True)
        self.button_digits.setChecked(True)

        self.layout_characters.addWidget(self.button_digits)

        self.button_symbols = QPushButton(self.verticalLayoutWidget_2)
        self.button_symbols.setObjectName(u"button_symbols")
        self.button_symbols.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_symbols.setStyleSheet(u"QPushButton:hover {\n"
"    border-color: #9370DB;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #b39edd;\n"
"    border-color:	#4B0082;\n"
"}")
        self.button_symbols.setCheckable(True)

        self.layout_characters.addWidget(self.button_symbols)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(11, 311, 441, 57))
        self.layout_length = QHBoxLayout(self.horizontalLayoutWidget)
        self.layout_length.setObjectName(u"layout_length")
        self.layout_length.setContentsMargins(0, 0, 0, 0)
        self.slider_length = QSlider(self.horizontalLayoutWidget)
        self.slider_length.setObjectName(u"slider_length")
        self.slider_length.setCursor(QCursor(Qt.PointingHandCursor))
        self.slider_length.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    background-color: transparent;\n"
"    height: 5px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: #4B0082;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background-color: #d9d9d9;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: #9370DB;\n"
"    width: 14px;\n"
"    border-radius: 6px;\n"
"    margin-top: -8px;\n"
"    margin-bottom: -8px;\n"
"}")
        self.slider_length.setMaximum(100)
        self.slider_length.setValue(8)
        self.slider_length.setOrientation(Qt.Horizontal)

        self.layout_length.addWidget(self.slider_length)

        self.spinbox_length = QSpinBox(self.horizontalLayoutWidget)
        self.spinbox_length.setObjectName(u"spinbox_length")
        self.spinbox_length.setStyleSheet(u"QSpinBox {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"    background: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border-color: #9370DB;\n"
"}")
        self.spinbox_length.setAlignment(Qt.AlignCenter)
        self.spinbox_length.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinbox_length.setMaximum(100)
        self.spinbox_length.setValue(8)
        self.spinbox_length.setDisplayIntegerBase(10)

        self.layout_length.addWidget(self.spinbox_length)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 130, 441, 111))
        self.layout_password = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.layout_password.setObjectName(u"layout_password")
        self.layout_password.setContentsMargins(0, 0, 0, 0)
        self.frame_password = QFrame(self.horizontalLayoutWidget_2)
        self.frame_password.setObjectName(u"frame_password")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_password.sizePolicy().hasHeightForWidth())
        self.frame_password.setSizePolicy(sizePolicy)
        self.frame_password.setStyleSheet(u"QFrame {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border-color: #9370DB;\n"
"}")
        self.frame_password.setFrameShape(QFrame.StyledPanel)
        self.frame_password.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_password)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.line_password = QLineEdit(self.frame_password)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setStyleSheet(u"QLineEdit {\n"
"    border: none;\n"
"    margin: 0;\n"
"    font-size: 20pt;\n"
"}")

        self.horizontalLayout_4.addWidget(self.line_password)

        self.button_visibility = QPushButton(self.frame_password)
        self.button_visibility.setObjectName(u"button_visibility")
        self.button_visibility.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_visibility.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    margin: 0;\n"
"    background-color: transparent;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/invisibleicon.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/visibleicon.svg", QSize(), QIcon.Normal, QIcon.On)
        self.button_visibility.setIcon(icon1)
        self.button_visibility.setIconSize(QSize(30, 30))
        self.button_visibility.setCheckable(True)
        self.button_visibility.setChecked(True)

        self.horizontalLayout_4.addWidget(self.button_visibility)


        self.layout_password.addWidget(self.frame_password)

        self.button_copy = QPushButton(self.horizontalLayoutWidget_2)
        self.button_copy.setObjectName(u"button_copy")
        self.button_copy.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_copy.setStyleSheet(u"QPushButton:hover {\n"
"    border-color: #9370DB;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #b39edd;\n"
"    border-color:	#4B0082;\n"
"}\n"
"\n"
"QPushButton {\n"
"    margin-right: 0;\n"
"    margin-left: 0;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/refreshicon.svg", QSize(), QIcon.Normal, QIcon.On)
        self.button_copy.setIcon(icon2)
        self.button_copy.setIconSize(QSize(52, 52))

        self.layout_password.addWidget(self.button_copy)

        self.button_refresh = QPushButton(self.horizontalLayoutWidget_2)
        self.button_refresh.setObjectName(u"button_refresh")
        self.button_refresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_refresh.setStyleSheet(u"QPushButton:hover {\n"
"    border-color: #9370DB;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #b39edd;\n"
"    border-color:	#4B0082;\n"
"}\n"
"\n"
"QPushButton {\n"
"    padding: 5px;\n"
"    margin-left: 0;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/copyicon.svg", QSize(), QIcon.Normal, QIcon.On)
        self.button_refresh.setIcon(icon3)
        self.button_refresh.setIconSize(QSize(42, 42))

        self.layout_password.addWidget(self.button_refresh)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 250, 441, 51))
        self.layout_info = QVBoxLayout(self.verticalLayoutWidget)
        self.layout_info.setObjectName(u"layout_info")
        self.layout_info.setContentsMargins(0, 0, 0, 0)
        self.label_strength = QLabel(self.verticalLayoutWidget)
        self.label_strength.setObjectName(u"label_strength")
        sizePolicy.setHeightForWidth(self.label_strength.sizePolicy().hasHeightForWidth())
        self.label_strength.setSizePolicy(sizePolicy)
        self.label_strength.setCursor(QCursor(Qt.ArrowCursor))
        self.label_strength.setAlignment(Qt.AlignCenter)

        self.layout_info.addWidget(self.label_strength)

        self.icon_lock = QPushButton(self.centralwidget)
        self.icon_lock.setObjectName(u"icon_lock")
        self.icon_lock.setEnabled(False)
        self.icon_lock.setGeometry(QRect(16, 17, 431, 101))
        self.icon_lock.setStyleSheet(u"border: none;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/mainicon.svg", QSize(), QIcon.Disabled, QIcon.On)
        self.icon_lock.setIcon(icon4)
        self.icon_lock.setIconSize(QSize(100, 100))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator ", None))
        self.button_upper.setText(QCoreApplication.translate("MainWindow", u"ABC", None))
        self.button_lower.setText(QCoreApplication.translate("MainWindow", u"abc", None))
        self.button_digits.setText(QCoreApplication.translate("MainWindow", u"123", None))
        self.button_symbols.setText(QCoreApplication.translate("MainWindow", u"!@#", None))
        self.button_visibility.setText("")
        self.button_copy.setText("")
        self.button_refresh.setText("")
        self.label_strength.setText("")
        self.icon_lock.setText("")
    # retranslateUi


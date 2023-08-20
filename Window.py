# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(729, 459)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 729, 459))
        self.firstPage = QWidget()
        self.firstPage.setObjectName(u"firstPage")
        self.layoutWidget = QWidget(self.firstPage)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(220, 110, 261, 301))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.timer = QPushButton(self.layoutWidget)
        self.timer.setObjectName(u"timer")

        self.verticalLayout.addWidget(self.timer)

        self.countdown = QPushButton(self.layoutWidget)
        self.countdown.setObjectName(u"countdown")

        self.verticalLayout.addWidget(self.countdown)

        self.about = QPushButton(self.layoutWidget)
        self.about.setObjectName(u"about")

        self.verticalLayout.addWidget(self.about)

        self.title = QLabel(self.firstPage)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(70, 10, 580, 101))
        font = QFont()
        font.setPointSize(55)
        self.title.setFont(font)
        self.title.setTextFormat(Qt.AutoText)
        self.title.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.firstPage)
        self.timerPage = QWidget()
        self.timerPage.setObjectName(u"timerPage")
        self.fullDisplayBtn1 = QPushButton(self.timerPage)
        self.fullDisplayBtn1.setObjectName(u"fullDisplayBtn1")
        self.fullDisplayBtn1.setGeometry(QRect(310, 340, 87, 27))
        self.nowTime = QLabel(self.timerPage)
        self.nowTime.setObjectName(u"nowTime")
        self.nowTime.setGeometry(QRect(70, 20, 571, 201))
        font1 = QFont()
        font1.setPointSize(60)
        self.nowTime.setFont(font1)
        self.nowTime.setAlignment(Qt.AlignCenter)
        self.nowDate = QLabel(self.timerPage)
        self.nowDate.setObjectName(u"nowDate")
        self.nowDate.setGeometry(QRect(80, 230, 571, 71))
        font2 = QFont()
        font2.setPointSize(38)
        self.nowDate.setFont(font2)
        self.nowDate.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.timerPage)
        self.countdownPage = QWidget()
        self.countdownPage.setObjectName(u"countdownPage")
        self.point1 = QLabel(self.countdownPage)
        self.point1.setObjectName(u"point1")
        self.point1.setGeometry(QRect(210, 80, 100, 120))
        font3 = QFont()
        font3.setPointSize(90)
        self.point1.setFont(font3)
        self.point1.setAlignment(Qt.AlignCenter)
        self.point2 = QLabel(self.countdownPage)
        self.point2.setObjectName(u"point2")
        self.point2.setGeometry(QRect(400, 80, 100, 120))
        self.point2.setFont(font3)
        self.point2.setAlignment(Qt.AlignCenter)
        self.startBtn = QPushButton(self.countdownPage)
        self.startBtn.setObjectName(u"startBtn")
        self.startBtn.setGeometry(QRect(310, 280, 87, 27))
        self.second = QLineEdit(self.countdownPage)
        self.second.setObjectName(u"second")
        self.second.setGeometry(QRect(490, 90, 120, 130))
        font4 = QFont()
        font4.setPointSize(70)
        self.second.setFont(font4)
        self.second.setMaxLength(2)
        self.second.setAlignment(Qt.AlignCenter)
        self.minute = QLineEdit(self.countdownPage)
        self.minute.setObjectName(u"minute")
        self.minute.setGeometry(QRect(300, 90, 120, 130))
        self.minute.setFont(font4)
        self.minute.setMaxLength(2)
        self.minute.setAlignment(Qt.AlignCenter)
        self.hour = QLineEdit(self.countdownPage)
        self.hour.setObjectName(u"hour")
        self.hour.setGeometry(QRect(100, 90, 120, 130))
        self.hour.setFont(font4)
        self.hour.setMaxLength(2)
        self.hour.setAlignment(Qt.AlignCenter)
        self.stopBtn = QPushButton(self.countdownPage)
        self.stopBtn.setObjectName(u"stopBtn")
        self.stopBtn.setGeometry(QRect(190, 280, 87, 27))
        self.fullDisplayBtn2 = QPushButton(self.countdownPage)
        self.fullDisplayBtn2.setObjectName(u"fullDisplayBtn2")
        self.fullDisplayBtn2.setGeometry(QRect(430, 280, 87, 27))
        self.stackedWidget.addWidget(self.countdownPage)
        self.abounPage = QWidget()
        self.abounPage.setObjectName(u"abounPage")
        self.stackedWidget.addWidget(self.abounPage)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.timer.setText(QCoreApplication.translate("Form", u"\u65f6\u949f", None))
        self.countdown.setText(QCoreApplication.translate("Form", u"\u5012\u8ba1\u65f6", None))
        self.about.setText(QCoreApplication.translate("Form", u"\u5173\u4e8e", None))
        self.title.setText(QCoreApplication.translate("Form", u"simpleTimper", None))
        self.fullDisplayBtn1.setText(QCoreApplication.translate("Form", u"\u5168\u5c4f\u663e\u793a", None))
        self.nowTime.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.nowDate.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.point1.setText(QCoreApplication.translate("Form", u":", None))
        self.point2.setText(QCoreApplication.translate("Form", u":", None))
        self.startBtn.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.second.setText("")
        self.stopBtn.setText(QCoreApplication.translate("Form", u"\u505c\u6b62", None))
        self.fullDisplayBtn2.setText(QCoreApplication.translate("Form", u"\u5168\u5c4f\u663e\u793a", None))
    # retranslateUi


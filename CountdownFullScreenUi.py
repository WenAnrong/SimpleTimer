# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CountdownFullScreenUi.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(944, 674)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.hour = QLabel(Form)
        self.hour.setObjectName(u"hour")
        font = QFont()
        font.setPointSize(160)
        self.hour.setFont(font)
        self.hour.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.hour)

        self.point1 = QLabel(Form)
        self.point1.setObjectName(u"point1")
        font1 = QFont()
        font1.setPointSize(150)
        self.point1.setFont(font1)
        self.point1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.point1)

        self.minute = QLabel(Form)
        self.minute.setObjectName(u"minute")
        self.minute.setFont(font)
        self.minute.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.minute)

        self.point2 = QLabel(Form)
        self.point2.setObjectName(u"point2")
        self.point2.setFont(font1)
        self.point2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.point2)

        self.second = QLabel(Form)
        self.second.setObjectName(u"second")
        self.second.setFont(font)
        self.second.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.second)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.hour.setText(QCoreApplication.translate("Form", u"00", None))
        self.point1.setText(QCoreApplication.translate("Form", u":", None))
        self.minute.setText(QCoreApplication.translate("Form", u"00", None))
        self.point2.setText(QCoreApplication.translate("Form", u":", None))
        self.second.setText(QCoreApplication.translate("Form", u"00", None))
    # retranslateUi


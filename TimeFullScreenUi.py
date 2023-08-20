# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TimeFullScreenUi.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(931, 766)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nowTime = QLabel(Form)
        self.nowTime.setObjectName(u"nowTime")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.nowTime.sizePolicy().hasHeightForWidth())
        self.nowTime.setSizePolicy(sizePolicy)
        self.nowTime.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(120)
        self.nowTime.setFont(font)
        self.nowTime.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.nowTime)

        self.nowDate = QLabel(Form)
        self.nowDate.setObjectName(u"nowDate")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.nowDate.sizePolicy().hasHeightForWidth())
        self.nowDate.setSizePolicy(sizePolicy1)
        self.nowDate.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(40)
        self.nowDate.setFont(font1)
        self.nowDate.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.nowDate)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.nowTime.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.nowDate.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi


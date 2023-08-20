from PySide6.QtGui import QKeyEvent, Qt, QFontDatabase
from PySide6.QtWidgets import QWidget

from CountdownFullScreenUi import Ui_Form

import time


class MyCDFullWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        QFontDatabase.addApplicationFont("./asset/VonwaonBitmap-16px.ttf")
        self.setStyleSheet(
            """
            background-color: #000000;
            color: #FFFFFF;
            font-family: VonwaonBitmap 16px;
            """
        )

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            print("esc")
            self.close()

    def changeDate(self, x):
        Convertedformat = time.strftime("%H:%M:%S", time.gmtime(x))
        a = Convertedformat.split(":", 3)
        self.second.setText(a[2])
        self.minute.setText(a[1])
        self.hour.setText(a[0])

from PySide6.QtGui import QKeyEvent, Qt, QFontDatabase
from PySide6.QtWidgets import QWidget

from TimeFullScreenUi import Ui_Form


class MyTimeFullWindow(QWidget, Ui_Form):
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
        myDate = x.split(" ", 2)
        self.nowTime.setText(myDate[1])
        self.nowDate.setText(myDate[0])

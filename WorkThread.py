from PySide6.QtCore import QDateTime, QThread, Signal

import time


class CountdownThread(QThread):
    mySignal = Signal(int)

    def __init__(self):
        super().__init__()

    def setNum(self, numHour, numMinute, numSecond):
        self.numSecond = numSecond
        self.numMinute = numMinute
        self.numHour = numHour

    def run(self):
        totalNum = self.numHour * 60 * 60 + self.numMinute * 60 + self.numSecond
        for i in range(totalNum, -1, -1):
            self.mySignal.emit(i)
            time.sleep(1)


class TimerThread(QThread):
    mySignal = Signal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            data = QDateTime.currentDateTime()
            currentTime = data.toString("yyyy-MM-dd hh:mm:ss")
            self.mySignal.emit(str(currentTime))
            time.sleep(1)

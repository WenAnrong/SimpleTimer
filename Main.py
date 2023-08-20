from PySide6.QtGui import QFontDatabase, QIntValidator, QPixmap, Qt
from PySide6.QtWidgets import QApplication, QWidget
import sys
import time
from Customization import MyCatLabel, MyDogLabel, MyExitLabel

from Window import Ui_Form
from WorkThread import CountdownThread, TimerThread
from TimeFullScreen import MyTimeFullWindow
from CountdownFullScreen import MyCDFullWindow


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setFirstPage()
        self.setMyWindow()
        self.setTimerPage()
        self.setAboutPage()
        self.setCountdownPage()

        # 提前初始化两个全屏界面
        self.fullCDWindow = MyCDFullWindow()
        self.fullTimeWindow = MyTimeFullWindow()

    def setMyWindow(self):
        # 设置大小不可变
        self.setFixedSize(729, 459)

        QFontDatabase.addApplicationFont("./asset/VonwaonBitmap-16px.ttf")
        self.setStyleSheet(
            """
            font-family: VonwaonBitmap 16px;
            background-image: url('./asset/background.png');
            """
        )

        # 去除边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 为每个页面添加咖啡
        exitImg = QPixmap("./asset/cup1.png")

        self.exit1 = MyExitLabel(self.firstPage)
        self.exit2 = MyExitLabel(self.timerPage)
        self.exit3 = MyExitLabel(self.countdownPage)
        self.exit4 = MyExitLabel(self.abounPage)

        self.MyIndex = "1"
        arr = [self.exit1, self.exit2, self.exit3, self.exit4]
        for i in arr:
            i.setStackedWidget(self.stackedWidget)
            i.setIndex(self.MyIndex)
            i.setScaledContents(True)
            i.setGeometry(30, 30, 35, 35)
            i.setPixmap(exitImg)
            x = int(self.MyIndex) + 1
            self.MyIndex = str(x)

        # 为每一个页面添加狗
        dogImg = QPixmap("./asset/Dog1.png")

        self.dog1 = MyDogLabel(self.firstPage)
        self.dog2 = MyDogLabel(self.timerPage)
        self.dog3 = MyDogLabel(self.countdownPage)
        self.dog4 = MyDogLabel(self.abounPage)

        arr2 = [self.dog1, self.dog2, self.dog3, self.dog4]
        for i in arr2:
            i.setScaledContents(True)
            i.setGeometry(620, 350, 90, 90)
            i.setPixmap(dogImg)

        # 为界面添加一只猫
        catImg = QPixmap("./asset/RightCat.png")

        self.cat1 = MyCatLabel(self.firstPage)
        self.cat2 = MyCatLabel(self.timerPage)
        self.cat3 = MyCatLabel(self.countdownPage)
        self.cat4 = MyCatLabel(self.abounPage)

        arr3 = [self.cat1, self.cat2, self.cat3, self.cat4]
        for i in arr3:
            i.setScaledContents(True)
            i.setGeometry(30, 350, 90, 90)
            i.setPixmap(catImg)

    def setFirstPage(self):
        self.timer.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.countdown.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.about.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

    def setTimerPage(self):
        self.TimerT = TimerThread()
        self.TimerT.mySignal.connect(self.changeDate)
        self.TimerT.start()

        self.fullDisplayBtn1.clicked.connect(self.fullDisplayTime)

    # 时间界面全屏展示
    def fullDisplayTime(self):
        self.fullTimeWindow.showFullScreen()

    def changeDate(self, x):
        myDate = x.split(" ", 2)
        self.nowTime.setText(myDate[1])
        self.nowDate.setText(myDate[0])

        # 将数据传给全屏显示界面
        self.fullTimeWindow.changeDate(x)

    def setAboutPage(self):
        pass

    def setCountdownPage(self):
        self.stopBtn.setVisible(False)
        self.fullDisplayBtn2.setVisible(False)

        arr = [self.second, self.hour, self.minute]
        for i in arr:
            i.setPlaceholderText("00")
            i.setValidator(QIntValidator())
        self.startBtn.clicked.connect(self.startCountdown)
        self.fullDisplayBtn2.clicked.connect(self.fullDisplayCD)

    # 倒计时界面全屏展示
    def fullDisplayCD(self):
        self.fullCDWindow.showFullScreen()

    # 倒计时开始按钮点击事件
    def startCountdown(self):
        self.hourNum = 0
        self.minuteNum = 0
        self.secondNum = 0
        if self.hour.text() != "":
            self.hourNum = int(self.hour.text())
        if self.minute.text() != "":
            self.minuteNum = int(self.minute.text())
        if self.second.text() != "":
            self.secondNum = int(self.second.text())

        self.countdownT = CountdownThread()
        self.countdownT.setNum(self.hourNum, self.minuteNum, self.secondNum)
        self.countdownT.mySignal.connect(self.changeLineEdit)
        self.countdownT.started.connect(self.startCD)
        self.countdownT.finished.connect(self.stopCD)
        self.countdownT.start()

    # 倒计时界面时间改变
    def changeLineEdit(self, x):
        Convertedformat = time.strftime("%H:%M:%S", time.gmtime(x))
        a = Convertedformat.split(":", 3)
        self.second.setText(a[2])
        self.minute.setText(a[1])
        self.hour.setText(a[0])

        # 将数据传给全屏显示界面
        self.fullCDWindow.changeDate(x)

    # 倒计时开始
    def startCD(self):
        self.startBtn.setVisible(False)
        self.fullDisplayBtn2.setVisible(True)
        self.stopBtn.setVisible(True)

        arr = [self.second, self.minute, self.hour]
        for i in arr:
            i.setReadOnly(True)
            i.clearFocus()

        # 点击停止按钮强行停止线程
        self.stopBtn.clicked.connect(lambda: self.countdownT.terminate())

    # 倒计时结束
    def stopCD(self):
        self.countdownT.deleteLater()
        self.startBtn.setVisible(True)
        self.fullDisplayBtn2.setVisible(False)
        self.stopBtn.setVisible(False)

        arr = [self.second, self.minute, self.hour]
        for i in arr:
            i.setReadOnly(False)
            i.clear()
            i.clearFocus()

    def setButtonTheme(self):
        pass

    # 让窗口可以被鼠标拖动
    def mousePressEvent(self, event):  ##事件开始
        if event.button() == Qt.LeftButton:
            self.Move = True  ##设定bool为True
            self.Point = event.globalPosition() - self.pos()  ##记录起始点坐标
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):  ##移动时间
        if Qt.LeftButton and self.Move:  ##切记这里的条件不能写死，只要判断move和鼠标执行即可！
            temp = QMouseEvent.globalPosition() - self.Point
            x = int(temp.x())
            y = int(temp.y())
            self.move(x, y)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  ##结束事件
        self.Move = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()

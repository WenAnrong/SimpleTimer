from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel

import sys


class MyExitLabel(QLabel):
    def setStackedWidget(self, MyStackedWidget):
        self.MyStackedWidget = MyStackedWidget

    def setIndex(self, myIndex):
        self.myIndex = myIndex

    def mousePressEvent(self, e):  # 单击
        if self.myIndex == "1":
            sys.exit()
        elif self.myIndex == "2":
            self.MyStackedWidget.setCurrentIndex(0)
        elif self.myIndex == "3":
            self.MyStackedWidget.setCurrentIndex(0)
        elif self.myIndex == "4":
            self.MyStackedWidget.setCurrentIndex(0)

    def leaveEvent(self, e):  # 鼠标离开label
        exitImg = QPixmap("./asset/cup1.png")
        self.setPixmap(exitImg)

    def enterEvent(self, e):  # 鼠标移入label
        exitImg = QPixmap("./asset/cup2.png")
        self.setPixmap(exitImg)


class MyCatLabel(QLabel):
    def mousePressEvent(self, e):  # 单击
        pass

    def leaveEvent(self, e):  # 鼠标离开label
        catImg = QPixmap("./asset/RightCat.png")
        self.setPixmap(catImg)

    def enterEvent(self, e):  # 鼠标移入label
        catImg = QPixmap("./asset/LeftCat.png")
        self.setPixmap(catImg)


class MyDogLabel(QLabel):
    def mousePressEvent(self, e):  # 单击
        pass

    def leaveEvent(self, e):  # 鼠标离开label
        dogImg = QPixmap("./asset/Dog1.png")
        self.setPixmap(dogImg)

    def enterEvent(self, e):  # 鼠标移入label
        dogImg = QPixmap("./asset/Dog2.png")
        self.setPixmap(dogImg)

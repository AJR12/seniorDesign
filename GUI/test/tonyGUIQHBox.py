import sys
import os
curDir = os.getcwd()
desDir1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
desDir2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '../venv'))
desDir3 = os.path.abspath(os.path.join(os.path.dirname(__file__), '../venv/Scripts/python36.zip'))
desDir4 = os.path.abspath(os.path.join(os.path.dirname(__file__), '../venv/lib'))
desDir5 = os.path.abspath(os.path.join(os.path.dirname(__file__), '../venv/lib/site-packages'))
desDir6 = os.path.abspath(os.path.join(os.path.dirname(__file__), '../venv/lib/site-packages/setuptools-40.8.0-py3.6.egg'))
desDir7 = os.path.abspath(os.path.join(os.path.dirname(__file__), '../venv/lib/site-packages/pip-19.0.3-py3.6.egg'))
desDir8 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
desDir9 = os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib'))

sys.path.extend([desDir1,desDir2,desDir3,desDir4,desDir5,desDir6,desDir7,desDir8,desDir9])

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5 import QtGui, QtCore


class Window(QDialog):

    #Constructor: Init's window, define window parameters
    def __init__(self):
        super().__init__()


        self.iconPath = "home.jpg"
        self.footballIconPath = "football.png"
        self.soccerIconPath = "Soccer.png"
        self.basketballIconPath = "Basketball.png"
        self.title = "iMay - AI in Your Hands"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.InitWindow()

        self.createLayout()
        vbox = QVBoxLayout();
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)


    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconPath))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()


    def createLayout(self):
        self.groupBox = QGroupBox("What Is Your Favorite Sport?")
        hboxlayout = QHBoxLayout()

        # Creating a pushbutton, defining geometry, setting icon and icon geo, creating tooltip
        button = QPushButton("Football", self)
        button.setIcon(QtGui.QIcon(self.footballIconPath))
        button.setIconSize(QtCore.QSize(40, 40))
        button.setMinimumHeight(40)
        hboxlayout.addWidget((button))

        # Creating a pushbutton, defining geometry, setting icon and icon geo, creating tooltip
        button1 = QPushButton("Soccer", self)
        button1.setIcon(QtGui.QIcon(self.soccerIconPath))
        button1.setIconSize(QtCore.QSize(40, 40))
        button1.setMinimumHeight(40)
        hboxlayout.addWidget((button1))

        # Creating a pushbutton, defining geometry, setting icon and icon geo, creating tooltip
        button2 = QPushButton("Basketball", self)
        button2.setIcon(QtGui.QIcon(self.basketballIconPath))
        button2.setIconSize(QtCore.QSize(40, 40))
        button2.setMinimumHeight(40)
        hboxlayout.addWidget((button2))

        self.groupBox.setLayout(hboxlayout)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
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

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5 import QtGui, QtCore

class Window(QDialog):

    #Constructor: Init's window, define window parameters
    def __init__(self):
        super().__init__()


        self.iconPath = "pic/home.jpg"
        self.pythonIconPath = "pic/python.png"
        self.javaIconPath = "pic/java.png"
        self.cppIconPath = "pic/cpp.png"
        self.csharpIconPath = "pic/c#.png"
        self.title = "PyQt5 Grid Layout"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.InitWindow()

        self.CreateLayout()
        vbox = QVBoxLayout();
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)


    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconPath))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

    def CreateLayout(self):
        self.groupBox = QGroupBox("What is your favorite programming language?")
        gridLayout = QGridLayout()

        # Creating a pushbutton, defining geometry, setting icon and icon geo, creating tooltip
        button = QPushButton("Python", self)
        button.setIcon(QtGui.QIcon(self.pythonIconPath))
        button.setIconSize(QtCore.QSize(40, 40))
        button.setMinimumHeight(40)
        gridLayout.addWidget(button, 0, 0)

        # Creating a pushbutton, defining geometry, setting icon and icon geo, creating tooltip
        button1 = QPushButton("Java", self)
        button1.setIcon(QtGui.QIcon(self.javaIconPath))
        button1.setIconSize(QtCore.QSize(40, 40))
        button1.setMinimumHeight(40)
        gridLayout.addWidget(button1, 0, 1)

        # Creating a pushbutton, defining geometry, setting icon and icon geo, creating tooltip
        button2 = QPushButton("C++", self)
        button2.setIcon(QtGui.QIcon(self.cppIconPath))
        button2.setIconSize(QtCore.QSize(40, 40))
        button2.setMinimumHeight(40)
        gridLayout.addWidget(button2, 1, 0)

        # Creating a pushbutton, defining geometry, setting icon and icon geo, creating tooltip
        button3 = QPushButton("C#", self)
        button3.setIcon(QtGui.QIcon(self.csharpIconPath))
        button3.setIconSize(QtCore.QSize(40, 40))
        button3.setMinimumHeight(40)
        gridLayout.addWidget(button3, 1, 1)

        self.groupBox.setLayout(gridLayout)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
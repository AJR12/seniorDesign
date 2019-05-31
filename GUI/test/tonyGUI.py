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

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "iMay - AI in Your Hands"
        self.iconPath = "home.jpg"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconPath))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())


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

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import QtGui, QtCore


class Window(QMainWindow):

    #Constructor: Init's window, define window parameters
    def __init__(self):
        super().__init__()

        title = "iMay - AI in Your Hands"
        self.iconPath = "home.jpg"
        top = 100
        left = 100
        width = 400
        height = 300

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(self.iconPath))
        self.setGeometry(left, top, width, height)
        self.UiComponents()

        self.show()

    def UiComponents(self):

        #Creating a pushbutton, defining geometry, setting icon and icon geo, creating tooltip
        button = QPushButton("Click ME", self)
        button.setGeometry(QtCore.QRect(100,100, 111, 120)) #QRect(xpos, ypos, width, height)
        button.setIcon(QtGui.QIcon(self.iconPath))
        button.setIconSize(QtCore.QSize(40,40))
        button.setToolTip("<h2>This is Click Me Button<h2>") #Appears when you hover pointer over the button

        #Create a signal: Signal calls a function to exec when the button is clicked. It's what ties a button to an action
        button.clicked.connect(self.ClickMe)


    #Creating a slot: Slot is the action taken when the button is clicked.
    def ClickMe(self):
        print("Hello World!")
        #sys.exit() # This line closes the window




if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())


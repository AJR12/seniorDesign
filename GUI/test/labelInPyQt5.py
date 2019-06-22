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

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel
from PyQt5 import QtGui, QtCore

class Window(QDialog):
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

        vbox = QVBoxLayout()
        label = QLabel("This is PyQt5 Label")
        vbox.addWidget(label)

        label2 = QLabel("This is Label 2")
        label2.setFont(QtGui.QFont("Sanserif", 20))
        label2.setStyleSheet("color:red")
        vbox.addWidget(label2)

        labelImage = QLabel(self)
        pixmap = QtGui.QPixmap(self.javaIconPath)
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)

        self.setLayout(vbox)


    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconPath))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()




if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
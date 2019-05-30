# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IMayProto.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("IMayPrototype")
        MainWindow.resize(730, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 541, 351))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.listWidget_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout.addWidget(self.listWidget_2)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(560, 60, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.NextButton = QtWidgets.QPushButton(self.centralwidget)
        self.NextButton.setGeometry(QtCore.QRect(570, 390, 75, 23))
        self.NextButton.setObjectName("NextButton")
        self.CancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.CancelButton.setGeometry(QtCore.QRect(650, 390, 75, 23))
        self.CancelButton.setObjectName("CancelButton")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(220, 40, 61, 19))
        self.toolButton.setObjectName("toolButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 21))
        self.menubar.setObjectName("menubar")
        self.menuIMay_prototype = QtWidgets.QMenu(self.menubar)
        self.menuIMay_prototype.setObjectName("menuIMay_prototype")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuIMay_prototype.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.NextButton.clicked.connect(lambda: self.Hello())
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.NextButton.setText(_translate("MainWindow", "Next"))
        self.CancelButton.setText(_translate("MainWindow", "Cancel"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.menuIMay_prototype.setTitle(_translate("MainWindow", "IMay prototype"))


    def Hello(self):
        print("Hello")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

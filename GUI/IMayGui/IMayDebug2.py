# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IMayProtoDebug2.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import IMayFunctions

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 589)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 0, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.formLayout.setSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.Debug_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Debug_1.setObjectName("Debug_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Debug_1)
        self.Debug_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Debug_2.setObjectName("Debug_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Debug_2)
        self.Debug_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Debug_3.setObjectName("Debug_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Debug_3)
        self.Debug_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Debug_4.setObjectName("Debug_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Debug_4)
        self.Debug_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Debug_5.setObjectName("Debug_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Debug_5)
        self.Debug_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Debug_6.setObjectName("Debug_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Debug_6)
        self.NextButton = QtWidgets.QPushButton(self.centralwidget)
        self.NextButton.setObjectName("NextButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.NextButton)
        self.CancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.CancelButton.setObjectName("CancelButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.CancelButton)
        self.gridLayout_2.addLayout(self.formLayout, 2, 2, 1, 1)
        self.addDirectory = QtWidgets.QToolButton(self.centralwidget)
        self.addDirectory.setObjectName("addDirectory")
        self.gridLayout_2.addWidget(self.addDirectory, 0, 0, 1, 1)
        self.listWidget_1 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_1.setObjectName("listWidget_1")
        self.gridLayout_2.addWidget(self.listWidget_1, 1, 0, 1, 2)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_2.addWidget(self.listWidget_2, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 26))
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

        # GUI Functionality section
        self.Debug_1.clicked.connect(lambda: IMayFunctions.rename())
        self.Debug_2.clicked.connect(lambda: IMayFunctions.zip_files())
        self.Debug_3.pressed.connect(lambda: self.file_dialog())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IMay"))
        self.Debug_1.setText(_translate("MainWindow", "Debug_1"))
        self.Debug_2.setText(_translate("MainWindow", "Debug_2"))
        self.Debug_3.setText(_translate("MainWindow", "Debug_3"))
        self.Debug_4.setText(_translate("MainWindow", "Debug_4"))
        self.Debug_5.setText(_translate("MainWindow", "Debug_5"))
        self.Debug_6.setText(_translate("MainWindow", "Debug_6"))
        self.NextButton.setText(_translate("MainWindow", "Next"))
        self.CancelButton.setText(_translate("MainWindow", "Cancel"))
        self.addDirectory.setText(_translate("MainWindow", "+"))
        #self.menuIMay_prototype.setTitle(_translate("MainWindow", "IMay prototype"))


    def file_dialog(self):
        path_to_project = QtWidgets.QFileDialog.getExistingDirectory(None, "Choose Directory", "F:\Senior_2" )
        self.lineEdit.setText(path_to_project)
        print(path_to_project)
        self.listWidget_1.addItem(path_to_project)
        #path_to_project = QtWidgets.QFileDialog.getExistingDirectory
            #(None, "Open Directory", "C:/", QtWidgets.QFileDialog.ShowDirsOnly|QtWidgets.QFileDialog.DontResolveSymlinks)


   # def add_label(self):


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

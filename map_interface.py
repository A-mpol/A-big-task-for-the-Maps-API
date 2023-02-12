# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'map_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.coords_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.coords_edit.setObjectName("coords_edit")
        self.gridLayout.addWidget(self.coords_edit, 0, 1, 1, 1)
        self.show_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_button.setObjectName("show_button")
        self.gridLayout.addWidget(self.show_button, 2, 1, 1, 1)
        self.size_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.size_edit.setObjectName("size_edit")
        self.gridLayout.addWidget(self.size_edit, 1, 1, 1, 1)
        self.size_label = QtWidgets.QLabel(self.centralwidget)
        self.size_label.setObjectName("size_label")
        self.gridLayout.addWidget(self.size_label, 1, 0, 1, 1)
        self.coords_label = QtWidgets.QLabel(self.centralwidget)
        self.coords_label.setObjectName("coords_label")
        self.gridLayout.addWidget(self.coords_label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setObjectName("image_label")
        self.gridLayout.addWidget(self.image_label, 3, 0, 1, 3)
        self.mistake_label = QtWidgets.QLabel(self.centralwidget)
        self.mistake_label.setEnabled(True)
        self.mistake_label.setMaximumSize(QtCore.QSize(1000, 50))
        self.mistake_label.setObjectName("mistake_label")
        self.gridLayout.addWidget(self.mistake_label, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.show_button.setText(_translate("MainWindow", "Show"))
        self.size_label.setText(_translate("MainWindow", "Size:"))
        self.coords_label.setText(_translate("MainWindow", "Coordinates:"))
        self.image_label.setText(_translate("MainWindow", ""))
        self.mistake_label.setText(_translate("MainWindow", ""))

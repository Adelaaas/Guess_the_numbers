# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 445)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter_6 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_6.setGeometry(QtCore.QRect(10, 20, 711, 411))
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.splitter_5 = QtWidgets.QSplitter(self.splitter_6)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.groupBox = QtWidgets.QGroupBox(self.splitter_5)
        self.groupBox.setObjectName("groupBox")
        self.splitter_3 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_3.setGeometry(QtCore.QRect(10, 30, 399, 90))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.countLineEdit = QtWidgets.QLineEdit(self.splitter)
        self.countLineEdit.setObjectName("countLineEdit")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setObjectName("label_2")
        self.countLineEdit_2 = QtWidgets.QLineEdit(self.splitter_2)
        self.countLineEdit_2.setObjectName("countLineEdit_2")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.startPushButton = QtWidgets.QPushButton(self.splitter_4)
        self.startPushButton.setObjectName("startPushButton")
        self.graphResultPushButton = QtWidgets.QPushButton(self.splitter_4)
        self.graphResultPushButton.setObjectName("graphResultPushButton")
        self.kmeansPushButton = QtWidgets.QPushButton(self.splitter_4)
        self.kmeansPushButton.setObjectName("kmeansPushButton")
        self.resultTableWidget = QtWidgets.QTableWidget(self.splitter_6)
        self.resultTableWidget.setObjectName("resultTableWidget")
        self.resultTableWidget.setColumnCount(3)
        self.resultTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.resultTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultTableWidget.setHorizontalHeaderItem(2, item)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Параметры для ввода пользователем "))
        self.label.setText(_translate("MainWindow", "Количество элементов из БД"))
        self.label_2.setText(_translate("MainWindow", "Введите 8-ми значное число"))
        self.startPushButton.setText(_translate("MainWindow", "Запустить анализ"))
        self.graphResultPushButton.setText(_translate("MainWindow", "Вывести графический результат"))
        self.kmeansPushButton.setText(_translate("MainWindow", "Разбиение на 4 кластера"))
        item = self.resultTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Дополнительное число"))
        item = self.resultTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Число из списка"))
        item = self.resultTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Результат анализа"))

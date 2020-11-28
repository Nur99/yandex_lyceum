# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created by: PyQt5 UI code generator 5.11
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 229)
        self.title = QtWidgets.QPlainTextEdit(Form)
        self.title.setGeometry(QtCore.QRect(110, 10, 281, 31))
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(9, 10, 81, 31))
        self.label.setObjectName("label")
        self.year = QtWidgets.QPlainTextEdit(Form)
        self.year.setGeometry(QtCore.QRect(111, 50, 281, 31))
        self.year.setObjectName("year")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 81, 31))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(110, 90, 281, 26))
        self.comboBox.setObjectName("comboBox")
        self.duration = QtWidgets.QPlainTextEdit(Form)
        self.duration.setGeometry(QtCore.QRect(111, 130, 281, 31))
        self.duration.setObjectName("duration")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 81, 31))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(242, 180, 141, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить элемент"))
        self.label.setText(_translate("Form", "Название"))
        self.label_2.setText(_translate("Form", "Год выпуска"))
        self.label_3.setText(_translate("Form", "Жанр"))
        self.label_4.setText(_translate("Form", "Длина"))
        self.pushButton.setText(_translate("Form", "Добавить"))


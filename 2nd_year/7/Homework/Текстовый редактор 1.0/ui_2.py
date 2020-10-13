# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui2.ui'
#
# Created by: PyQt5 UI code generator 5.11
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(544, 346)
        self.open = QtWidgets.QPushButton(Form)
        self.open.setGeometry(QtCore.QRect(20, 70, 151, 51))
        self.open.setObjectName("open")
        self.save = QtWidgets.QPushButton(Form)
        self.save.setGeometry(QtCore.QRect(20, 140, 151, 51))
        self.save.setObjectName("save")
        self.new_2 = QtWidgets.QPushButton(Form)
        self.new_2.setGeometry(QtCore.QRect(20, 210, 151, 51))
        self.new_2.setObjectName("new_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(170, 20, 351, 301))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 141, 31))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Текстовый редактор"))
        self.open.setText(_translate("Form", "Открыть файл"))
        self.save.setText(_translate("Form", "Сохранить файл"))
        self.new_2.setText(_translate("Form", "Создать новый "))


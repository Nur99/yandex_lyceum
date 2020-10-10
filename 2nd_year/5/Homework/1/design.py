# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui.ui'
#
# Created by: PyQt5 UI code generator 5.11
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.Phones = QtWidgets.QListWidget(Form)
        self.Phones.setGeometry(QtCore.QRect(10, 100, 371, 191))
        self.Phones.setObjectName("Phones")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 40, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.Name = QtWidgets.QLineEdit(Form)
        self.Name.setGeometry(QtCore.QRect(90, 20, 171, 21))
        self.Name.setObjectName("Name")
        self.Contact = QtWidgets.QLineEdit(Form)
        self.Contact.setGeometry(QtCore.QRect(90, 60, 171, 21))
        self.Contact.setObjectName("Contact")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 60, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Записная книжка"))
        self.pushButton.setText(_translate("Form", "Добавить"))
        self.label.setText(_translate("Form", "Имя"))
        self.label_2.setText(_translate("Form", "Телефон"))


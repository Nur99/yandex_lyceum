import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton
import sqlite3

from PyQt5.uic.properties import QtWidgets, QtCore


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(748, 371)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 711, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Формирование запросов"))


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("films.db")
        self.elements = []
        for i in range(32):
            self.elements.append(QPushButton(chr(i + 1040), self))
            self.elements[i].clicked.connect(self.select)
            self.elements[i].resize(25, 25)
            self.elements[i].move(i * 25 + 2, 10)

    def select(self):
        character = self.sender().text()
        req = f"SELECT * FROM films WHERE title LIKE '{character}%'"
        cur = self.con.cursor()
        result = cur.execute(req).fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels(['ID:', 'Название:', "Год выпуска:", "Жанр:", "Продолжительность:"])
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

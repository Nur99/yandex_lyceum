import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QTextEdit
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget, QPushButton
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(748, 371)
        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setGeometry(QRect(20, 60, 711, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QPushButton(Form)
        self.pushButton.setGeometry(QRect(360, 20, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setGeometry(QRect(480, 20, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QTextEdit(Form)
        self.textEdit.setGeometry(QRect(70, 20, 181, 31))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Формирование запросов"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("films.db")
        self.pushButton.clicked.connect(self.get_result)
        self.pushButton_2.clicked.connect(self.save_results)
        self.modified = {}
        self.result = None
        self.titles = None

    def get_result(self):
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        item_id = self.textEdit.toPlainText()
        self.result = cur.execute(f"SELECT * FROM Films WHERE id={item_id}").fetchall()
        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(len(self.result))
        # Если запись не нашлась, то не будем ничего делать
        if not self.result:
            self.statusBar().showMessage('Ничего не нашлось')
            return
        else:
            self.statusBar().showMessage(f"Нашлась запись с id = {item_id}")
        self.tableWidget.setColumnCount(len(self.result[0]))
        self.titles = [description[0] for description in cur.description]
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(self.result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def save_results(self):
        cur = self.con.cursor()
        entry = self.result[0]
        id = entry[0]
        title = entry[1][::-1]
        year = str(int(entry[2]) + 1000)
        query = f"UPDATE Films SET title = '{title}', year = {year}, duration = duration * 2 WHERE id = {id}"
        cur.execute(query).fetchall()
        self.con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())

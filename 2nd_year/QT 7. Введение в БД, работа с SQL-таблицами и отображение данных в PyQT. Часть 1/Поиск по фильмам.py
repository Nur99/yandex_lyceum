import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from ui_5 import Ui_Form
import sqlite3


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.params = {"Год выпуска": "year",
                       "Название": "title",
                       "Продолжительность": "duration"}
        self.comboBox.addItems(list(self.params.keys()))
        self.con = sqlite3.connect("films.db")
        self.pushButton.clicked.connect(self.select)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(5)

    def select(self):
        req = "SELECT * FROM Films WHERE {} = {}".format(self.params.get(self.comboBox.currentText()),
                                                         self.lineEdit.text())
        cur = self.con.cursor()
        result = cur.execute(req).fetchone()
        for i, val in enumerate(result):
            self.tableWidget.setItem(0, i, QTableWidgetItem(str(val)))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem
from UI import Ui_Form
import sqlite3

class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("films.db")
        self.pushButton.clicked.connect(self.select)
        self.setWindowTitle('Поиск по фильмам 2.0')

    def select(self):
        title, duration, year = self.title.text(), self.duration.text(), self.year.text()
        req = "SELECT * FROM films "
        if title:
            req += "WHERE title {}".format(title)
        if duration:
            if 'WHERE' in req:
                req += " AND duration {}".format(duration)
            else:
                req += "WHERE duration {}".format(duration)
        if year:
            if 'WHERE' in req:
                req += " AND year {}".format(year)
            else:
                req += "WHERE year {}".format(year)
        cur = self.con.cursor()
        result = cur.execute(req).fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels([i[0] for i in cur.description])
        print(cur.description)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))



app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

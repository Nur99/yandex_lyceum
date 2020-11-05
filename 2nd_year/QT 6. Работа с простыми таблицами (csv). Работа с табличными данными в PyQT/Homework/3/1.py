import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QColor
import random
from ui_1 import Ui_Form
import csv


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadTable('rez.csv')
        self.colorFive()

    def loadTable(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
            expensive = sorted(reader, key=lambda x: int(x['Цена']), reverse=True)
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderLabels(["Название", "Цена"])
            self.tableWidget.setRowCount(len(expensive))
            for i, row in enumerate(expensive):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(row['Название']))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(row['Цена']))
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)

    def colorRow(self, row, color):
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.item(row, i).setBackground(color)

    def colorFive(self):
        for i in range(5):
            self.colorRow(i, QColor(random.randrange(10, 250), random.randrange(10, 250), random.randrange(10, 250)))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

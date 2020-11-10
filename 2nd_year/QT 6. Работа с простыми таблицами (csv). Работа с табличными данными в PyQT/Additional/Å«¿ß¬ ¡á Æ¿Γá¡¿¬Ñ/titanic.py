import csv
import sys

from PyQt5 import uic
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QWidget, QTableWidget


class TitanicSearch(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.title, self.raw_data = self.load_table('titanic.csv')
        self.display_data(self.raw_data)
        self.searchEdit.textChanged.connect(self.filter)

    def filter(self):
        value = self.searchEdit.text()
        if len(value) < 3:
            self.display_data(self.raw_data)
            return
        new_data = [x for x in self.raw_data if value.lower() in x[1].lower()]
        self.display_data(new_data)

    def load_table(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            title = next(reader)
            data = list(reader)
            return title, data

    def display_data(self, data):
        table_widget: QTableWidget = self.resultTable
        table_widget.clear()
        table_widget.setColumnCount(len(self.title))
        table_widget.setHorizontalHeaderLabels(self.title)
        table_widget.setRowCount(len(data))
        for i, row in enumerate(data):
            for j, item in enumerate(row):
                table_widget.setItem(i, j, QTableWidgetItem(item))
            if row[-2] == '1':
                self.color_row(table_widget, i, QColor(0, 250, 0))
            else:
                self.color_row(table_widget, i, QColor(200, 0, 0))

    def color_row(self, widget, row, color):
        for i in range(widget.columnCount()):
            widget.item(row, i).setBackground(color)


def excepthook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TitanicSearch()
    ex.show()
    sys.excepthook = excepthook
    sys.exit(app.exec())

import csv
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QHeaderView, QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.load_table('price.csv')
        self.tableWidget.itemChanged.connect(self.update_check)

    def load_table(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            title = next(reader)
            self.tableWidget.setColumnCount(len(title) + 1)
            self.tableWidget.setHorizontalHeaderLabels(title + ["Количество"])
            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(0, QHeaderView.Stretch)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(reader):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(elem))
                self.tableWidget.setItem(i, j, QTableWidgetItem('0'))
            self.tableWidget.resizeColumnsToContents()

    def update_check(self):
        price = [int(self.tableWidget.item(i, 1).text()) for i in range(self.tableWidget.rowCount())]
        count = [int(self.tableWidget.item(i, 2).text()) if self.tableWidget.item(i, 2).text() != '' else 0 for i in
                 range(self.tableWidget.rowCount())]
        sum_of = 0
        for i in range(len(price)):
            sum_of += price[i] * count[i]
        self.lineEdit.setText(str(sum_of))


def exception_hook(cls, exception, traceback):
    sys.__exception_hook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = exception_hook
    sys.exit(app.exec_())

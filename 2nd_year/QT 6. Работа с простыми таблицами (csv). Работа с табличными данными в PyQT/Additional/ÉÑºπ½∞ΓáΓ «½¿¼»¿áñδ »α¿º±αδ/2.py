import csv
import sys

from PyQt5 import uic
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.school = ['Все']
        self.classe = {}
        self.data_name = 'rez.csv'
        self.loadSchoolsClasses(self.data_name)
        self.schools.addItems(self.school)
        self.classes.addItems(['Все'])
        self.schools.currentIndexChanged.connect(self.filter)
        self.pushButton.clicked.connect(self.results)

    def filter(self):
        self.classes.addItems(sorted(list(set(self.classe.get(self.schools.currentText(), [])))))

    def results(self):
        sh, k = [self.schools.currentText(), self.classes.currentText()]
        new_data = self.table_filter(sh, k)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Фамилия', 'Результат', 'Логин'])
        self.tableWidget.setRowCount(len(new_data))
        for i in range(len(new_data)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(new_data[i][1]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(new_data[i][0])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(new_data[i][2])))
        self.colorFirstThreePlaces()

    def table_filter(self, sh, k):
        with open(self.data_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            last_name = []
            for index, row in enumerate(reader):
                if row[2] != "login":
                    fio = row[2].split('-')
                    if (fio[2] == sh and fio[3] == k) or (fio[2] == sh and k == 'Все') or (
                            fio[3] == k and sh == 'Все') or ('Все' == sh == k):
                        name = row[1].split()
                        last_name.append((int(row[7]), name[-2], row[1]))
            last_name = sorted(last_name, reverse=True)
            return last_name

    def loadSchoolsClasses(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for i, row in enumerate(reader):
                if row[2] != "login":
                    fio = row[2].split('-')
                    sch, cls = fio[2], fio[3]
                    if sch not in self.school:
                        self.school.append(sch)
                    if sch in self.classe.keys():
                        self.classe[sch].append(cls)
                    else:
                        self.classe[sch] = [cls]

    def loadTable(self, table_name):

        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            title = next(reader)
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(reader):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                if row[2] != "login":
                    fio = row[2].split('-')
                    sch, cls = fio[2], fio[3]
                    if sch not in self.school:
                        self.school.append(sch)
                    if sch in self.classe.keys():
                        self.classe[sch].append(cls)
                    else:
                        self.classe[sch] = [cls]
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(elem))

    def colorRow(self, row, color):
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.item(row, i).setBackground(color)

    def colorFirstThreePlaces(self):
        colors = [QColor(225, 215, 0), QColor(181, 181, 189), QColor(156, 82, 33)]
        now = 0
        index = 0
        color_index = 0
        while True:
            try:
                tmp = int(self.tableWidget.item(index,1).text())
            except AttributeError:
                break
            if tmp >= now:
                self.colorRow(index,colors[color_index])
                now = tmp
            else:
                now = tmp
                color_index+=1
                self.colorRow(index, colors[color_index])
            index+=1
            if color_index==3:
                break


def excepthook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = excepthook
    sys.exit(app.exec())

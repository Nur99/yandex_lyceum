import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem,QHeaderView
from PyQt5.QtGui import QColor
from ui import Ui_Form
import csv

class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.school = ['Все']
        self.classe = {}
        self.data_name = 'rez.csv'
        self.loadTable(self.data_name)
        self.classes.addItems(['Все','9','10','11'])
        self.pushButton.clicked.connect(self.filter)

    def loadTable(self,table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            expensive = sorted(reader, key=lambda x: int(x['Score']), reverse= True)
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(["Логин","ФИО","Суммарный бал"])
            self.tableWidget.setRowCount(len(expensive))
            for i, row in enumerate(expensive):
                elem = [row['login'],row['user_name'],row['Score']]
                for j in range(3):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(elem[j]))
        self.tableWidget.resizeColumnsToContents()
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        self.colorFirstThreePlaces()

    def filter(self):
        class_number = self.classes.currentText()
        if class_number=='9':
            class_number='09'
        elif class_number=='Все':
            self.loadTable(self.data_name)
            return
        final_data = []
        with open(self.data_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for index, row in enumerate(reader):
                if row[2] != "login":
                    fio = row[2].split('-')
                    if  fio[3] == class_number :
                        final_data.append([row[2],row[1],row[-1]])
        final_data.sort(key=lambda x: int(x[-1]),reverse=True)
        for i, row in enumerate(final_data):
            for j in range(3):
                self.tableWidget.setItem(i, j, QTableWidgetItem(row[j]))
        self.tableWidget.resizeColumnsToContents()
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        self.colorFirstThreePlaces()

    def colorRow(self, row, color):
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.item(row, i).setBackground(color)


    def colorFirstThreePlaces(self):
        colors = [QColor(225,215,0),QColor(181,181,189),QColor(156,82,33)]
        now = 0
        index = 0
        color_index = 0
        while True:
            tmp = int(self.tableWidget.item(index,2).text())
            if tmp >= now:
                self.colorRow(index,colors[color_index])
                now = tmp
            else:
                now = tmp
                color_index+=1
                self.colorRow(index, colors[color_index])
            index+=1
            if color_index==2:
                break



app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

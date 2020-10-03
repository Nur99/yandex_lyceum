import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from ui2 import Ui_MainWindow
import datetime


class DiaryEvent():
    def __init__(self, datetime, title):
        self.datetime = datetime
        self.title = title

    def to_str(self):
        return "{} - {}".format(self.datetime, self.title)

    def __str__(self):
        return self.to_str()


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.events = []
        self.pushButton.clicked.connect(self.add)

    def add(self):
        if self.lineEdit.text():
            ## Получение даты и времени
            t = datetime.datetime(self.calendarWidget.selectedDate().year(), self.calendarWidget.selectedDate().month(),
                                  self.calendarWidget.selectedDate().day(), self.timeEdit.time().hour(),
                                  self.timeEdit.time().minute())
            ## Создание события
            my_event = DiaryEvent(t, self.lineEdit.text())
            self.events.append(my_event)
            ## Сортировка по полю дата_время
            self.events = sorted(self.events, key=lambda x: x.datetime)
            self.listWidget.clear()
            ## Вывод списка
            self.listWidget.addItems([i.to_str() for i in self.events])


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

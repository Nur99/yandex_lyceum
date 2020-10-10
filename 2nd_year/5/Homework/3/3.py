import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidgetItem, QPushButton
from design import Ui_Form
import random


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.count = 37
        self.setupUi(self)
        self.lcdNumber.display(self.count)
        self.takeButton.clicked.connect(self.get)
        self.win = False

    def get(self):
        data = int(self.lineEdit.text())
        if data not in range(1, 6):
            self.label.setText("Невозможно взять столько")
        else:
            if not self.win:
                self.listWidget.addItem("Игрок взял - {}".format(data))
                if data >= self.count:
                    self.label.setText("Победа пользователя!")
                    self.win = True
                else:
                    self.count -= data
                self.lcdNumber.display(self.count)
                self.computer()

    def computer(self):
        cdata = random.randrange(1, 6)
        if not self.win:
            self.listWidget.addItem("Компьютер взял - {}".format(cdata))
            if cdata >= self.count:
                self.win = True
                self.label.setText("Победа компьютера!")
            else:
                self.count -= cdata
            self.lcdNumber.display(self.count)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

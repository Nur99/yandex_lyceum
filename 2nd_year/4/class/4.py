import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel, QCheckBox


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Прятки для виджетов ')
        self.setGeometry(500, 500, 500, 500)
        # self.setFixedSize(1000, 1000)

        # Левая часть
        self.label1 = QLabel(self)
        self.label1.setText("edit1")
        self.label1.move(40, 10)
        self.input_value1 = QLineEdit(self)
        self.input_value1.move(70, 10)
        self.input_value1.resize(130, 25)
        self.input_value1.setText("Поле edit1")
        self.checkbox1 = QCheckBox(self)
        self.checkbox1.move(15, 15)
        self.checkbox1.clicked.connect(self.convert)
        self.checkbox1.h = 0
        self.checkbox1.con = self.input_value1


        self.label2 = QLabel(self)
        self.label2.setText("edit2")
        self.label2.move(40, 50)
        self.input_value2 = QLineEdit(self)
        self.input_value2.move(70, 50)
        self.input_value2.resize(130, 25)
        self.input_value2.setText("Поле edit2")
        self.checkbox2 = QCheckBox(self)
        self.checkbox2.move(15, 50)
        self.checkbox2.clicked.connect(self.convert)
        self.checkbox2.h = 0
        self.checkbox2.con = self.input_value2

        self.label3 = QLabel(self)
        self.label3.setText("edit3")
        self.label3.move(40, 90)
        self.input_value3 = QLineEdit(self)
        self.input_value3.move(70, 90)
        self.input_value3.resize(130, 25)
        self.input_value3.setText("Поле edit3")
        self.checkbox3 = QCheckBox(self)
        self.checkbox3.move(15, 90)
        self.checkbox3.clicked.connect(self.convert)
        self.checkbox3.h = 0
        self.checkbox3.con = self.input_value3

        self.label4 = QLabel(self)
        self.label4.setText("edit4")
        self.label4.move(40, 130)
        self.input_value4 = QLineEdit(self)
        self.input_value4.move(70, 130)
        self.input_value4.resize(130, 25)
        self.input_value4.setText("Поле edit4")
        self.checkbox4 = QCheckBox(self)
        self.checkbox4.move(15, 130)
        self.checkbox4.clicked.connect(self.convert)
        self.checkbox4.h = 0
        self.checkbox4.con = self.input_value4

    def convert(self):
        if self.sender().h == 0:
            self.sender().con.hide()
        else:
            self.sender().con.show()
        self.sender().h = 1 - self.sender().h


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
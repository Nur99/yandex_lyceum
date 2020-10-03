import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from calc import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ## Подключаем цифры
        [i.clicked.connect(self.run) for i in self.buttonGroup_digits.buttons()]
        ## Подключаем бинарные операции (+,-,*,/)
        [i.clicked.connect(self.calc) for i in self.buttonGroup_binary.buttons()]
        ## Подключаем точку
        self.btn_dot.clicked.connect(self.run)
        ## Подключаем кнопку равно
        self.btn_eq.clicked.connect(self.result)
        ## Подключаем кнопку очистки
        self.btn_clear.clicked.connect(self.clear)
        ## Подключаем унарные операции
        self.btn_sqrt.clicked.connect(self.sqrt)
        self.btn_fact.clicked.connect(self.fact)

        ## Переменная, в которых хранятся последнее введённое число/результат вычисленного выражения
        self.data = ''
        ## Переменная, в которых хранятся выражение, которое нужно подсчитать
        self.data_eval = ''

    def real_fact(self, n):
        if n < 0:
            return -1
        if n == 0:
            return 1
        else:
            return n * self.real_fact(n - 1)

    def fact(self):
        if self.data_eval:
            self.data_eval = "self.real_fact({})".format(self.data_eval)
            print(self.data_eval)
            self.result()

    ## Сброс всех данных, очистка экрана
    def clear(self):
        self.data = ''
        self.data_eval = ''
        self.table.display('')

    def run(self):
        ## Формируется число, с помощью нажатий кнопок и отображается на дисплее
        if self.sender().text() == '.':
            if '.' in self.data:
                return
        if self.data != '0' or (self.data == '0' and self.sender().text() == '.'):
            self.data = self.data + self.sender().text()
            self.data_eval = self.data_eval + self.sender().text()
            self.table.display(self.data)
        else:
            self.data = self.sender().text()
            self.data_eval = self.sender().text()
            self.table.display(self.data)

    def sqrt(self):
        if self.data_eval:
            self.data_eval += '**0.5'
            self.result()

    def result(self):
        ## Происходит попытка вычисления выражения, в случае попытки деления на 0, выводится ошибка
        try:
            float(self.data_eval)
        except:
            try:

                self.data = eval(self.data_eval)
                self.data_eval = str(self.data)
                self.table.display(self.data)
            except ZeroDivisionError:
                self.table.display('Error')
            except:
                pass
        self.data = ''

    def calc(self):
        ## Происходит вычисление текущего выражения и дописывается новый знак. Если последним был уже знак действия, то он менятся.
        if self.data_eval:
            self.result()
            if (self.data_eval[-1] not in ['+', '-', '/', '*']):
                self.data_eval += self.sender().text()
            else:
                self.data_eval = self.data_eval[0:len(self.data_eval) - 1] + self.sender().text()
            self.data_eval = self.data_eval.replace('^', '**')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

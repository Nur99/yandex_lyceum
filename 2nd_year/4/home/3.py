from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QPlainTextEdit, QLineEdit

import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.menu = {"Чизбургер": 10, "Гамбургер": 20, "Кока-кола": 15, "Нагетсы": 30}
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 300, 300, 400)
        self.setWindowTitle('Заказ в Макдональдсе')

        self.check_b = []
        self.input_count = []

        k = 0
        ##Вывод QCheckBox и поля для ввода количества порций
        for i in self.menu.keys():
            tmp = QCheckBox(self)
            tmp.setText(i)
            tmp.move(10, 20 * k)
            tmp.stateChanged.connect(self.select_count)
            self.check_b.append(tmp)

            input_tmp = QLineEdit('', self)
            input_tmp.move(120, 20 * k)
            input_tmp.resize(30, 20)
            input_tmp.setEnabled(False)
            input_tmp.setText('0')
            self.input_count.append(input_tmp)
            k += 1

        ## Кнопка заказа
        self.btn = QPushButton('Заказать', self)
        self.btn.clicked.connect(self.run)
        self.btn.move(10, 20 * (len(self.check_b) + 1))

        ## Отображаем заказ на экране
        self.result = QPlainTextEdit(self)
        self.result.setEnabled(False)
        self.result.move(10, 20 * (len(self.check_b) + 3))

    ## Если блюдо выбрано, то становится доступен ввод количества
    def select_count(self, state):
        if state == 2:
            self.input_count[self.check_b.index(self.sender())].setText('1')
            self.input_count[self.check_b.index(self.sender())].setEnabled(True)
        else:
            self.input_count[self.check_b.index(self.sender())].setText('0')
            self.input_count[self.check_b.index(self.sender())].setEnabled(False)

    def run(self):
        self.result.clear()
        ## Получение массива кортежей формата (Блюдо, количество, итоговая стоимость)
        data = [(self.check_b[self.input_count.index(i)].text(), i.text(),
                 self.menu[self.check_b[self.input_count.index(i)].text()] * int(i.text())) for i in self.input_count if
                i.text() != '0']
        result = ["{}-----{}-----{}".format(*i) for i in data]
        result.insert(0, "Ваш заказ\n")
        self.result.appendPlainText("\n".join(result))
        self.result.appendPlainText("\nИтого: {}".format(sum(i[2] for i in data)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Вычисление выражений')
        self.setGeometry(300, 300, 300, 300)
        self.setFixedSize(310, 500)

        self.input_value = QLineEdit(self)
        self.input_value.move(10, 40)
        self.input_value.resize(130, 25)

        self.convert_button = QPushButton(self)

        self.convert_button.setText('->')
        self.convert_button.move(145, 40)
        self.convert_button.resize(25, 25)
        self.convert_button.clicked.connect(self.convert)
        self.cbs = 1

        self.label = QLabel(self)
        self.label.setText("Выражение:")
        self.label.move(10, 10)

        self.label1 = QLabel(self)
        self.label1.setText("Результат:")
        self.label1.move(175, 10)

        self.output_value = QLineEdit(self)
        # self.output_value.setEnabled(False)
        self.output_value.move(175, 40)
        self.output_value.resize(130, 25)

    def convert(self):
        self.output_value.setText(str(eval(self.input_value.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())


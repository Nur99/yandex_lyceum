import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton

convert_button_symbol = ['->', '<-']
convert_out = ['Фокус', '']
convert_in = ['', 'Фокус']


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Фокус со словами')
        self.setGeometry(300, 300, 300, 300)
        self.setFixedSize(310, 40)

        self.input_value = QLineEdit(self)
        self.input_value.move(10, 10)
        self.input_value.resize(130, 25)
        self.input_value.setText('Фокус')

        self.convert_button = QPushButton(self)

        self.convert_button.setText('->')
        self.convert_button.move(145, 10)
        self.convert_button.resize(25, 25)
        self.convert_button.clicked.connect(self.convert)
        self.cbs = 1

        self.output_value = QLineEdit(self)
        # self.output_value.setEnabled(False)
        self.output_value.move(175, 10)
        self.output_value.resize(130, 25)

    def convert(self):
        self.cbs = 1 - self.cbs
        self.convert_button.setText(convert_button_symbol[self.cbs])
        self.output_value.setText(convert_out[self.cbs])
        self.input_value.setText(convert_in[self.cbs])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())


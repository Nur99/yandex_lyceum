import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt5.QtWidgets import QLabel, QCheckBox


class Focus(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(600, 400, 285, 130)
        self.setWindowTitle('Прятки для виджетов')

        self.show_places = []
        show_places_row = 75
        show_places_col = 10
        show_places_length = 130
        show_places_width = 20

        for i in range(4):
            self.show_places.append(QLineEdit(self))
            self.show_places[i].move(show_places_row, show_places_col)
            self.show_places[i].resize(show_places_length, show_places_width)
            self.show_places[i].setText('Поле edit{}'.format(i + 1))
            show_places_col += 30


        self.checkboxes = []
        checkbox_row = 15
        checkbox_col = 12
        for i in range(4):
            self.checkboxes.append(QCheckBox(self))
            self.checkboxes[i].move(checkbox_row, checkbox_col)
            print(self.checkboxes[i])
            self.checkboxes[i].setText("edit{}".format(i + 1))
            self.checkboxes[i].setChecked(False)
            checkbox_col += 30
            self.checkboxes[i].stateChanged.connect(self.conv)


    def conv(self, checkbox):
        print(self.checkboxes)
        # position = int(checkbox.text()[-1])
        # print(position)
        # if checkbox.isChecked():
        #     self.show_places[position].hide()
        #     checkbox.setChecked(False)
        # else:
        #     self.show_places[position].show()
        #     checkbox.setChecked(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Focus()
    ex.show()
    sys.exit(app.exec())

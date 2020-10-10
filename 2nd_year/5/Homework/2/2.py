import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidgetItem, QPushButton
from U1 import Ui_Form
from PyQt5 import QtCore, QtMultimedia


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tr()

    def tr(self):
        mat = [
            [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        ]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                elem = QPushButton()
                if mat[i][j] == 1:
                    elem.setText("*")
                elem.setFixedSize(40, 40)
                self.gridLayout.addWidget(elem, i, j)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

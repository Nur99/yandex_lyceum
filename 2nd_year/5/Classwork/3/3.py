import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from ui_design import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        ## Подключение функционала к RadioButton
        self.buttonGroup.buttonClicked.connect(self.run2)
        self.buttonGroup.buttons()[0].setChecked(True)
        self.buttonGroup_2.buttonClicked.connect(self.run2)
        self.buttonGroup_3.buttonClicked.connect(self.run2)
        self.data = {self.buttonGroup: 'Синий', self.buttonGroup_2: 'Синий', self.buttonGroup_3: 'Синий'}

    def run(self):
        self.label_3.setText('Цвета: {}, {} и {}'.format(*self.data.values()))
        print('Цвета: {}, {} и {}'.format(*self.data.values()))

    def run2(self, button):
        self.data[self.sender()] = button.text()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

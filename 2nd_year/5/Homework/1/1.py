import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from design import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.addContact)

    def addContact(self):
        self.Phones.addItem("{} {}".format(self.Name.text(), self.Contact.text()))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

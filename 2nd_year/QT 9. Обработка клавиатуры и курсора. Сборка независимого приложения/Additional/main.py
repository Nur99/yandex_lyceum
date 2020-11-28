import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QPushButton
from PyQt5.QtGui import QPixmap
import sqlite3
from book_ui import Ui_Form as Ui_Book
from main_ui import Ui_Form


class MainWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("library.db")
        self.params = {"Автор": "author", "Название": "title"}
        self.searchButton.clicked.connect(self.search)

    def search(self):
        self.listWidget.clear()
        el = self.comboBox.currentText()
        if self.params.get(el) == "title":
            req = "SELECT id,title FROM books WHERE title LIKE '%{}%'".format(self.Title.text())
        else:
            req = "SELECT id,title FROM books WHERE author in (SELECT id from authors WHERE surname LIKE '%{}%')".format(
                self.Title.text())
        cur = self.con.cursor()
        data = cur.execute(req).fetchall()
        elems = [[QPushButton(i[1], self), i[0]] for i in data]
        for btn, loc_id in elems:
            btn.clicked.connect(self.show_info(loc_id))

        items = [QListWidgetItem() for _ in elems]
        for i in range(len(items)):
            self.listWidget.addItem(items[i])
            items[i].setSizeHint(elems[i][0].sizeHint())
            self.listWidget.setItemWidget(items[i], elems[i][0])

    def show_info(self, loc_id):
        def call_info():
            cur = self.con.cursor()
            title, year, author_id, image, genre_id = cur.execute(
                "SELECT title,year,author,image,genre From books Where id = {}".format(loc_id)).fetchone()
            author = " ".join(cur.execute("SELECT surname,name from authors where id={}".format(author_id)).fetchone())
            genre = cur.execute("SELECT title FROM genres WHERE id ={}".format(genre_id)).fetchone()[0]
            if image:
                info_book = BookWidget(self, title, author, str(year), genre, image)
            else:
                info_book = BookWidget(self, title, author, str(year), genre)
            info_book.show()

        return call_info


class BookWidget(QMainWindow, Ui_Book):
    def __init__(self, parent=None, title=None, author=None, year=None, genre=None, image='noname.png'):
        super().__init__(parent)
        self.setupUi(self)
        self.label_3.setText(title)
        self.label_7.setText(author)
        self.label_4.setText(year)
        self.label_8.setText(genre)

        self.pixmap = QPixmap(image)
        self.label.setPixmap(self.pixmap)


app = QApplication(sys.argv)
ex = MainWidget()
ex.show()
sys.exit(app.exec_())

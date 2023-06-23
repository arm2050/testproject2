import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class MenuPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Register and Login buttons
        register_btn = QtWidgets.QPushButton('Register', self)
        login_btn = QtWidgets.QPushButton('Login', self)

        register_btn.setGeometry(QtCore.QRect(20, 20, 80, 30))
        login_btn.setGeometry(QtCore.QRect(120, 20, 80, 30))

        # Category buttons
        clothes_btn = QtWidgets.QPushButton('Clothes', self)
        phone_btn = QtWidgets.QPushButton('Phone', self)
        laptop_btn = QtWidgets.QPushButton('Laptop', self)
        shoe_btn = QtWidgets.QPushButton('Shoe', self)
        electronic_btn = QtWidgets.QPushButton('Electronic', self)

        clothes_btn.setGeometry(QtCore.QRect(380, 20, 80, 30))
        phone_btn.setGeometry(QtCore.QRect(460, 20, 80, 30))
        laptop_btn.setGeometry(QtCore.QRect(540, 20, 80, 30))
        shoe_btn.setGeometry(QtCore.QRect(620, 20, 80, 30))
        electronic_btn.setGeometry(QtCore.QRect(700, 20, 80, 30))

        # Dropdown menus
        clothes_menu = QtWidgets.QMenu(self)
        clothes_menu.addAction('Option 1')
        clothes_menu.addAction('Option 2')
        clothes_menu.addAction('Option 3')
        clothes_menu.addAction('Option 4')
        clothes_btn.setMenu(clothes_menu)

        phone_menu = QtWidgets.QMenu(self)
        phone_menu.addAction('Option 1')
        phone_menu.addAction('Option 2')
        phone_menu.addAction('Option 3')
        phone_menu.addAction('Option 4')
        phone_btn.setMenu(phone_menu)

        laptop_menu = QtWidgets.QMenu(self)
        laptop_menu.addAction('Option 1')
        laptop_menu.addAction('Option 2')
        laptop_menu.addAction('Option 3')
        laptop_menu.addAction('Option 4')
        laptop_btn.setMenu(laptop_menu)

        shoe_menu = QtWidgets.QMenu(self)
        shoe_menu.addAction('Option 1')
        shoe_menu.addAction('Option 2')
        shoe_menu.addAction('Option 3')
        shoe_menu.addAction('Option 4')
        shoe_btn.setMenu(shoe_menu)

        electronic_menu = QtWidgets.QMenu(self)
        electronic_menu.addAction('Option 1')
        electronic_menu.addAction('Option 2')
        electronic_menu.addAction('Option 3')
        electronic_menu.addAction('Option 4')
        electronic_btn.setMenu(electronic_menu)

        # Search bar
        search_bar = QtWidgets.QLineEdit(self)
        search_bar.setPlaceholderText('Search')
        search_bar.setGeometry(QtCore.QRect(250, 100, 300, 30))

        # Set window properties
        self.setGeometry(100, 100, 800, 400)
        self.setWindowTitle('Menu Page')

        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MenuPage()
    sys.exit(app.exec_())

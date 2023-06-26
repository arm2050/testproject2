import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
import sqlite3

user = {}


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

        register_btn.clicked.connect(self.show_register_page)
        login_btn.clicked.connect(self.show_login_page)

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
        search_bar.setGeometry(QtCore.QRect(250, 150, 300, 30))

        # Set window properties
        self.setGeometry(100, 100, 800, 400)
        self.setWindowTitle('Menu Page')

        self.show()

    def show_register_page(self):
        register_dialog = RegisterDialog(self)
        register_dialog.exec_()

    def show_login_page(self):
        login_dialog = LoginDialog(self)
        login_dialog.exec_()


class RegisterDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Register Page')

        username_label = QtWidgets.QLabel('Username:')
        password_label = QtWidgets.QLabel('Password:')
        self.username_edit = QtWidgets.QLineEdit()
        self.password_edit = QtWidgets.QLineEdit()
        register_btn = QtWidgets.QPushButton('Register')
        register_btn.clicked.connect(self.showusername)

        layout = QtWidgets.QFormLayout()
        layout.addRow(username_label, self.username_edit)
        layout.addRow(password_label, self.password_edit)
        layout.addRow(register_btn)

        self.setLayout(layout)

    def showusername(self):
        username_text = self.username_edit.text()
        password_text = self.password_edit.text()

        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()

        # Create the table if it doesn't exist
        cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")

        try:
            # Insert the username and password into the table
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username_text, password_text))
            connection.commit()
            QMessageBox.information(self, "Registration", "Registration successful!")
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Registration", "Username already exists!")

        connection.close()


class LoginDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('login Page')

        username_label = QtWidgets.QLabel('Username:')
        password_label = QtWidgets.QLabel('Password:')
        self.username_edit = QtWidgets.QLineEdit()
        self.password_edit = QtWidgets.QLineEdit()
        register_btn = QtWidgets.QPushButton('Register')
        register_btn.clicked.connect(self.showusername)

        layout = QtWidgets.QFormLayout()
        layout.addRow(username_label, self.username_edit)
        layout.addRow(password_label, self.password_edit)
        layout.addRow(register_btn)

        self.setLayout(layout)

    def showusername(self):
        username_text = self.username_edit.text()
        password_text = self.password_edit.text()

        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()

        cursor.execute("SELECT password FROM users WHERE username = ?", (username_text,))
        result = cursor.fetchone()

        if result is None:
            message = "User doesn't exist."
        elif result[0] == password_text:
            message = "Welcome!"
        else:
            message = "Wrong password."

        QMessageBox.information(self, "Login Result", message)

        connection.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MenuPage()
    sys.exit(app.exec_())
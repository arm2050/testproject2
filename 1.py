import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
import sqlite3
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QGroupBox, QGridLayout, QLineEdit, QPushButton


user = {}


class MenuPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Register and Login buttons
        self.register_btn = QtWidgets.QPushButton('Register', self)
        self.login_btn = QtWidgets.QPushButton('Login', self)

        self.register_btn.setGeometry(QtCore.QRect(20, 20, 80, 30))
        self.login_btn.setGeometry(QtCore.QRect(120, 20, 80, 30))

        self.register_btn.clicked.connect(self.show_register_page)
        self.login_btn.clicked.connect(self.show_login_page)

        # Category buttons
        self.clothes_btn = QtWidgets.QPushButton('Clothes', self)
        self.phone_btn = QtWidgets.QPushButton('Phone', self)
        self.laptop_btn = QtWidgets.QPushButton('Laptop', self)
        self.shoe_btn = QtWidgets.QPushButton('Shoe', self)
        self.electronic_btn = QtWidgets.QPushButton('Electronic', self)

        self.clothes_btn.setGeometry(QtCore.QRect(380, 20, 80, 30))
        self.phone_btn.setGeometry(QtCore.QRect(460, 20, 80, 30))
        self.laptop_btn.setGeometry(QtCore.QRect(540, 20, 80, 30))
        self.shoe_btn.setGeometry(QtCore.QRect(620, 20, 80, 30))
        self.electronic_btn.setGeometry(QtCore.QRect(700, 20, 80, 30))

        # Dropdown menus
        self.clothes_menu = QtWidgets.QMenu(self)
        self.clothes_menu.addAction('Option 1')
        self.clothes_menu.addAction('Option 2')
        self.clothes_menu.addAction('Option 3')
        self.clothes_menu.addAction('Option 4')
        self.clothes_btn.setMenu(self.clothes_menu)

        self.phone_menu = QtWidgets.QMenu(self)
        self.phone_menu.addAction('Option 1')
        self.phone_menu.addAction('Option 2')
        self.phone_menu.addAction('Option 3')
        self.phone_menu.addAction('Option 4')
        self.phone_btn.setMenu(self.phone_menu)

        self.laptop_menu = QtWidgets.QMenu(self)
        self.laptop_menu.addAction('Option 1')
        self.laptop_menu.addAction('Option 2')
        self.laptop_menu.addAction('Option 3')
        self.laptop_menu.addAction('Option 4')
        self.laptop_btn.setMenu(self.laptop_menu)

        self.shoe_menu = QtWidgets.QMenu(self)
        self.shoe_menu.addAction('Option 1')
        self.shoe_menu.addAction('Option 2')
        self.shoe_menu.addAction('Option 3')
        self.shoe_menu.addAction('Option 4')
        self.shoe_btn.setMenu(self.shoe_menu)

        self.electronic_menu = QtWidgets.QMenu(self)
        self.electronic_menu.addAction('Option 1')
        self.electronic_menu.addAction('Option 2')
        self.electronic_menu.addAction('Option 3')
        self.electronic_menu.addAction('Option 4')
        self.electronic_btn.setMenu(self.electronic_menu)

        # Search bar
        self.search_bar = QtWidgets.QLineEdit(self)
        self.search_bar.setPlaceholderText('Search')
        self.search_bar.setGeometry(QtCore.QRect(250, 150, 300, 30))
        
        self.search_btn = QPushButton('Search', self)
        self.search_btn.setGeometry(QtCore.QRect(250, 200, 300, 30))
        self.search_btn.clicked.connect(self.search_button_clicked)

        # Set window properties
        self.setGeometry(100, 100, 800, 400)
        self.setWindowTitle('Menu Page')

        self.show()
        
    def search_button_clicked(self):
        search_text = self.search_bar.text()
        print(search_text)
    # Call the search function or method using the search_text


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
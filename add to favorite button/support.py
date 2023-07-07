import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
import sqlite3
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QGroupBox, QGridLayout, QLineEdit
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QGroupBox, QGridLayout, QLineEdit
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont, QDesktopServices
from PyQt5 import QtWidgets
from selenium import webdriver
from PyQt5 import *
from lxml import etree
from PyQt5 import QtWidgets, QtGui, QtCore, uic


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

        # Dropdown menus

        # Search bar

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
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")

        try:
            # Insert the username and password into the table
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)", (username_text, password_text))
            connection.commit()
            QMessageBox.information(
                self, "Registration", "Registration successful!")
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Registration",
                                "Username already exists!")

        connection.close()


class LoginDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('login Page')

        username_label = QtWidgets.QLabel('Username:')
        password_label = QtWidgets.QLabel('Password:')
        self.username_edit = QtWidgets.QLineEdit()
        self.password_edit = QtWidgets.QLineEdit()
        register_btn = QtWidgets.QPushButton('Registerr')
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

        cursor.execute(
            "SELECT password FROM users WHERE username = ?", (username_text,))
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

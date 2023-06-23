from PyQt5 import QtWidgets , uic
import sys
import mysql.connector as mysql
import sqlite3
import pymysql
from time import sleep
e1 = sqlite3.connect('i.db')
c = e1.cursor()
class Myclass(QtWidgets.QMainWindow) :
    def __init__(self):
        self.username_name = None
        self.password_name = None
        super().__init__()
        uic.loadUi('test1.ui', self)
        self.show()
        self.sign_up.clicked.connect(self.sign_up1)
        self.login.clicked.connect(self.login11)
    def sign_up1(self):
        uic.loadUi('sign_up.ui', self)
        self.sign_up2.clicked.connect(self.sign_up22)
        self.back.clicked.connect(self.sign_up33)
    def sign_up22(self):
        global s
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (username text , password text);
        """)
        s = e1.execute("""
            SELECT * FROM users;
        """)
        if (self.username_box.text() , self.password_box.text()) not in s.fetchall() :
            # pass
            c.execute("""
                INSERT INTO users (username , password) VALUES (:username , :password)
            """ , {'username' :self.username_box.text() , 'password' :self.password_box.text()})
            s = e1.execute("""
                SELECT * FROM users;
            """)
            print(s.fetchall())
        # else :
        #     print("another username with this password and username created")
    def sign_up33(self):
        uic.loadUi('test1.ui', self)
        self.show()
        self.sign_up.clicked.connect(self.sign_up1)
        self.login.clicked.connect(self.login11)
    def login11(self):
        uic.loadUi('login.ui', self)
        self.show()
        self.login2.clicked.connect(self.login22)
    def login22(self):
        s = e1.execute("""
            SELECT * FROM users;
        """)
        print(s.fetchall())
        print((self.username_login.text() , self.password_login.text()))
        print((self.username_login.text() , self.password_login.text()) in s.fetchall())
        if tuple((self.username_login.text() , self.password_login.text())) in list(s.fetchall()) :
            print("1")
            self.username_name = self.username_login.text()
            self.password_name = self.password_login.text()
            uic.loadUi('test1.ui', self)
            self.show()
            self.sign_up.clicked.connect(self.sign_up1)
            self.login.clicked.connect(self.login11)
        # else:
        #     print("you havent sign up until now")

print(("a" , "b") in [("a" , "b")])












# db = pymysql.connect(
#     host = "localhost" ,
#     user = "admin" ,
#     password = "admin" ,
# )
# db = pymysql.connect(user='root', passwd='pwd', unix_socket="/tmp/mysql.sock")
# print(db)


app = QtWidgets.QApplication(sys.argv)
w1 = Myclass()
sys.exit(app.exec_())
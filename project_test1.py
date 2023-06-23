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
        super().__init__()
        uic.loadUi('test1.ui', self)
        self.show()
        self.sign_up.clicked.connect(self.sign_up1)
    def sign_up1(self):
        uic.loadUi('sign_up.ui', self)
        self.sign_up2.clicked.connect(self.sign_up22)
        self.back.clicked.connect(self.sign_up33)
    def sign_up22(self):
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
from PyQt5 import QtWidgets , uic
import sys
from time import sleep
class Myclass(QtWidgets.QMainWindow) :
    def __init__(self):
        super().__init__()
        uic.loadUi('test1.ui', self)
        self.show()
        self.sign_up.clicked.connect(self.sign_up1)
    def sign_up1(self):
        uic.loadUi('sign_up.ui', self)




app = QtWidgets.QApplication(sys.argv)
w1 = Myclass()
sys.exit(app.exec_())
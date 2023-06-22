from PyQt5 import QtWidgets , uic
import sys
from time import sleep
class Myclass(QtWidgets.QMainWindow) :
    def __init__(self):
        super().__init__()
        uic.loadUi('test1.ui', self)
        self.show()





app = QtWidgets.QApplication(sys.argv)
w1 = Myclass()
sys.exit(app.exec_())
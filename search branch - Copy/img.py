import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from urllib.request import urlopen
from urllib.parse import quote

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Viewer")
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

        # Provide the URL of the image
        url = "https://dkstatics-public.digikala.com/digikala-products/1206571.jpg?x-oss-process=image/resize,m_lfit,h_300,w_300/quality,q_80.jpg"

        # Encode the URL
        encoded_url = quote(url, safe=':/?&=')  # Encode special characters

        # Load the image from the URL
        image_data = urlopen(encoded_url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(image_data)

        # Set the pixmap on the QLabel
        self.label.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

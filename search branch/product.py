import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QGroupBox, QGridLayout, QLineEdit
from PyQt5.QtGui import QPixmap, QFont
from PyQt5 import QtWidgets
from selenium import webdriver
import sys
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import requests
from bs4 import BeautifulSoup
import threading
class Product:
    def __init__(self, image_path, name, price):
        self.image_path = image_path
        self.name = name
        self.price = price
    def __repr__(self):
        return self.image_path + self.name + self.price

class ImageViewer(QWidget):
    def __init__(self, product):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.group_box = QGroupBox()
        self.group_layout = QVBoxLayout()
        self.group_box.setLayout(self.group_layout)

        self.image_label = QLabel()
        self.group_layout.addWidget(self.image_label)

        self.name_label = QLabel(product.name)
        self.group_layout.addWidget(self.name_label)

        self.price_label = QLabel(product.price)
        self.group_layout.addWidget(self.price_label)

        self.load_image(product.image_path)

    def load_image(self, image_path):
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            self.image_label.setText("Invalid image file!")
        else:
            self.image_label.setPixmap(
                pixmap.scaled(200, 200, aspectRatioMode=1))
products = []
s = 1
def a() :
    global s
    srcs = []
    driver = webdriver.Chrome()
    driver.get("https://basalam.com/search/subcategory/men-homewear")
    # driver.execute_script("window.scrollBy(0,6000)", "")
    for i in range(1 , 6) :
        driver.implicitly_wait(5)
        name1 = driver.find_element(By.XPATH , value='/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[2]/div/div[2]/section/div[' + str(i) + ']/div[2]/a')
        driver.implicitly_wait(5)
        price1 = driver.find_element(By.XPATH , '/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[2]/div/div[2]/section/div[' + str(i) + ' ]/div[2]/div[3]/div[2]/span')
        image = driver.find_element(By.XPATH , value='/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[2]/div/div[2]/section/div[' + str(i) + ']/div[1]/a/img')
        image_src = image.get_attribute("src")
        srcs.append(image_src)
        product1 = Product(str(s) + '.png', name1.text, price1.text)
        products.append(product1)
        print(product1)
        s = s + 1
    s = 1
    for src in srcs:
        response = requests.get(src)
        open(str(s) + '.png', 'wb').write(response.content)
        s = s + 1

    threads = []
    def download(url):
        global s
        response = requests.get(url)
        open(str(s) + '.png', 'wb').write(response.content)
        s = s + 1
    for src in srcs:
        t1 = threading.Thread(target=download , args=(src , ))
        threads.append(t1)
        t1.start()
        # response = requests.get(src)
        # print(src)
        # open(str(s) + '.jpg', 'wb').write(response.content)
        # s = s + 1
    for thread in threads:
        thread.join()
    # for i in range(1 , 6) :
    #     a1 = Product(srcs[i - 1] , name , price)
    #     products.append(a1)
    row = 1
    col = 0
    for product in products:
        viewer = ImageViewer(product)
        layout.addWidget(viewer.group_box, row, col)
        col += 1
        if col == 5:  # Change the number of columns as needed
            col = 0
            row += 1
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create a list of products
    # products = [
    #     Product("C:/Users/MR Razeghi/Desktop/final project ap/search branch/1.png",
    #             "Product 1", "$9.99"),
    #     Product("C:/Users/MR Razeghi/Desktop/final project ap/search branch/2.png",
    #             "Product 2", "$19.99"),
    #     Product("C:/Users/MR Razeghi/Desktop/final project ap/search branch/3.png",
    #             "Product 3", "$14.99"),
    #     Product("C:/Users/MR Razeghi/Desktop/final project ap/search branch/1.png",
    #             "Product 1", "$9.99"),
    #     Product("C:/Users/MR Razeghi/Desktop/final project ap/search branch/1.png",
    #             "Product 1", "$9.99"),
    #     # Add more products here...
    # ]

    # Create a main window
    main_window = QMainWindow()
    main_window.setWindowTitle("Image Viewer")
    main_window.setGeometry(100, 100, 600, 600)

    # Create a central widget to hold the layout
    central_widget = QWidget()
    main_window.setCentralWidget(central_widget)

    # Create a grid layout
    layout = QGridLayout()
    central_widget.setLayout(layout)

    # Add a search bar
    search_bar = QLineEdit()
    # Add the search bar at row 0, spanning 1 row and 5 columns
    layout.addWidget(search_bar, 0, 1, 1, 2)

    search_btn = QtWidgets.QPushButton('search')
    layout.addWidget(search_btn, 0, 3, 1, 1)
    search_btn.clicked.connect(a)
    # Create ImageViewer objects for each product



    # Show the main window
    main_window.show()
    sys.exit(app.exec_())

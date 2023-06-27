import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QGroupBox, QGridLayout, QLineEdit
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont
from PyQt5 import QtWidgets
from selenium import webdriver
from PyQt5 import *
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
from PyQt5.QtCore import *
class Product:
    def __init__(self, image_path, name, price):
        self.image_path = image_path
        self.name = name
        self.price = price
    def __repr__(self):
        return self.image_path + ' ' + self.name + ' ' +self.price

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
        ImageViewer.l = [self.name_label , self.price_label]
    def load_image(self, image_path):
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            self.image_label.setText("Invalid image file!")
        else:
            self.image_label.setPixmap(
                pixmap.scaled(200, 200, aspectRatioMode=1))
products = []
l1 = []
s = 1
p = 0
def a() :
    global s
    global p
    global l1
    global layout
    if p > 0 :
        for i in l1:
            i.setParent(None)
    text1 = search_bar.text()
    srcs = []
    driver = webdriver.Chrome()
    driver.get("https://basalam.com/s?q=" + str(text1))
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

    s = 1
    for src in srcs:
        response = requests.get(src)
        open(str(s) + '.png', 'wb').write(response.content)
        s = s + 1

    row = 1
    col = 0
    for product in products:
        viewer = ImageViewer(product)
        layout.addWidget(viewer.group_box, row, col)
        l1.append(viewer.group_box)
        col += 1
        if col == 5:  # Change the number of columns as needed
            col = 0
            row += 1
    s = 1
    for i in range(0 , len(products)) :
        products.pop(0)
    p = p + 1
def b(word) :
    global s
    global p
    srcs = []
    driver = webdriver.Chrome()
    driver.get("https://basalam.com/s?q=" + str(word))
    # driver.execute_script("window.scrollBy(0,6000)", "")
    for i in range(1, 6):
        driver.implicitly_wait(5)
        name1 = driver.find_element(By.XPATH,
                                    value='/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[2]/div/div[2]/section/div[' + str(
                                        i) + ']/div[2]/a')
        driver.implicitly_wait(5)
        price1 = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[2]/div/div[2]/section/div[' + str(
                                         i) + ' ]/div[2]/div[3]/div[2]/span')
        image = driver.find_element(By.XPATH,
                                    value='/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[2]/div/div[2]/section/div[' + str(
                                        i) + ']/div[1]/a/img')
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
    s = 1
    for src in srcs:
        response = requests.get(src)
        open(str(s) + '.png', 'wb').write(response.content)
        s = s + 1
    row = 1
    col = 0
    for product in products:
        viewer = ImageViewer(product)
        layout.addWidget(viewer.group_box, row, col)
        col += 1
        if col == 5:  # Change the number of columns as needed
            col = 0
            row += 1
    s = 1
    for i in range(0, len(products)):
        products.pop(0)
    p = p + 1
if __name__ == "__main__":
    app = QApplication(sys.argv)

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
    layout.addWidget(search_bar, 0, 1, 1 , 1 )
    layout2 = QGridLayout()
    layout.addLayout(layout2 , 0 , 0 , 1 , 1)
    search_btn = QtWidgets.QPushButton('search')
    layout.addWidget(search_btn, 0, 3, 1, 1)
    search_btn.clicked.connect(a)
    electronic_menu = QtWidgets.QMenu()

    p1 = electronic_menu.addAction('یخچال و فریزر')
    p2 = electronic_menu.addAction('ماشین لباسشویی')
    p12 = electronic_menu.addAction('بخاری و گرمایشی')
    p13 = electronic_menu.addAction('پنکه')

    electronic_btn = QtWidgets.QPushButton('لوازم برقی')
    electronic_btn.setMenu(electronic_menu)
    layout.addWidget(electronic_btn , 0 , 4 , 1 , 1)
    food_menu = QtWidgets.QMenu()
    p3 = food_menu.addAction('ماهی')
    p4 = food_menu.addAction('برنج')
    p9 = food_menu.addAction('نان')
    p10 = food_menu.addAction('شیرینی')
    p11 = food_menu.addAction('فندق')
    food_btn = QtWidgets.QPushButton('خوراکی')
    food_btn.setMenu(food_menu)
    clothes_btn = QtWidgets.QPushButton('لباس')
    clothes_menu = QtWidgets.QMenu()
    p5 = clothes_menu.addAction('کفش مردانه' )

    p6 = clothes_menu.addAction('شلوار مردانه')
    p7 = clothes_menu.addAction('کفش زنانه')
    p8 = clothes_menu.addAction('شلوار زنانه')
    clothes_btn.setMenu(clothes_menu)

    layout2.addWidget(electronic_btn, 0, 4, 1, 1)
    layout2.addWidget(food_btn , 0 , 5 , 1 , 1)
    layout2.addWidget(clothes_btn , 0 , 6 , 1 , 1)


    # l1 = [p1 , p2 , p3 , p4 , p5 , p6 , p7 , p8 , p9, p10 , p11]
    p1.triggered.connect(lambda : b(p1.text()))
    p2.triggered.connect(lambda : b(p2.text()))
    p3.triggered.connect(lambda : b(p3.text()))
    p4.triggered.connect(lambda : b(p4.text()))
    p5.triggered.connect(lambda : b(p5.text()))
    p6.triggered.connect(lambda : b(p6.text()))
    p7.triggered.connect(lambda : b(p7.text()))
    p8.triggered.connect(lambda : b(p8.text()))
    p9.triggered.connect(lambda: b(p9.text()))
    p10.triggered.connect(lambda: b(p10.text()))
    p11.triggered.connect(lambda: b(p11.text()))
    p12.triggered.connect(lambda: b(p12.text()))
    p13.triggered.connect(lambda: b(p13.text()))
    # for i in l1 :
    #     print(i.text())
    #     i.triggered.connect(lambda : b(i.text()))









    # Show the main window
    main_window.show()
    sys.exit(app.exec_())

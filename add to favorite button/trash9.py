import sys
from product3 import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont,QDesktopServices
from PyQt5 import *
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import requests

from PyQt5.QtCore import *
class Product:
    def __init__(self, image_path, name, price,href,src,site):
        self.image_path = image_path
        self.name = name
        self.price = price
        self.href = href
        self.src = src
        self.site = site
    def __repr__(self):
        return self.image_path + ' ' + self.name + ' ' +self.price + ' ' + self.href
products2 = []
class ImageViewer(QWidget):

    def __init__(self, product,user = None):
        global main_user
        super().__init__()

        user = main_user
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
        
        self.button = QPushButton("Open URL", self)
        self.button.clicked.connect(lambda: self.open_url(product.href))
        self.group_layout.addWidget(self.button)
        
        self.add_favorite_button = QPushButton("Add to Favorites")
        self.add_favorite_button.clicked.connect(lambda: self.add_to_favorites(product, user))
        self.group_layout.addWidget(self.add_favorite_button)

        self.show_details_button = QPushButton("Show Details")
        self.show_details_button.clicked.connect(lambda: self.show_product_details(product))
        self.group_layout.addWidget(self.show_details_button)

        self.load_image(product.image_path)
        ImageViewer.l = [self.name_label , self.price_label]
    def load_image(self, image_path):
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            self.image_label.setText("Invalid image file!")
        else:
            self.image_label.setPixmap(
                pixmap.scaled(200, 200, aspectRatioMode=1))
    def open_url(self,href):
        QDesktopServices.openUrl(QUrl(href))
    global main_user
    def add_to_favorites(self, product, main_user):
        print(main_user)
        main_user.favorites.append(product)
        # products2.append(product)
        QMessageBox.information(self, "Success", "Product added to favorites!")
        
    def show_product_details(self, product):
        if product.site == "basalam":
            details_dialog = QDialog(self)
            details_dialog.setWindowTitle("Product Details")

            driver = webdriver.Chrome('path/to/chromedriver')
            url = product.href
            driver.get(url)
            driver.implicitly_wait(5)
            # Find the element using XPath
            xpath = '//li[contains(@class, "product-attributes__item")]'
            elements = driver.find_elements(By.XPATH, xpath)
            # Extract the text from the element
            texts = [element.text.strip() for element in elements]
            # Close the browser window and quit the driver
            driver.quit()

            text_edit = QPlainTextEdit(details_dialog)
            text_edit.setPlainText('\n'.join(texts))  # Convert list to a single string
            text_edit.setReadOnly(True)  # Make the text read-only
            details_dialog.adjustSize()  # Adjust dialog size to fit the contents
            details_dialog.exec_()
        elif product.site == "timcheh":
            details_dialog = QDialog(self)
            details_dialog.setWindowTitle("Product Details")

            driver = webdriver.Chrome('path/to/chromedriver')
            url = product.href
            driver.get(url)
            button = driver.find_element(By.XPATH, "/html/body/div[1]/main/article/div/div[2]/div/ul/li[2]/a/i")

            # Click the button
            button.click()
            texts = []
            elements = driver.find_elements(
            By.XPATH, '//*[@id="product_tab_holder"]/section/div/div/div/ul/li')
            texts = []
        # Print the text content of each element (you can perform any desired action with the elements)
            for element in elements:
                texts.append(element.text)
            driver.quit()

            text_edit = QPlainTextEdit(details_dialog)
            text_edit.setPlainText('\n'.join(texts))  # Convert list to a single string
            text_edit.setReadOnly(True)  # Make the text read-only

            details_dialog.adjustSize()  # Adjust dialog size to fit the contents

            details_dialog.exec_()
        elif product.site == "fafa":
            details_dialog = QDialog(self)
            details_dialog.setWindowTitle("Product Details")
            
            driver = webdriver.Chrome('path/to/chromedriver')

            url = product.href
            # Open the webpage
            driver.get(url)


            elements = driver.find_elements(
                By.XPATH, '//*[@id="product-layout"]/div[2]/div/div[2]/div/div[3]/ul/li')
            texts = []
            
            for element in elements:
                texts.append(element.text)
            
            text_edit = QPlainTextEdit(details_dialog)
            text_edit.setPlainText('\n'.join(texts))  # Convert list to a single string
            text_edit.setReadOnly(True)  # Make the text read-only
            

class User:
    def __init__(self, name,password):
        self.name = name
        self.password = password
        self.favorites = []
    def __repr__(self):
        return self.name + self.password
ss = 6
pp = 6
l1 = []
def show_favorite():
    print("5")
    global main_user
    global pp
    ss = 6
    srcs2 = []
    for i in l1 :
        i.setParent(None)
    for product in main_user.favorites:
        srcs2.append(product.src)
    for src in srcs2:
        response = requests.get(src)
        open(str(ss) + '.png', 'wb').write(response.content)
        ss = ss + 1

    ss = 6
    # for i in range(len(products)):
    #     products.pop(0)

    # for i in user.fa

    row = 1
    col = 0
    for product in main_user.favorites :
        viewer = ImageViewer(product)
        layout.addWidget(viewer.group_box, row, col)
        l1.append(viewer.group_box)
        col += 1
        if col == 5:  # Change the number of columns as needed
            col = 0
            row += 1



    
products = []

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
    url = "https://basalam.com/s?q=" + str(text1)
    driver = webdriver.Chrome()
    driver.get(url)
    # driver.execute_script("window.scrollBy(0,6000)", "")
    for i in range(1 , 6) :
        driver.implicitly_wait(5)
        name1 = driver.find_element(By.XPATH , value='/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[2]/div/div[2]/section/div[' + str(i) + ']/div[2]/a')
        xpath = '/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[2]/div/div[2]/section/div[' + str(i) + ']/div[2]/a'
        response = requests.get(url)
        html = response.text

        tree = etree.HTML(html)
        element = tree.xpath(xpath)

        if element:
            href = element[0].get("href")
            href = "https://basalam.com" + href
        print(href)
        driver.implicitly_wait(5)
        try:
             price1 = driver.find_element(By.XPATH , '/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[2]/div/div[2]/section/div[' + str(i) + ' ]/div[2]/div[3]/div[2]/span')
        except NoSuchElementException:
            price = "unknown"
        
        image = driver.find_element(By.XPATH , value='/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[2]/div/div[2]/section/div[' + str(i) + ']/div[1]/a/img')
        image_src = image.get_attribute("src")
        srcs.append(image_src)
        product1 = Product(str(s) + '.png', name1.text, price1.text,href,image_src,"basalam")
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
    s = 1
    url = "https://timcheh.com/search?q=" + str(text1)
    driver = webdriver.Chrome()
    driver.get(url)
    driver.execute_script("window.scrollBy(0,200)", "")
    l1 = []
    sleep(7)
    for i in range(0 , len(srcs)) :
        srcs.pop(0)
    for i in range(1, 6):
        driver.implicitly_wait(10)
        name = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div[4]/div/div[2]/div[2]/ul/li[' + str(i) + ']/a/div[2]/h3').text
        driver.implicitly_wait(10)
        try:
            price = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div[2]/ul/li[' + str(
                i) + ']/a/div[2]/div[4]/div[1]').text
        except NoSuchElementException:
            price = "unknown"
        
        xpath = "/html/body/div[1]/div[4]/div/div[2]/div[2]/ul/li["+str(i) +"]/a"
        element = driver.find_element(By.XPATH, xpath)
        # Extract the href attribute from the element
        href = element.get_attribute("href")
        
        driver.implicitly_wait(10)
        image_address = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div[2]/ul/li[' + str(
            i) + ']/a/div[1]/div[1]/img').get_attribute("src")
        srcs.append(image_address)
        product1 = Product(str(i + 5) + '.png' , name , price, href, image_address,"timcheh")
        products.append(product1)
    for src in srcs :
        response = requests.get(src)
        open(str(s + 5) + '.png', 'wb').write(response.content)
        s = s + 1
    s = 1
    for i in range(0 , len(srcs)):
        srcs.pop(0)
    driver.get('https://fafait.net/')
    driver.implicitly_wait(14)
    driver.find_element(By.ID, 'search-product-input').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/header/form/input').send_keys(text1)
    driver.implicitly_wait(14)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[3]/button').click()
    for i in range(1, 6):
        driver.implicitly_wait(14)
        name = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[' + str(
            i) + ']/a/div[2]/div/h2').text
        
        xpath = "/html/body/div[2]/div[1]/div/div/div/div/div[2]/div["+str(i)+"]/a"
        element = driver.find_element(By.XPATH, xpath)
        # Extract the href attribute from the element
        href = element.get_attribute("href")
        
        driver.implicitly_wait(14)
        
        try:
            price = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[' + str(
                i) + ']/a/div[2]/div/div[3]/div/div/div/div/div/span[1]').text
        except NoSuchElementException:
            price = "unknown"
        
        driver.implicitly_wait(14)
        img_address = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[' + str(
            i) + ']/a/div[1]/img').get_attribute('src')
        srcs.append(img_address)
        product1 = Product(str(i + 10) + '.png' , name, price, href, img_address,"fafa")
        products.append(product1)
    s = 1
    for src in srcs:
        response = requests.get(src)
        open(str(s + 10) + '.png', 'wb').write(response.content)
        s = s + 1
    s = 1



    row = 1
    col = 0
    for product in products:
        viewer = ImageViewer(product)
        layout.addWidget(viewer.group_box, row, col)
        l1.append(viewer.group_box)
        col += 1
        if col == 3:  # Change the number of columns as needed
            col = 0
            row += 1
    s = 1
    for i in range(0 , len(products)) :
        products.pop(0)
    p = p + 1
def b(word) :
    global s
    global p
    global l1
    global layout
    if p > 0:
        for i in l1:
            i.setParent(None)
    srcs = []
    driver = webdriver.Chrome()
    url = "https://basalam.com/s?q=" + str(word)
    driver.get(url)
    # driver.execute_script("window.scrollBy(0,6000)", "")
    for i in range(1, 6):
        driver.implicitly_wait(5)
        name1 = driver.find_element(By.XPATH,
                                    value='/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[2]/div/div[2]/section/div[' + str(
                                        i) + ']/div[2]/a')
        xpath = '/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[2]/div/div[2]/section/div[' + str(i) + ']/div[2]/a'
        response = requests.get(url)
        html = response.text

        tree = etree.HTML(html)
        element = tree.xpath(xpath)

        if element:
            href = element[0].get("href")
            href = "https://basalam.com" + href
        print(href)
        driver.implicitly_wait(5)
        try:
            price1 = driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[2]/div/div[2]/section/div[' + str(
                                            i) + ' ]/div[2]/div[3]/div[2]/span')
        except NoSuchElementException:
            price = "unknown"
        image = driver.find_element(By.XPATH,
                                    value='/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[2]/div/div[2]/section/div[' + str(
                                        i) + ']/div[1]/a/img')
        image_src = image.get_attribute("src")
        srcs.append(image_src)
        product1 = Product(str(s) + '.png', name1.text, price1.text,href,image_src,"basalam")
        products.append(product1)
        print(product1)
        s = s + 1
    driver.close()
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
    s = 1
    url = "https://timcheh.com/search?q=" + str(word)
    driver = webdriver.Chrome()
    driver.get(url)
    driver.execute_script("window.scrollBy(0,300)", "")
    l1 = []
    sleep(7)
    for i in range(0, len(srcs)):
        srcs.pop(0)
    for i in range(1, 6):
        driver.implicitly_wait(10)
        
        name = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div[4]/div/div[2]/div[2]/ul/li[' + str(i) + ']/a/div[2]/h3').text
        
        xpath = "/html/body/div[1]/div[4]/div/div[2]/div[2]/ul/li["+str(i) +"]/a"
        element = driver.find_element(By.XPATH, xpath)
        # Extract the href attribute from the element
        href = element.get_attribute("href")
        
        driver.implicitly_wait(10)
        try:
            price = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div[2]/ul/li[' + str(
                i) + ']/a/div[2]/div[4]/div[1]').text
        except NoSuchElementException:
            price = "unknown"
        driver.implicitly_wait(10)
        
        image_address = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div[2]/ul/li[' + str(
            i) + ']/a/div[1]/div[1]/img').get_attribute("src")
        srcs.append(image_address)
        product1 = Product(str(i + 5) + '.png', name, price, href, image_address,"timcheh")
        products.append(product1)
    for src in srcs:
        response = requests.get(src)
        open(str(s + 5) + '.png', 'wb').write(response.content)
        s = s + 1
    driver.close()
    s = 1
    for i in range(0, len(products)):
        products.pop(0)
    
    driver = webdriver.Chrome()
    driver.get('https://fafait.net/')
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'search-product-input').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/header/form/input').send_keys(word)
    driver.implicitly_wait(14)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[3]/button').click()
    for i in range(1, 6):
        driver.implicitly_wait(14)
        name = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[' + str(
            i) + ']/a/div[2]/div/h2').text
        
        xpath = "/html/body/div[2]/div[1]/div/div/div/div/div[2]/div["+str(i)+"]/a"
        element = driver.find_element(By.XPATH, xpath)
        # Extract the href attribute from the element
        href = element.get_attribute("href")
         
        driver.implicitly_wait(14)
        try:
            price = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[' + str(
                i) + ']/a/div[2]/div/div[3]/div/div/div/div/div/span[1]').text
        except NoSuchElementException:
            price = "unknown"
        
        
        driver.implicitly_wait(14)
        img_address = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[' + str(
            i) + ']/a/div[1]/img').get_attribute('src')
        srcs.append(img_address)
        product1 = Product(str(i + 10) + '.png' , name, price, href, img_address,"fafa")
        products.append(product1)
    driver.close()
    s = 1
    for src in srcs:
        response = requests.get(src)
        open(str(s + 10) + '.png', 'wb').write(response.content)
        s = s + 1
    s = 1
    
    row = 1
    col = 0
    for product in products:
        viewer = ImageViewer(product)
        layout.addWidget(viewer.group_box, row, col)
        l1.append(viewer.group_box)
        col += 1
        if col == 3:  # Change the number of columns as needed
            col = 0
            row += 1
    s = 1
    for i in range(0 , len(products)) :
        products.pop(0)
    p = p + 1
userss = []
def g() :
    global layout
    global userss
    g1 = QDialog()

    username_label = QtWidgets.QLabel('Username:')
    password_label = QtWidgets.QLabel('Password:')
    username_edit = QtWidgets.QLineEdit()
    password_edit = QtWidgets.QLineEdit()
    register_btn = QtWidgets.QPushButton('Register')
    def s() :
        global userss
        if (username_edit.text(), password_edit.text()) in userss:
            print(userss)
            msg = QMessageBox()
            msg.setText("Username already exists!")
            msg.exec_()

        else:
            print("--------------")
            msg = QMessageBox()
            
            msg.setText("Registration successful!")
            msg.exec_()
            userss.append(User(username_edit.text() , password_edit.text()))
        g1.setParent(None)
        layout3.setParent(None)
        return None
    register_btn.clicked.connect(s)

    layout3 = QtWidgets.QFormLayout()
    layout3.addRow(username_label, username_edit)
    layout3.addRow(password_label, password_edit)
    layout3.addRow(register_btn)

    g1.setLayout(layout3)

    layout.addWidget(g1 , 1 ,0 , 1 , 1)
def h() :
    global layout
    global userss
    g1 = QDialog()

    username_label = QtWidgets.QLabel('Username:')
    password_label = QtWidgets.QLabel('Password:')
    username_edit = QtWidgets.QLineEdit()
    password_edit = QtWidgets.QLineEdit()
    register_btn = QtWidgets.QPushButton('login')
    def s() :
        global userss
        global main_user
        for user in userss:
            if user.name == username_edit.text():
                if user.password == password_edit.text():
                    msg = QMessageBox()
                    main_user = user
                    msg.setText("Logging successful")
                    msg.exec_()
                    break  # Exit 
                else:
                    msg = QMessageBox()
                    msg.setText("wrong password!")
                    msg.exec_()
        else:
            msg = QMessageBox()

            msg.setText("username and password does not exists!")
            msg.exec_()
        g1.setParent(None)
        layout3.setParent(None)
        return None
    register_btn.clicked.connect(s)

    layout3 = QtWidgets.QFormLayout()
    layout3.addRow(username_label, username_edit)
    layout3.addRow(password_label, password_edit)
    layout3.addRow(register_btn)

    g1.setLayout(layout3)

    layout.addWidget(g1 , 1 ,0 , 1 , 1)
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

    main_user = None
    
    # Add a search bar
    search_bar = QLineEdit()
    # Add the search bar at row 0, spanning 1 row and 5 columns
    layout.addWidget(search_bar, 0, 1, 1 , 1 )
    layout2 = QGridLayout()
    layout.addLayout(layout2 , 0 , 0 , 1 , 1)
    search_btn = QtWidgets.QPushButton('search')
    favorite_menu_btn = QtWidgets.QPushButton('favorites')
    sign_up_btn = QtWidgets.QPushButton('sign_up')
    login_btn = QtWidgets.QPushButton('login')
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
    p3 = food_menu.addAction('لپتاپ')
    p4 = food_menu.addAction('هدفون')
    p9 = food_menu.addAction('دوربین')
    p10 = food_menu.addAction('هارد')
    food_btn = QtWidgets.QPushButton('لپتاپ و وسایل مربوطه')
    food_btn.setMenu(food_menu)
    clothes_btn = QtWidgets.QPushButton('گوشی و وسایل مربوطه')
    clothes_menu = QtWidgets.QMenu()
    p5 = clothes_menu.addAction('اسپیکر' )

    p6 = clothes_menu.addAction('لوازم جانبی گوشی')
    p7 = clothes_menu.addAction('ساعت هوشمند')
    p8 = clothes_menu.addAction('گوشی')
    clothes_btn.setMenu(clothes_menu)

    layout2.addWidget(electronic_btn, 0, 5, 1, 1)
    layout2.addWidget(food_btn , 0 , 6 , 1 , 1)
    layout2.addWidget(clothes_btn , 0 , 7 , 1 , 1)
    layout2.addWidget(favorite_menu_btn , 0 , 2 , 1 , 1)
    layout2.addWidget(sign_up_btn , 0 , 3 , 1 , 1)
    layout2.addWidget(login_btn, 0, 4, 1, 1)



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
    p12.triggered.connect(lambda: b(p12.text()))
    p13.triggered.connect(lambda: b(p13.text()))


    sign_up_btn.clicked.connect(g)
    login_btn.clicked.connect(h)
    favorite_menu_btn.clicked.connect(show_favorite)
    # for i in l1 :
    #     print(i.text())
    #     i.triggered.connect(lambda : b(i.text()))

    # Show the main window
    main_window.show()
    sys.exit(app.exec_())
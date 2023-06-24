import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import requests
from bs4 import BeautifulSoup


class MenuPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Register and Login buttons
        register_btn = QtWidgets.QPushButton('Register', self)
        login_btn = QtWidgets.QPushButton('Login', self)
        search_button = QtWidgets.QPushButton('search', self)
        search_button.setGeometry(QtCore.QRect(400, 320 , 80 , 30))
        register_btn.setGeometry(QtCore.QRect(20, 20, 80, 30))
        login_btn.setGeometry(QtCore.QRect(120, 20, 80, 30))

        # Category buttons
        clothes_btn = QtWidgets.QPushButton('Clothes', self)
        phone_btn = QtWidgets.QPushButton('Phone', self)
        laptop_btn = QtWidgets.QPushButton('Laptop', self)
        shoe_btn = QtWidgets.QPushButton('Shoe', self)
        electronic_btn = QtWidgets.QPushButton('Electronic', self)

        clothes_btn.setGeometry(QtCore.QRect(380, 20, 80, 30))
        phone_btn.setGeometry(QtCore.QRect(460, 20, 80, 30))
        laptop_btn.setGeometry(QtCore.QRect(540, 20, 80, 30))
        shoe_btn.setGeometry(QtCore.QRect(620, 20, 80, 30))
        electronic_btn.setGeometry(QtCore.QRect(700, 20, 80, 30))

        # Dropdown menus
        clothes_menu = QtWidgets.QMenu(self)
        clothes_menu.addAction('Option 1')
        clothes_menu.addAction('Option 2')
        clothes_menu.addAction('Option 3')
        clothes_menu.addAction('Option 4')
        clothes_btn.setMenu(clothes_menu)

        phone_menu = QtWidgets.QMenu(self)
        phone_menu.addAction('Option 1')
        phone_menu.addAction('Option 2')
        phone_menu.addAction('Option 3')
        phone_menu.addAction('Option 4')
        phone_btn.setMenu(phone_menu)

        laptop_menu = QtWidgets.QMenu(self)
        laptop_menu.addAction('Option 1')
        laptop_menu.addAction('Option 2')
        laptop_menu.addAction('Option 3')
        laptop_menu.addAction('Option 4')
        laptop_btn.setMenu(laptop_menu)

        shoe_menu = QtWidgets.QMenu(self)
        shoe_menu.addAction('Option 1')
        shoe_menu.addAction('Option 2')
        shoe_menu.addAction('Option 3')
        shoe_menu.addAction('Option 4')
        shoe_btn.setMenu(shoe_menu)

        electronic_menu = QtWidgets.QMenu(self)
        electronic_menu.addAction('Option 1')
        electronic_menu.addAction('Option 2')
        electronic_menu.addAction('Option 3')
        electronic_menu.addAction('Option 4')
        electronic_btn.setMenu(electronic_menu)

        # Search bar
        search_bar = QtWidgets.QLineEdit(self)
        search_bar.setPlaceholderText('Search')
        search_bar.setGeometry(QtCore.QRect(250, 100, 300, 30))

        # Set window properties
        self.setGeometry(100, 100, 800, 400)
        self.setWindowTitle('Menu Page')
        search_button.clicked.connect(self.a)
        self.show()
    def a(self):
        driver = webdriver.Chrome()
        driver.get("https://www.digikala.com/search/category-mobile-phone/xiaomi/")
        # driver.find_element(by=By.CSS_SELECTOR , value='#search').send_keys("gg")
        # driver.implicitly_wait(45)

        # products = driver.find_elements(by=By.CSS_SELECTOR , value='h3.ellipsis-2.text-body2-strong.color-700.styles_VerticalProductCard__productTitle__6zjjN')
        # print(products)
        # for i in products :
        #     print(i.text)
        # driver.find_element(by=By.XPATH , value = '//*[@id="__next"]/div[1]/div[2]/div[4]/div[1]/header/div[2]/div[1]/div/div/div/svg/use').click()
        products = []
        # names = driver.find_elements(by=By.CSS_SELECTOR,value='h3.ellipsis-2.text-body2-strong color-700.styles_VerticalProductCard__productTitle__6zjjN')
        # names = driver.find_elements(by=By.XPATH,value='')
        # prices = driver.find_elements(by=By.CSS_SELECTOR,value='div.d-flex.ai-center.jc-end.gap-1.color-700.color-400.text-h5.grow-1')
        # prices = driver.find_elements(by=By.XPATH,value='div')
        # ProductListPagesWrapper > section > div.product-list_ProductList__pagesContainer__zAhrX.product-list_ProductList__pagesContainer--withoutSidebar__aty9j > div:nth-child(1) > a > div > article > div.d-flex.grow-1.pos-relative.flex-column > div.grow-1.d-flex.flex-column.ai-stretch.jc-start > div:nth-child(2) > h3
        # names = driver.find_element(by=By.CSS_SELECTOR, value='')
        driver.implicitly_wait(35)
        prices = driver.find_elements(by=By.CSS_SELECTOR , value='div.d-flex.ai-center.jc-end.gap-1.color-700.color-400.text-h5.grow-1')
        names = driver.find_elements(by=By.CSS_SELECTOR , value='h3.ellipsis-2.text-body2-strong.color-700.styles_VerticalProductCard__productTitle__6zjjN')
        for i in range(0 , 3) :
            # name = driver.find_element(by=By.XPATH , value='/html/body/div[1]/div[1]/div[2]/div[4]/div[2]/div[3]/section/div[2]/div[' + str(i) + ']/a/div/article/div[2]/div[2]/div[2]/h3').text
            # price = driver.find_element(by=By.XPATH , value='/html/body/div[1]/div[1]/div[2]/div[4]/div[2]/div[3]/section/div[2]/div[' + str(i) + ']/a/div/article/div[2]/div[2]/div[4]/div[1]/div/span').text
            #
            # a1 = A(0 , prices[i] , None)
            # products.append(a1)
            pass
        for i in range(0 , 10) :
            print(prices[i].text , names[i].text)
        return None

class A:
        def __init__(self , name , price , img):
            self.name = name
            self.price = price
            self.img = img
        def __repr__(self):
            return self.name + self.price
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MenuPage()
    sys.exit(app.exec_())


























# /html/body/div[1]/div[1]/div[2]/div[4]/div[2]/div[3]/section/div[2]/div[1]/a/div/article/div[2]/div[2]/div[2]/h3
# /html/body/div[1]/div[1]/div[2]/div[4]/div[2]/div[3]/section/div[2]/div[3]/a/div/article/div[2]/div[2]/div[2]/h3
# /html/body/div[1]/div[1]/div[2]/div[4]/div[2]/div[3]/section/div[2]/div[4]/a/div/article/div[2]/div[2]/div[2]/h3

















# /html/body/div[1]/div[1]/div[2]/div[4]/div[2]/div[3]/section/div[2]/div[1]/a/div/article/div[2]/div[2]/div[4]/div[1]/div/span
# /html/body/div[1]/div[1]/div[2]/div[4]/div[2]/div[3]/section/div[2]/div[2]/a/div/article/div[2]/div[2]/div[4]/div[1]/div/span

















# /html/body/div[1]/div[1]/div[2]/div[4]/div[2]/div[3]/section/div[2]/div[1]/a/div/article/div[2]/div[2]/div[2]/h3
# /html/body/div[1]/div[1]/div[2]/div[4]/div[2]/div[3]/section/div[2]/div[2]/a/div/article/div[2]/div[2]/div[2]/h3





#ProductListPagesWrapper > section > div.product-list_ProductList__pagesContainer__zAhrX.product-list_ProductList__pagesContainer--withoutSidebar__aty9j > div:nth-child(1) > a > div > article > div.d-flex.grow-1.pos-relative.flex-column > div.grow-1.d-flex.flex-column.ai-stretch.jc-start > div:nth-child(2) > h3

#ProductListPagesWrapper > section > div.product-list_ProductList__pagesContainer__zAhrX.product-list_ProductList__pagesContainer--withoutSidebar__aty9j > div:nth-child(1) > a > div > article > div.d-flex.grow-1.pos-relative.flex-column > div.grow-1.d-flex.flex-column.ai-stretch.jc-start > div:nth-child(2) > h3

#ProductListPagesWrapper > section > div.product-list_ProductList__pagesContainer__zAhrX.product-list_ProductList__pagesContainer--withoutSidebar__aty9j > div:nth-child(1) > a > div > article > div.d-flex.grow-1.pos-relative.flex-row > div.grow-1.d-flex.flex-column.ai-stretch.jc-start > div:nth-child(2) > h3
#ProductListPagesWrapper > section > div.product-list_ProductList__pagesContainer__zAhrX.product-list_ProductList__pagesContainer--withoutSidebar__aty9j > div:nth-child(2) > a > div > article > div.d-flex.grow-1.pos-relative.flex-row > div.grow-1.d-flex.flex-column.ai-stretch.jc-start > div:nth-child(2) > h3



#ProductListPagesWrapper > section > div.product-list_ProductList__pagesContainer__zAhrX.product-list_ProductList__pagesContainer--withoutSidebar__aty9j > div:nth-child(1) > a > div > article > div.d-flex.grow-1.pos-relative.flex-column > div.grow-1.d-flex.flex-column.ai-stretch.jc-start > div:nth-child(2) > h3
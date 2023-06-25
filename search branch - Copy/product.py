import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QGroupBox, QGridLayout
from PyQt5.QtGui import QPixmap, QFont

class Product:
    def __init__(self, image_path, name, price):
        self.image_path = image_path
        self.name = name
        self.price = price

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
            self.image_label.setPixmap(pixmap.scaled(200, 200, aspectRatioMode=1))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create a list of products
    products = [
        Product("C:/Users\MR Razeghi/Desktop/final project ap/search branch/1.png",
                "Product 1", "$9.99"),
        Product("C:/Users\MR Razeghi/Desktop/final project ap/search branch/2.png",
                "Product 2", "$19.99"),
        Product("C:/Users\MR Razeghi/Desktop/final project ap/search branch/3.png",
                "Product 3", "$14.99"),
        Product("C:/Users\MR Razeghi/Desktop/final project ap/search branch/1.png",
                "Product 1", "$9.99"),
        Product("C:/Users\MR Razeghi/Desktop/final project ap/search branch/1.png",
                "Product 1", "$9.99"),
        # Add more products here...
    ]

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

    # Create ImageViewer objects for each product
    row = 0
    col = 0
    for product in products:
        viewer = ImageViewer(product)
        layout.addWidget(viewer.group_box, row, col)
        col += 1
        if col == 5:  # Change the number of columns as needed
            col = 0
            row += 1

    # Show the main window
    main_window.show()
    sys.exit(app.exec_())

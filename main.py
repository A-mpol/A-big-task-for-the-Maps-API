import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from map_interface import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class Map(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Map")

        self.show_button.clicked.connect(self.set_image)

    def geocode(self):
        coordinates = self.coords_edit.text()
        size = self.size_edit.text()
        map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + coordinates + "&z=" + size + "&l=map"
        response = requests.get(map_request)
        return response.content

    def set_image(self):
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(self.geocode())

        self.pixmap = QPixmap(self.map_file)
        self.image_label.setPixmap(self.pixmap)

    def closeEvent(self, event):
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Map()
    ex.show()
    sys.exit(app.exec_())

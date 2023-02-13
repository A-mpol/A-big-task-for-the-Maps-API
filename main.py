import os
import sys

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from map_interface import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class ResponseError(Exception):
    pass


class Map(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Map")

        self.show_button.clicked.connect(self.set_image)

    def geocode(self):
        coordinates = str(self.coordinates[0]) + "," + str(self.coordinates[1])
        size = str(self.size)
        map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + coordinates + "&z=" + size + "&l=map"
        response = requests.get(map_request)
        return response.content

    def set_image(self):
        if self.check_parameters():
            self.map_file = "map.png"
            with open(self.map_file, "wb") as file:
                file.write(self.geocode())

            self.pixmap = QPixmap(self.map_file)
            self.image_label.setPixmap(self.pixmap)

    def check_parameters(self):
        self.mistake_label.setText("")
        try:
            self.coordinates = self.coords_edit.text().replace(" ", "").split(",")
            self.coordinates = tuple([float(self.coordinates[0]), float(self.coordinates[1])])
            self.size = int(self.size_edit.text())
            if not self.geocode():
                raise ResponseError
            return True
        except Exception:
            self.mistake_label.setText("Некорректные данные!")
            return False

    def closeEvent(self, event):
        os.remove(self.map_file)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            if self.size < 19:
                self.size += 1
                self.size_edit.setText(str(self.size))
                self.set_image()
        elif event.key() == Qt.Key_PageDown:
            if self.size > 1:
                self.size -= 1
                self.size_edit.setText(str(self.size))
                self.set_image()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Map()
    ex.show()
    sys.exit(app.exec_())

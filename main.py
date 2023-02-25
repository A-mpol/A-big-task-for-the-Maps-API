import os
import sys
import requests

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from map_interface import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

from functions import *


class ResponseError(Exception):
    pass


class Map(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Map")

        self.map_file = "map.png"
        self.coordinates = [0, 0]
        self.size = 1
        self.map_type = "map"
        self.point_cords = None

        self.show_button.clicked.connect(self.make_request)
        self.search_button.clicked.connect(self.make_request)
        self.reset_button.clicked.connect(self.reset_search)

        self.map_radiobutton.setChecked(True)
        self.map_radiobutton.clicked.connect(self.change_type_of_map)
        self.sat_radiobutton.clicked.connect(self.change_type_of_map)
        self.sat_skl_radiobutton.clicked.connect(self.change_type_of_map)

    def change_type_of_map(self):
        if self.map_radiobutton.isChecked():
            self.map_type = "map"
        elif self.sat_radiobutton.isChecked():
            self.map_type = "sat"
        elif self.sat_skl_radiobutton.isChecked():
            self.map_type = "sat,skl"
        self.set_image(self.geocode())

    def make_request(self):
        if self.sender().text() == "Show" and self.set_show_parameters():
            self.point_cords = None
            self.set_image(self.geocode())
        elif self.sender().text() == "Search" and self.set_search_parameters():
            self.point_cords = self.coordinates.copy()
            self.set_image(self.geocode())

    def reset_search(self):
        self.point_cords = None
        self.set_image(self.geocode())

    def geocode(self):
        coordinates = str(self.coordinates[0]) + "," + str(self.coordinates[1])
        size = str(self.size)
        map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + coordinates + "&z=" + size + "&l=" + self.map_type
        if self.point_cords is not None:
            map_request += "&pt=" + ','.join([str(num) for num in self.point_cords])
        response = requests.get(map_request)
        return response.content

    def set_image(self, data):
        with open(self.map_file, "wb") as file:
            file.write(data)

        self.pixmap = QPixmap(self.map_file)
        self.image_label.setPixmap(self.pixmap)

    def set_show_parameters(self):
        self.mistake_label.setText("")
        try:
            self.coordinates = self.coords_edit.text().replace(" ", "").split(",")
            self.coordinates = [float(self.coordinates[0]), float(self.coordinates[1])]
            self.size = int(self.size_edit.text())
            if not geocode(self.coordinates, self.size, self.map_type):
                raise ResponseError
            return True
        except Exception:
            self.mistake_label.setText("Некорректные данные!")
            return False

    def set_search_parameters(self):
        self.mistake_label.setText("")
        try:
            address = self.object_edit.text()
            full_address = full_address_object(address)
            self.address_edit.setText(full_address)
            self.coordinates = object_coordinates(address)
            self.size = int(self.size_edit.text())
            if not geocode(self.coordinates, self.size, self.map_type):
                raise ResponseError
            return True
        except Exception:
            self.mistake_label.setText("Некорректные данные!")
            return False

    def moving(self):
        size = self.size
        if 10 < size < 13:
            return size / (((size % 10) + size % 10) * 100)
        elif 13 < size < 18:
            return 0.005
        else:
            return 0.5

    def closeEvent(self, event):
        if os.access(self.map_file, os.F_OK):
            os.remove(self.map_file)

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            if self.size < 19:
                self.size += 1
                self.size_edit.setText(str(self.size))
                self.set_image(self.geocode())
        if event.key() == Qt.Key_PageDown:
            if self.size > 1:
                self.size -= 1
                self.size_edit.setText(str(self.size))
                self.set_image(self.geocode())
        if event.key() == Qt.Key_Up:
            if self.coordinates[1] < 89:
                self.coordinates[1] += self.moving()
                self.coords_edit.setText(str(self.coordinates[0]) + ", " + str(self.coordinates[1]))
                self.set_image(self.geocode())
        if event.key() == Qt.Key_Down:
            if self.coordinates[1] > -89:
                self.coordinates[1] -= self.moving()
                self.coords_edit.setText(str(self.coordinates[0]) + ", " + str(self.coordinates[1]))
                self.set_image(self.geocode())
        if event.key() == Qt.Key_Left:
            if self.coordinates[0] > -179:
                self.coordinates[0] -= self.moving()
                self.coords_edit.setText(str(self.coordinates[0]) + ", " + str(self.coordinates[1]))
                self.set_image(self.geocode())
        if event.key() == Qt.Key_Right:
            if self.coordinates[0] < 179:
                self.coordinates[0] += self.moving()
                self.coords_edit.setText(str(self.coordinates[0]) + ", " + str(self.coordinates[1]))
                self.set_image(self.geocode())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Map()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())

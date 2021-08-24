from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow
import os


class MainWindow(QMainWindow):

    def __init__(self, app):

        super(MainWindow, self).__init__()

        # TODO: Find a way to auto detect sub-dirs "ui" and "main_window", and, maybe, .ui filename?
        ui_path = os.path.join(app.info.path, 'ui', 'main_window', 'main_window.ui')
        uic.loadUi(ui_path, self)

        self.show()

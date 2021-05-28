from PyQt5.QtWidgets import QApplication

from ui.main_window import MainWindow


class ImagerApplication(QApplication):

    def __init__(self, *args):
        QApplication.__init__(self, *args)

        self.window = MainWindow(self)


    class Info:

        import os

        path = os.path.dirname(os.path.realpath(__file__))

    info = Info  # just a lowercase alias for static Info class

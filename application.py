import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_main import Ui_MainWindow

from resources import *

class Generator(QMainWindow):
    def __init__(self):
        super(Generator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Generator()
    window.show()

    sys.exit(app.exec())
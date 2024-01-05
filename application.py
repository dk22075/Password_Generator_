import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtGui import QCloseEvent


from ui_main import Ui_MainWindow

from resources import *
import buttons
import password

class Generator(QMainWindow):
    def __init__(self):
        super(Generator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.connect_slider_to_spinbox()
        self.set_password()
        for button in buttons.GENERATE_PASSWORD:
            getattr(self.ui, button).clicked.connect(self.set_password)
        
        self.ui.button_visibility.clicked.connect(self.change_password_visibility)
        self.ui.button_copy.clicked.connect(self.copy_to_clipboard)


    def connect_slider_to_spinbox(self) -> None:
      self.ui.slider_length.valueChanged.connect(self.ui.spinbox_length.setValue)
      self.ui.spinbox_length.valueChanged.connect(self.ui.slider_length.setValue)
      self.ui.spinbox_length.valueChanged.connect(self.set_password)


    def get_characters(self) -> str:
        chars = ""

        for btn in buttons.Characters:
            if getattr(self.ui, btn.name).isChecked():
                chars += btn.value

        return chars
    

    def set_password(self) -> None:
        try:
            self.ui.line_password.setText(
                password.create_new(
                    length=self.ui.slider_length.value(),
                    characters=self.get_characters())
            )
        except IndexError:
            self.ui.line_password.clear()

        self.set_strength()

    # Funkcija, kas atgriež summu no vērtībām, kas atbilst atlasītajiem pogām interfeisā     
    def get_character_number(self) -> int:
        return sum(value for btn, value in buttons.CHARACTER_NUMBER.items() if getattr(self.ui, btn).isChecked())



    def set_strength(self) -> None:
        length = len(self.ui.line_password.text())
        char_num = self.get_character_number()

        for strength in password.StrengthToEntropy:
            if password.get_entropy(length, char_num) >= strength.value:
                self.ui.label_strength.setText(f"Strength: {strength.name}")


    def change_password_visibility(self) -> None:
        if self.ui.button_visibility.isChecked():
            self.ui.line_password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.line_password.setEchoMode(QLineEdit.Password)

    def copy_to_clipboard(self) -> None:
        QApplication.clipboard().setText(self.ui.line_password.text())


    def closeEvent(self, event: QCloseEvent) -> None:
        QApplication.clipboard().clear()


    def do_when_password_edit(self) -> None:
        self.ui.line_password.textEdited.connect(self.set_strength)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Generator()
    window.show()

    sys.exit(app.exec())
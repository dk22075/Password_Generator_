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
         # Pieslēdz pogas, kas ģenerē paroli, pie set_password funkcijas.
        for button in buttons.GENERATE_PASSWORD:
            getattr(self.ui, button).clicked.connect(self.set_password)
        
        # Pieslēdz pogas redzamībai un kopēšanai pie attiecīgajām funkcijām.
        self.ui.button_visibility.clicked.connect(self.change_password_visibility)
        self.ui.button_copy.clicked.connect(self.copy_to_clipboard)

    #  Pieslēdz signālus starp slīdni un spinboksu, lai atjauninātu un iestatītu paroli pārmaiņu gadījumā.
    def connect_slider_to_spinbox(self) -> None:
      self.ui.slider_length.valueChanged.connect(self.ui.spinbox_length.setValue)
      self.ui.spinbox_length.valueChanged.connect(self.ui.slider_length.setValue)
      self.ui.spinbox_length.valueChanged.connect(self.set_password)

    # Izgūst simbolus, pamatojoties uz izvēlētajām pogām interfeisā.
    def get_characters(self) -> str:
        return ''.join(btn.value for btn in buttons.Characters if getattr(self.ui, btn.name).isChecked())

    # Iestata jaunu paroli līnijas rediģēšanas laukā, pamatojoties uz slīdņa garumu un izvēlētajiem simboliem.
    def set_password(self) -> None:
        try:
            self.ui.line_password.setText(password.create_new(length=self.ui.slider_length.value(), characters=self.get_characters()))
        except IndexError:
            self.ui.line_password.clear()

        self.set_strength()

    # Atgriež summu no vērtībām, kas atbilst izvēlētajām pogām interfeisā. 
    def get_character_number(self) -> int:
        return sum(value for btn, value in buttons.CHARACTER_NUMBER.items() if getattr(self.ui, btn).isChecked())

    # Iestata stipruma marķējumu, pamatojoties uz aprēķināto paroles entropiju.
    def set_strength(self) -> None:
        length = len(self.ui.line_password.text())
        char_num = self.get_character_number()

        for strength in password.StrengthToEntropy:
            if password.get_entropy(length, char_num) >= strength.value:
                self.ui.label_strength.setText(f"Strength: {strength.name}")

    # Pārslēdz paroles redzamību atkarībā no redzamības pogas stāvokļa.
    def change_password_visibility(self) -> None:
        if self.ui.button_visibility.isChecked():
            self.ui.line_password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.line_password.setEchoMode(QLineEdit.Password)

    # Kopē pašreizējo paroli uz clipboard.
    def copy_to_clipboard(self) -> None:
        QApplication.clipboard().setText(self.ui.line_password.text())

    # Notīra clipboard, kad logs tiek aizvērts.
    def closeEvent(self, event: QCloseEvent) -> None:
        QApplication.clipboard().clear()

    # Pieslēdz paroles rediģēšanas lauka signālu pie set_strength funkcijas.
    def do_when_password_edit(self) -> None:
        self.ui.line_password.textEdited.connect(self.set_strength)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Generator()
    window.show()

    sys.exit(app.exec())
from PySide6.QtGui import QValidator
from PySide6.QtWidgets import QMessageBox, QLineEdit

from datetime import datetime


# Check whether the input is upper case or digits
class UpperCaseNumValidator(QValidator):
    def validate(self, arg__1: str, arg__2: int) -> object:
        if arg__1.isupper() or arg__1.isdigit():
            return QValidator.Acceptable, arg__1, arg__2
        elif arg__1 == "":
            return QValidator.Intermediate, arg__1, arg__2
        else:
            return QValidator.Invalid, arg__1, arg__2


def get_time() -> str:
    current_time = datetime.now().strftime("%I:%M %p")
    return current_time

def get_date() -> str:
    current_date = datetime.now().strftime("%d %b, %Y")
    return current_date

def show_message(title: str, message: str):
    message_box = QMessageBox()
    message_box.setWindowTitle(title)
    message_box.setText(message)
    message_box.exec()

def show_dialog(title: str, message: str):
    message_box = QMessageBox()
    message_box.setWindowTitle(title)
    message_box.setText(message)
    message_box.setIcon(QMessageBox.Question)
    message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    return message_box.exec()

def validate_line_edit(line_edit: QLineEdit, error_message: str = "") -> bool:
    # custom style sheets
    error_stylesheet = "QLineEdit:focus {border: 1px solid red;}"
    normal_stylesheet = ""
        
    text = line_edit.text()
    if not text:
        if error_message != "":
            show_message("Error", error_message)

        line_edit.setStyleSheet(error_stylesheet)
        line_edit.setFocus()
        return False
    else:
        line_edit.setStyleSheet(normal_stylesheet)
    return True

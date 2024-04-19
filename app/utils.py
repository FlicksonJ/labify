from PySide6.QtCore import QAbstractTableModel, QSortFilterProxyModel
from PySide6.QtGui import QValidator
from PySide6.QtWidgets import QMessageBox, QLineEdit

from datetime import datetime
from thefuzz import fuzz


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

def fuzzy_search(model: QAbstractTableModel, search_term: str) -> QSortFilterProxyModel | None:
    proxy_model = QSortFilterProxyModel()
    proxy_model.setSourceModel(model)

    filtered_rows = []
    for row in range(proxy_model.rowCount()):
        name_index = model.index(row, 1)
        name = model.data(name_index)
        similiarity = fuzz.partial_token_sort_ratio(search_term.lower(), name.lower())
        if similiarity > 70:
            # value of row starts from 0 but cid of table starts from 1
            filtered_rows.append(row+1)

    if len(filtered_rows) < 1:
        return None
    proxy_model.setFilterKeyColumn(0)
    proxy_model.setFilterFixedString("")
    proxy_model.setFilterRegularExpression("")
    regex_pattern = "|".join(map(str, filtered_rows))
    proxy_model.setFilterRegularExpression(f"^(?:{regex_pattern})$")

    return proxy_model


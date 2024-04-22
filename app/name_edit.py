from PySide6.QtWidgets import QWidget
from app.ui.ui_name_edit import Ui_NameEdit

class NameEdit(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_NameEdit()
        self.ui.setupUi(self)

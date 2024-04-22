from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QWidget
from app.ui.ui_quantity_edit import Ui_QuantityEdit

class QuantityEdit(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_QuantityEdit()
        self.ui.setupUi(self)

        self.ui.qty_input.setValidator(QDoubleValidator())

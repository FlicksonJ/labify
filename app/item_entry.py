from PySide6.QtWidgets import QWidget
from app.ui.ui_item_entry import Ui_ItemEntry

class ItemEntry(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_ItemEntry()
        self.ui.setupUi(self)

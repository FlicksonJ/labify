from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QTableView, QWidget, QSystemTrayIcon

from datetime import datetime

from app.ui.ui_quantity_edit import Ui_QtyEdit
from app import utils

class QtyEdit(QWidget):
    def __init__(self, parent, data: dict[str, str | QTableView]) -> None:
        super().__init__()
        self.ui = Ui_QtyEdit()
        self.ui.setupUi(self)

        self.parent = parent
        self.inventory_manager = parent.inventory_manager
        self.data = data
        self.tray_icon = parent.tray_icon

        self.ui.qty_input.setValidator(QDoubleValidator())

        self.ui.update_button.clicked.connect(self.update_qty)

    
    def validate_qty_input(self) -> bool:
        if not utils.validate_line_edit(self.ui.qty_input, "Please enter a value"):
            return False

        qty = self.ui.qty_input.text()
        try:
            qty = float(qty)
        except:
            utils.show_message("Error", "Not a valid number")
            return False

        if qty < 0:
            utils.show_message("Error", "Enter a value greater than 0")
            return False

        return True
        

    def update_qty(self):
        if not self.validate_qty_input():
            return

        name = self.data["name"]
        lab = self.data["lab"]
        location = self.data["location"]
        qty = float(self.ui.qty_input.text())

        if self.inventory_manager.update_qty(name, lab, location, qty):
            utils.show_message("Quantity updated", f"Changed quantity to {qty}")
            self.parent.state["items_model"] = self.inventory_manager.retrieve_item_info(self.data["item_type"])
            self.data["table"].setModel(self.parent.state["items_model"])
        else:
            utils.show_message("Error", "Cannot update quantity")

        self.ui.qty_input.clear()

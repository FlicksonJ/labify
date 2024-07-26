from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QTableView, QWidget, QSystemTrayIcon

from datetime import datetime

from app.ui.ui_move_item import Ui_MoveItem
from app import utils

class MoveItem(QWidget):
    def __init__(self, parent, data: dict[str, str | QTableView]) -> None:
        super().__init__()
        self.ui = Ui_MoveItem()
        self.ui.setupUi(self)

        self.parent = parent
        self.location = parent.state["location_data"]
        self.inventory_manager = parent.inventory_manager
        self.data = data
        self.tray_icon = parent.tray_icon

        self.ui.qty_input.setValidator(QDoubleValidator())

        # Update locations
        self.ui.lab_input.addItems(self.inventory_manager.retrieve_labs())

        self.ui.location_label.setText(f'Location ({data["name"]}):')
        lab_index = self.ui.lab_input.findText(data["lab"])
        self.ui.lab_input.setCurrentIndex(lab_index)
        self.update_loc()
        self.ui.location_input.setText(data["location"])

        self.ui.lab_input.currentIndexChanged.connect(self.update_loc)
        self.ui.move_item_button.clicked.connect(self.move_item)

        if self.data["item_type"] == "chemical_liquid":
            self.ui.qty_label.setText(f'Qty - {data["name"]} (Litre):')
        elif self.data["item_type"] == "chemical_salt":
            self.ui.qty_label.setText(f'Qty - {data["name"]} (gram):')
        else:
            self.ui.qty_label.setText(f'Qty - {data["name"]} (Pcs.):')

    def update_loc(self):
        self.ui.location_input.clear()

    def validate_qty_input(self) -> bool:
        if not utils.validate_line_edit(self.ui.qty_input, "Please enter a value"):
            return False

        qty = self.ui.qty_input.text()
        try:
            qty = float(qty)
        except:
            utils.show_message("Error", "Not a valid number")
            return False

        if qty <= 0:
            utils.show_message("Error", "Enter a value greater than 0")
            return False

        return True
        

    def move_item(self):
        if not self.validate_qty_input():
            return
        if not utils.validate_line_edit(self.ui.location_input, "Please enter a value"):
            return

        name = self.data["name"]
        stock_type = self.data["item_type"]
        current_lab = self.data["lab"]
        current_location = self.data["location"]
        new_lab = self.ui.lab_input.currentText()
        new_location = self.ui.location_input.text()
        qty = float(self.ui.qty_input.text())

        if qty > float(self.data["qty"]):
            utils.show_message("Error", "Qty value exceeds current stock value")
            return

        if current_lab == new_lab and current_location == new_location:
            utils.show_message("Error", "Change locations to update")
            return

        if not self.inventory_manager.location_exists(new_lab, new_location):
            self.inventory_manager.insert_location(new_lab, new_location)

        if self.inventory_manager.move_item(name,
                                                stock_type,
                                                current_lab,
                                                current_location,
                                                new_lab,
                                                new_location,
                                                qty):
            utils.show_message("Moved item location", f"Moved {name}({qty}L/g) to {new_lab} - {new_location}")
            self.parent.state["items_model"] = self.inventory_manager.retrieve_item_info(self.data["item_type"])
            self.data["table"].setModel(self.parent.state["items_model"])
        else:
            utils.show_message("Error", "Cannot move item")

        self.ui.qty_input.clear()

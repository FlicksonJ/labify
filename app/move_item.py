from datetime import datetime
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QTableView, QWidget, QSystemTrayIcon

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

        self.ui.lab_input.addItems(self.inventory_manager.retrieve_labs())

        self.ui.move_item_button.clicked.connect(self.move_item)

        self.ui.item_location_label.setText(f"{data['name']} (Location-{data['location']})")
        if self.data["item_type"] == "chemical_liquid":
            self.ui.qty_label.setText(' Qty(Litre):')
        elif self.data["item_type"] == "chemical_salt":
            self.ui.qty_label.setText(' Qty(gram):')
        else:
            self.ui.qty_label.setText(' Qty(Pcs.):')

    def validate_qty_input(self) -> bool:
        valid = True
        if not utils.validate_line_edit(self.ui.qty_input, "Please enter a value"):
            valid = False

        qty = self.ui.qty_input.text()
        try:
            qty = float(qty)
            assert qty > 0, f"Excpected a value greater than 0, got {qty}"
        except ValueError as e:
            utils.show_message("Error", "Not a valid number")
            valid = False
            raise ValueError(e)
        except AssertionError as e:
            utils.show_message("Error", "Enter a value greater than 0")
            valid = False
            raise AssertionError(e)
        
        return valid

    def move_item(self):
        if not self.validate_qty_input():
            return

        name = self.data["name"]
        user = self.data["user"]
        stock_type = self.data["item_type"]
        current_location = self.data["location"]
        new_location = self.ui.lab_input.currentText()
        qty = float(self.ui.qty_input.text())
        date = datetime.now().strftime('%Y-%m-%d')
        time = datetime.now().strftime('%I:%M %p')
        action = "Moved To"

        transaction = {
            "date": date,
            "time": time,
            "user": user,
            "name": name,
            "qty": qty,
            "action": action,
            "location": f"{current_location} -> {new_location}"
        }

        try:
            assert isinstance(self.data["qty"], float)
            assert qty < self.data["qty"], f"Expected a value less than the current stock value, got {qty}"
        except AssertionError as e:
            utils.show_message("Error", "Qty value exceeds current stock value")
            raise AssertionError(e)

        if qty > float(self.data["qty"]):
            utils.show_message("Error", "Qty value exceeds current stock value")
            return

        if current_location == new_location:
            utils.show_message("Error", "Change locations to update")
            return

        if not self.inventory_manager.check_item_location(name, current_location):
            utils.show_message("Error", f"Item {name} does not exist in store, {current_location}. Enter a valid location")
            return

        if self.inventory_manager.move_item(name,
                                                stock_type,
                                                current_location,
                                                new_location,
                                                qty):
            if self.data["item_type"] == "chemical_liquid":
                utils.show_message("Moved item location", f"Moved {name}({qty} Litre) to {new_location}")
            elif self.data["item_type"] == "chemical_salt":
                utils.show_message("Moved item location", f"Moved {name}({qty} gram) to {new_location}")
            self.parent.state["items_model"] = self.inventory_manager.retrieve_item_info(self.data["item_type"])
            self.data["table"].setModel(self.inventory_manager.retrieve_item_info(self.data["item_type"]))
            self.inventory_manager.add_transaction(transaction)
        else:
            utils.show_message("Error", "Cannot move item")

        self.ui.qty_input.clear()

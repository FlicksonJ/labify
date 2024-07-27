from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QTableView, QWidget, QSystemTrayIcon

from datetime import datetime

from app.ui.ui_quantity_restock import Ui_QtyRestock
from app import utils

class QtyRestock(QWidget):
    def __init__(self, parent, data: dict[str, str | float | int | QTableView]) -> None:
        super().__init__()
        self.ui = Ui_QtyRestock()
        self.ui.setupUi(self)

        self.parent = parent
        self.inventory_manager = parent.inventory_manager
        self.data = data
        self.tray_icon = parent.tray_icon

        self.ui.qty_input.setValidator(QDoubleValidator())

        self.ui.add_stock_button.clicked.connect(self.add_stock)
        self.ui.remove_stock_button.clicked.connect(self.remove_stock)

        if self.data["item_type"] == "chemical_liquid":
            self.ui.qty_label.setText(f'{data["name"]} - New Qty(Litre):')
        elif self.data["item_type"] == "chemical_salt":
            self.ui.qty_label.setText(f'{data["name"]} - New Qty(gram):')
        else:
            self.ui.qty_label.setText(f'{data["name"]} - New Qty(Pcs.):')

    
    def validate_qty_input(self) -> bool:
        if not utils.validate_line_edit(self.ui.qty_input, "Please enter a value"):
            return False

        qty = self.ui.qty_input.text()
        try:
            qty = float(qty)
            assert qty > 0, f"Expected a value greater than 0, got {qty}"
        except ValueError as e:
            utils.show_message("Error", "Not a valid number")
            raise ValueError(e)
        except AssertionError as e:
            utils.show_message("Error", "Enter a value greater than 0")
            raise AssertionError(e)

        return True
        

    def add_stock(self):
        if not self.validate_qty_input():
            return

        name = self.data["name"]
        user = self.data["user"]
        location = self.data["location"]
        qty = float(self.ui.qty_input.text())
        date = datetime.now().strftime('%Y-%m-%d')
        time = datetime.now().strftime('%I:%M %p')
        action = "Added To"

        transaction = {
            "date": date,
            "time": time,
            "user": user,
            "name": name,
            "qty": qty,
            "action": action,
            "location": location
        }

        if self.inventory_manager.add_qty_to_item(name, location, qty):
            utils.show_message("Qty updated", f"Added {qty} to the stock")
            self.inventory_manager.add_transaction(transaction)
            self.parent.state["items_model"] = self.inventory_manager.retrieve_item_info(self.data["item_type"])
            self.data["table"].setModel(self.parent.state["items_model"])
        else:
            utils.show_message("Error", "Cannot update qty")

        self.ui.qty_input.clear()

    
    def remove_stock(self):
        if not self.validate_qty_input():
            return

        name = self.data["name"]
        user = self.data["user"]
        location = self.data["location"]
        qty = float(self.ui.qty_input.text())
        date = datetime.now().strftime('%Y-%m-%d')
        time = datetime.now().strftime('%I:%M %p')
        action = "Taken From"
        item_type = self.data['item_type']

        try:
            assert isinstance(self.data["qty"], float)
            assert qty < self.data["qty"], f"Expected a value less than the current stock value, got {qty}"
        except AssertionError as e:
            utils.show_message("Error", "Qty value exceeds current stock value")
            raise AssertionError(e)

        if item_type == 'chemical_liquid' and (self.data["qty"] - qty) <= 2.5:
            self.tray_icon.showMessage("Alert", f"{self.data['name']} is below margin level", QSystemTrayIcon.Information, 5000)
        elif item_type == 'chemical_salt' and (self.data["qty"] - qty) <= 500:
            self.tray_icon.showMessage("Alert", f"{self.data['name']} is below margin level", QSystemTrayIcon.Information, 5000)
        elif (item_type == 'glassware' or item_type == 'equipment') and (self.data["qty"] - qty) <= 5:
            self.tray_icon.showMessage("Alert", f"{self.data['name']} is below margin level", QSystemTrayIcon.Information, 5000)

        transaction = {
            "date": date,
            "time": time,
            "user": user,
            "name": name,
            "qty": qty,
            "action": action,
            "location": location
        }

        if self.inventory_manager.remove_qty_from_item(name, location, qty):
            utils.show_message("Qty updated", f"Removed {qty} from the stock")
            self.inventory_manager.add_transaction(transaction)
            self.parent.state["items_model"] = self.inventory_manager.retrieve_item_info(self.data["item_type"])
            self.data["table"].setModel(self.parent.state["items_model"])
        else:
            utils.show_message("Error", "Cannot update qty")

        self.ui.qty_input.clear()

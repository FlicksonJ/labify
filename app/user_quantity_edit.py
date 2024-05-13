from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QTableView, QWidget, QSystemTrayIcon

from datetime import datetime

from app.ui.ui_user_quantity_edit import Ui_UserQuantityEdit
from app import utils

class UserQuantityEdit(QWidget):
    def __init__(self, inventory_manager, tray_icon, data: dict[str, str | QTableView]) -> None:
        super().__init__()
        self.ui = Ui_UserQuantityEdit()
        self.ui.setupUi(self)

        self.inventory_manager = inventory_manager
        self.data = data
        self.tray_icon = tray_icon

        self.ui.qty_input.setValidator(QDoubleValidator())

        self.ui.used_button.clicked.connect(self.remove_stock)

    
    def validate_qty_input(self) -> bool:
        if not utils.validate_line_edit(self.ui.qty_input, "Please enter a value"):
            return False

        qty = self.ui.qty_input.text()
        try:
            qty = int(qty)
        except:
            utils.show_message("Error", "Not a valid number")
            return False

        if qty <= 0:
            utils.show_message("Error", "Enter a value greater than 0")
            return False

        return True
        

    def remove_stock(self):
        if not self.validate_qty_input():
            return

        name = self.data["name"]
        user = self.data["user"]
        lab = self.data["lab"]
        location = self.data["location"]
        qty = float(self.ui.qty_input.text())
        date = datetime.now().strftime('%Y-%m-%d')
        time = datetime.now().strftime('%I:%M %p')
        action = "Taken"

        if qty > float(self.data["qty"]):
            utils.show_message("Error", "Qty value exceeds current stock value")
            return

        if (self.data["qty"] - qty) <= 250:
            self.tray_icon.showMessage("Alert", f"{self.data['name']} is below margin level", QSystemTrayIcon.Information, 5000)

        transaction = {
            "date": date,
            "time": time,
            "user": user,
            "name": name,
            "qty": qty,
            "action": action,
            "lab": lab,
            "location": location
        }

        if self.inventory_manager.remove_qty_from_item(name, lab, location, qty):
            utils.show_message("Qty updated", f"Removed {qty} from the stock")
            self.inventory_manager.add_transaction(transaction)
            self.data["table"].setModel(self.inventory_manager.retrieve_item_info(self.data["item_type"], with_qty=False))
        else:
            utils.show_message("Error", "Cannot update qty")


from PySide6.QtWidgets import QWidget, QMessageBox

from app.ui.ui_name_edit import Ui_NameEdit
from app import utils

class NameEdit(QWidget):
    def __init__(self, inventory_manager, data: dict[str, str]) -> None:
        super().__init__()
        self.ui = Ui_NameEdit()
        self.ui.setupUi(self)

        self.inventory_manager = inventory_manager
        self.data = data

        self.ui.update_name_button.clicked.connect(self.update_name)
        self.ui.name_input.returnPressed.connect(self.update_name)


    def update_name(self):
        if not utils.validate_line_edit(self.ui.name_input, "Please enter a name"):
            return

        current_name = self.data["name"]
        new_name = self.ui.name_input.text()
        lab = self.data["lab"]
        location = self.data["location"]
        
        if current_name.strip() == new_name.strip():
            utils.show_message("Error", "Change the value of name to update")
            return

        confirm = utils.show_dialog(
                "Are you sure?", 
                f"Do you really want to update the name to {new_name}"
                )
        if confirm == QMessageBox.No:
            return

        if self.inventory_manager.update_item_name(current_name, lab, location, new_name):
            utils.show_message("Name Updated", f"Changed name from {current_name} to {new_name}")
        else:
            utils.show_message("Error", "Cannot update name")

        self.ui.name_input.clear()

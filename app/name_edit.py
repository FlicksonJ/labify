from PySide6.QtWidgets import QTableView, QWidget, QMessageBox

from app.ui.ui_name_edit import Ui_NameEdit
from app import utils

class NameEdit(QWidget):
    def __init__(self, parent, data: dict[str, str | QTableView]) -> None:
        super().__init__()
        self.ui = Ui_NameEdit()
        self.ui.setupUi(self)

        self.parent = parent
        self.inventory_manager = parent.inventory_manager
        self.data = data

        self.ui.update_name_button.clicked.connect(self.update_name)
        self.ui.name_input.returnPressed.connect(self.update_name)

        try:
            assert isinstance(data["name"], str), f"Expected a string for name, got {type(data['name'])}"
            self.ui.name_input.setText(data["name"])
        except AssertionError as e:
            raise AssertionError(e)


    def update_name(self):
        if not utils.validate_line_edit(self.ui.name_input, "Please enter a name"):
            return

        current_name = self.data["name"]
        new_name = self.ui.name_input.text()
        location = self.data["location"]
        
        if current_name.strip() == new_name.strip():
            utils.show_message("Error", "Change the value of name to update")
            return

        if self.inventory_manager.check_item_location(new_name, location):
            utils.show_message("Item exists!", f"Item {new_name} already exists in store, {location}")
            return

        confirm = utils.show_dialog(
                "Are you sure?", 
                f"Do you really want to update the name to {new_name}"
                )
        if confirm == QMessageBox.No:
            return

        if self.inventory_manager.update_item_name(current_name, location, new_name):
            utils.show_message("Name Updated", f"Changed name from {current_name} to {new_name}")
            self.parent.state["items_model"] = self.inventory_manager.retrieve_item_info(self.data["item_type"])
            self.data["table"].setModel(self.parent.state["items_model"])
        else:
            utils.show_message("Error", "Cannot update name")

        self.ui.name_input.clear()

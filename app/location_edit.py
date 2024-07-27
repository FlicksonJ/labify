from PySide6.QtWidgets import QTableView, QWidget, QMessageBox

from app.ui.ui_location_edit import Ui_LocationEdit
from app import utils

class LocationEdit(QWidget):
    def __init__(self, 
                 parent,
                 data: dict[str, str | QTableView]) -> None:
        super().__init__()
        self.ui = Ui_LocationEdit()
        self.ui.setupUi(self)
        
        self.parent = parent
        self.locations = parent.state["location_data"]
        self.inventory_manager = parent.inventory_manager
        self.data = data

        self.ui.location_label.setText(f'New Location ({data["name"]}):')
        self.ui.location_input.clear()
        try:
            assert isinstance(data["location"], str), f"Expected a string for location, got {type(data['location'])}"
            self.ui.location_input.setText(data["location"])
        except AssertionError as e:
            raise AssertionError(e)

        self.ui.update_location_button.clicked.connect(self.update_item_location)
        self.ui.location_input.returnPressed.connect(self.update_item_location)

    def update_item_location(self):
        name = self.data["name"]
        current_location = self.data["location"]
        new_location = self.ui.location_input.text()

        if not utils.validate_line_edit(self.ui.location_input, "Please enter a location"):
            return

        if current_location == new_location:
            utils.show_message("Error", "Change locations to update")
            return

        if not self.inventory_manager.location_exists(new_location):
            self.inventory_manager.insert_location(new_location)
        
        if self.inventory_manager.check_item_location(name, new_location):
            utils.show_message("Item exists!", f"Item {name} already exists in store, {new_location}")
            return

        confirm = utils.show_dialog(
                "Are you sure?", 
                f"Do you really want to update the location to store, {new_location}?"
                )
        if confirm == QMessageBox.No:
            return

        if self.inventory_manager.update_item_location(
                name,
                current_location,
                new_location
                ):
            utils.show_message("Name Updated", f"Changed location from store, {current_location} to store, {new_location}")
            self.parent.state["items_model"] = self.inventory_manager.retrieve_item_info(self.data["item_type"])
            self.data["table"].setModel(self.parent.state["items_model"])
        else:
            utils.show_message("Error", "Cannot update location")


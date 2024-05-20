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

        # Update locations
        self.ui.lab_input.addItems(self.locations.keys())
        self.ui.lab_input.currentIndexChanged.connect(self.update_loc)

        self.ui.update_location_button.clicked.connect(self.update_item_location)

    def update_loc(self, index):
        selected_lab = self.ui.lab_input.currentText()
        self.ui.location_input.clear()

        if selected_lab in self.locations:
            self.ui.location_input.addItems(self.locations[selected_lab])

    def update_item_location(self):
        name = self.data["name"]
        current_lab = self.data["lab"]
        current_location = self.data["location"]
        new_lab = self.ui.lab_input.currentText()
        new_location = self.ui.location_input.currentText()

        if current_lab == new_lab and current_location == new_location:
            utils.show_message("Error", "Change locations to update")
            return

        if self.inventory_manager.check_item_location(name, new_lab, new_location):
            utils.show_message("Item exists!", f"Item {name} already exists in {new_lab}, {new_location}")
            return

        confirm = utils.show_dialog(
                "Are you sure?", 
                f"Do you really want to update the location to {new_lab}, {new_location}?"
                )
        if confirm == QMessageBox.No:
            return

        if self.inventory_manager.update_item_location(
                name,
                current_lab,
                current_location,
                new_lab,
                new_location
                ):
            utils.show_message("Name Updated", f"Changed location from {current_lab}, {current_location} to {new_lab}, {new_location}")
            self.parent.state["items_model"] = self.inventory_manager.retrieve_item_info(self.data["item_type"])
            self.data["table"].setModel(self.parent.state["items_model"])
        else:
            utils.show_message("Error", "Cannot update location")


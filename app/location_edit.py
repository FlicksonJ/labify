from PySide6.QtWidgets import QWidget
from app.ui.ui_location_edit import Ui_LocationEdit

class LocationEdit(QWidget):
    def __init__(self, locations: dict[str, list[str]]) -> None:
        super().__init__()
        self.ui = Ui_LocationEdit()
        self.ui.setupUi(self)
        
        self.locations = locations

        # Update locations
        self.ui.lab_input.addItems(self.locations.keys())
        self.ui.lab_input.currentIndexChanged.connect(self.update_loc)

    def update_loc(self, index):
        selected_lab = self.ui.lab_input.currentText()
        self.ui.location_input.clear()

        if selected_lab in self.locations:
            self.ui.location_input.addItems(self.locations[selected_lab])

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import QSize

class HomePage(QWidget):
    def __init__(self, main_window, username, user_type):
        super().__init__()

        self.user_type = user_type
        self.username = username
        self.main_window = main_window
        layout = QVBoxLayout()
        welcome_label = QLabel(f"Hello {self.username}. Welcome to the Home Page!")
        self.setMinimumSize(QSize(800, 600))
        layout.addWidget(welcome_label)

        self.setLayout(layout)

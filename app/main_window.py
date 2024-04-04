from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from app.login import LoginWindow
from app.home_screen import HomePage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ICMS")

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.login_screen = LoginWindow(self)
        self.central_widget.addWidget(self.login_screen)

        self.central_widget.setCurrentWidget(self.login_screen)

    def show_home_screen(self, username, user_type):
        # Customize home page based on user information (implementation omitted)
        if not hasattr(self, "homepage"):
            self.home_screen = HomePage(self, username, user_type)
            self.central_widget.addWidget(self.home_screen)
            self.central_widget.setCurrentWidget(self.home_screen)


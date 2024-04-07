from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from app.login import LoginWindow
from app.home_screen import HomePage
from app.ui.ui_main import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.inventory_page)

    #     self.setWindowTitle("ICMS")

    #     self.central_widget = QStackedWidget()
    #     self.setCentralWidget(self.central_widget)

    #     self.login_screen = LoginWindow(self)
    #     self.central_widget.addWidget(self.login_screen)

    #     self.central_widget.setCurrentWidget(self.login_screen)

    # def show_home_screen(self, username, user_type):
    #     # Customize home page based on user information (implementation omitted)
    #     if not hasattr(self, "homepage"):
    #         self.home_screen = HomePage(self, username, user_type)
    #         self.central_widget.addWidget(self.home_screen)
    #         self.central_widget.setCurrentWidget(self.home_screen)


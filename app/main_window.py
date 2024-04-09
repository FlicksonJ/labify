from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QMainWindow, QMessageBox 
from app.ui.ui_main import Ui_MainWindow

from app import utils

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.db = utils.init_db()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # for managing user access control
        self.user_type = ""
        self.login()


    def login(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.login_page)
        self.ui.login_button.clicked.connect(self.login_clicked)


    
    #***************************************************************
    #Slots
    #***************************************************************
    
    def login_clicked(self):
        """
        This slot is triggered when the login_button is clicked.
        It handles the login of the app.
        """
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()

        query = QSqlQuery()
        query.prepare("SELECT * FROM users WHERE username = :username")
        query.bindValue(":username", username)

        if not query.exec():
            QMessageBox.critical(self, "Error", "Failed to execute query!")

        if query.first():
            if (hashed_password := query.value("hashed_password")) and utils.verify_pw(hashed_password, password):
                user_type = query.value("user_type")
                self.user_type = user_type
                self.show_home_screen(username, user_type)

                
    def show_home_screen(self, username: str, user_type: str):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.ui.header_username_label.setText(username.upper())


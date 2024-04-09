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
        self.ui.login_button.clicked.connect(self.handle_login)
        self.ui.password_input.returnPressed.connect(self.handle_login)


    
    #***************************************************************
    #Slots
    #***************************************************************
    
    def handle_login(self):
        """
        This slot is triggered when the login_button is clicked.
        It handles the login of the app.
        """

        login_error_style = "QLineEdit {border: 2px solid red;}"
        
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
                self.show_home_screen(username)
            else:
                self.ui.username_input.setStyleSheet(login_error_style)
                self.ui.password_input.setStyleSheet(login_error_style)
        else:
            self.ui.username_input.setStyleSheet(login_error_style)

    def show_transaction_page(self):
        """
        This slot is triggered when the transaction_history_button is clicked.
        Show the transactions_page.
        """

        self.ui.stackedWidget_3.setCurrentWidget(self.ui.transactions_page)
        #@TODO: Add tableview 

    def show_alerts_page(self):
        """
        This slot is triggered when the alerts_button is clicked.
        Show the alerts_page.
        """

        self.ui.stackedWidget_3.setCurrentWidget(self.ui.alerts_page)
        #@TODO: Add tableview

                
    def show_home_screen(self, username: str):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.ui.header_username_label.setText(username.upper())
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.inventory_page_default)

        self.ui.transaction_history_button.clicked.connect(self.show_transaction_page)
        self.ui.alerts_button.clicked.connect(self.show_alerts_page)


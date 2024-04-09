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
        # `user_type`: admin, user
        # `item_type`: glassware, equipments, chemicals
        self.state = {"user_type": "", "item_type": "", "inventory_page_func": "search"}
        self.login()


    def login(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.login_page)
        self.ui.login_button.clicked.connect(self.handle_login)
        self.ui.password_input.returnPressed.connect(self.handle_login)


    def show_home_screen(self, username: str):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.ui.header_username_label.setText(username.upper())
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.inventory_page_default)
        
        self.ui.logout_button.clicked.connect(self.handle_logout)
        self.ui.transaction_history_button.clicked.connect(self.show_transaction_page)
        self.ui.alerts_button.clicked.connect(self.show_alerts_page)

        self.ui.inventory_type_input.activated.connect(self.handle_inventory_page)
        # Change the value of inventory_type_input combo box to the default value
        self.ui.stackedWidget_3.currentChanged.connect(self.inventory_view_changed)

        self.ui.add_entry_button.clicked.connect(self.show_add_entry_page)

    
    def update_item_type_label(self):
        text = {
            "add": "ADD NEW",
            "update": "UPDATE",
            "delete": "DELETE"
        }

        return f"{text[self.state['inventory_page_func']]} {self.state['item_type'].upper()}"
    

    def deactivate_page_change(self):
        self.ui.transaction_history_button.setEnabled(False)
        self.ui.alerts_button.setEnabled(False)
        self.ui.create_user_button.setEnabled(False)

    def activate_page_change(self):
        self.ui.transaction_history_button.setEnabled(True)
        self.ui.alerts_button.setEnabled(True)
        self.ui.create_user_button.setEnabled(True)

    

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
                self.state["user_type"] = user_type
                self.ui.username_input.clear()
                self.ui.password_input.clear()
                self.show_home_screen(username)
            else:
                self.ui.username_input.setStyleSheet(login_error_style)
                self.ui.password_input.setStyleSheet(login_error_style)
        else:
            self.ui.username_input.setStyleSheet(login_error_style)
    
    def handle_logout(self):
        """
        This slot is triggered when the logout_button is clicked.
        It handles logout.
        """

        self.state["user_type"] = ""
        self.login()

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
    
    def handle_inventory_page(self, index):
        """
        This slot is triggered when the inventory_type_input is activated.
        Handles the inventory_view_page.
        """

        self.ui.stackedWidget_3.setCurrentWidget(self.ui.inventory_view_page)
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.item_search_page)
        self.state["item_type"] = self.ui.inventory_type_input.currentText().lower()

    def inventory_view_changed(self, index):
        """
        This slot is triggered whenever the stackedWidget_3 widget is changed.
        This will deactivate the inventory_type_input combo box.
        This will deactivate item_manage button group.
        """

        # 3 is the index of inventory_view_page
        if index != 3:
            self.ui.inventory_type_input.setCurrentIndex(-1)

            # deselect all button in item_manage QButtonGroup
            self.ui.item_manage.setExclusive(False)
            checked_id = self.ui.item_manage.checkedId()
            if checked_id != -1:
                button = self.ui.item_manage.button(checked_id)
                button.setChecked(False)
            self.ui.item_manage.setExclusive(True)

    def show_add_entry_page(self):
        """
        This slot is triggered when the add_entry_button is clicked.
        Show add_entry_page.
        """

        self.ui.stackedWidget_4.setCurrentWidget(self.ui.add_entry_page)
        self.state["inventory_page_func"] = "add"
        self.ui.add_entry_label.setText(self.update_item_type_label())
        self.deactivate_page_change()


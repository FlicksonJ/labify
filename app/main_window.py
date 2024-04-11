from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QListWidgetItem, QMainWindow, QMessageBox, QLineEdit 

from app.ui.ui_main import Ui_MainWindow
from app.item_entry import ItemEntry

from app.utils import DatabaseManager
from app.access_controls import admin_access

from datetime import datetime

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.db_manager = DatabaseManager()
        self.account_manager = self.db_manager.account_manager
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Labify")
        self.setWindowIcon(QIcon('../images/logo.ico'))
        
        # for managing user access control
        # `user_type`: admin, user
        # `item_type`: glassware, equipments, chemicals
        self.state = {
            "username": "",
            "user_type": "", 
            "item_type": "", 
            "inventory_page_func": "search"
            }

        # View login screen
        self.ui.stackedWidget.setCurrentWidget(self.ui.login_page)
        self.ui.username_input.setFocus()
        self.ui.username_input.clear()
        self.ui.password_input.clear()

        # Set time and date
        self.ui.time_label.setText(self.get_time())
        self.ui.date_label.setText(self.get_date())

        # =============================================== #
        # ===============  Signals ====================== #
        # =============================================== #
        self.ui.login_button.clicked.connect(self.handle_login)
        self.ui.password_input.returnPressed.connect(self.handle_login)

        self.ui.create_user_button.clicked.connect(self.show_create_account_page)
        self.ui.cancel_button.clicked.connect(self.handle_cancel_button)
        self.ui.create_account_button.clicked.connect(self.handle_create_account)

        self.ui.logout_button.clicked.connect(self.handle_logout)
        self.ui.transaction_history_button.clicked.connect(self.show_transaction_page)
        self.ui.alerts_button.clicked.connect(self.show_alerts_page)

        self.ui.inventory_type_input.activated.connect(self.handle_inventory_page)
        self.ui.inventory_type_input.currentTextChanged.connect(self.handle_inventory_page)
        # Change the value of inventory_type_input combo box to the default value
        self.ui.stackedWidget_3.currentChanged.connect(self.inventory_view_changed)

        self.ui.add_entry_button.clicked.connect(self.show_add_entry_page)
        self.ui.add_entry_cancel_button.clicked.connect(self.handle_inventory_page)
        self.ui.add_entry_add_button.clicked.connect(self.add_entry)

        self.ui.update_entry_button.clicked.connect(self.show_update_entry_page)
        self.ui.update_entry_cancel_button.clicked.connect(self.handle_inventory_page)

        self.ui.delete_entry_button.clicked.connect(self.show_delete_entry_page)
        self.ui.delete_entry_cancel_button.clicked.connect(self.handle_inventory_page)


    def show_home_screen(self, username: str):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.ui.header_username_label.setText(username.upper())
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.inventory_page_default)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.inventory_page)
        
    
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

    def deselect_button_group(self):
        self.ui.item_manage.setExclusive(False)
        checked_id = self.ui.item_manage.checkedId()
        if checked_id != -1:
            button = self.ui.item_manage.button(checked_id)
            button.setChecked(False)
        self.ui.item_manage.setExclusive(True)

    def show_message(self, title, message):
        message_box = QMessageBox()
        message_box.setWindowTitle(title)
        message_box.setText(message)
        message_box.exec()
    
    def validate_line_edit(self, line_edit: QLineEdit, error_message: str) -> bool:
        text = line_edit.text()
        if not text:
            self.show_message("Error", error_message)
            line_edit.setFocus()
            return False
        return True

    def get_time(self) -> str:
        current_time = datetime.now().strftime("%I:%M %p")
        return current_time

    def get_date(self) -> str:
        current_date = datetime.now().strftime("%d %b, %Y")
        return current_date

    

    #***************************************************************
    #Slots
    #***************************************************************
    
    def handle_login(self):
        """
        This slot is triggered when the login_button is clicked.
        It handles the login of the app.
        """

        if not self.validate_line_edit(self.ui.username_input, "Please enter a username"):
            return
        if not self.validate_line_edit(self.ui.password_input, "Please enter a password"):
            return
        
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()

        query = QSqlQuery()
        query.prepare("SELECT * FROM users WHERE username = :username")
        query.bindValue(":username", username)

        if not query.exec():
            QMessageBox.critical(self, "Error", "Failed to execute query!")

        if query.first():
            if (hashed_password := query.value("hashed_password")) and self.account_manager.verify_pw(hashed_password, password):
                user_type = query.value("user_type")
                self.state["user_type"] = user_type
                self.state["username"] = username
                self.show_home_screen(username)
            else:
                self.show_message("Error", "Wrong credentials!")
        else:
            self.show_message("Error", "Wrong credentials!")

    def handle_create_account(self):
        """
        This slot is triggered when the create_account_button is clicked.
        To create new user account
        """

        # Check if the inputs are empty
        if not self.validate_line_edit(self.ui.cu_username_input, "Please enter a username"):
            return
        if not self.validate_line_edit(self.ui.cu_password_input, "Please enter a password"):
            return
        if not self.validate_line_edit(self.ui.cu_confirm_password_input, "Please confirm password"):
            return

        username = self.ui.cu_username_input.text()
        password = self.ui.cu_password_input.text()
        confirm_password = self.ui.cu_confirm_password_input.text()

        if password != confirm_password:
            self.show_message("Error", "Passwords do not match!")
            return 
            
        if self.account_manager.account_exists(username):
            self.show_message("Error", "Account already exists!")
            return
            
        self.account_manager.create_user(username, confirm_password)
        self.show_message("Success", "Account created successfully!")
        self.ui.cu_username_input.clear()
        self.ui.cu_password_input.clear()
        self.ui.cu_confirm_password_input.clear()
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.inventory_page)

    
    def handle_logout(self):
        """
        This slot is triggered when the logout_button is clicked.
        It handles logout.
        """

        self.state["user_type"] = ""
        self.state["username"] = ""
        self.ui.stackedWidget.setCurrentWidget(self.ui.login_page)
        self.ui.username_input.setFocus()
        self.ui.username_input.clear()
        self.ui.password_input.clear()


    @admin_access
    def show_create_account_page(self):
        """
        This slot is triggered when the create_user_button is clicked.
        Shows create_account_page.
        Access level: admin
        """
        if self.state["user_type"] == 'admin':
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.create_user_page)


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
    
    def handle_inventory_page(self):
        """
        This slot is triggered when the inventory_type_input is activated.
        Handles the inventory_view_page.
        """

        # To avoid side effects from inventory_view_changed function
        # Bug: The inventory_view_changed also changes the current value of the combo box,
        # it will trigger the currentTextChanged signal and will connect to this slot.
        # Fix: check the currentIndex is not -1 before setting currentWidget
        if self.ui.inventory_type_input.currentIndex() != -1:
            self.ui.stackedWidget_3.setCurrentWidget(self.ui.inventory_view_page)
            self.ui.stackedWidget_4.setCurrentWidget(self.ui.item_search_page)
            self.state["item_type"] = self.ui.inventory_type_input.currentText().lower()
            self.deselect_button_group()
            self.activate_page_change()

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
            self.deselect_button_group()

    @admin_access
    def show_add_entry_page(self):
        """
        This slot is triggered when the add_entry_button is clicked.
        Show add_entry_page.
        Access level: admin
        """

        self.ui.stackedWidget_4.setCurrentWidget(self.ui.add_entry_page)
        self.state["inventory_page_func"] = "add"
        self.ui.add_entry_label.setText(self.update_item_type_label())
        self.deactivate_page_change()

    def add_entry(self):
        item_entry = ItemEntry()
        list_item = QListWidgetItem()
        list_item.setSizeHint(item_entry.sizeHint() + QSize(45, 45))
        id = str(self.ui.add_entry_list.count() + 1)
        name = self.ui.item_name_input.text()
        qty = self.ui.item_qty_input.text()
        location = self.ui.item_location_input.text()
        lab = self.ui.item_lab_input.text()

        item_entry.ui.id.setText(id)
        item_entry.ui.name.setText(name)
        item_entry.ui.qty.setText(qty)
        item_entry.ui.location.setText(location)
        item_entry.ui.lab.setText(lab)

        self.ui.add_entry_list.addItem(list_item)
        self.ui.add_entry_list.setItemWidget(list_item, item_entry)
        


    def show_update_entry_page(self):
        """
        This slot is triggered when the update_entry_button is clicked.
        Show update_entry_page.
        """

        self.ui.stackedWidget_4.setCurrentWidget(self.ui.update_entry_page)
        self.state["inventory_page_func"] = "update"
        self.ui.update_entry_label.setText(self.update_item_type_label())
        self.deactivate_page_change()

    @admin_access
    def show_delete_entry_page(self):
        """
        This slot is triggered when the delete_entry_button is clicked.
        Show delete_entry_page.
        Access level: admin
        """

        self.ui.stackedWidget_4.setCurrentWidget(self.ui.delete_entry_page)
        self.state["inventory_page_func"] = "delete"
        self.ui.delete_entry_label.setText(self.update_item_type_label())
        self.deactivate_page_change()

    def handle_cancel_button(self):
        """
        This slot is triggered when the cancel_button is clicked.
        Go back to home_page
        """
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.inventory_page)

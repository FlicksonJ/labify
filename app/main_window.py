from PySide6.QtCore import Qt 
from PySide6.QtGui import QIcon, QDoubleValidator
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QListWidgetItem, QMainWindow, QMessageBox, QTableView 

from app.ui.ui_main import Ui_MainWindow
from app.item_entry import ItemEntry
from app.quantity_edit import QuantityEdit
from app.name_edit import NameEdit
from app.location_edit import LocationEdit

from app.manager import DatabaseManager
from app import utils
from app.access_controls import admin_access, restrict_page_change

from datetime import datetime


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.db_manager = DatabaseManager()
        self.account_manager = self.db_manager.account_manager
        self.inventory_manager = self.db_manager.inventory_manager
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Labify")
        self.setWindowIcon(QIcon(':/icon/images/logo.ico'))

        # for managing user access control
        # `user_type`: admin, user
        # `item_type`: glassware, equipments, chemicals
        self.state = {
            "username": "",
            "user_type": "", 
            "item_type": "", 
            "inventory_page_func": "search",
            "location_data": self.db_manager.inventory_manager.retrieve_locations(),
            "items_model": None
            }

        # Update locations
        self.ui.item_lab_input.addItems(self.state["location_data"].keys())
        self.update_locations(0)

        # View login screen
        self.ui.stackedWidget.setCurrentWidget(self.ui.login_page)
        self.ui.username_input.setFocus()
        self.ui.username_input.clear()
        self.ui.password_input.clear()

        # Set time and date
        self.ui.time_label.setText(utils.get_time())
        self.ui.date_label.setText(utils.get_date())

        # Set input validators
        self.ui.item_qty_input.setValidator(QDoubleValidator())

        # Update entry page inputs
        self.name_edit = NameEdit()
        self.quantity_edit = QuantityEdit()
        self.location_edit = LocationEdit(self.state["location_data"])

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

        self.ui.inventory_type_input.currentTextChanged.connect(self.handle_inventory_page)
        # Change the value of inventory_type_input combo box to the default value
        self.ui.stackedWidget_3.currentChanged.connect(self.inventory_view_changed)

        self.ui.search_button.clicked.connect(self.view_inventory_search)
        self.ui.search_bar_input.returnPressed.connect(self.view_inventory_search)

        self.ui.add_entry_button.clicked.connect(self.show_add_entry_page)
        self.ui.add_entry_cancel_button.clicked.connect(self.handle_inventory_page)
        self.ui.add_entry_add_button.clicked.connect(self.add_entry)
        self.ui.item_lab_input.currentIndexChanged.connect(self.update_locations)
        # self.ui.add_entry_save_button.clicked.connect(self.save_entry)

        self.ui.update_entry_button.clicked.connect(self.show_update_entry_page)
        self.ui.update_entry_cancel_button.clicked.connect(self.handle_inventory_page)
        self.ui.update_entry_table.clicked.connect(self.update_entry_table_clicked)
        self.ui.update_entry_search_button.clicked.connect(self.update_inventory_search)
        self.ui.update_entry_search_input.returnPressed.connect(self.update_inventory_search)

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
            "update": "EDIT",
            "delete": "REMOVE"
        }

        return f"{text[self.state['inventory_page_func']]} {self.state['item_type'].upper()}"
    

    def deactivate_page_change(self):
        self.ui.inventory_type_input.setEnabled(False)

    def activate_page_change(self):
        self.ui.inventory_type_input.setEnabled(True)

    def deselect_button_group(self):
        self.ui.item_manage.setExclusive(False)
        checked_id = self.ui.item_manage.checkedId()
        if checked_id != -1:
            button = self.ui.item_manage.button(checked_id)
            button.setChecked(False)
        self.ui.item_manage.setExclusive(True)

    def set_default_inventory_table(self, table: QTableView = None):
        if not table:
            table = self.ui.item_search_table
        self.state["items_model"] = self.inventory_manager.retrieve_item_info(self.state["item_type"])
        if self.state["items_model"]:
            table.setModel(self.state["items_model"])

    def remove_current_update_input(self):
        widget_count = self.ui.verticalLayout_13.count()
        if widget_count > 2:
            current_edit_input = self.ui.verticalLayout_13.itemAt(widget_count - 1)
            widget = current_edit_input.widget()
            if widget:
                widget.setParent(None)

    
    def add_update_input(self, data: dict[str, str]):
        if self.state["user_type"] == "user":
            self.ui.verticalLayout_13.addWidget(self.quantity_edit)
            self.quantity_edit.ui.qty_label.setText(f'Qty ({data["name"]}):')

            self.ui.verticalLayout_13.setStretch(0, 1)
            self.ui.verticalLayout_13.setStretch(1, 7)
            self.ui.verticalLayout_13.setStretch(2, 2)
        else:
            if data["header"] == "Qty":
                self.ui.verticalLayout_13.addWidget(self.quantity_edit)
                self.quantity_edit.ui.qty_label.setText(f'Qty ({data["name"]}):')
                self.ui.verticalLayout_13.setStretch(0, 1)
                self.ui.verticalLayout_13.setStretch(1, 7)
                self.ui.verticalLayout_13.setStretch(2, 2)
            elif data["header"] == "Name":
                self.ui.verticalLayout_13.addWidget(self.name_edit)
                self.name_edit.ui.name_input.setText(data["name"])
                self.ui.verticalLayout_13.setStretch(0, 1)
                self.ui.verticalLayout_13.setStretch(1, 7)
                self.ui.verticalLayout_13.setStretch(2, 2)
            elif data["header"] == "Lab" or data["header"] == "Location":
                self.ui.verticalLayout_13.addWidget(self.location_edit)
                self.location_edit.ui.location_label.setText(f'Location ({data["name"]}):')
                lab_index = self.location_edit.ui.lab_input.findText(data["lab"])
                self.location_edit.ui.lab_input.setCurrentIndex(lab_index)
                self.location_edit.update_loc(lab_index)
                location_index = self.location_edit.ui.location_input.findText(data["location"])
                self.location_edit.ui.location_input.setCurrentIndex(location_index)

                self.ui.verticalLayout_13.setStretch(0, 1)
                self.ui.verticalLayout_13.setStretch(1, 7)
                self.ui.verticalLayout_13.setStretch(2, 2)
        
        
    def search_inventory(self, search_term: str, table: QTableView = None):
        if not table:
            table = self.ui.item_search_table

        self.set_default_inventory_table(table)
        if search_term.strip() == "":
            return
        model = self.state["items_model"]
        proxy_model = utils.fuzzy_search(model, search_term)
        if proxy_model:
            self.state["items_model"] = proxy_model
            table.setModel(self.state["items_model"])
        else:
            utils.show_message("No item", f"Item not found: {search_term}")


    #***************************************************************
    #Slots
    #***************************************************************
    
    def handle_login(self):
        """
        This slot is triggered when the login_button is clicked.
        It handles the login of the app.
        """

        if not utils.validate_line_edit(self.ui.username_input, "Please enter a username"):
            return
        if not utils.validate_line_edit(self.ui.password_input, "Please enter a password"):
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
                utils.show_message("Error", "Wrong credentials!")
        else:
            utils.show_message("Error", "Wrong credentials!")

    def handle_create_account(self):
        """
        This slot is triggered when the create_account_button is clicked.
        To create new user account
        """

        # Check if the inputs are empty
        if not utils.validate_line_edit(self.ui.cu_username_input, "Please enter a username"):
            return
        if not utils.validate_line_edit(self.ui.cu_password_input, "Please enter a password"):
            return
        if not utils.validate_line_edit(self.ui.cu_confirm_password_input, "Please confirm password"):
            return

        username = self.ui.cu_username_input.text()
        password = self.ui.cu_password_input.text()
        confirm_password = self.ui.cu_confirm_password_input.text()

        if password != confirm_password:
            utils.show_message("Error", "Passwords do not match!")
            return 
            
        if self.account_manager.account_exists(username):
            utils.show_message("Error", "Account already exists!")
            return
            
        self.account_manager.create_user(username, confirm_password)
        utils.show_message("Success", "Account created successfully!")
        self.ui.cu_username_input.clear()
        self.ui.cu_password_input.clear()
        self.ui.cu_confirm_password_input.clear()
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.inventory_page)

    
    # @restrict_page_change
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
    # @restrict_page_change
    def show_create_account_page(self):
        """
        This slot is triggered when the create_user_button is clicked.
        Shows create_account_page.
        Access level: admin
        """
        if self.state["user_type"] == 'admin':
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.create_user_page)


    # @restrict_page_change
    def show_transaction_page(self):
        """
        This slot is triggered when the transaction_history_button is clicked.
        Show the transactions_page.
        """

        self.ui.stackedWidget_3.setCurrentWidget(self.ui.transactions_page)
        #@TODO: Add tableview 

    # @restrict_page_change
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
        if self.ui.inventory_type_input.currentIndex() == -1:
            return

        # clear the list view widget items if the current page is add_entry_page
        if self.ui.stackedWidget_4.currentWidget() == self.ui.add_entry_page:
            self.ui.add_entry_list.clear()
            self.ui.item_name_input.clear()
            self.ui.item_qty_input.clear()
            self.update_locations(0)


        self.ui.stackedWidget_3.setCurrentWidget(self.ui.inventory_view_page)
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.item_search_page)
        self.state["item_type"] = self.ui.inventory_type_input.currentText().lower()
        self.state["inventory_page_func"] = "search"
        self.deselect_button_group()
        # self.activate_page_change()
        
        # Show inventory table data
        self.set_default_inventory_table()

        # Table design
        # table_header = self.ui.item_search_table.horizontalHeader()
        # table_header.resizeSection(0, 100)        
        # table_header.resizeSection(1, 450)        
        # table_header.resizeSection(2, 100)        
        # table_header.resizeSection(3, 350)        

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

    def view_inventory_search(self):
        search_term = self.ui.search_bar_input.text()
        self.search_inventory(search_term)

    @admin_access
    # @restrict_page_change
    def show_add_entry_page(self):
        """
        This slot is triggered when the add_entry_button is clicked.
        Show add_entry_page.
        Access level: admin
        """

        self.ui.stackedWidget_4.setCurrentWidget(self.ui.add_entry_page)
        self.state["inventory_page_func"] = "add"
        self.ui.add_entry_label.setText(self.update_item_type_label())
        # self.deactivate_page_change()

    def add_entry(self):
        if not utils.validate_line_edit(self.ui.item_name_input):
            return
        if not utils.validate_line_edit(self.ui.item_qty_input):
            return


        confirm = utils.show_dialog(
                "Are you sure?", 
                "Do you really want to add this entry to the database?"
                )
        if confirm == QMessageBox.No:
            return

        item_type = self.state["item_type"]
        name = self.ui.item_name_input.text()
        qty = self.ui.item_qty_input.text()
        location = self.ui.item_location_input.currentText()
        lab = self.ui.item_lab_input.currentText()

        item_entry = {
            "name": name,
            "qty": qty,
            "location": location,
            "lab": lab
        }

        if self.inventory_manager.check_item_location(name, lab, location):
            utils.show_message("Item exists!", f"""Item {name} already exists in {lab}, {location}.
Use Edit Entry option to change the quantity of an existing item.""")
            return

        self.inventory_manager.add_entry(item_type, **item_entry)

        # item_entry = ItemEntry()
        # list_item = QListWidgetItem()
        # list_item.setSizeHint(item_entry.sizeHint() + QSize(45, 45))
        # id = str(self.ui.add_entry_list.count() + 1)
        # name = self.ui.item_name_input.text()
        # qty = self.ui.item_qty_input.text()
        # location = self.ui.item_location_input.currentText()
        # lab = self.ui.item_lab_input.currentText()

        # item_entry.ui.id.setText(id)
        # item_entry.ui.name.setText(name)
        # item_entry.ui.qty.setText(qty)
        # item_entry.ui.location.setText(location)
        # item_entry.ui.lab.setText(lab)

        # self.ui.add_entry_list.addItem(list_item)
        # self.ui.add_entry_list.setItemWidget(list_item, item_entry)

        # Clear current input values
        self.ui.item_name_input.clear()
        self.ui.item_qty_input.clear()
        self.update_locations(0)


    def update_locations(self, index):
        selected_lab = self.ui.item_lab_input.currentText()
        self.ui.item_location_input.clear()

        if selected_lab in self.state["location_data"]:
            self.ui.item_location_input.addItems(self.state["location_data"][selected_lab])

    def save_entry(self):
        confirm = utils.show_dialog(
                "Are you sure?", 
                "Do you really want to add this entry to the database?"
                )
        if confirm == QMessageBox.Yes:
            entries = []
            item_type = self.state["item_type"]
            for i in range(self.ui.add_entry_list.count()):
                item_widget = self.ui.add_entry_list.itemWidget(self.ui.add_entry_list.item(i))
                name = item_widget.ui.name.text()
                qty = item_widget.ui.qty.text()
                location = item_widget.ui.location.text()
                lab = item_widget.ui.lab.text()

                item_entry = {
                        "name": name,
                        "qty": qty,
                        "location": location,
                        "lab": lab
                        }
                entries.append(item_entry)
            
            for item in entries:
                self.inventory_manager.add_entry(item_type, **item)

            self.handle_inventory_page()


    # @restrict_page_change
    def show_update_entry_page(self):
        """
        This slot is triggered when the update_entry_button is clicked.
        Show update_entry_page.
        """

        self.ui.stackedWidget_4.setCurrentWidget(self.ui.update_entry_page)
        self.state["inventory_page_func"] = "update"
        self.ui.update_entry_label.setText(self.update_item_type_label())
        self.set_default_inventory_table(self.ui.update_entry_table)
        self.remove_current_update_input()
        # self.deactivate_page_change()

    def update_entry_table_clicked(self, index):
        self.remove_current_update_input()
        row = index.row()
        column = index.column()

        model = self.state["items_model"]
        header = model.headerData(column, Qt.Horizontal)
        name = model.index(row, 1).data()
        qty = model.index(row, 2).data()
        lab = model.index(row, 3).data()
        location = model.index(row, 4).data()

        data = {
            "header": header,
            "name": name,
            "qty": qty,
            "lab": lab,
            "location": location
        }

        self.add_update_input(data)

    def update_inventory_search(self):
        search_term = self.ui.update_entry_search_input.text()
        self.search_inventory(search_term, self.ui.update_entry_table)

    @admin_access
    # @restrict_page_change
    def show_delete_entry_page(self):
        """
        This slot is triggered when the delete_entry_button is clicked.
        Show delete_entry_page.
        Access level: admin
        """

        self.ui.stackedWidget_4.setCurrentWidget(self.ui.delete_entry_page)
        self.state["inventory_page_func"] = "delete"
        self.ui.delete_entry_label.setText(self.update_item_type_label())
        # self.deactivate_page_change()

    def handle_cancel_button(self):
        """
        This slot is triggered when the cancel_button is clicked.
        Go back to home_page
        """
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.inventory_page)

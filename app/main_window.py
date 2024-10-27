from PySide6.QtCore import QTimer, Qt 
from PySide6.QtGui import QIcon, QDoubleValidator
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QLayout, QMainWindow, QMenu, QMessageBox, QSystemTrayIcon, QTableView, QVBoxLayout, QFileDialog

from app.ui.ui_main import Ui_MainWindow
from app.quantity_edit import QtyEdit
from app.user_quantity_edit import UserQuantityEdit
from app.quantity_restock import QtyRestock
from app.name_edit import NameEdit
from app.location_edit import LocationEdit
from app.move_item import MoveItem

from app.manager import DatabaseManager
from app import utils
from app.access_controls import admin_access


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
        # `item_type`: glassware, equipments, chemical_liquid, chemical_salt
        # `inventory_page_func`: search, add, update, restock, move, delete
        self.state = {
            "username": "",
            "user_type": "", 
            "item_type": "", 
            "inventory_page_func": "search",
            "location_data": self.db_manager.inventory_manager.retrieve_locations(),
            "items_model": None
            }

        # View login screen
        self.ui.stackedWidget.setCurrentWidget(self.ui.login_page)
        self.ui.username_input.setFocus()
        self.ui.username_input.clear()
        self.ui.password_input.clear()

        # Set time and date
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.set_time)
        self.timer.start(1000)
        self.set_time()
        self.ui.date_label.setText(utils.get_date())
        self.ui.date_label_2.setText(utils.get_date())

        # Set input validators
        self.ui.item_qty_input.setValidator(QDoubleValidator())

        # Setup tray icon for showing alert notifications
        self.tray_icon = QSystemTrayIcon(QIcon(":/icon/images/logo.ico"), self)
        self.tray_icon.setToolTip("Alert")
        self.tray_icon_menu = QMenu()
        self.tray_icon.setContextMenu(self.tray_icon_menu)
        self.tray_icon.show()


        # =============================================== #
        # ===============  Signals ====================== #
        # =============================================== #
        self.ui.login_button.clicked.connect(self.handle_login)
        self.ui.password_input.returnPressed.connect(self.handle_login)

        self.ui.create_user_button.clicked.connect(self.show_create_account_page)
        self.ui.cancel_button.clicked.connect(self.handle_cancel_button)
        self.ui.create_account_button.clicked.connect(self.handle_create_account)
        self.ui.cu_confirm_password_input.returnPressed.connect(self.handle_create_account)

        self.ui.logout_button.clicked.connect(self.handle_logout)
        self.ui.transaction_history_button.clicked.connect(self.show_transaction_page)
        self.ui.alerts_button.clicked.connect(self.show_alerts_page)

        self.ui.transaction_history_button_2.clicked.connect(self.show_user_transaction_page)
        self.ui.go_back_button.clicked.connect(self.show_user_page)
        self.ui.update_entry_search_button_2.clicked.connect(self.user_update_inventory_search)
        self.ui.update_entry_search_input_2.returnPressed.connect(self.user_update_inventory_search)
        self.ui.update_entry_table_2.clicked.connect(self.user_update_entry_table_clicked)
        self.ui.user_item_type_input.currentTextChanged.connect(self.update_user_item_table)

        self.ui.inventory_type_input.currentTextChanged.connect(self.handle_inventory_page)
        # Change the value of inventory_type_input combo box to the default value
        self.ui.stackedWidget_3.currentChanged.connect(self.inventory_view_changed)

        self.ui.search_button.clicked.connect(self.view_inventory_search)
        self.ui.search_bar_input.returnPressed.connect(self.view_inventory_search)

        self.ui.add_entry_button.clicked.connect(self.show_add_entry_page)
        self.ui.add_entry_cancel_button.clicked.connect(self.handle_inventory_page)
        self.ui.add_entry_add_button.clicked.connect(self.add_entry)
        self.ui.item_location_input.returnPressed.connect(self.add_entry)

        self.ui.update_entry_button.clicked.connect(self.show_update_entry_page)
        self.ui.update_entry_cancel_button.clicked.connect(self.handle_inventory_page)
        self.ui.update_entry_table.clicked.connect(self.update_entry_table_clicked)
        self.ui.update_entry_search_button.clicked.connect(self.update_inventory_search)
        self.ui.update_entry_search_input.returnPressed.connect(self.update_inventory_search)

        self.ui.restock_entry_button.clicked.connect(self.show_restock_entry_page)
        self.ui.restock_entry_cancel_button.clicked.connect(self.handle_inventory_page)
        self.ui.restock_entry_table.clicked.connect(self.restock_entry_table_clicked)
        self.ui.restock_entry_search_button.clicked.connect(self.restock_inventory_search)
        self.ui.restock_entry_search_input.returnPressed.connect(self.restock_inventory_search)

        self.ui.move_entry_button.clicked.connect(self.show_move_entry_page)
        self.ui.move_entry_cancel_button.clicked.connect(self.handle_inventory_page)
        self.ui.move_entry_table.clicked.connect(self.move_entry_table_clicked)
        self.ui.move_entry_search_button.clicked.connect(self.move_inventory_search)
        self.ui.move_entry_search_input.returnPressed.connect(self.move_inventory_search)

        self.ui.delete_entry_button.clicked.connect(self.show_delete_entry_page)
        self.ui.delete_entry_cancel_button.clicked.connect(self.handle_inventory_page)
        self.ui.delete_entry_search_button.clicked.connect(self.delete_inventory_search)
        self.ui.delete_entry_search_input.returnPressed.connect(self.delete_inventory_search)
        self.ui.delete_entry_delete_button.clicked.connect(self.delete_entry)

        self.ui.print_items_button.clicked.connect(self.print_items)
        self.ui.print_transactions_button.clicked.connect(self.print_transactions)


    def set_time(self):
        self.ui.time_label.setText(utils.get_time())
        self.ui.time_label_2.setText(utils.get_time())

    def update_item_type_input(self):
        # Format the item_type string
        # eg: "chemical_liquid" -> "Chemical - Liquid"
        item_types_formatted = [" - ".join(item.split("_")).title() for item in self.inventory_manager.item_types]
        self.ui.inventory_type_input.clear()
        
        # With this in the ui it will show "Chemical - Liquid" but in the code 
        # we can use "chemical_liquid" by using inventory_type_input.currentData()
        for formatted, item in zip(item_types_formatted, self.inventory_manager.item_types):
            self.ui.inventory_type_input.addItem(formatted, userData=item)

    def update_user_item_type_input(self):
        user_item_types = ["chemical_liquid", "chemical_salt"]
        item_types_formatted = [" - ".join(item.split("_")).title() for item in user_item_types]
        self.ui.user_item_type_input.clear()

        for formatted, item in zip(item_types_formatted, user_item_types):
            self.ui.user_item_type_input.addItem(formatted, userData=item)
    
    def show_user_page(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.user_page)
        self.ui.stackedWidget_5.setCurrentWidget(self.ui.update_entry_page_2)
        self.ui.update_entry_search_input_2.clear()
        self.remove_current_update_input(self.ui.verticalLayout_16)

    def show_home_screen(self, username: str):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.ui.header_username_label.setText(username.upper())

        # Show screen based on 'user_type'
        # Add and/or remove 'create_user_button' based on 'user_type'
        create_user_button = self.ui.create_user_button
        button_present = self.ui.horizontalLayout_2.count() > 1
        if self.state['user_type'] == 'admin':
            # Update item_types:
            self.update_item_type_input()

            self.ui.stackedWidget_3.setCurrentWidget(self.ui.inventory_page_default)
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.inventory_page)
            self.show_alert_notifications()
            if not button_present:
                self.ui.horizontalLayout_2.insertWidget(0, create_user_button)
                create_user_button.show()
        elif self.state['user_type'] == 'user':
            self.update_user_item_type_input()
            self.state['item_type'] = self.ui.user_item_type_input.currentData()

            self.set_default_inventory_table(self.ui.update_entry_table_2)
            table_header = self.ui.update_entry_table_2.horizontalHeader()
            table_header.resizeSection(0, 100)        
            table_header.resizeSection(1, 450)        
            self.show_user_page()
            if button_present:
                create_user_button.hide()
                self.ui.horizontalLayout_2.removeWidget(create_user_button)
        
    def show_alert_notifications(self):
        query = QSqlQuery()
        query.prepare(self.inventory_manager.RETRIEVE_ALERTS_SQL)
        query.exec()
        
        while query.next():
            item = query.value("Name")
            self.tray_icon.showMessage("Alert", f"{item} is below margin level", QSystemTrayIcon.Information, 5000)
    
    def update_item_type_label(self):
        text = {
            "add": "ADD NEW",
            "update": "EDIT EXISTING",
            "restock": "RESTOCK",
            "move": "MOVE",
            "delete": "REMOVE EXISTING"
        }

        # @NOTE:
        # If item_type is chemical_liquid then it will be formatted to Chemical only
        # Because of length contraints - might change in the future.
        item_type_formatted = self.state["item_type"].split("_")[0].upper()
        return f"{text[self.state['inventory_page_func']]} {item_type_formatted}"
    

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
        if self.state["user_type"] == "admin":
            self.state["items_model"] = self.inventory_manager.retrieve_item_info(self.state["item_type"])
        else:
            self.state["items_model"] = self.inventory_manager.retrieve_item_info(self.state["item_type"],
                                                      with_qty=False)
        if self.state["items_model"]:
            table.setModel(self.state["items_model"])

    def remove_current_update_input(self, layout: QLayout = None):
        if not layout:
            layout = self.ui.verticalLayout_13
        widget_count = layout.count()
        if widget_count > 3:
            current_edit_input = layout.itemAt(widget_count - 1)
            widget = current_edit_input.widget()
            if widget:
                widget.setParent(None)

    
    def add_update_input(self, data: dict[str, str | QTableView], layout: QVBoxLayout = None):
        if not layout:
            layout = self.ui.verticalLayout_13
        # Update entry page inputs
        self.name_edit = NameEdit(self, data)
        self.quantity_edit = QtyEdit(self, data)
        self.user_quantity_edit = UserQuantityEdit(self, data)
        self.location_edit = LocationEdit(self, data)

        if self.state["user_type"] == "user":
            layout.addWidget(self.user_quantity_edit)

        else:
            if data["header"] == "Qty":
                layout.addWidget(self.quantity_edit)

                layout.setStretch(0, 1)
                layout.setStretch(2, 7)
                layout.setStretch(3, 1)

            elif data["header"] == "Name":
                layout.addWidget(self.name_edit)

                layout.setStretch(0, 1)
                layout.setStretch(2, 7)
                layout.setStretch(3, 1)

            elif data["header"]  == "Store":
                layout.addWidget(self.location_edit)

                layout.setStretch(0, 1)
                layout.setStretch(2, 7)
                layout.setStretch(3, 1)
        
        
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
        self.transactions_model = self.inventory_manager.retrieve_transactions_info()
        self.ui.transactions_table.setModel(self.transactions_model)

        # Resize table headers
        transaction_table_header = self.ui.transactions_table.horizontalHeader()
        transaction_table_header.resizeSection(1, 150)
        transaction_table_header.resizeSection(2, 150)
        transaction_table_header.resizeSection(4, 350)

    def show_user_transaction_page(self):
        """
        This slot is triggered when the transaction history button under user
        page is clicked.
        """

        self.ui.stackedWidget_5.setCurrentWidget(self.ui.user_transactions_page)
        self.transactions_model = self.inventory_manager.retrieve_transactions_info(self.state['username'])
        self.ui.transactions_table_2.setModel(self.transactions_model)

        # Resize table headers
        transaction_table_header = self.ui.transactions_table_2.horizontalHeader()
        transaction_table_header.resizeSection(1, 150)
        transaction_table_header.resizeSection(2, 150)
        transaction_table_header.resizeSection(4, 350)

    def show_alerts_page(self):
        """
        This slot is triggered when the alerts_button is clicked.
        Show the alerts_page.
        """

        self.ui.stackedWidget_3.setCurrentWidget(self.ui.alerts_page)
        self.alerts_model = self.inventory_manager.retrieve_alerts_info()
        self.ui.alerts_table.setModel(self.alerts_model)

        # Resize table headers
        alerts_table_header = self.ui.alerts_table.horizontalHeader()
        alerts_table_header.resizeSection(0, 100)
        alerts_table_header.resizeSection(1, 400)
    
    def handle_inventory_page(self):
        """
        This slot is triggered when the inventory_type_input is activated.
        Handles the inventory_view_page.
        """

        # To avoid side effects from inventory_view_changed function
        #@NOTE: The inventory_view_changed also changes the current value of the combo box,
        # it will trigger the currentTextChanged signal and will connect to this slot.
        # Fix: check the currentIndex is not -1 before setting currentWidget
        if self.ui.inventory_type_input.currentIndex() == -1:
            return

        # clear the list view widget items if the current page is add_entry_page
        if self.ui.stackedWidget_4.currentWidget() == self.ui.add_entry_page:
            self.ui.add_entry_list.clear()
            self.ui.item_name_input.clear()
            self.ui.item_qty_input.clear()
            self.ui.item_location_input.clear()


        self.ui.stackedWidget_3.setCurrentWidget(self.ui.inventory_view_page)
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.item_search_page)
        self.state["item_type"] = self.ui.inventory_type_input.currentData()
        self.state["inventory_page_func"] = "search"
        self.deselect_button_group()
        
        # Show inventory table data
        self.set_default_inventory_table()

        # Table design
        table_header = self.ui.item_search_table.horizontalHeader()
        table_header.resizeSection(0, 100)        
        table_header.resizeSection(1, 450)        
        table_header.resizeSection(4, 200)        

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

    def print_items(self):
        """
        This slot is triggered when the print_items_button is clicked.
        This will print the entries of the current selected item.
        """
        
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save PDF", "", "PDF Files (*.pdf);;All Files (*)"
        )

        if not file_path:
            return

        title = ''
        if self.state['item_type'].startswith('chemical'):
            title = 'Chemical'
        else:
            title = self.state['item_type'].title()

        # generate pdf file
        utils.create_pdf(title, file_path, self.state['items_model'])

    def print_transactions(self):
        """
        This slot is triggered when the print_transactions_button is clicked.
        This will print the entries of the transactions table.
        """

        if self.transactions_model:
            file_path, _ = QFileDialog.getSaveFileName(
                self, "Save PDF", "", "PDF Files (*.pdf);;All Files (*)"
            )

            if not file_path:
                return

            title = 'Transactions History'

            # generate pdf file
            utils.create_pdf(title, file_path, self.transactions_model)

        else:
            utils.show_message("Error", "Unable to print transactions:\nTransaction history empty!")


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
        if self.state["item_type"] == "chemical_liquid":
            self.ui.qty_label.setText("Qty (Litre)")
        elif self.state["item_type"] == "chemical_salt":
            self.ui.qty_label.setText("Qty (gram)")
        else:
            self.ui.qty_label.setText("Qty (Pcs.)")

    def add_entry(self):
        if not utils.validate_line_edit(self.ui.item_name_input):
            return
        if not utils.validate_line_edit(self.ui.item_qty_input):
            return
        if not utils.validate_line_edit(self.ui.item_location_input):
            return


        confirm = utils.show_dialog(
                "Are you sure?", 
                "Do you really want to add this entry to the database?"
                )
        if confirm == QMessageBox.No:
            return

        item_type = self.state["item_type"]
        name = self.ui.item_name_input.text()
        qty = float(self.ui.item_qty_input.text())
        location = self.ui.item_location_input.text()

        item_entry = {
            "name": name,
            "qty": qty,
            "location": location
        }

        # If the location is not already present under the Store, add the location
        if not self.inventory_manager.location_exists(location):
            self.inventory_manager.insert_location(location)
            
        # If the item is already present in the given location, show the error message
        if self.inventory_manager.check_item_location(name, location):
            utils.show_message("Item exists!", f"""Item {name} already exists in store, {location}.
Use Edit Entry option to change the quantity of an existing item.""")
            return

        if self.inventory_manager.add_entry(item_type, **item_entry):
            utils.show_message("Item Added", f"Item {name} added to the database")

        # Clear current input values
        self.ui.item_name_input.clear()
        self.ui.item_qty_input.clear()
        self.ui.item_location_input.clear()

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
        self.ui.update_entry_search_input.clear()

        # Resize table headers
        update_table_header = self.ui.update_entry_table.horizontalHeader()
        update_table_header.resizeSection(0, 100)        
        update_table_header.resizeSection(1, 450)        

    def update_entry_table_clicked(self, index):
        self.remove_current_update_input()
        row = index.row()
        column = index.column()

        model = self.state["items_model"]
        header = model.headerData(column, Qt.Horizontal)
        name = model.index(row, 1).data()
        user = self.state["username"]
        qty = model.index(row, 2).data()
        location = model.index(row, 3).data()

        data = {
            "table": self.ui.update_entry_table,
            "item_type": self.state["item_type"],
            "header": header,
            "user": user,
            "name": name,
            "qty": qty,
            "location": location
        }

        self.add_update_input(data)

    def user_update_entry_table_clicked(self, index):
        self.remove_current_update_input(self.ui.verticalLayout_16)
        row = index.row()
        column = index.column()

        model = self.state["items_model"]
        header = model.headerData(column, Qt.Horizontal)
        name = model.index(row, 1).data()
        user = self.state["username"]
        location = model.index(row, 2).data()
        loc_id = self.inventory_manager.retrieve_loc_id(location)
        qty = self.inventory_manager.retrieve_qty(name, loc_id)

        data = {
            "table": self.ui.update_entry_table_2,
            "item_type": self.state["item_type"],
            "header": header,
            "user": user,
            "name": name,
            "qty": qty,
            "location": location
        }

        self.add_update_input(data, self.ui.verticalLayout_16)

    def update_user_item_table(self):
        """
        This slot is triggered when the user_item_type_input is changed.
        It will update the  current table model to the selected one.
        """
        self.remove_current_update_input(self.ui.verticalLayout_16)
        self.state["item_type"] = self.ui.user_item_type_input.currentData()
        self.state["items_model"] = self.inventory_manager.retrieve_item_info(self.state["item_type"],
                                                with_qty=False)
        if self.state["items_model"]:
            self.ui.update_entry_table_2.setModel(self.state["items_model"])
        

    def update_inventory_search(self):
        search_term = self.ui.update_entry_search_input.text()
        self.search_inventory(search_term, self.ui.update_entry_table)

    def user_update_inventory_search(self):
        search_term = self.ui.update_entry_search_input_2.text()
        self.search_inventory(search_term, self.ui.update_entry_table_2)
    
    def show_move_entry_page(self):
        """
        This slot is triggered when the move_entry_button is clicked.
        Show move_entry_page
        """

        self.ui.stackedWidget_4.setCurrentWidget(self.ui.move_entry_page)
        self.state["inventory_page_func"] = "move"
        self.ui.move_entry_label.setText(self.update_item_type_label())
        self.set_default_inventory_table(self.ui.move_entry_table)
        self.remove_current_update_input(self.ui.verticalLayout_24)
        self.ui.move_entry_search_input.clear()

        # Resize table headers
        move_table_header = self.ui.move_entry_table.horizontalHeader()
        move_table_header.resizeSection(0, 100)
        move_table_header.resizeSection(1, 450) 
    
    def move_inventory_search(self):
        search_term = self.ui.move_entry_search_input.text()
        self.search_inventory(search_term, self.ui.move_entry_table)
    
    def move_entry_table_clicked(self, index):
        self.remove_current_update_input(self.ui.verticalLayout_24)
        row = index.row()
        column = index.column()

        model = self.state["items_model"]
        header = model.headerData(column, Qt.Horizontal)
        name = model.index(row, 1).data()
        user = self.state["username"]
        qty = model.index(row, 2).data()
        location = model.index(row, 3).data()

        data = {
            "table": self.ui.move_entry_table,
            "item_type": self.state["item_type"],
            "header": header,
            "user": user,
            "name": name,
            "qty": qty,
            "location": location
        }

        self.move_item = MoveItem(self, data)
        layout = self.ui.verticalLayout_24
        layout.addWidget(self.move_item)

        layout.setStretch(0, 1)
        layout.setStretch(2, 7)
        layout.setStretch(3, 1)

    def show_restock_entry_page(self):
        """
        This slot is triggered when the restock_entry_button is clicked.
        Show restock_entry_page.
        """

        self.ui.stackedWidget_4.setCurrentWidget(self.ui.restock_entry_page)
        self.state["inventory_page_func"] = "restock"
        self.ui.restock_entry_label.setText(self.update_item_type_label())
        self.set_default_inventory_table(self.ui.restock_entry_table)
        self.remove_current_update_input(self.ui.verticalLayout_18)
        self.ui.restock_entry_search_input.clear()

        # Resize table headers
        restock_table_header = self.ui.restock_entry_table.horizontalHeader()
        restock_table_header.resizeSection(0, 100)
        restock_table_header.resizeSection(1, 450) 

    def restock_inventory_search(self):
        search_term = self.ui.restock_entry_search_input.text()
        self.search_inventory(search_term, self.ui.restock_entry_table)

    def restock_entry_table_clicked(self,index):
        self.remove_current_update_input(self.ui.verticalLayout_18)
        row = index.row()
        column = index.column()

        model = self.state["items_model"]
        header = model.headerData(column, Qt.Horizontal)
        name = model.index(row, 1).data()
        user = self.state["username"]
        qty = model.index(row, 2).data()
        location = model.index(row, 3).data()

        data = {
            "table": self.ui.restock_entry_table,
            "item_type": self.state["item_type"],
            "header": header,
            "user": user,
            "name": name,
            "qty": qty,
            "location": location
        }

        self.quantity_restock = QtyRestock(self, data)
        layout = self.ui.verticalLayout_18
        layout.addWidget(self.quantity_restock)

        layout.setStretch(0, 1)
        layout.setStretch(2, 7)
        layout.setStretch(3, 1)


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
        self.set_default_inventory_table(self.ui.delete_entry_table)
        self.ui.delete_entry_search_input.clear()

        # Resize table headers
        delete_table_header = self.ui.delete_entry_table.horizontalHeader()
        delete_table_header.resizeSection(0, 100)        
        delete_table_header.resizeSection(1, 450)        

    def delete_inventory_search(self):
        search_term = self.ui.delete_entry_search_input.text()
        self.search_inventory(search_term, self.ui.delete_entry_table)

    def delete_entry(self):
        current_index = self.ui.delete_entry_table.currentIndex()
        if not current_index.isValid():
            utils.show_message("Error", "Select an item in the table to remove")
            return

        row = current_index.row()
        model = self.state["items_model"]
        name = model.index(row, 1).data()
        location = model.index(row, 3).data()

        confirm = utils.show_dialog(
                "Are you sure?",
                f"Do you really want to delete {name} from database?"
                )
        if confirm == QMessageBox.No:
            return

        if self.inventory_manager.delete_item(name, location):
            utils.show_message("Item deleted", f"Item: {name} successfully deleted from the database")
            self.set_default_inventory_table(self.ui.delete_entry_table)
        else:
            utils.show_message("Error", "Cannot delete item")
        

    def handle_cancel_button(self):
        """
        This slot is triggered when the cancel_button is clicked.
        Go back to home_page
        """
        self.ui.cu_username_input.clear()
        self.ui.cu_password_input.clear()
        self.ui.cu_confirm_password_input.clear()
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.inventory_page)


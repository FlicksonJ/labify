import os
import sys
import bcrypt  # Import secure hashing library
from itsdangerous import URLSafeTimedSerializer

from PySide6.QtWidgets import QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel

from app import settings

serializer = URLSafeTimedSerializer(settings.SECRET)


class DatabaseManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.setup_database()
        return cls._instance

    def setup_database(self):
        self.db_name = settings.DATABASE
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.db_name)

        # check if the database file exists
        if not os.path.exists(self.db_name):
            os.makedirs(os.path.dirname(self.db_name), exist_ok=True)
            if not self.create_database():
                QMessageBox.critical(None, "Error", "Failed to create database file")
                sys.exit(1)

        if not self.db.open():
            QMessageBox.critical(None, "Error", f"Failed to open database: {self.db.lastError().text()}")
            sys.exit(1)

        if not self.db.open():
            print("Error: cannot open database")

        self.inventory_manager = InventoryManager(self.db)
        self.account_manager = AccountManager(self.db)

    def create_database(self) -> bool:
        """
        Create database if doesn't exist already
        """
        try:
            open(self.db.databaseName(), 'a').close()
            return True
        except Exception as e:
            print(f"Error creating database file: {e}")
            return False


class AccountManager:
    def __init__(self, db_connection):
        self.db = db_connection

        self.USERS_TABLE_SQL = """
            create table if not exists users (
                uid integer primary key autoincrement,
                username text unique not null,
                hashed_password text not null,
                user_type text not null
            )
            """
        self.INSERT_ADMIN_SQL = """
            INSERT INTO users (username, hashed_password, user_type) 
            VALUES (?, ?, "admin")
            """
        self.INSERT_USER_SQL = """
            INSERT INTO users (username, hashed_password, user_type) 
            VALUES (?, ?, "user")
            """
        self.SEARCH_USERNAME_SQL = """
            SELECT * FROM users WHERE username = (?)
            """

        self.create_table()
        # Create test admin user
        # @TODO: Change it and create admin user at installation
        self.create_admin("admin", "admin@123")


    def create_table(self):
        query = QSqlQuery()
        query.exec(self.USERS_TABLE_SQL)

    def account_exists(self, username):
        query = QSqlQuery()
        query.prepare(self.SEARCH_USERNAME_SQL)
        query.addBindValue(username)
        query.exec()
        return query.next()
    
    def create_account(self, query, username, password):
        # Securely hash password
        hashed_password = self.hash_pw(password)

        query.addBindValue(username)
        query.addBindValue(hashed_password)
        query.exec()

    def create_user(self, username, password):
        query = QSqlQuery()
        query.prepare(self.INSERT_USER_SQL)
        self.create_account(query, username, password)
    
    def create_admin(self, username, password):
        query = QSqlQuery()
        query.prepare(self.INSERT_ADMIN_SQL)
        self.create_account(query, username, password)

        
    def hash_pw(self, password):
        """
        Hashes a password using bcrypt with a secure salt.
    
        Args:
            password (str): The password to be hashed.
    
        Returns:
            str: The hashed password.
        """
        salt = bcrypt.gensalt(14)
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        serialized_data = serializer.dumps({"salt": salt.decode(), "hashed_password": hashed_password.decode()})
        return serialized_data
    
    def verify_pw(self, hashed_password, password_to_check):
        """
        Verifies a password against a stored hashed password.
    
        Args:
          hashed_password (str): The stored hashed password (serialized format).
          password_to_check (str): The password to be verified.
    
        Returns:
          bool: True if the password matches the stored hash, False otherwise.
        """
        try:
          # Deserialize the stored data to access salt and hashed password
          data = serializer.loads(hashed_password.encode("utf-8"))
          salt = data["salt"]
          stored_hashed_password = data["hashed_password"]
    
        except Exception as e:
          # Handle deserialization errors gracefully (e.g., invalid format)
          print(f"Error deserializing hashed password: {e}")
          return False
    
        # Verify the password using the retrieved salt and hashed password
        return bcrypt.checkpw(password_to_check.encode(), stored_hashed_password.encode())


class InventoryManager:
    def __init__(self, db_connection):
        self.db = db_connection

        self.ITEMS_TABLE_SQL = """
        CREATE TABLE IF NOT EXISTS Items (
            item_id INTEGER PRIMARY KEY,
            name VARCHAR(255),
            qty REAL,
            stock_id INTEGER,
            location_id INT,
            FOREIGN KEY (stock_id) REFERENCES StockType(stock_id)
            FOREIGN KEY (location_id) REFERENCES Locations(loc_id)
            UNIQUE(name, location_id)
        )"""
        self.STOCK_TYPE_TABLE_SQL = """
        CREATE TABLE IF NOT EXISTS StockType (
            stock_id INTEGER PRIMARY KEY,
            type VARCHAR(255) UNIQUE
        )"""
        self.LOCATIONS_TABLE_SQL = """
        CREATE TABLE IF NOT EXISTS Locations (
            loc_id INTEGER PRIMARY KEY,
            name VARCHAR(255),
            lab_id INTEGER,
            FOREIGN KEY (lab_id) REFERENCES Labs(lab_id)
            UNIQUE(name, lab_id)
        )"""
        self.LABS_TABLE_SQL = """        
        CREATE TABLE IF NOT EXISTS Labs (
            lab_id INTEGER PRIMARY KEY,
            name VARCHAR(255) UNIQUE
        )"""
        self.TRANSACTION_TABLE_SQL = """
        CREATE TABLE IF NOT EXISTS Transactions (
            tid INTEGER PRIMARY KEY,
            date DATE,
            time VARCHAR(255),
            user VARCHAR(255),
            name VARCHAR(255),
            qty REAL,
            action VARCHAR(50),
            lab VARCHAR(50),
            location VARCHAR(50)
        )"""

        self.INSERT_STOCK_TYPE_SQL = """
        INSERT OR IGNORE INTO StockType (type)
        VALUES (?)
        """
        self.INSERT_LABS_SQL = """
        INSERT OR IGNORE INTO Labs (name)
        VALUES (?)
        """
        self.INSERT_LOCATIONS_SQL = """
        INSERT OR IGNORE INTO Locations (name, lab_id)
        VALUES (?, ?)
        """
        self.INSERT_ITEM_SQL = """
        INSERT OR IGNORE INTO Items (name, qty, stock_id, location_id)
        VALUES (?, ?, 
                (SELECT stock_id FROM StockType WHERE type = (?)),
                (SELECT loc_id FROM Locations WHERE name = (?) AND lab_id = 
                (SELECT lab_id FROM Labs WHERE name = (?))))
        """
        self.INSERT_TRANSACTION_SQL = """
        INSERT INTO Transactions (date, time, user, name, qty, action, lab, location)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.RETRIEVE_TRANSACTION_SQL = """
        SELECT * FROM Transactions
        """
        self.RETRIEVE_LAB_ID_SQL = """
        SELECT lab_id FROM Labs WHERE name = (?)
        """
        self.RETRIEVE_LABS_SQL = """
        SELECT name FROM Labs;
        """
        self.RETRIEVE_LOCATIONS_SQL = """
        SELECT Labs.name AS lab_name, Locations.name AS location_name
        FROM Labs
        INNER JOIN Locations ON Labs.lab_id = Locations.lab_id
        """
        self.RETRIEVE_ITEM_INFO_SQL = """
        SELECT 
            ROW_NUMBER() OVER (ORDER BY Items.item_id) AS CID, 
            Items.name AS Name, 
            Items.qty AS Qty, 
            Labs.name AS Lab,
            Locations.name AS Location
        FROM Items
        JOIN StockType ON Items.stock_id = StockType.stock_id
        JOIN Locations ON Items.location_id = Locations.loc_id
        JOIN Labs ON Locations.lab_id = Labs.lab_id
        WHERE StockType.type = (?)
        """
        self.USER_RETRIEVE_ITEM_INFO_SQL = """
        SELECT 
            ROW_NUMBER() OVER (ORDER BY Items.item_id) AS CID, 
            Items.name AS Name, 
            Labs.name AS Lab,
            Locations.name AS Location
        FROM Items
        JOIN StockType ON Items.stock_id = StockType.stock_id
        JOIN Locations ON Items.location_id = Locations.loc_id
        JOIN Labs ON Locations.lab_id = Labs.lab_id
        WHERE StockType.type = (?)
        """
        self.RETRIEVE_ITEM_LOCATION_SQL = """
        SELECT Labs.name AS Lab, Locations.name AS Location
        FROM Items
        JOIN Locations ON Items.location_id = Locations.loc_id
        JOIN Labs ON Locations.lab_id = Labs.lab_id
        WHERE Items.name = (?)
        """
        self.RETRIEVE_LOCATION_ID_SQL = """
         SELECT loc_id FROM Locations WHERE name = (?) AND lab_id = 
         (SELECT lab_id FROM Labs WHERE name = (?))
        """
        self.RETRIEVE_ALERTS_SQL = """
        SELECT 
            ROW_NUMBER() OVER (ORDER BY Items.item_id) AS CID, 
            Items.name AS Name, 
            Items.qty AS Qty, 
            Labs.name AS Lab,
            Locations.name AS Location
        FROM Items
        JOIN StockType ON Items.stock_id = StockType.stock_id
        JOIN Locations ON Items.location_id = Locations.loc_id
        JOIN Labs ON Locations.lab_id = Labs.lab_id
        WHERE (qty <= 5 AND StockType.type IN ('glassware', 'equipment')) OR
              (qty <= 2.5 AND StockType.type = 'chemical_liquid') OR
              (qty <= 500 AND StockType.type = 'chemical_salt')
        """
        self.UPDATE_ITEM_NAME_SQL = """
        UPDATE Items
        SET name = (?)
        WHERE name = (?) AND location_id =  (?)
        """
        self.UPDATE_ITEM_LOCATION_SQL = """
        UPDATE Items
        SET location_id = (?)
        WHERE name = (?) AND location_id = (?)
        """
        self.UPDATE_QTY_SQL = """
        UPDATE Items
        SET qty = (?)
        WHERE name = (?) AND location_id = (?)
        """
        self.UPDATE_ITEM_ADD_QTY_SQL = """
        UPDATE Items
        SET qty = qty + (?)
        WHERE name = (?) AND location_id = (?)
        """
        self.UPDATE_ITEM_REMOVE_QTY_SQL = """
        UPDATE Items
        SET qty = qty - (?)
        WHERE name = (?) AND location_id = (?)
        """
        self.GET_ITEM_QTY_SQL = """
        SELECT qty FROM Items
        WHERE name = (?) AND location_id = (?)
        """
        self.DELETE_ITEM_SQL = """
        DELETE FROM Items
        WHERE name = (?) AND location_id = (?)
        """

        self.item_types = ["glassware", "chemical_salt", "chemical_liquid", "equipment"]
        self.create_tables()
        self.insert_item_types(self.item_types)
        
        # @TODO: Change it and create locations at Installation
        self.lab_names = ["Main lab", "Sub lab", "MSc lab", "Down lab", "Upstairs lab", "Store"]
        self.insert_labs(self.lab_names)


    def create_tables(self):
        query = QSqlQuery()
        query.exec(self.ITEMS_TABLE_SQL)
        query.exec(self.STOCK_TYPE_TABLE_SQL)
        query.exec(self.LOCATIONS_TABLE_SQL)
        query.exec(self.LABS_TABLE_SQL)
        query.exec(self.TRANSACTION_TABLE_SQL)

        # Enter default stocktype values
        query.exec(self.INSERT_STOCK_TYPE_SQL)

    def insert_item_types(self, item_types: list[str]):
        query = QSqlQuery()
        for item_type in item_types:
            query.prepare(self.INSERT_STOCK_TYPE_SQL)
            query.addBindValue(item_type)
            query.exec()

    def insert_labs(self, lab_names: list[str]):
        query = QSqlQuery()
        for lab in lab_names:
            query.prepare(self.INSERT_LABS_SQL)
            query.addBindValue(lab)
            query.exec()
    
    def location_exists(self, lab: str, location: str) -> bool:
        query = QSqlQuery()
        sql = """
        SELECT 1 FROM Locations
        WHERE name = (?) AND lab_id = (
            SELECT lab_id FROM Labs
            WHERE name = (?)
        )
        """
        query.prepare(sql)
        query.addBindValue(location)
        query.addBindValue(lab)
        query.exec()

        if query.next():
            return True
        else:
            return False

    def insert_location(self, lab: str, location: str):
        query = QSqlQuery()
        # Retrieve `lab_id` for the current lab
        lab_id_query = QSqlQuery()
        lab_id_query.prepare(self.RETRIEVE_LAB_ID_SQL)
        lab_id_query.addBindValue(lab)
        lab_id_query.exec()
        lab_id_query.next()
        lab_id = lab_id_query.value(0)

        # Insert locations for the current lab
        query.prepare(self.INSERT_LOCATIONS_SQL)
        query.addBindValue(location)
        query.addBindValue(lab_id)
        query.exec()

    def retrieve_labs(self) -> list[str]:
        query = QSqlQuery()
        labs = []
        query.exec(self.RETRIEVE_LABS_SQL)

        while query.next():
            lab_name = query.value("name")
            labs.append(lab_name)
        
        return labs

    def retrieve_locations(self) -> dict[str, list[str]]:
        query = QSqlQuery()
        locations = {}
        query.exec(self.RETRIEVE_LOCATIONS_SQL)

        while query.next():
            lab_name = query.value("lab_name")
            location_name = query.value("location_name")

            if lab_name not in locations:
                locations[lab_name] = []
            locations[lab_name].append(location_name)
        
        return locations

    def check_item_location(self, name: str, lab: str, location: str) -> bool:

        item_exist = False
        query = QSqlQuery()
        query.prepare(self.RETRIEVE_ITEM_LOCATION_SQL)
        query.addBindValue(name)
        query.exec()

        while query.next():
            # Check if item with same lab and location already exists in database
            if query.value("Lab") == lab and query.value("Location") == location:
               item_exist = True 

        return item_exist

    
    def add_transaction(self, transaction: dict[str, str]) -> bool:
        query = QSqlQuery()
        query.prepare(self.INSERT_TRANSACTION_SQL)
        query.addBindValue(transaction["date"])
        query.addBindValue(transaction["time"])
        query.addBindValue(transaction["user"])
        query.addBindValue(transaction["name"])
        query.addBindValue(transaction["qty"])
        query.addBindValue(transaction["action"])
        query.addBindValue(transaction["lab"])
        query.addBindValue(transaction["location"])
        if not query.exec():
            print(query.lastError().text())
            return False
        else:
            return True


    def add_entry(self, 
                  stock_type: str, 
                  name: str, 
                  qty: str, 
                  location: str, 
                  lab: str) -> bool:
        query = QSqlQuery()

        # insert new item into the Items table
        query.prepare(self.INSERT_ITEM_SQL)
        query.addBindValue(name)
        query.addBindValue(qty)
        query.addBindValue(stock_type)
        query.addBindValue(location)
        query.addBindValue(lab)
        if not query.exec():
            print(query.lastError().text())
            return False
        else:
            return True


    def retrieve_item_info(self, stock_type: str, with_qty: bool = True) -> QSqlQueryModel | None:
        query = QSqlQuery()
        if with_qty:
            query.prepare(self.RETRIEVE_ITEM_INFO_SQL)
        else:
            query.prepare(self.USER_RETRIEVE_ITEM_INFO_SQL)
        query.addBindValue(stock_type)
        if not query.exec():
            print(query.lastError().text())

        model = QSqlQueryModel()
        model.setQuery(query)

        return model

    def retrieve_alerts_info(self) -> QSqlQueryModel | None:
        model = QSqlQueryModel()
        model.setQuery(self.RETRIEVE_ALERTS_SQL)

        if model.rowCount() > 0:
            return model
        else:
            return None

    def retrieve_transactions_info(self, user: str = 'admin') -> QSqlQueryModel | None:
        model = QSqlQueryModel()

        # User 'admin' should be able to view all the transactions
        # and other users should only be able view their own transactions.
        if user == 'admin':
            model.setQuery(self.RETRIEVE_TRANSACTION_SQL)
        else:
            query = QSqlQuery()
            query.prepare(self.RETRIEVE_TRANSACTION_SQL + " WHERE user = (?)")
            query.addBindValue(user)
            if not query.exec():
                print(query.lastError().text())

            model.setQuery(query)
        
        if model.rowCount() > 0:
            return model
        else:
            return None

    def update_item_name(self, 
                         current_name: str, 
                         lab: str, 
                         location: str, 
                         new_name: str) -> bool:
        loc_id = -1
        query = QSqlQuery()
        query.prepare(self.RETRIEVE_LOCATION_ID_SQL)
        query.addBindValue(location)
        query.addBindValue(lab)
        query.exec()

        while query.next():
            loc_id = query.value("loc_id")

        if loc_id == -1:
            print(query.lastError().text())
            return False

        query.prepare(self.UPDATE_ITEM_NAME_SQL)
        query.addBindValue(new_name)
        query.addBindValue(current_name)
        query.addBindValue(loc_id)
        if not query.exec():
            print(query.lastError().text())
            return False
        else:
            return True

    def retrieve_loc_id(self, lab: str, location: str) -> int:
        loc_id = -1
        query = QSqlQuery()
        query.prepare(self.RETRIEVE_LOCATION_ID_SQL)
        query.addBindValue(location)
        query.addBindValue(lab)
        query.exec()
        
        while query.next():
            loc_id = query.value("loc_id")

        if loc_id == -1:
            print(query.lastError().text())

        return loc_id

    def retrieve_qty(self, name: str, loc_id: int) -> float | None:
        qty = -1.0
        query = QSqlQuery()
        query.prepare(self.GET_ITEM_QTY_SQL)
        query.addBindValue(name)
        query.addBindValue(loc_id)
        query.exec()
        while query.next():
            qty = query.value("qty")

        if qty == -1.0:
            print(query.lastError().text())
            return None

        return qty

    def update_item_location(self, 
                             name: str, 
                             current_lab: str, 
                             current_location: str, 
                             new_lab: str, 
                             new_location: str) -> bool:

        current_loc_id = self.retrieve_loc_id(current_lab, current_location)
        new_loc_id = self.retrieve_loc_id(new_lab, new_location)
        if current_loc_id == -1:
            return False
        if new_loc_id == -1:
            return False

        query = QSqlQuery()
        query.prepare(self.UPDATE_ITEM_LOCATION_SQL)
        query.addBindValue(new_loc_id)
        query.addBindValue(name)
        query.addBindValue(current_loc_id)
        if not query.exec():
            print(query.lastError().text())
            return False
        else:
            return True
    
    def move_item(self,
                  name: str,
                  stock_type: str,
                  current_lab: str,
                  current_location: str,
                  new_lab: str,
                  new_location: str,
                  qty: float) -> bool:
        current_loc_id = self.retrieve_loc_id(current_lab, current_location)
        new_loc_id = self.retrieve_loc_id(new_lab, new_location)
        if current_loc_id == -1:
            return False
        if new_loc_id == -1:
            return False

        self.remove_qty_from_item(name, current_lab, current_location, qty)
        if self.check_item_location(name, new_lab, new_location):
            if not self.add_qty_to_item(name, new_lab, new_location, qty):
                return False
        else:
            if not self.add_entry(stock_type, name, qty, new_location, new_lab):
                return False

        return True

    def update_qty(self,
                   name: str,
                   lab: str,
                   location: str,
                   qty: float) -> bool:

        loc_id = self.retrieve_loc_id(lab, location)
        if loc_id == -1:
            return False

        query = QSqlQuery()
        query.prepare(self.UPDATE_QTY_SQL)
        query.addBindValue(qty)
        query.addBindValue(name)
        query.addBindValue(loc_id)
        if not query.exec():
            print(query.lastError().text())
            return False

        return True
    
    def add_qty_to_item(self, 
                        name: str, 
                        lab: str, 
                        location: str, 
                        qty: float) -> bool:

        loc_id = self.retrieve_loc_id(lab, location)
        if loc_id == -1:
            return False

        query = QSqlQuery()
        query.prepare(self.UPDATE_ITEM_ADD_QTY_SQL)
        query.addBindValue(qty)
        query.addBindValue(name)
        query.addBindValue(loc_id)
        if not query.exec():
            print(query.lastError().text())
            return False
        else:
            return True

    def remove_qty_from_item(self,
                             name: str,
                             lab: str,
                             location: str,
                             qty: float) -> bool:
        loc_id = self.retrieve_loc_id(lab, location)
        if loc_id == -1:
            return False

        query = QSqlQuery()
        query.prepare(self.UPDATE_ITEM_REMOVE_QTY_SQL)
        query.addBindValue(qty)
        query.addBindValue(name)
        query.addBindValue(loc_id)
        if not query.exec():
            print(query.lastError().text())
            return False
        else:
            return True

    def delete_item(self, name: str, lab: str, location: str) -> bool:
        loc_id = self.retrieve_loc_id(lab, location)
        if loc_id == -1:
            return False

        query = QSqlQuery()
        query.prepare(self.DELETE_ITEM_SQL)
        query.addBindValue(name)
        query.addBindValue(loc_id)
        if not query.exec():
            print(query.lastError().text())
            return False
        else:
            return True
        


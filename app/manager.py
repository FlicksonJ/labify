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

        self.INSERT_STOCK_TYPE_SQL = """
        INSERT OR IGNORE INTO StockType (type)
        VALUES ('glassware'), ('chemical'), ('equipment')
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
        self.RETRIEVE_LAB_ID_SQL = """
        SELECT lab_id FROM Labs WHERE name = (?)
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
        WHERE StockType.type = '{stock_type}'
        """

        self.create_tables()
        
        # @TODO: Change it and create locations at Installation
        locations = {
            "Lab1": ["A", "B", "C"],
            "Lab2": ["A", "B", "C", "D"],
        }
        lab_names = list(locations.keys())
        self.insert_labs(lab_names)
        self.insert_locations(locations)


    def create_tables(self):
        query = QSqlQuery()
        query.exec(self.ITEMS_TABLE_SQL)
        query.exec(self.STOCK_TYPE_TABLE_SQL)
        query.exec(self.LOCATIONS_TABLE_SQL)
        query.exec(self.LABS_TABLE_SQL)

        # Enter default stocktype values
        query.exec(self.INSERT_STOCK_TYPE_SQL)

    def insert_labs(self, lab_names: list[str]):
        query = QSqlQuery()
        for lab in lab_names:
            query.prepare(self.INSERT_LABS_SQL)
            query.addBindValue(lab)
            query.exec()

    def insert_locations(self, locations: dict[str, list[str]]):
        query = QSqlQuery()
        for lab_name, shelves in locations.items():
            # Retrieve `lab_id` for the current lab
            lab_id_query = QSqlQuery()
            lab_id_query.prepare(self.RETRIEVE_LAB_ID_SQL)
            lab_id_query.addBindValue(lab_name)
            lab_id_query.exec()
            lab_id_query.next()
            lab_id = lab_id_query.value(0)

            # Insert locations for the current lab
            for shelf in shelves:
                # location_name = f"{lab_name}_{shelf}"
                query.prepare(self.INSERT_LOCATIONS_SQL)
                query.addBindValue(shelf)
                query.addBindValue(lab_id)
                query.exec()

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


    def add_entry(self, stock_type: str, name: str, qty: str, location: str, lab: str):
        query = QSqlQuery()

        # insert new item into the Items table
        query.prepare(self.INSERT_ITEM_SQL)
        query.addBindValue(name)
        query.addBindValue(qty)
        query.addBindValue(stock_type)
        query.addBindValue(location)
        query.addBindValue(lab)
        query.exec()


    def retrieve_item_info(self, stock_type: str) -> QSqlQueryModel | None:
        model = QSqlQueryModel()
        model.setQuery(self.RETRIEVE_ITEM_INFO_SQL.format(stock_type=stock_type), self.db)

        return model




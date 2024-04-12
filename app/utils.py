import os
import sys
import bcrypt  # Import secure hashing library
from itsdangerous import URLSafeTimedSerializer

from PySide6.QtWidgets import QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlQuery

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
            if not self.create_database():
                QMessageBox.critical(None, "Error", "Failed to create database file")
                sys.exit(1)

        if not self.db.open():
            QMessageBox.critical(None, "Error", f"Failed to open database: {self.db.lastError().text()}")
            sys.exit(1)

        self.db.open()

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
            SELECT * FROM users WHERE username = ?
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
            name VARCHAR(255) UNIQUE,
            qty REAL,
            stock_id INTEGER,
            FOREIGN KEY (stock_id) REFERENCES StockType(stock_id)
        )"""

        self.STOCK_TYPE_TABLE_SQL = """
        CREATE TABLE IF NOT EXISTS StockType (
            stock_id INTEGER PRIMARY KEY,
            type VARCHAR(255) UNIQUE
        )"""

        self.LOCATIONS_TABLE_SQL = """
        CREATE TABLE IF NOT EXISTS Locations (
            loc_id INTEGER PRIMARY KEY,
            name VARCHAR(255) UNIQUE,
            lab_id INTEGER,
            FOREIGN KEY (lab_id) REFERENCES Labs(lab_id)
        )"""

        self.LABS_TABLE_SQL = """        
        CREATE TABLE IF NOT EXISTS Labs (
            lab_id INTEGER PRIMARY KEY,
            name VARCHAR(255) UNIQUE
        )"""

        self.ITEM_LOCATION_TABLE_SQL = """
        CREATE TABLE IF NOT EXISTS ItemLocation (
            id INTEGER PRIMARY KEY,
            item_id INTEGER,
            location_id INTEGER,
            FOREIGN KEY (item_id) REFERENCES Items(item_id),
            FOREIGN KEY (location_id) REFERENCES Locations(loc_id)
        )
        """
        self.INSERT_STOCK_TYPE_SQL = """
        INSERT OR IGNORE INTO StockType (type)
        VALUES ('glassware'), ('chemical'), ('equipment')
        """
        self.INSERT_ITEM_SQL = """
        INSERT INTO Items (name, qty, stock_id)
        SELECT ?, ?, stock_id FROM StockType WHERE type = ?
        """
        self.INSERT_ITEM_LOCATION_SQL = """
        INSERT INTO ItemLocation (item_id, location_id)
        SELECT ?, loc_id FROM Locations
        WHERE name = ?
        AND lab_id = (SELECT lab_id FROM Labs WHERE name = ?)
        """
        self.RETRIEVE_ITEM_INFO_SQL = """
        SELECT Items.name AS name, Items.qty, Location.name AS location, Labs.name AS lab
        FROM ItemLocation
        INNER JOIN Items ON ItemLocation.item_id = Items.item_id
        INNER JOIN Locations ON ItemLocation.location_id = Locations.loc_id
        INNER JOIN Labs ON Location.lab_id = Labs.lab_id
        INNER JOIN StockType ON Items.stock_id = StockType.stock_id
        WHERE StockType.type = ?
        """

        self.create_tables()

    def create_tables(self):
        query = QSqlQuery()
        query.exec(self.ITEMS_TABLE_SQL)
        query.exec(self.STOCK_TYPE_TABLE_SQL)
        query.exec(self.LOCATIONS_TABLE_SQL)
        query.exec(self.LABS_TABLE_SQL)
        query.exec(self.ITEM_LOCATION_TABLE_SQL)

        # Enter default stocktype values
        query.exec(self.INSERT_STOCK_TYPE_SQL)

    def add_entry(self, stock_type: str, name: str, qty: str, location: str, lab: str):
        query = QSqlQuery()

        # insert new item into the Items table
        query.prepare(self.INSERT_ITEM_SQL)
        query.addBindValue(name)
        query.addBindValue(qty)
        query.addBindValue(stock_type)
        query.exec()
        item_id = query.lastInsertId()

        # Update the ItemLocation table
        query.prepare(self.INSERT_ITEM_LOCATION_SQL)
        query.addBindValue(item_id)
        query.addBindValue(location)
        query.addBindValue(lab)
        query.exec()


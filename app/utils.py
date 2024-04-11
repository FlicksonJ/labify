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

        self.account_manager = AccountManager(self.db)
        self.inventory_manager = InventoryManager(self.db)

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

        self.ICMS_LOGIN_SQL = """
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
        self.SEARCH_USERNAME = """
            SELECT * FROM users WHERE username = ?
            """

        self.create_table()
        # Create test admin user
        # @TODO: Change it and create admin user at installation
        self.create_admin("admin", "admin@123")


    def create_table(self):
        query = QSqlQuery()
        query.exec(self.ICMS_LOGIN_SQL)

    def account_exists(self, username):
        query = QSqlQuery()
        query.prepare(self.SEARCH_USERNAME)
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

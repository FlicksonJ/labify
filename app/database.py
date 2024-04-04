import bcrypt  # Import secure hashing library
from itsdangerous import URLSafeTimedSerializer
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

serializer = URLSafeTimedSerializer("DrrOEWvcDHPycjnfsRv-r1WMWqObSXSsRmpnf438Rbk")

ICMS_LOGIN_SQL = """
    create table if not exists users (
        uid integer primary key autoincrement,
        username text unique not null,
        hashed_password text not null,
        user_type text not null
    )
    """
INSERT_ADMIN_SQL = """
    INSERT INTO users (username, hashed_password, user_type) 
    VALUES (?, ?, "admin")
    """
INSERT_USER_SQL = """
    INSERT INTO users (username, hashed_password, user_type) 
    VALUES (?, ?, "user")
    """

def check(func, *args):
    if not func(*args):
        raise ValueError(func.__self__.lastError())

def hash_pw(password):
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

def verify_pw(hashed_password, password_to_check):
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



def add_user(q, user, password):
    # Securely hash password
    hashed_password = hash_pw(password)

    q.addBindValue(user)
    q.addBindValue(hashed_password)
    q.exec()

def init_db():
    """
    init_db()
    initialize the database
    If tables "icms_login" are already in the database, do nothing.
    Return value: db or raises ValueError
    The error value is the QtSql error instance.
    """
    
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("app/database/app.db")

    check(db.open)

    q = QSqlQuery()
    check(q.exec, ICMS_LOGIN_SQL)

    # Create test admin user
    # @TODO: Change it and create admin user at installation
    check(q.prepare, INSERT_ADMIN_SQL)
    add_user(q, "admin", "admin@123")

    return db

from PyQt6.QtWidgets import (QApplication, QWidget,
                             QVBoxLayout, QHBoxLayout, QLabel,
                             QLineEdit, QPushButton, QMessageBox)
from PyQt6.QtSql import QSqlQuery

from app import database

class LoginWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.db = database.init_db()
        self.main_window = main_window
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Login")
        self.setGeometry(300, 300, 300, 150)

        layout = QVBoxLayout(self)

        labels = {}
        self.inputs = {}

        labels["Username"] = QLabel("Username:")
        self.inputs["Username"] = QLineEdit()
        labels["Password"] = QLabel("Password:")
        self.inputs["Password"] = QLineEdit()        
        self.inputs["Password"].setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(labels["Username"])
        layout.addWidget(self.inputs["Username"])
        layout.addWidget(labels["Password"])
        layout.addWidget(self.inputs["Password"])

        button_layout = QHBoxLayout()
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.handle_login)

        button_layout.addWidget(login_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def handle_login(self):
        username = self.inputs["Username"].text()
        password = self.inputs["Password"].text()

        query = QSqlQuery()
        query.prepare("SELECT * FROM users WHERE username = :username")
        query.bindValue(":username", username)

        if not query.exec():
            QMessageBox.critical(self, "Error", "Failed to execute query!")

        if query.first():
            if (hashed_password := query.value("hashed_password")) and database.verify_pw(hashed_password, password):
                user_type = query.value("user_type")
                self.close()
                self.main_window.show_home_screen(username, user_type)

            else:
                QMessageBox.warning(self, "Login", "Invalid password!")
        else:
            QMessageBox.warning(self, "Login", "Invalid username!")

    def create_account(self):
        # Implement logic to create a new user account (restricted to admin)
        # You can open a new window for account creation
        QMessageBox.information(self, "Create Account", "Feature not yet implemented!")
    


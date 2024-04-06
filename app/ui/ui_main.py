# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1600, 900))
        MainWindow.setMaximumSize(QSize(1600, 900))
        MainWindow.setStyleSheet(u"* {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#login_page {\n"
"	background-image: url(:/images/images/bg.jpeg);\n"
"	background-size: cover;\n"
"}\n"
"\n"
"#login_page QLabel {\n"
"	margin-left: 40px;\n"
"	font-size: 15pt\n"
"}\n"
"\n"
"#login_page QLineEdit, QPushButton {\n"
"	height: 70px;\n"
"	margin-left: 40px;\n"
"	margin-right: 40px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#login_page QLineEdit {\n"
"	background: rgb(255, 255, 255);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	font-size: 18pt;\n"
"	color: black;\n"
"}\n"
"\n"
"#login_page QPushButton {\n"
"	background: rgb(0, 159, 161);\n"
"	font-size: 23pt;\n"
"	margin-top: 40px;\n"
"}\n"
"\n"
"#header {\n"
"	background: rgb(52, 62, 162);\n"
"}\n"
"\n"
"#mic_logo {\n"
"	max-width: 75px;\n"
"	max-height: 75px;\n"
"}\n"
"\n"
"#labify_logo {\n"
"	margin-left: 20px;\n"
"	max-width: 100px;\n"
"	min-height: 95px;\n"
"}\n"
"\n"
"#header QPus"
                        "hButton {\n"
"	background: rgb(255, 255, 255);\n"
"	margin: 0;\n"
"	width: 100px;\n"
"	margin-top: 10px;\n"
"	margin-bottom: 10px;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"#create_user_button {\n"
"	color: rgb(0, 159, 161);\n"
"}\n"
"\n"
"#logout_button {\n"
"	color: rgb(224, 27, 36)\n"
"}\n"
"\n"
"#header_username_label {\n"
"	background: #fff;\n"
"	color: rgb(52, 62, 162);\n"
"	font-size: 18pt;\n"
"	padding: 5px 40px 5px 40px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#footer {\n"
"	background: rgb(0, 159, 161);\n"
"}\n"
"\n"
"#footer QLabel {\n"
"	margin: 0;\n"
"}\n"
"\n"
"#create_user_page {\n"
"	background: #fff;\n"
"}\n"
"\n"
"#create_user_form QLabel {\n"
"	color: rgb(52, 62, 162);\n"
"	font-size: 15pt;\n"
"	max-height: 20px;\n"
"	margin-top: 10px;\n"
"	padding-top:30px\n"
"}\n"
"\n"
"#create_user_form QLineEdit {\n"
"	border: 1px solid;\n"
"	min-height: 80px;\n"
"	border-radius: 5px;\n"
"	border-color: rgb(52, 62, 162);\n"
"	color: black;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"}\n"
"\n"
"#"
                        "create_account_button {\n"
"	background: rgb(0, 159, 161);\n"
"	font-size: 25pt;\n"
"	margin: 0;\n"
"	margin-right: 40px;\n"
"}\n"
"\n"
"#cancel_button {\n"
"	border: 1px solid;\n"
"	border-color: rgb(224, 27, 36);\n"
"	color: rgb(224, 27, 36);\n"
"	font-size: 25pt;\n"
"	margin: 0;\n"
"	padding: 0px 50px 0px 50px\n"
"}\n"
"\n"
"#home_page {\n"
"	background: #fff;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1600, 900))
        self.stackedWidget.setStyleSheet(u"")
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.verticalLayoutWidget = QWidget(self.login_page)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(880, 190, 571, 401))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.username_label = QLabel(self.verticalLayoutWidget)
        self.username_label.setObjectName(u"username_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.username_label.sizePolicy().hasHeightForWidth())
        self.username_label.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.username_label)

        self.username_input = QLineEdit(self.verticalLayoutWidget)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setMinimumSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.username_input)

        self.password_label = QLabel(self.verticalLayoutWidget)
        self.password_label.setObjectName(u"password_label")
        sizePolicy1.setHeightForWidth(self.password_label.sizePolicy().hasHeightForWidth())
        self.password_label.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.password_label)

        self.password_input = QLineEdit(self.verticalLayoutWidget)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password_input)

        self.login_button = QPushButton(self.verticalLayoutWidget)
        self.login_button.setObjectName(u"login_button")

        self.verticalLayout.addWidget(self.login_button)

        self.stackedWidget.addWidget(self.login_page)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"")
        self.layoutWidget = QWidget(self.home_page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1602, 899))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.layoutWidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(1600, 100))
        self.header.setMaximumSize(QSize(1600, 120))
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.mic_logo = QLabel(self.header)
        self.mic_logo.setObjectName(u"mic_logo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mic_logo.sizePolicy().hasHeightForWidth())
        self.mic_logo.setSizePolicy(sizePolicy2)
        self.mic_logo.setMinimumSize(QSize(0, 0))
        self.mic_logo.setMaximumSize(QSize(75, 75))
        self.mic_logo.setPixmap(QPixmap(u":/images/images/mic.jpeg"))
        self.mic_logo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.mic_logo)

        self.labify_logo = QLabel(self.header)
        self.labify_logo.setObjectName(u"labify_logo")
        sizePolicy2.setHeightForWidth(self.labify_logo.sizePolicy().hasHeightForWidth())
        self.labify_logo.setSizePolicy(sizePolicy2)
        self.labify_logo.setPixmap(QPixmap(u":/images/images/labify.jpeg"))
        self.labify_logo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.labify_logo)

        self.header_title = QLabel(self.header)
        self.header_title.setObjectName(u"header_title")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(6)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.header_title.sizePolicy().hasHeightForWidth())
        self.header_title.setSizePolicy(sizePolicy3)
        self.header_title.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setPointSize(23)
        font.setBold(False)
        self.header_title.setFont(font)
        self.header_title.setScaledContents(False)
        self.header_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.header_title)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetFixedSize)
        self.header_username_label = QLabel(self.header)
        self.header_username_label.setObjectName(u"header_username_label")
        self.header_username_label.setMaximumSize(QSize(200, 16777215))
        self.header_username_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.header_username_label)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.create_user_button = QPushButton(self.header)
        self.create_user_button.setObjectName(u"create_user_button")
        self.create_user_button.setMaximumSize(QSize(1688888, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        self.create_user_button.setFont(font1)
        self.create_user_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.create_user_button)

        self.logout_button = QPushButton(self.header)
        self.logout_button.setObjectName(u"logout_button")
        self.logout_button.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.logout_button.setFont(font2)
        self.logout_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.logout_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.header)

        self.stackedWidget_2 = QStackedWidget(self.layoutWidget)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(3, 0))
        self.create_user_page = QWidget()
        self.create_user_page.setObjectName(u"create_user_page")
        self.widget = QWidget(self.create_user_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, -10, 1601, 751))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(3)
        sizePolicy4.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy4)
        self.widget1.setStyleSheet(u"")
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, -50, 670, 800))
        self.label_2.setLineWidth(0)
        self.label_2.setPixmap(QPixmap(u":/images/images/create_user.jpeg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.widget1)

        self.create_user_form = QWidget(self.widget)
        self.create_user_form.setObjectName(u"create_user_form")
        sizePolicy4.setHeightForWidth(self.create_user_form.sizePolicy().hasHeightForWidth())
        self.create_user_form.setSizePolicy(sizePolicy4)
        self.verticalLayoutWidget_2 = QWidget(self.create_user_form)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(80, 70, 561, 611))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cu_username_label = QLabel(self.verticalLayoutWidget_2)
        self.cu_username_label.setObjectName(u"cu_username_label")

        self.verticalLayout_3.addWidget(self.cu_username_label)

        self.cu_username_input = QLineEdit(self.verticalLayoutWidget_2)
        self.cu_username_input.setObjectName(u"cu_username_input")
        font3 = QFont()
        font3.setPointSize(21)
        self.cu_username_input.setFont(font3)
        self.cu_username_input.setFrame(True)

        self.verticalLayout_3.addWidget(self.cu_username_input)

        self.cu_password_label = QLabel(self.verticalLayoutWidget_2)
        self.cu_password_label.setObjectName(u"cu_password_label")

        self.verticalLayout_3.addWidget(self.cu_password_label)

        self.cu_password_input = QLineEdit(self.verticalLayoutWidget_2)
        self.cu_password_input.setObjectName(u"cu_password_input")
        self.cu_password_input.setFont(font3)
        self.cu_password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.cu_password_input)

        self.cu_confirm_password_label = QLabel(self.verticalLayoutWidget_2)
        self.cu_confirm_password_label.setObjectName(u"cu_confirm_password_label")

        self.verticalLayout_3.addWidget(self.cu_confirm_password_label)

        self.cu_confirm_password_input = QLineEdit(self.verticalLayoutWidget_2)
        self.cu_confirm_password_input.setObjectName(u"cu_confirm_password_input")
        self.cu_confirm_password_input.setFont(font3)
        self.cu_confirm_password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.cu_confirm_password_input)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.create_account_button = QPushButton(self.verticalLayoutWidget_2)
        self.create_account_button.setObjectName(u"create_account_button")
        self.create_account_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.create_account_button)

        self.cancel_button = QPushButton(self.verticalLayoutWidget_2)
        self.cancel_button.setObjectName(u"cancel_button")
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)
        self.cancel_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.cancel_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_3.addWidget(self.create_user_form)

        self.stackedWidget_2.addWidget(self.create_user_page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_2.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget_2)

        self.footer = QWidget(self.layoutWidget)
        self.footer.setObjectName(u"footer")
        self.footer.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.footer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.footer)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setFont(font1)
        self.label.setAutoFillBackground(False)
        self.label.setLineWidth(0)
        self.label.setTextFormat(Qt.RichText)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.footer)

        self.stackedWidget.addWidget(self.home_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.cancel_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.username_label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.password_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"SIGN IN", None))
        self.mic_logo.setText("")
        self.labify_logo.setText("")
        self.header_title.setText(QCoreApplication.translate("MainWindow", u"CHEMISTRY INVENTORY MANAGEMENT SOFTWARE", None))
        self.header_username_label.setText(QCoreApplication.translate("MainWindow", u"ADMIN", None))
        self.create_user_button.setText(QCoreApplication.translate("MainWindow", u"Create User", None))
        self.logout_button.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_2.setText("")
        self.cu_username_label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.cu_password_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.cu_confirm_password_label.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.create_account_button.setText(QCoreApplication.translate("MainWindow", u"CREATE ACCOUNT", None))
        self.cancel_button.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"&copy; 2024, Dept. of CS", None))
    # retranslateUi


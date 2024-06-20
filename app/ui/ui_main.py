# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QButtonGroup,
    QComboBox, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableView,
    QVBoxLayout, QWidget)
from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 0))
        MainWindow.setMaximumSize(QSize(1602, 900))
        MainWindow.setStyleSheet(u"* {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"\n"
"/* Scrollbar */\n"
"\n"
"QScrollBar:vertical {\n"
"	border:none;\n"
"	background-color: rgb(251, 254, 255);\n"
"	margin:15px 0 15px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: rgba(0, 159, 161,50%);\n"
"	border-radius: 5px;\n"
"	min-height:30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: rgba(0, 159, 161,100%);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin"
                        ";\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"/* -- */\n"
"\n"
"#login_page {\n"
"	background-image: url(:/images/images/bg.jpeg);\n"
"	/*background-size: cover;*/\n"
"}\n"
"\n"
"#login_page QLabel {\n"
"	font-size: 15pt;\n"
"}\n"
"\n"
"#login_page QLineEdit, QPushButton {\n"
"	height: 70px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#login_page QLineEdit {\n"
"	background: rgb(255, 255, 255);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	font-size: 18pt;\n"
"	color: rgb(0, 159, 161);\n"
"}\n"
"\n"
"#login_page QLineEdit:hover {\n"
"	border: 3px solid rgb(0, 159, 161);\n"
"}\n"
"\n"
"#login_page QPushButton {\n"
"	background: rgb(0, 159, 161);\n"
"	font-size: 23pt;\n"
"	margin-top: 40px;\n"
"}\n"
"\n"
"#login_page QPushButton:hover{\n"
"	background: rgb(255, 255, 255);\n"
"    color: rgb(0, 159, 161);\n"
"}\n"
"\n"
"#header {\n"
"	"
                        "background: rgb(52, 62, 162);\n"
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
"#header QPushButton {\n"
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
"#create_user_button:hover {\n"
"	background-color: rgb(0, 159, 161);\n"
"	color: #fff;\n"
"}\n"
"\n"
"#logout_button {\n"
"	color: rgb(224, 27, 36)\n"
"}\n"
"\n"
"#logout_button:hover {\n"
"	background-color: rgb(224, 27, 36);\n"
"	color:#fff;\n"
"}\n"
"\n"
"#alerts_button:hover,\n"
"#transaction_history_button:hover,\n"
"#transaction_history_button_2:hover {\n"
"	background-color: rgb(52, 62, 162);\n"
"	color:#fff;\n"
"}\n"
"\n"
"#header_username_label {\n"
"	background: #fff;\n"
"	color: rgb(52, 62, 162);\n"
"	font-size: 18pt;\n"
"	padding: 5px 40px "
                        "5px 40px;\n"
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
"	color:  rgb(0, 159, 161);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"}\n"
"\n"
"#create_user_form QLineEdit:hover {\n"
"	border: 3px solid;\n"
"	border-color: rgb(0, 159, 161);\n"
"}\n"
"\n"
"#create_account_button {\n"
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
"	padding: 0"
                        "px 50px 0px 50px\n"
"}\n"
"\n"
"#create_account_button:hover{\n"
"	background-color: rgb(52, 62, 162);\n"
"	color: #fff;\n"
"}\n"
"\n"
"#cancel_button:hover {\n"
"	color:#fff;\n"
"	background-color: rgb(224, 27, 36);\n"
"}\n"
"\n"
"#home_page {\n"
"	background: #fff;\n"
"}\n"
"\n"
"#inventory_header,\n"
"#inventory_header_2 {\n"
"	background: rgb(0, 159, 161)\n"
"}\n"
"\n"
"#inventory_header QPushButton,\n"
"#inventory_header_2 QPushButton {\n"
"	background: rgb(251, 254, 255);\n"
"	color: rgb(0, 159, 161);\n"
"	font-size: 15pt;;\n"
"	width: 150px;\n"
"	height: 40px;\n"
"	margin: 0;\n"
"}\n"
"\n"
"/*combo box location and lab*/\n"
"\n"
"#item_location_input,\n"
"#item_lab_input\n"
"{\n"
"	color: rgb(0, 159, 161);\n"
"}\n"
"\n"
"#item_location_input:hover,\n"
"#item_lab_input:hover\n"
"{\n"
"	color: rgb(52, 62, 162);\n"
"}\n"
"\n"
"#item_lab_input::drop-down\n"
"{\n"
"	border: 0px;\n"
"}\n"
"\n"
"#item_lab_input::down-arrow\n"
"{\n"
"	image: url(:/icon/images/down-arrow.ico);\n"
"	width: 15px;\n"
"	height: 15px"
                        ";\n"
"	margin-right: 20px\n"
"}\n"
"\n"
"#item_lab_input:on\n"
"{\n"
"	border: 2px solid rgba(0, 159, 161, 10%);\n"
"}\n"
"\n"
"#item_lab_input QListView\n"
"{\n"
"	font-size: 15pt;\n"
"	border: 1px solid rgba(0, 0, 0, 10%);\n"
"	padding: 3px;\n"
"	background-color: rgb(251, 254, 255);\n"
"	outline: 0px;\n"
"}\n"
"\n"
"#item_lab_input QListView::item\n"
"{\n"
"	padding-left: 10px;\n"
"	background-color: rgb(251, 254, 255);\n"
"}\n"
"\n"
"#item_lab_input QListView::item:hover\n"
"{\n"
"	background: rgb(0, 159, 161);\n"
"	color: rgb(251, 254, 255);\n"
"}\n"
"\n"
"#item_lab_input QListView::item:selected\n"
"{\n"
"	background: rgb(0, 159, 161);\n"
"	color: rgb(251, 254, 255);\n"
"}\n"
"\n"
"#item_lab_input QListView\n"
"{\n"
"	color: rgb(0, 159, 161);\n"
"}\n"
"\n"
"/*----*/\n"
"\n"
"#item_name_input:hover,\n"
"#item_qty_input:hover {\n"
"	border: 2px solid rgb(0, 159, 161);\n"
"}\n"
"\n"
"/* combo box */\n"
"\n"
"#inventory_type_input {\n"
"	background: rgb(251, 254, 255);\n"
"	color: rgb(0, 159, 161);\n"
"	heig"
                        "ht: 40px;\n"
"	border-radius: 5px;\n"
"	font-size: 18pt;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"#inventory_type_input:hover {\n"
"	color: rgb(52, 62, 162);\n"
"}\n"
"\n"
"#inventory_type_input::drop-down {\n"
"	border: 0px;\n"
"}\n"
"\n"
"#inventory_type_input::down-arrow {\n"
"	image: url(:/icon/images/down-arrow.ico);\n"
"	width: 30px;\n"
"	height: 30px;\n"
"	margin-right: 20px\n"
"}\n"
"\n"
"#inventory_type_input:on {\n"
"	border: 2px solid rgba(0, 159, 161, 10%);\n"
"}\n"
"\n"
"#inventory_type_input QListView{\n"
"	font-size: 15pt;\n"
"	border: 1px solid rgba(0, 0, 0, 10%);\n"
"	padding: 3px;\n"
"	background-color: rgb(251, 254, 255);\n"
"	outline: 0px;\n"
"}\n"
"\n"
"#inventory_type_input QListView::item {\n"
"	padding-left: 10px;\n"
"	background-color: rgb(251, 254, 255);\n"
"}\n"
"\n"
"#inventory_type_input QListView::item:hover {\n"
"	background: rgb(0, 159, 161);\n"
"	color: rgb(251, 254, 255);\n"
"}\n"
"\n"
"#inventory_type_input QListView::item:selected {\n"
"	background: rgb(0, 159, 161);\n"
"	col"
                        "or: rgb(251, 254, 255);\n"
"}\n"
"\n"
"#inventory_type_input QListView {\n"
"	color: rgb(0, 159, 161);\n"
"}\n"
"\n"
"/* -- */\n"
"\n"
"#add_entry_button, \n"
"#update_entry_button,\n"
"#restock_entry_button,\n"
"#move_entry_button,\n"
"#delete_entry_button {\n"
"	background: rgb(52, 62, 162);\n"
"	margin: 0;\n"
"	font-size: 15pt;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"	border-radius: 0;\n"
"	height: 50px;\n"
"}\n"
"\n"
"#add_entry_button {\n"
"	border-top-left-radius: 5px ;\n"
"	border-top-right-radius: 5px ;\n"
"}\n"
"\n"
"#delete_entry_button {\n"
"	border-bottom-left-radius: 5px ;\n"
"	border-bottom-right-radius: 5px ;\n"
"}\n"
"\n"
"#add_entry_button:hover, \n"
"#update_entry_button:hover,\n"
"#restock_entry_button:hover,\n"
"#move_entry_button:hover,\n"
"#delete_entry_button:hover {\n"
"	background: rgb(0, 159, 161);\n"
"	color: #fff;\n"
"}\n"
"\n"
"#add_entry_button:checked, \n"
"#update_entry_button:checked,\n"
"#restock_entry_button:checked,\n"
"#move_entry_button:checked,\n"
"#delete_ent"
                        "ry_button:checked {\n"
"	background: #fff;\n"
"	color: rgb(52, 62, 162);\n"
"}\n"
"\n"
"#add_entry_add_button:hover{\n"
"	background: rgb(0, 159, 161);\n"
"	color: #fff;\n"
"}\n"
"\n"
"#add_entry_cancel_button:hover,\n"
"#delete_entry_cancel_button:hover,\n"
"#delete_entry_delete_button:hover,\n"
"#update_entry_cancel_button:hover,\n"
"#move_entry_cancel_button:hover,\n"
"#restock_entry_cancel_button:hover,\n"
"#go_back_button:hover {\n"
"	background: rgb(224, 27, 36);\n"
"	color:#fff;\n"
"}\n"
"\n"
"#search_bar_container,\n"
"#search_bar_container_2,\n"
"#search_bar_container_3,\n"
"#search_bar_container_4,\n"
"#search_bar_container_5,\n"
"#search_bar_container_6 {\n"
"	border: 1px solid rgb(0, 159, 161);\n"
"	border-radius: 15px;\n"
"	margin: 1px;\n"
"}\n"
"\n"
"#search_bar_container:hover,\n"
"#search_bar_container_2:hover,\n"
"#search_bar_container_3:hover,\n"
"#search_bar_container_4:hover,\n"
"#search_bar_container_5:hover,\n"
"#search_bar_container_6:hover {\n"
"	border: 2px solid rgb(0, 159, 161);\n"
""
                        "}\n"
"\n"
"#search_button,\n"
"#search_bar_input,\n"
"#update_entry_search_button,\n"
"#update_entry_search_button_2,\n"
"#restock_entry_search_button,\n"
"#move_entry_search_button,\n"
"#update_entry_search_input,\n"
"#update_entry_search_input_2,\n"
"#move_entry_search_input,\n"
"#restock_entry_search_input,\n"
"#delete_entry_search_button,\n"
"#delete_entry_search_input {\n"
"	color: rgb(0, 159, 161);\n"
"	font-size: 18pt;\n"
"}\n"
"\n"
"/* Fix search button overflow error*/\n"
"#delete_entry_search_button,\n"
"#restock_entry_search_button {\n"
"	margin-right: 20px;\n"
"}\n"
"\n"
"#search_button:hover,\n"
"#search_bar_input:hover,\n"
"#update_entry_search_button:hover,\n"
"#update_entry_search_button_2:hover,\n"
"#restock_entry_search_button:hover,\n"
"#update_entry_search_input:hover,\n"
"#update_entry_search_input_2:hover,\n"
"#move_entry_search_input:hover,\n"
"#restock_entry_search_button:hover,\n"
"#delete_entry_search_button:hover,\n"
"#delete_entry_search_input:hover {\n"
"	color: rgb(52, 62, 162);\n"
""
                        "}\n"
"\n"
"#search_bar_input,\n"
"#update_entry_search_input,\n"
"#update_entry_search_input_2,\n"
"#restock_entry_search_input,\n"
"#move_entry_search_input,\n"
"#delete_entry_search_input {\n"
"	padding-left: 20px;\n"
"}\n"
"\n"
"#add_entry_table_header QLabel {\n"
"	background: rgb(0, 159, 161);\n"
"	font-size: 18pt;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	margin: 0;\n"
"	min-height: 40px;\n"
"}\n"
"\n"
"#add_entry_add_button,\n"
"#add_entry_cancel_button,\n"
"#update_entry_cancel_button,\n"
"#update_entry_cancel_button_2,\n"
"#restock_entry_cancel_button,\n"
"#move_entry_cancel_button,\n"
"#delete_entry_delete_button,\n"
"#delete_entry_cancel_button,\n"
"#go_back_button {\n"
"	border: 1px solid;\n"
"	margin: 0;\n"
"	font-size: 18pt;\n"
"	height: 40px;\n"
"	width: 100px;\n"
"	margin-left: 20px;\n"
"}\n"
"\n"
"#add_entry_add_button {\n"
"	color: rgb(0, 159, 161);\n"
"	border-color: rgb(0, 159, 161);\n"
"}\n"
"\n"
"#add_entry_cancel_button,\n"
"#update_entry_cancel_button,\n"
"#restock_entry_c"
                        "ancel_button,\n"
"#move_entry_cancel_button,\n"
"#delete_entry_delete_button,\n"
"#delete_entry_cancel_button,\n"
"#go_back_button {\n"
"	color: rgb(224, 27, 36);\n"
"	border-color: rgb(224, 27, 36);\n"
"}\n"
"\n"
"#add_entry_inputs QLineEdit,QComboBox {\n"
"	border: 1px solid rgb(0, 159, 161);\n"
"	height: 35px;\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"	font-size: 15pt;\n"
"	color: rgb(0, 159, 161);\n"
"}\n"
"\n"
"#update_entry_search_input,\n"
"#update_entry_search_input_2,\n"
"#delete_entry_search_input {\n"
"	max-width: 350px;\n"
"}\n"
"\n"
"#add_entry_list {\n"
"	padding-top: 20px;\n"
"	margin-bottom: 30px;\n"
"}\n"
"\n"
"/* Table Styling */\n"
"\n"
"QTableView {\n"
"	font-size: 20pt;\n"
"	alternate-background-color: rgb(209, 235, 236);\n"
"	border: none;\n"
"	gridline-color: rgb(0, 159, 161);\n"
"}\n"
"\n"
"QTableView QHeaderView {\n"
"	font-size: 20pt;\n"
"	border: none;\n"
"	gridline-color: rgb(0, 159, 161);\n"
"}\n"
"\n"
"QTableView QHeaderView::section {\n"
"	background: rgb(0, 159, 161"
                        ");\n"
"	color: #fff;\n"
"	font-size: 20pt;\n"
"	gridline-color: transparent;\n"
"}\n"
"\n"
"QTableView QHeaderView::section:selected {\n"
"	color: #fff;\n"
"	font-size: 20pt;\n"
"}\n"
"\n"
"QTableView QHeaderView::section:first {\n"
"    border-top-left-radius: 10px;\n"
"}\n"
"\n"
"QTableView QHeaderView::section:horizontal:last {\n"
"    border-top-right-radius: 10px;\n"
"}\n"
"\n"
"QTableView QHeaderView::section:vertical:last {\n"
"    border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"QTableView QHeaderView::section:vertical {\n"
"    width: 30px;\n"
"}\n"
"\n"
"QTableView::item {\n"
"	color: rgb(0, 159, 161);\n"
"	gridline-color: rgb(0, 159, 161);\n"
"	border: 1px solid rgb(0, 159, 161);\n"
"	min-width: 500px;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"	background-color:  rgb(21,117,118);\n"
"	color: #fff;\n"
"	selection-background-color: rgb(21,117,118);\n"
"}\n"
"\n"
"#label_13 {\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"\n"
"#label_9 {\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"\n"
"#label_14,#l"
                        "abel_15,#label_16,#label_17 {\n"
"	border-radius: 5px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_22 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.horizontalLayout_24 = QHBoxLayout(self.login_page)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, 200, 150, 200)
        self.horizontalSpacer_12 = QSpacerItem(100, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_12)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.username_label = QLabel(self.login_page)
        self.username_label.setObjectName(u"username_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.username_label.sizePolicy().hasHeightForWidth())
        self.username_label.setSizePolicy(sizePolicy1)
        self.username_label.setMaximumSize(QSize(592, 16777215))

        self.verticalLayout.addWidget(self.username_label)

        self.username_input = QLineEdit(self.login_page)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setMinimumSize(QSize(300, 0))
        self.username_input.setMaximumSize(QSize(592, 16777215))

        self.verticalLayout.addWidget(self.username_input)

        self.password_label = QLabel(self.login_page)
        self.password_label.setObjectName(u"password_label")
        sizePolicy1.setHeightForWidth(self.password_label.sizePolicy().hasHeightForWidth())
        self.password_label.setSizePolicy(sizePolicy1)
        self.password_label.setMaximumSize(QSize(592, 16777215))

        self.verticalLayout.addWidget(self.password_label)

        self.password_input = QLineEdit(self.login_page)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMinimumSize(QSize(300, 0))
        self.password_input.setMaximumSize(QSize(592, 16777215))
        self.password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password_input)

        self.login_button = QPushButton(self.login_page)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setMaximumSize(QSize(592, 16777215))
        self.login_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.login_button)


        self.horizontalLayout_23.addLayout(self.verticalLayout)

        self.horizontalLayout_23.setStretch(0, 7)
        self.horizontalLayout_23.setStretch(1, 5)

        self.horizontalLayout_24.addLayout(self.horizontalLayout_23)

        self.stackedWidget.addWidget(self.login_page)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"")
        self.verticalLayout_23 = QVBoxLayout(self.home_page)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.header = QWidget(self.home_page)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(1600, 100))
        self.header.setMaximumSize(QSize(1600, 120))
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.mic_logo = QLabel(self.header)
        self.mic_logo.setObjectName(u"mic_logo")
        sizePolicy.setHeightForWidth(self.mic_logo.sizePolicy().hasHeightForWidth())
        self.mic_logo.setSizePolicy(sizePolicy)
        self.mic_logo.setMinimumSize(QSize(0, 0))
        self.mic_logo.setMaximumSize(QSize(75, 75))
        self.mic_logo.setPixmap(QPixmap(u":/images/images/mic white.png"))
        self.mic_logo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.mic_logo)

        self.labify_logo = QLabel(self.header)
        self.labify_logo.setObjectName(u"labify_logo")
        sizePolicy.setHeightForWidth(self.labify_logo.sizePolicy().hasHeightForWidth())
        self.labify_logo.setSizePolicy(sizePolicy)
        self.labify_logo.setPixmap(QPixmap(u":/images/images/labify.jpeg"))
        self.labify_logo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.labify_logo)

        self.header_title = QLabel(self.header)
        self.header_title.setObjectName(u"header_title")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(6)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.header_title.sizePolicy().hasHeightForWidth())
        self.header_title.setSizePolicy(sizePolicy2)
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
        self.header_username_label.setMaximumSize(QSize(212, 16777215))
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

        self.stackedWidget_2 = QStackedWidget(self.home_page)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(3, 0))
        self.stackedWidget_2.setStyleSheet(u"")
        self.inventory_page = QWidget()
        self.inventory_page.setObjectName(u"inventory_page")
        self.verticalLayoutWidget_3 = QWidget(self.inventory_page)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 1601, 751))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.inventory_header = QWidget(self.verticalLayoutWidget_3)
        self.inventory_header.setObjectName(u"inventory_header")
        self.inventory_header.setMinimumSize(QSize(0, 90))
        self.layoutWidget = QWidget(self.inventory_header)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 0, 181, 101))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 10, 0, 10)
        self.time_label = QLabel(self.layoutWidget)
        self.time_label.setObjectName(u"time_label")
        font3 = QFont()
        font3.setPointSize(25)
        font3.setBold(True)
        self.time_label.setFont(font3)
        self.time_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.time_label)

        self.date_label = QLabel(self.layoutWidget)
        self.date_label.setObjectName(u"date_label")
        font4 = QFont()
        font4.setPointSize(21)
        font4.setWeight(QFont.Light)
        font4.setItalic(False)
        self.date_label.setFont(font4)
        self.date_label.setTextFormat(Qt.AutoText)
        self.date_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.date_label)

        self.layoutWidget1 = QWidget(self.inventory_header)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(370, 0, 411, 91))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_7.setSpacing(40)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.transaction_history_button = QPushButton(self.layoutWidget1)
        self.transaction_history_button.setObjectName(u"transaction_history_button")
        self.transaction_history_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.transaction_history_button)

        self.alerts_button = QPushButton(self.layoutWidget1)
        self.alerts_button.setObjectName(u"alerts_button")
        self.alerts_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.alerts_button)

        self.layoutWidget2 = QWidget(self.inventory_header)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(980, 0, 571, 91))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_8.setSpacing(40)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")
        font5 = QFont()
        font5.setPointSize(20)
        font5.setWeight(QFont.Light)
        self.label_3.setFont(font5)

        self.horizontalLayout_8.addWidget(self.label_3)

        self.inventory_type_input = QComboBox(self.layoutWidget2)
        self.inventory_type_input.addItem("")
        self.inventory_type_input.addItem("")
        self.inventory_type_input.addItem("")
        self.inventory_type_input.setObjectName(u"inventory_type_input")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.inventory_type_input.sizePolicy().hasHeightForWidth())
        self.inventory_type_input.setSizePolicy(sizePolicy3)
        self.inventory_type_input.setMinimumSize(QSize(0, 30))
        font6 = QFont()
        font6.setPointSize(18)
        self.inventory_type_input.setFont(font6)
        self.inventory_type_input.setCursor(QCursor(Qt.PointingHandCursor))
        self.inventory_type_input.setInsertPolicy(QComboBox.InsertAtBottom)
        self.inventory_type_input.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.inventory_type_input.setIconSize(QSize(16, 16))
        self.inventory_type_input.setFrame(False)

        self.horizontalLayout_8.addWidget(self.inventory_type_input)


        self.verticalLayout_4.addWidget(self.inventory_header)

        self.stackedWidget_3 = QStackedWidget(self.verticalLayoutWidget_3)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.inventory_page_default = QWidget()
        self.inventory_page_default.setObjectName(u"inventory_page_default")
        self.label_4 = QLabel(self.inventory_page_default)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 1600, 650))
        font7 = QFont()
        font7.setPointSize(25)
        self.label_4.setFont(font7)
        self.label_4.setStyleSheet(u"color: rgb(0, 159, 161)")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.stackedWidget_3.addWidget(self.inventory_page_default)
        self.transactions_page = QWidget()
        self.transactions_page.setObjectName(u"transactions_page")
        self.layoutWidget3 = QWidget(self.transactions_page)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(250, 110, 1311, 461))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget3)
        self.label_5.setObjectName(u"label_5")
        font8 = QFont()
        font8.setPointSize(25)
        font8.setWeight(QFont.Light)
        self.label_5.setFont(font8)
        self.label_5.setStyleSheet(u"color: rgb(0, 159, 161)")

        self.verticalLayout_7.addWidget(self.label_5)

        self.transactions_table = QTableView(self.layoutWidget3)
        self.transactions_table.setObjectName(u"transactions_table")
        self.transactions_table.setFrameShape(QFrame.NoFrame)
        self.transactions_table.setFrameShadow(QFrame.Plain)
        self.transactions_table.setLineWidth(0)
        self.transactions_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.transactions_table.setAlternatingRowColors(True)
        self.transactions_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.transactions_table.setShowGrid(False)
        self.transactions_table.setSortingEnabled(True)
        self.transactions_table.setCornerButtonEnabled(False)
        self.transactions_table.horizontalHeader().setCascadingSectionResizes(True)
        self.transactions_table.horizontalHeader().setMinimumSectionSize(100)
        self.transactions_table.horizontalHeader().setDefaultSectionSize(100)
        self.transactions_table.horizontalHeader().setHighlightSections(False)
        self.transactions_table.horizontalHeader().setStretchLastSection(True)
        self.transactions_table.verticalHeader().setVisible(False)

        self.verticalLayout_7.addWidget(self.transactions_table)

        self.stackedWidget_3.addWidget(self.transactions_page)
        self.alerts_page = QWidget()
        self.alerts_page.setObjectName(u"alerts_page")
        self.layoutWidget4 = QWidget(self.alerts_page)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(247, 115, 1311, 451))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font8)
        self.label_6.setStyleSheet(u"color: rgb(0, 159, 161)")

        self.verticalLayout_8.addWidget(self.label_6)

        self.alerts_table = QTableView(self.layoutWidget4)
        self.alerts_table.setObjectName(u"alerts_table")
        self.alerts_table.setFrameShape(QFrame.NoFrame)
        self.alerts_table.setFrameShadow(QFrame.Plain)
        self.alerts_table.setLineWidth(0)
        self.alerts_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.alerts_table.setAlternatingRowColors(True)
        self.alerts_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.alerts_table.setShowGrid(False)
        self.alerts_table.setSortingEnabled(True)
        self.alerts_table.setCornerButtonEnabled(False)
        self.alerts_table.horizontalHeader().setCascadingSectionResizes(True)
        self.alerts_table.horizontalHeader().setMinimumSectionSize(100)
        self.alerts_table.horizontalHeader().setDefaultSectionSize(200)
        self.alerts_table.horizontalHeader().setHighlightSections(False)
        self.alerts_table.horizontalHeader().setStretchLastSection(True)
        self.alerts_table.verticalHeader().setVisible(False)

        self.verticalLayout_8.addWidget(self.alerts_table)

        self.stackedWidget_3.addWidget(self.alerts_page)
        self.inventory_view_page = QWidget()
        self.inventory_view_page.setObjectName(u"inventory_view_page")
        self.stackedWidget_4 = QStackedWidget(self.inventory_view_page)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.stackedWidget_4.setGeometry(QRect(270, 109, 1291, 531))
        self.item_search_page = QWidget()
        self.item_search_page.setObjectName(u"item_search_page")
        self.verticalLayoutWidget_4 = QWidget(self.item_search_page)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(19, -1, 1251, 491))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_10.setSpacing(30)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.search_bar_container = QWidget(self.verticalLayoutWidget_4)
        self.search_bar_container.setObjectName(u"search_bar_container")
        self.search_bar_container.setMinimumSize(QSize(0, 45))
        self.horizontalLayoutWidget = QWidget(self.search_bar_container)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(-1, 0, 681, 42))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.search_bar_input = QLineEdit(self.horizontalLayoutWidget)
        self.search_bar_input.setObjectName(u"search_bar_input")
        sizePolicy3.setHeightForWidth(self.search_bar_input.sizePolicy().hasHeightForWidth())
        self.search_bar_input.setSizePolicy(sizePolicy3)

        self.horizontalLayout_11.addWidget(self.search_bar_input)

        self.line = QFrame(self.horizontalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background: rgb(0, 159, 161);\n"
"margin-top: 8px;\n"
"margin-bottom: 6px;")
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_11.addWidget(self.line)

        self.search_button = QPushButton(self.horizontalLayoutWidget)
        self.search_button.setObjectName(u"search_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.search_button.sizePolicy().hasHeightForWidth())
        self.search_button.setSizePolicy(sizePolicy4)
        self.search_button.setMinimumSize(QSize(0, 40))
        self.search_button.setFont(font6)
        self.search_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.search_button)


        self.horizontalLayout_9.addWidget(self.search_bar_container)

        self.horizontalSpacer_3 = QSpacerItem(560, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.item_search_table = QTableView(self.verticalLayoutWidget_4)
        self.item_search_table.setObjectName(u"item_search_table")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.item_search_table.sizePolicy().hasHeightForWidth())
        self.item_search_table.setSizePolicy(sizePolicy5)
        self.item_search_table.setMinimumSize(QSize(0, 0))
        self.item_search_table.setMaximumSize(QSize(16777215, 16777215))
        self.item_search_table.setFrameShape(QFrame.NoFrame)
        self.item_search_table.setFrameShadow(QFrame.Plain)
        self.item_search_table.setLineWidth(0)
        self.item_search_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.item_search_table.setAlternatingRowColors(True)
        self.item_search_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.item_search_table.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.item_search_table.setShowGrid(False)
        self.item_search_table.setGridStyle(Qt.SolidLine)
        self.item_search_table.setSortingEnabled(True)
        self.item_search_table.setCornerButtonEnabled(False)
        self.item_search_table.horizontalHeader().setCascadingSectionResizes(True)
        self.item_search_table.horizontalHeader().setMinimumSectionSize(100)
        self.item_search_table.horizontalHeader().setDefaultSectionSize(200)
        self.item_search_table.horizontalHeader().setHighlightSections(False)
        self.item_search_table.horizontalHeader().setProperty("showSortIndicator", True)
        self.item_search_table.horizontalHeader().setStretchLastSection(True)
        self.item_search_table.verticalHeader().setVisible(False)
        self.item_search_table.verticalHeader().setHighlightSections(True)

        self.verticalLayout_10.addWidget(self.item_search_table)

        self.stackedWidget_4.addWidget(self.item_search_page)
        self.update_entry_page = QWidget()
        self.update_entry_page.setObjectName(u"update_entry_page")
        self.verticalLayoutWidget_6 = QWidget(self.update_entry_page)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(0, 0, 1291, 491))
        self.verticalLayout_13 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_13.setSpacing(20)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.update_entry_label = QLabel(self.verticalLayoutWidget_6)
        self.update_entry_label.setObjectName(u"update_entry_label")
        self.update_entry_label.setMaximumSize(QSize(340, 16777215))
        font9 = QFont()
        font9.setPointSize(21)
        font9.setWeight(QFont.Light)
        self.update_entry_label.setFont(font9)
        self.update_entry_label.setStyleSheet(u"color: rgb(0, 159, 161);")

        self.horizontalLayout_16.addWidget(self.update_entry_label)

        self.horizontalSpacer_7 = QSpacerItem(50, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_7)

        self.search_bar_container_2 = QWidget(self.verticalLayoutWidget_6)
        self.search_bar_container_2.setObjectName(u"search_bar_container_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.search_bar_container_2.sizePolicy().hasHeightForWidth())
        self.search_bar_container_2.setSizePolicy(sizePolicy6)
        self.search_bar_container_2.setMinimumSize(QSize(0, 45))
        self.search_bar_container_2.setMaximumSize(QSize(560, 16777215))
        self.horizontalLayoutWidget_4 = QWidget(self.search_bar_container_2)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(-1, 0, 561, 42))
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.update_entry_search_input = QLineEdit(self.horizontalLayoutWidget_4)
        self.update_entry_search_input.setObjectName(u"update_entry_search_input")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.update_entry_search_input.sizePolicy().hasHeightForWidth())
        self.update_entry_search_input.setSizePolicy(sizePolicy7)
        self.update_entry_search_input.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_17.addWidget(self.update_entry_search_input)

        self.line_2 = QFrame(self.horizontalLayoutWidget_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background: rgb(0, 159, 161);\n"
"margin-top: 8px;\n"
"margin-bottom: 6px;")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_17.addWidget(self.line_2)

        self.update_entry_search_button = QPushButton(self.horizontalLayoutWidget_4)
        self.update_entry_search_button.setObjectName(u"update_entry_search_button")
        sizePolicy7.setHeightForWidth(self.update_entry_search_button.sizePolicy().hasHeightForWidth())
        self.update_entry_search_button.setSizePolicy(sizePolicy7)
        self.update_entry_search_button.setMinimumSize(QSize(0, 40))
        self.update_entry_search_button.setMaximumSize(QSize(16777215, 16777215))
        self.update_entry_search_button.setFont(font6)
        self.update_entry_search_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_17.addWidget(self.update_entry_search_button)


        self.horizontalLayout_16.addWidget(self.search_bar_container_2)

        self.horizontalSpacer_6 = QSpacerItem(120, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_6)

        self.update_entry_cancel_button = QPushButton(self.verticalLayoutWidget_6)
        self.update_entry_cancel_button.setObjectName(u"update_entry_cancel_button")
        self.update_entry_cancel_button.setMaximumSize(QSize(120, 16777215))
        self.update_entry_cancel_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_16.addWidget(self.update_entry_cancel_button)


        self.verticalLayout_13.addLayout(self.horizontalLayout_16)

        self.label_15 = QLabel(self.verticalLayoutWidget_6)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setMaximumSize(QSize(16777215, 30))
        font10 = QFont()
        font10.setPointSize(14)
        font10.setItalic(True)
        self.label_15.setFont(font10)
        self.label_15.setStyleSheet(u"background-color:rgb(0, 159, 161);\n"
"padding: 5px;")

        self.verticalLayout_13.addWidget(self.label_15)

        self.update_entry_table = QTableView(self.verticalLayoutWidget_6)
        self.update_entry_table.setObjectName(u"update_entry_table")
        self.update_entry_table.setFrameShape(QFrame.NoFrame)
        self.update_entry_table.setFrameShadow(QFrame.Plain)
        self.update_entry_table.setLineWidth(0)
        self.update_entry_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.update_entry_table.setAlternatingRowColors(True)
        self.update_entry_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.update_entry_table.setShowGrid(False)
        self.update_entry_table.setSortingEnabled(False)
        self.update_entry_table.setCornerButtonEnabled(False)
        self.update_entry_table.horizontalHeader().setCascadingSectionResizes(True)
        self.update_entry_table.horizontalHeader().setMinimumSectionSize(100)
        self.update_entry_table.horizontalHeader().setDefaultSectionSize(200)
        self.update_entry_table.horizontalHeader().setHighlightSections(False)
        self.update_entry_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.update_entry_table.horizontalHeader().setStretchLastSection(True)
        self.update_entry_table.verticalHeader().setVisible(False)
        self.update_entry_table.verticalHeader().setHighlightSections(True)

        self.verticalLayout_13.addWidget(self.update_entry_table)

        self.stackedWidget_4.addWidget(self.update_entry_page)
        self.move_entry_page = QWidget()
        self.move_entry_page.setObjectName(u"move_entry_page")
        self.verticalLayoutWidget_8 = QWidget(self.move_entry_page)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(0, 0, 1291, 491))
        self.verticalLayout_24 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_24.setSpacing(20)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.move_entry_label = QLabel(self.verticalLayoutWidget_8)
        self.move_entry_label.setObjectName(u"move_entry_label")
        self.move_entry_label.setMaximumSize(QSize(340, 16777215))
        self.move_entry_label.setFont(font9)
        self.move_entry_label.setStyleSheet(u"color: rgb(0, 159, 161);")

        self.horizontalLayout_25.addWidget(self.move_entry_label)

        self.horizontalSpacer_13 = QSpacerItem(50, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_13)

        self.search_bar_container_6 = QWidget(self.verticalLayoutWidget_8)
        self.search_bar_container_6.setObjectName(u"search_bar_container_6")
        sizePolicy6.setHeightForWidth(self.search_bar_container_6.sizePolicy().hasHeightForWidth())
        self.search_bar_container_6.setSizePolicy(sizePolicy6)
        self.search_bar_container_6.setMinimumSize(QSize(0, 45))
        self.search_bar_container_6.setMaximumSize(QSize(560, 16777215))
        self.horizontalLayoutWidget_8 = QWidget(self.search_bar_container_6)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(-1, 0, 561, 42))
        self.horizontalLayout_26 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.move_entry_search_input = QLineEdit(self.horizontalLayoutWidget_8)
        self.move_entry_search_input.setObjectName(u"move_entry_search_input")
        sizePolicy7.setHeightForWidth(self.move_entry_search_input.sizePolicy().hasHeightForWidth())
        self.move_entry_search_input.setSizePolicy(sizePolicy7)
        self.move_entry_search_input.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_26.addWidget(self.move_entry_search_input)

        self.line_6 = QFrame(self.horizontalLayoutWidget_8)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"background: rgb(0, 159, 161);\n"
"margin-top: 8px;\n"
"margin-bottom: 6px;")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_26.addWidget(self.line_6)

        self.move_entry_search_button = QPushButton(self.horizontalLayoutWidget_8)
        self.move_entry_search_button.setObjectName(u"move_entry_search_button")
        sizePolicy7.setHeightForWidth(self.move_entry_search_button.sizePolicy().hasHeightForWidth())
        self.move_entry_search_button.setSizePolicy(sizePolicy7)
        self.move_entry_search_button.setMinimumSize(QSize(0, 40))
        self.move_entry_search_button.setMaximumSize(QSize(16777215, 16777215))
        self.move_entry_search_button.setFont(font6)
        self.move_entry_search_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_26.addWidget(self.move_entry_search_button)


        self.horizontalLayout_25.addWidget(self.search_bar_container_6)

        self.horizontalSpacer_14 = QSpacerItem(120, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_14)

        self.move_entry_cancel_button = QPushButton(self.verticalLayoutWidget_8)
        self.move_entry_cancel_button.setObjectName(u"move_entry_cancel_button")
        self.move_entry_cancel_button.setMaximumSize(QSize(120, 16777215))
        self.move_entry_cancel_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_25.addWidget(self.move_entry_cancel_button)


        self.verticalLayout_24.addLayout(self.horizontalLayout_25)

        self.label_18 = QLabel(self.verticalLayoutWidget_8)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setMaximumSize(QSize(16777215, 30))
        self.label_18.setFont(font10)
        self.label_18.setStyleSheet(u"background-color:rgb(0, 159, 161);\n"
"padding: 5px;")

        self.verticalLayout_24.addWidget(self.label_18)

        self.move_entry_table = QTableView(self.verticalLayoutWidget_8)
        self.move_entry_table.setObjectName(u"move_entry_table")
        self.move_entry_table.setFrameShape(QFrame.NoFrame)
        self.move_entry_table.setFrameShadow(QFrame.Plain)
        self.move_entry_table.setLineWidth(0)
        self.move_entry_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.move_entry_table.setAlternatingRowColors(True)
        self.move_entry_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.move_entry_table.setShowGrid(False)
        self.move_entry_table.setSortingEnabled(False)
        self.move_entry_table.setCornerButtonEnabled(False)
        self.move_entry_table.horizontalHeader().setCascadingSectionResizes(True)
        self.move_entry_table.horizontalHeader().setMinimumSectionSize(100)
        self.move_entry_table.horizontalHeader().setDefaultSectionSize(200)
        self.move_entry_table.horizontalHeader().setHighlightSections(False)
        self.move_entry_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.move_entry_table.horizontalHeader().setStretchLastSection(True)
        self.move_entry_table.verticalHeader().setVisible(False)
        self.move_entry_table.verticalHeader().setHighlightSections(True)

        self.verticalLayout_24.addWidget(self.move_entry_table)

        self.stackedWidget_4.addWidget(self.move_entry_page)
        self.restock_entry_page = QWidget()
        self.restock_entry_page.setObjectName(u"restock_entry_page")
        self.verticalLayout_20 = QVBoxLayout(self.restock_entry_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(20)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.restock_entry_label = QLabel(self.restock_entry_page)
        self.restock_entry_label.setObjectName(u"restock_entry_label")
        self.restock_entry_label.setMaximumSize(QSize(340, 16777215))
        self.restock_entry_label.setFont(font9)
        self.restock_entry_label.setStyleSheet(u"color: rgb(0, 159, 161);")

        self.horizontalLayout_20.addWidget(self.restock_entry_label)

        self.horizontalSpacer_8 = QSpacerItem(50, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_8)

        self.search_bar_container_5 = QWidget(self.restock_entry_page)
        self.search_bar_container_5.setObjectName(u"search_bar_container_5")
        sizePolicy6.setHeightForWidth(self.search_bar_container_5.sizePolicy().hasHeightForWidth())
        self.search_bar_container_5.setSizePolicy(sizePolicy6)
        self.search_bar_container_5.setMinimumSize(QSize(0, 45))
        self.search_bar_container_5.setMaximumSize(QSize(560, 16777215))
        self.horizontalLayoutWidget_7 = QWidget(self.search_bar_container_5)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(-1, 0, 561, 42))
        self.horizontalLayout_22 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.restock_entry_search_input = QLineEdit(self.horizontalLayoutWidget_7)
        self.restock_entry_search_input.setObjectName(u"restock_entry_search_input")
        sizePolicy4.setHeightForWidth(self.restock_entry_search_input.sizePolicy().hasHeightForWidth())
        self.restock_entry_search_input.setSizePolicy(sizePolicy4)
        self.restock_entry_search_input.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_22.addWidget(self.restock_entry_search_input)

        self.line_5 = QFrame(self.horizontalLayoutWidget_7)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"background: rgb(0, 159, 161);\n"
"margin-top: 8px;\n"
"margin-bottom: 6px;")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_22.addWidget(self.line_5)

        self.restock_entry_search_button = QPushButton(self.horizontalLayoutWidget_7)
        self.restock_entry_search_button.setObjectName(u"restock_entry_search_button")
        sizePolicy6.setHeightForWidth(self.restock_entry_search_button.sizePolicy().hasHeightForWidth())
        self.restock_entry_search_button.setSizePolicy(sizePolicy6)
        self.restock_entry_search_button.setMinimumSize(QSize(0, 40))
        self.restock_entry_search_button.setMaximumSize(QSize(16777215, 16777215))
        self.restock_entry_search_button.setFont(font6)
        self.restock_entry_search_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_22.addWidget(self.restock_entry_search_button)


        self.horizontalLayout_20.addWidget(self.search_bar_container_5)

        self.horizontalSpacer_9 = QSpacerItem(120, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_9)

        self.restock_entry_cancel_button = QPushButton(self.restock_entry_page)
        self.restock_entry_cancel_button.setObjectName(u"restock_entry_cancel_button")
        self.restock_entry_cancel_button.setMaximumSize(QSize(120, 16777215))
        self.restock_entry_cancel_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_20.addWidget(self.restock_entry_cancel_button)


        self.verticalLayout_18.addLayout(self.horizontalLayout_20)

        self.label_17 = QLabel(self.restock_entry_page)
        self.label_17.setObjectName(u"label_17")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy8)
        self.label_17.setMaximumSize(QSize(16777215, 30))
        self.label_17.setFont(font10)
        self.label_17.setStyleSheet(u"background-color:rgb(0, 159, 161);\n"
"padding: 5px;")

        self.verticalLayout_18.addWidget(self.label_17)

        self.restock_entry_table = QTableView(self.restock_entry_page)
        self.restock_entry_table.setObjectName(u"restock_entry_table")
        self.restock_entry_table.setFrameShape(QFrame.NoFrame)
        self.restock_entry_table.setFrameShadow(QFrame.Plain)
        self.restock_entry_table.setLineWidth(0)
        self.restock_entry_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.restock_entry_table.setAlternatingRowColors(True)
        self.restock_entry_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.restock_entry_table.setShowGrid(False)
        self.restock_entry_table.setSortingEnabled(False)
        self.restock_entry_table.setCornerButtonEnabled(False)
        self.restock_entry_table.horizontalHeader().setCascadingSectionResizes(True)
        self.restock_entry_table.horizontalHeader().setMinimumSectionSize(100)
        self.restock_entry_table.horizontalHeader().setDefaultSectionSize(200)
        self.restock_entry_table.horizontalHeader().setHighlightSections(False)
        self.restock_entry_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.restock_entry_table.horizontalHeader().setStretchLastSection(True)
        self.restock_entry_table.verticalHeader().setVisible(False)
        self.restock_entry_table.verticalHeader().setHighlightSections(True)

        self.verticalLayout_18.addWidget(self.restock_entry_table)


        self.verticalLayout_20.addLayout(self.verticalLayout_18)

        self.stackedWidget_4.addWidget(self.restock_entry_page)
        self.add_entry_page = QWidget()
        self.add_entry_page.setObjectName(u"add_entry_page")
        self.verticalLayoutWidget_5 = QWidget(self.add_entry_page)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(-1, 9, 1291, 521))
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 3, -1, -1)
        self.add_entry_label = QLabel(self.verticalLayoutWidget_5)
        self.add_entry_label.setObjectName(u"add_entry_label")
        self.add_entry_label.setFont(font9)
        self.add_entry_label.setStyleSheet(u"color: rgb(0, 159, 161)")

        self.horizontalLayout_12.addWidget(self.add_entry_label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)

        self.add_entry_cancel_button = QPushButton(self.verticalLayoutWidget_5)
        self.add_entry_cancel_button.setObjectName(u"add_entry_cancel_button")
        self.add_entry_cancel_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.add_entry_cancel_button)

        self.add_entry_add_button = QPushButton(self.verticalLayoutWidget_5)
        self.add_entry_add_button.setObjectName(u"add_entry_add_button")
        self.add_entry_add_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.add_entry_add_button)


        self.verticalLayout_11.addLayout(self.horizontalLayout_12)

        self.add_entry_table_header = QGroupBox(self.verticalLayoutWidget_5)
        self.add_entry_table_header.setObjectName(u"add_entry_table_header")
        self.horizontalLayout_15 = QHBoxLayout(self.add_entry_table_header)
        self.horizontalLayout_15.setSpacing(2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 28, 0, 0)
        self.label_13 = QLabel(self.add_entry_table_header)
        self.label_13.setObjectName(u"label_13")
        sizePolicy6.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy6)

        self.horizontalLayout_15.addWidget(self.label_13)

        self.label_12 = QLabel(self.add_entry_table_header)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(550, 16777215))

        self.horizontalLayout_15.addWidget(self.label_12)

        self.qty_label = QLabel(self.add_entry_table_header)
        self.qty_label.setObjectName(u"qty_label")
        sizePolicy.setHeightForWidth(self.qty_label.sizePolicy().hasHeightForWidth())
        self.qty_label.setSizePolicy(sizePolicy)
        self.qty_label.setMinimumSize(QSize(0, 40))
        self.qty_label.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_15.addWidget(self.qty_label)

        self.label_10 = QLabel(self.add_entry_table_header)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 40))
        self.label_10.setMaximumSize(QSize(350, 16777215))

        self.horizontalLayout_15.addWidget(self.label_10)

        self.label_9 = QLabel(self.add_entry_table_header)
        self.label_9.setObjectName(u"label_9")
        sizePolicy6.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy6)
        self.label_9.setMinimumSize(QSize(200, 40))

        self.horizontalLayout_15.addWidget(self.label_9)


        self.verticalLayout_11.addWidget(self.add_entry_table_header)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.add_entry_inputs = QGroupBox(self.verticalLayoutWidget_5)
        self.add_entry_inputs.setObjectName(u"add_entry_inputs")
        self.add_entry_inputs.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_13 = QHBoxLayout(self.add_entry_inputs)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 10, 10, 0)
        self.horizontalSpacer_5 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.item_name_input = QLineEdit(self.add_entry_inputs)
        self.item_name_input.setObjectName(u"item_name_input")
        sizePolicy7.setHeightForWidth(self.item_name_input.sizePolicy().hasHeightForWidth())
        self.item_name_input.setSizePolicy(sizePolicy7)
        self.item_name_input.setMinimumSize(QSize(510, 0))
        self.item_name_input.setMaximumSize(QSize(500, 16777215))
        font11 = QFont()
        font11.setPointSize(15)
        self.item_name_input.setFont(font11)

        self.horizontalLayout_13.addWidget(self.item_name_input)

        self.item_qty_input = QLineEdit(self.add_entry_inputs)
        self.item_qty_input.setObjectName(u"item_qty_input")
        sizePolicy7.setHeightForWidth(self.item_qty_input.sizePolicy().hasHeightForWidth())
        self.item_qty_input.setSizePolicy(sizePolicy7)
        self.item_qty_input.setMinimumSize(QSize(140, 0))
        self.item_qty_input.setMaximumSize(QSize(150, 16777215))
        self.item_qty_input.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)

        self.horizontalLayout_13.addWidget(self.item_qty_input)

        self.item_lab_input = QComboBox(self.add_entry_inputs)
        self.item_lab_input.setObjectName(u"item_lab_input")
        self.item_lab_input.setMinimumSize(QSize(330, 0))
        self.item_lab_input.setMaximumSize(QSize(350, 16777215))

        self.horizontalLayout_13.addWidget(self.item_lab_input)

        self.item_location_input = QLineEdit(self.add_entry_inputs)
        self.item_location_input.setObjectName(u"item_location_input")

        self.horizontalLayout_13.addWidget(self.item_location_input)


        self.verticalLayout_12.addWidget(self.add_entry_inputs)

        self.add_entry_list = QListWidget(self.verticalLayoutWidget_5)
        self.add_entry_list.setObjectName(u"add_entry_list")

        self.verticalLayout_12.addWidget(self.add_entry_list)


        self.verticalLayout_11.addLayout(self.verticalLayout_12)

        self.stackedWidget_4.addWidget(self.add_entry_page)
        self.delete_entry_page = QWidget()
        self.delete_entry_page.setObjectName(u"delete_entry_page")
        self.verticalLayoutWidget_7 = QWidget(self.delete_entry_page)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(0, 0, 1291, 491))
        self.verticalLayout_14 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_14.setSpacing(20)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.delete_entry_label = QLabel(self.verticalLayoutWidget_7)
        self.delete_entry_label.setObjectName(u"delete_entry_label")
        self.delete_entry_label.setMaximumSize(QSize(3456789, 16777215))
        self.delete_entry_label.setFont(font9)
        self.delete_entry_label.setStyleSheet(u"color: rgb(0, 159, 161);")

        self.horizontalLayout_18.addWidget(self.delete_entry_label)

        self.search_bar_container_3 = QWidget(self.verticalLayoutWidget_7)
        self.search_bar_container_3.setObjectName(u"search_bar_container_3")
        sizePolicy6.setHeightForWidth(self.search_bar_container_3.sizePolicy().hasHeightForWidth())
        self.search_bar_container_3.setSizePolicy(sizePolicy6)
        self.search_bar_container_3.setMinimumSize(QSize(0, 45))
        self.search_bar_container_3.setMaximumSize(QSize(560, 16777215))
        self.horizontalLayoutWidget_5 = QWidget(self.search_bar_container_3)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(-1, 0, 521, 42))
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 10, 0)
        self.delete_entry_search_input = QLineEdit(self.horizontalLayoutWidget_5)
        self.delete_entry_search_input.setObjectName(u"delete_entry_search_input")
        sizePolicy7.setHeightForWidth(self.delete_entry_search_input.sizePolicy().hasHeightForWidth())
        self.delete_entry_search_input.setSizePolicy(sizePolicy7)
        self.delete_entry_search_input.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_19.addWidget(self.delete_entry_search_input)

        self.line_3 = QFrame(self.horizontalLayoutWidget_5)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background: rgb(0, 159, 161);\n"
"margin-top: 8px;\n"
"margin-bottom: 6px;")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.line_3)

        self.delete_entry_search_button = QPushButton(self.horizontalLayoutWidget_5)
        self.delete_entry_search_button.setObjectName(u"delete_entry_search_button")
        sizePolicy7.setHeightForWidth(self.delete_entry_search_button.sizePolicy().hasHeightForWidth())
        self.delete_entry_search_button.setSizePolicy(sizePolicy7)
        self.delete_entry_search_button.setMinimumSize(QSize(0, 40))
        self.delete_entry_search_button.setMaximumSize(QSize(16777215, 16777215))
        self.delete_entry_search_button.setFont(font6)
        self.delete_entry_search_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_19.addWidget(self.delete_entry_search_button)


        self.horizontalLayout_18.addWidget(self.search_bar_container_3)

        self.delete_entry_cancel_button = QPushButton(self.verticalLayoutWidget_7)
        self.delete_entry_cancel_button.setObjectName(u"delete_entry_cancel_button")
        self.delete_entry_cancel_button.setMaximumSize(QSize(120, 16777215))
        self.delete_entry_cancel_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_18.addWidget(self.delete_entry_cancel_button)

        self.delete_entry_delete_button = QPushButton(self.verticalLayoutWidget_7)
        self.delete_entry_delete_button.setObjectName(u"delete_entry_delete_button")
        self.delete_entry_delete_button.setMaximumSize(QSize(120, 16777215))
        self.delete_entry_delete_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_entry_delete_button.setStyleSheet(u"margin: 0;")

        self.horizontalLayout_18.addWidget(self.delete_entry_delete_button)


        self.verticalLayout_14.addLayout(self.horizontalLayout_18)

        self.label_14 = QLabel(self.verticalLayoutWidget_7)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setMaximumSize(QSize(16777215, 30))
        font12 = QFont()
        font12.setPointSize(14)
        font12.setItalic(True)
        font12.setUnderline(False)
        self.label_14.setFont(font12)
        self.label_14.setStyleSheet(u"background-color: rgb(0, 159, 161);\n"
"padding: 5px;")

        self.verticalLayout_14.addWidget(self.label_14)

        self.delete_entry_table = QTableView(self.verticalLayoutWidget_7)
        self.delete_entry_table.setObjectName(u"delete_entry_table")
        self.delete_entry_table.setFrameShape(QFrame.NoFrame)
        self.delete_entry_table.setFrameShadow(QFrame.Plain)
        self.delete_entry_table.setLineWidth(0)
        self.delete_entry_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.delete_entry_table.setAlternatingRowColors(True)
        self.delete_entry_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.delete_entry_table.setShowGrid(False)
        self.delete_entry_table.setSortingEnabled(False)
        self.delete_entry_table.setCornerButtonEnabled(False)
        self.delete_entry_table.horizontalHeader().setCascadingSectionResizes(True)
        self.delete_entry_table.horizontalHeader().setMinimumSectionSize(100)
        self.delete_entry_table.horizontalHeader().setDefaultSectionSize(200)
        self.delete_entry_table.horizontalHeader().setHighlightSections(False)
        self.delete_entry_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.delete_entry_table.horizontalHeader().setStretchLastSection(True)
        self.delete_entry_table.verticalHeader().setVisible(False)
        self.delete_entry_table.verticalHeader().setHighlightSections(True)

        self.verticalLayout_14.addWidget(self.delete_entry_table)

        self.stackedWidget_4.addWidget(self.delete_entry_page)
        self.layoutWidget5 = QWidget(self.inventory_view_page)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(40, 190, 211, 306))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_9.setSpacing(1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font6)
        self.label_7.setStyleSheet(u"color: rgb(52, 62, 162)")
        self.label_7.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_9.addWidget(self.label_7)

        self.add_entry_button = QPushButton(self.layoutWidget5)
        self.item_manage = QButtonGroup(MainWindow)
        self.item_manage.setObjectName(u"item_manage")
        self.item_manage.setExclusive(True)
        self.item_manage.addButton(self.add_entry_button)
        self.add_entry_button.setObjectName(u"add_entry_button")
        self.add_entry_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_entry_button.setCheckable(True)

        self.verticalLayout_9.addWidget(self.add_entry_button)

        self.update_entry_button = QPushButton(self.layoutWidget5)
        self.item_manage.addButton(self.update_entry_button)
        self.update_entry_button.setObjectName(u"update_entry_button")
        self.update_entry_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.update_entry_button.setMouseTracking(True)
        self.update_entry_button.setCheckable(True)

        self.verticalLayout_9.addWidget(self.update_entry_button)

        self.restock_entry_button = QPushButton(self.layoutWidget5)
        self.item_manage.addButton(self.restock_entry_button)
        self.restock_entry_button.setObjectName(u"restock_entry_button")
        self.restock_entry_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.restock_entry_button.setCheckable(True)

        self.verticalLayout_9.addWidget(self.restock_entry_button)

        self.move_entry_button = QPushButton(self.layoutWidget5)
        self.item_manage.addButton(self.move_entry_button)
        self.move_entry_button.setObjectName(u"move_entry_button")
        self.move_entry_button.setCheckable(True)

        self.verticalLayout_9.addWidget(self.move_entry_button)

        self.delete_entry_button = QPushButton(self.layoutWidget5)
        self.item_manage.addButton(self.delete_entry_button)
        self.delete_entry_button.setObjectName(u"delete_entry_button")
        self.delete_entry_button.setFont(font11)
        self.delete_entry_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_entry_button.setCheckable(True)

        self.verticalLayout_9.addWidget(self.delete_entry_button)

        self.stackedWidget_3.addWidget(self.inventory_view_page)
        self.layoutWidget2.raise_()
        self.stackedWidget_4.raise_()

        self.verticalLayout_4.addWidget(self.stackedWidget_3)

        self.stackedWidget_2.addWidget(self.inventory_page)
        self.user_page = QWidget()
        self.user_page.setObjectName(u"user_page")
        self.layoutWidget6 = QWidget(self.user_page)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(0, 0, 1601, 751))
        self.verticalLayout_17 = QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_17.setSpacing(50)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.inventory_header_2 = QWidget(self.layoutWidget6)
        self.inventory_header_2.setObjectName(u"inventory_header_2")
        self.inventory_header_2.setMinimumSize(QSize(0, 90))
        self.horizontalLayout_10 = QHBoxLayout(self.inventory_header_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(60, 0, 60, 0)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.time_label_2 = QLabel(self.inventory_header_2)
        self.time_label_2.setObjectName(u"time_label_2")
        self.time_label_2.setFont(font3)
        self.time_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.time_label_2)

        self.date_label_2 = QLabel(self.inventory_header_2)
        self.date_label_2.setObjectName(u"date_label_2")
        self.date_label_2.setFont(font4)
        self.date_label_2.setTextFormat(Qt.AutoText)
        self.date_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.date_label_2)


        self.horizontalLayout_10.addLayout(self.verticalLayout_15)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_11)

        self.label_8 = QLabel(self.inventory_header_2)
        self.label_8.setObjectName(u"label_8")
        font13 = QFont()
        font13.setPointSize(23)
        font13.setWeight(QFont.Medium)
        self.label_8.setFont(font13)

        self.horizontalLayout_10.addWidget(self.label_8)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)

        self.transaction_history_button_2 = QPushButton(self.inventory_header_2)
        self.transaction_history_button_2.setObjectName(u"transaction_history_button_2")
        sizePolicy4.setHeightForWidth(self.transaction_history_button_2.sizePolicy().hasHeightForWidth())
        self.transaction_history_button_2.setSizePolicy(sizePolicy4)
        self.transaction_history_button_2.setMinimumSize(QSize(200, 0))
        self.transaction_history_button_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.transaction_history_button_2)


        self.verticalLayout_17.addWidget(self.inventory_header_2)

        self.stackedWidget_5 = QStackedWidget(self.layoutWidget6)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        self.stackedWidget_5.setMinimumSize(QSize(0, 0))
        self.update_entry_page_2 = QWidget()
        self.update_entry_page_2.setObjectName(u"update_entry_page_2")
        self.verticalLayout_19 = QVBoxLayout(self.update_entry_page_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(30)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(150, -1, 150, -1)
        self.search_bar_container_4 = QWidget(self.update_entry_page_2)
        self.search_bar_container_4.setObjectName(u"search_bar_container_4")
        sizePolicy6.setHeightForWidth(self.search_bar_container_4.sizePolicy().hasHeightForWidth())
        self.search_bar_container_4.setSizePolicy(sizePolicy6)
        self.search_bar_container_4.setMinimumSize(QSize(0, 45))
        self.search_bar_container_4.setMaximumSize(QSize(560, 16777215))
        self.horizontalLayoutWidget_6 = QWidget(self.search_bar_container_4)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(-1, 0, 561, 42))
        self.horizontalLayout_21 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.update_entry_search_input_2 = QLineEdit(self.horizontalLayoutWidget_6)
        self.update_entry_search_input_2.setObjectName(u"update_entry_search_input_2")
        sizePolicy7.setHeightForWidth(self.update_entry_search_input_2.sizePolicy().hasHeightForWidth())
        self.update_entry_search_input_2.setSizePolicy(sizePolicy7)
        self.update_entry_search_input_2.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_21.addWidget(self.update_entry_search_input_2)

        self.line_4 = QFrame(self.horizontalLayoutWidget_6)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"background: rgb(0, 159, 161);\n"
"margin-top: 8px;\n"
"margin-bottom: 6px;")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_21.addWidget(self.line_4)

        self.update_entry_search_button_2 = QPushButton(self.horizontalLayoutWidget_6)
        self.update_entry_search_button_2.setObjectName(u"update_entry_search_button_2")
        sizePolicy7.setHeightForWidth(self.update_entry_search_button_2.sizePolicy().hasHeightForWidth())
        self.update_entry_search_button_2.setSizePolicy(sizePolicy7)
        self.update_entry_search_button_2.setMinimumSize(QSize(0, 40))
        self.update_entry_search_button_2.setMaximumSize(QSize(16777215, 16777215))
        self.update_entry_search_button_2.setFont(font6)
        self.update_entry_search_button_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_21.addWidget(self.update_entry_search_button_2)


        self.verticalLayout_16.addWidget(self.search_bar_container_4)

        self.label_16 = QLabel(self.update_entry_page_2)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setMaximumSize(QSize(16777215, 30))
        self.label_16.setFont(font10)
        self.label_16.setStyleSheet(u"background-color:rgb(0, 159, 161);\n"
"padding: 5px;")

        self.verticalLayout_16.addWidget(self.label_16)

        self.update_entry_table_2 = QTableView(self.update_entry_page_2)
        self.update_entry_table_2.setObjectName(u"update_entry_table_2")
        self.update_entry_table_2.setStyleSheet(u"")
        self.update_entry_table_2.setFrameShape(QFrame.NoFrame)
        self.update_entry_table_2.setFrameShadow(QFrame.Plain)
        self.update_entry_table_2.setLineWidth(0)
        self.update_entry_table_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.update_entry_table_2.setAlternatingRowColors(True)
        self.update_entry_table_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.update_entry_table_2.setShowGrid(False)
        self.update_entry_table_2.setSortingEnabled(False)
        self.update_entry_table_2.setCornerButtonEnabled(False)
        self.update_entry_table_2.horizontalHeader().setCascadingSectionResizes(True)
        self.update_entry_table_2.horizontalHeader().setMinimumSectionSize(100)
        self.update_entry_table_2.horizontalHeader().setDefaultSectionSize(200)
        self.update_entry_table_2.horizontalHeader().setHighlightSections(False)
        self.update_entry_table_2.horizontalHeader().setProperty("showSortIndicator", False)
        self.update_entry_table_2.horizontalHeader().setStretchLastSection(True)
        self.update_entry_table_2.verticalHeader().setVisible(False)
        self.update_entry_table_2.verticalHeader().setCascadingSectionResizes(False)
        self.update_entry_table_2.verticalHeader().setHighlightSections(True)

        self.verticalLayout_16.addWidget(self.update_entry_table_2)


        self.verticalLayout_19.addLayout(self.verticalLayout_16)

        self.stackedWidget_5.addWidget(self.update_entry_page_2)
        self.user_transactions_page = QWidget()
        self.user_transactions_page.setObjectName(u"user_transactions_page")
        self.verticalLayout_21 = QVBoxLayout(self.user_transactions_page)
        self.verticalLayout_21.setSpacing(50)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(150, -1, 150, 50)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, -1)
        self.label_11 = QLabel(self.user_transactions_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font8)
        self.label_11.setStyleSheet(u"color: rgb(0, 159, 161)")

        self.horizontalLayout_14.addWidget(self.label_11)

        self.go_back_button = QPushButton(self.user_transactions_page)
        self.go_back_button.setObjectName(u"go_back_button")

        self.horizontalLayout_14.addWidget(self.go_back_button)

        self.horizontalLayout_14.setStretch(0, 9)
        self.horizontalLayout_14.setStretch(1, 1)

        self.verticalLayout_21.addLayout(self.horizontalLayout_14)

        self.transactions_table_2 = QTableView(self.user_transactions_page)
        self.transactions_table_2.setObjectName(u"transactions_table_2")
        self.transactions_table_2.setFrameShape(QFrame.NoFrame)
        self.transactions_table_2.setFrameShadow(QFrame.Plain)
        self.transactions_table_2.setLineWidth(0)
        self.transactions_table_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.transactions_table_2.setAlternatingRowColors(True)
        self.transactions_table_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.transactions_table_2.setShowGrid(False)
        self.transactions_table_2.setSortingEnabled(True)
        self.transactions_table_2.setCornerButtonEnabled(False)
        self.transactions_table_2.horizontalHeader().setCascadingSectionResizes(True)
        self.transactions_table_2.horizontalHeader().setMinimumSectionSize(100)
        self.transactions_table_2.horizontalHeader().setDefaultSectionSize(100)
        self.transactions_table_2.horizontalHeader().setHighlightSections(False)
        self.transactions_table_2.horizontalHeader().setStretchLastSection(True)
        self.transactions_table_2.verticalHeader().setVisible(False)

        self.verticalLayout_21.addWidget(self.transactions_table_2)

        self.stackedWidget_5.addWidget(self.user_transactions_page)

        self.verticalLayout_17.addWidget(self.stackedWidget_5)

        self.verticalLayout_17.setStretch(0, 1)
        self.verticalLayout_17.setStretch(1, 9)
        self.stackedWidget_2.addWidget(self.user_page)
        self.create_user_page = QWidget()
        self.create_user_page.setObjectName(u"create_user_page")
        self.layoutWidget7 = QWidget(self.create_user_page)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(0, -10, 1601, 751))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.layoutWidget7)
        self.widget.setObjectName(u"widget")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(3)
        sizePolicy9.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy9)
        self.widget.setStyleSheet(u"")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 800, 770))
        self.label_2.setLineWidth(0)
        self.label_2.setPixmap(QPixmap(u":/images/images/create_user.jpeg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.widget)

        self.create_user_form = QWidget(self.layoutWidget7)
        self.create_user_form.setObjectName(u"create_user_form")
        sizePolicy9.setHeightForWidth(self.create_user_form.sizePolicy().hasHeightForWidth())
        self.create_user_form.setSizePolicy(sizePolicy9)
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
        font14 = QFont()
        font14.setPointSize(21)
        self.cu_username_input.setFont(font14)
        self.cu_username_input.setFrame(True)

        self.verticalLayout_3.addWidget(self.cu_username_input)

        self.cu_password_label = QLabel(self.verticalLayoutWidget_2)
        self.cu_password_label.setObjectName(u"cu_password_label")

        self.verticalLayout_3.addWidget(self.cu_password_label)

        self.cu_password_input = QLineEdit(self.verticalLayoutWidget_2)
        self.cu_password_input.setObjectName(u"cu_password_input")
        self.cu_password_input.setFont(font14)
        self.cu_password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.cu_password_input)

        self.cu_confirm_password_label = QLabel(self.verticalLayoutWidget_2)
        self.cu_confirm_password_label.setObjectName(u"cu_confirm_password_label")

        self.verticalLayout_3.addWidget(self.cu_confirm_password_label)

        self.cu_confirm_password_input = QLineEdit(self.verticalLayoutWidget_2)
        self.cu_confirm_password_input.setObjectName(u"cu_confirm_password_input")
        self.cu_confirm_password_input.setFont(font14)
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
        sizePolicy7.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy7)
        self.cancel_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.cancel_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_3.addWidget(self.create_user_form)

        self.stackedWidget_2.addWidget(self.create_user_page)

        self.verticalLayout_2.addWidget(self.stackedWidget_2)

        self.footer = QWidget(self.home_page)
        self.footer.setObjectName(u"footer")
        self.footer.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.footer)
        self.horizontalLayout_5.setSpacing(0)
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


        self.verticalLayout_23.addLayout(self.verticalLayout_2)

        self.stackedWidget.addWidget(self.home_page)

        self.verticalLayout_22.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.login_button.setDefault(True)
        self.stackedWidget_2.setCurrentIndex(0)
        self.inventory_type_input.setCurrentIndex(-1)
        self.stackedWidget_3.setCurrentIndex(3)
        self.stackedWidget_4.setCurrentIndex(4)
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
        self.time_label.setText(QCoreApplication.translate("MainWindow", u"12:00 AM", None))
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"20 Feb, 2024", None))
        self.transaction_history_button.setText(QCoreApplication.translate("MainWindow", u"Transaction History", None))
        self.alerts_button.setText(QCoreApplication.translate("MainWindow", u"Alert Notifications", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select Inventory: ", None))
        self.inventory_type_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Glassware", None))
        self.inventory_type_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Equipment", None))
        self.inventory_type_input.setItemText(2, QCoreApplication.translate("MainWindow", u"Chemical", None))

        self.inventory_type_input.setCurrentText("")
        self.inventory_type_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"      -- Select an option --", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nothing to Show", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TRANSACTION HISTORY", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ALERTS", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.update_entry_label.setText(QCoreApplication.translate("MainWindow", u"EDIT EXISTING GLASSWARE", None))
        self.update_entry_search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.update_entry_cancel_button.setText(QCoreApplication.translate("MainWindow", u"Go Back", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Click any cell of the table to select the item", None))
        self.move_entry_label.setText(QCoreApplication.translate("MainWindow", u"MOVE ITEM", None))
        self.move_entry_search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.move_entry_cancel_button.setText(QCoreApplication.translate("MainWindow", u"Go Back", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Click any cell of the table to select the item", None))
        self.restock_entry_label.setText(QCoreApplication.translate("MainWindow", u"RESTOCK ITEM", None))
        self.restock_entry_search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.restock_entry_cancel_button.setText(QCoreApplication.translate("MainWindow", u"Go Back", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Click any cell of the table to select the item", None))
        self.add_entry_label.setText(QCoreApplication.translate("MainWindow", u"ADD NEW GLASSWARE", None))
        self.add_entry_cancel_button.setText(QCoreApplication.translate("MainWindow", u"Go Back", None))
        self.add_entry_add_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.add_entry_table_header.setTitle("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.qty_label.setText(QCoreApplication.translate("MainWindow", u"Qty", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Lab", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.add_entry_inputs.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.delete_entry_label.setText(QCoreApplication.translate("MainWindow", u"REMOVE EXISTING GLASSWARE", None))
        self.delete_entry_search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.delete_entry_cancel_button.setText(QCoreApplication.translate("MainWindow", u"Go Back", None))
        self.delete_entry_delete_button.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Click any cell of the table to select the item", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"OPTIONS", None))
        self.add_entry_button.setText(QCoreApplication.translate("MainWindow", u"Add New Item", None))
        self.update_entry_button.setText(QCoreApplication.translate("MainWindow", u"Edit Existing Item", None))
        self.restock_entry_button.setText(QCoreApplication.translate("MainWindow", u"Restock Item", None))
        self.move_entry_button.setText(QCoreApplication.translate("MainWindow", u"Move Item ", None))
        self.delete_entry_button.setText(QCoreApplication.translate("MainWindow", u"Remove Existing Item", None))
        self.time_label_2.setText(QCoreApplication.translate("MainWindow", u"12:00 AM", None))
        self.date_label_2.setText(QCoreApplication.translate("MainWindow", u"20 Feb, 2024", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Chemical Usage Log", None))
        self.transaction_history_button_2.setText(QCoreApplication.translate("MainWindow", u"Transaction History", None))
        self.update_entry_search_button_2.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Click any cell of the table to select the item", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TRANSACTION HISTORY", None))
        self.go_back_button.setText(QCoreApplication.translate("MainWindow", u"Go back", None))
        self.label_2.setText("")
        self.cu_username_label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.cu_password_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.cu_confirm_password_label.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.create_account_button.setText(QCoreApplication.translate("MainWindow", u"CREATE ACCOUNT", None))
        self.cancel_button.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"&copy; 2024, Dept. of CS", None))
    # retranslateUi


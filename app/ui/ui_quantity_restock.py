# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quantity_restock.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_QtyRestock(object):
    def setupUi(self, QtyRestock):
        if not QtyRestock.objectName():
            QtyRestock.setObjectName(u"QtyRestock")
        QtyRestock.resize(836, 95)
        QtyRestock.setMinimumSize(QSize(0, 95))
        QtyRestock.setMaximumSize(QSize(16777215, 100))
        QtyRestock.setStyleSheet(u"* {\n"
"	background: #fff\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #fff;\n"
"	background: rgb(0, 159, 161);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid rgb(0, 159, 161);\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"	color: rgb(0, 159, 161)\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(0, 159, 161);\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: 1px solid;\n"
"	margin: 0;\n"
"	height: 40px;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#add_stock_button {\n"
"	color: rgb(0, 159, 161);\n"
"	border-color: rgb(0, 159, 161);\n"
"}\n"
"\n"
"#add_stock_button:hover{\n"
"	background: rgb(0, 159, 161);\n"
"	color: #fff;\n"
"}\n"
"\n"
"#remove_stock_button {\n"
"	border-color: rgb(224, 27, 36);\n"
"	color: rgb(224, 27, 36);\n"
"}\n"
"\n"
"#remove_stock_button:hover {\n"
"	color:#fff;\n"
"	background-color: rgb(224, 27, 36);\n"
"}")
        self.verticalLayout = QVBoxLayout(QtyRestock)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(QtyRestock)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setItalic(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qty_label = QLabel(QtyRestock)
        self.qty_label.setObjectName(u"qty_label")
        self.qty_label.setMaximumSize(QSize(356356, 45))
        font1 = QFont()
        font1.setPointSize(18)
        self.qty_label.setFont(font1)
        self.qty_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.qty_label)

        self.qty_input = QLineEdit(QtyRestock)
        self.qty_input.setObjectName(u"qty_input")
        self.qty_input.setMaximumSize(QSize(200, 45))
        self.qty_input.setFont(font1)
        self.qty_input.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout.addWidget(self.qty_input)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.add_stock_button = QPushButton(QtyRestock)
        self.add_stock_button.setObjectName(u"add_stock_button")
        self.add_stock_button.setMaximumSize(QSize(134, 45))
        self.add_stock_button.setFont(font1)

        self.horizontalLayout.addWidget(self.add_stock_button)

        self.remove_stock_button = QPushButton(QtyRestock)
        self.remove_stock_button.setObjectName(u"remove_stock_button")
        self.remove_stock_button.setMaximumSize(QSize(161, 45))
        self.remove_stock_button.setFont(font1)

        self.horizontalLayout.addWidget(self.remove_stock_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(QtyRestock)

        QMetaObject.connectSlotsByName(QtyRestock)
    # setupUi

    def retranslateUi(self, QtyRestock):
        QtyRestock.setWindowTitle(QCoreApplication.translate("QtyRestock", u"Form", None))
        self.label.setText(QCoreApplication.translate("QtyRestock", u"Enter quantity taken from or added to the inventory", None))
        self.qty_label.setText(QCoreApplication.translate("QtyRestock", u"Qty", None))
        self.add_stock_button.setText(QCoreApplication.translate("QtyRestock", u"Add Stock", None))
        self.remove_stock_button.setText(QCoreApplication.translate("QtyRestock", u"Remove Stock", None))
    # retranslateUi


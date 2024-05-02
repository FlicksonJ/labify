# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quantity_edit_input.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_QuantityEdit(object):
    def setupUi(self, QuantityEdit):
        if not QuantityEdit.objectName():
            QuantityEdit.setObjectName(u"QuantityEdit")
        QuantityEdit.resize(836, 55)
        QuantityEdit.setMinimumSize(QSize(0, 55))
        QuantityEdit.setMaximumSize(QSize(16777215, 63))
        QuantityEdit.setStyleSheet(u"* {\n"
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
        self.horizontalLayout = QHBoxLayout(QuantityEdit)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qty_label = QLabel(QuantityEdit)
        self.qty_label.setObjectName(u"qty_label")
        self.qty_label.setMaximumSize(QSize(356356, 45))
        font = QFont()
        font.setPointSize(18)
        self.qty_label.setFont(font)
        self.qty_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.qty_label)

        self.qty_input = QLineEdit(QuantityEdit)
        self.qty_input.setObjectName(u"qty_input")
        self.qty_input.setMaximumSize(QSize(200, 45))
        self.qty_input.setFont(font)
        self.qty_input.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout.addWidget(self.qty_input)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.add_stock_button = QPushButton(QuantityEdit)
        self.add_stock_button.setObjectName(u"add_stock_button")
        self.add_stock_button.setMaximumSize(QSize(134, 45))
        self.add_stock_button.setFont(font)

        self.horizontalLayout.addWidget(self.add_stock_button)

        self.remove_stock_button = QPushButton(QuantityEdit)
        self.remove_stock_button.setObjectName(u"remove_stock_button")
        self.remove_stock_button.setMaximumSize(QSize(161, 45))
        self.remove_stock_button.setFont(font)

        self.horizontalLayout.addWidget(self.remove_stock_button)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 4)
        self.horizontalLayout.setStretch(3, 2)
        self.horizontalLayout.setStretch(4, 2)

        self.retranslateUi(QuantityEdit)

        QMetaObject.connectSlotsByName(QuantityEdit)
    # setupUi

    def retranslateUi(self, QuantityEdit):
        QuantityEdit.setWindowTitle(QCoreApplication.translate("QuantityEdit", u"Form", None))
        self.qty_label.setText(QCoreApplication.translate("QuantityEdit", u"Qty", None))
        self.add_stock_button.setText(QCoreApplication.translate("QuantityEdit", u"Add Stock", None))
        self.remove_stock_button.setText(QCoreApplication.translate("QuantityEdit", u"Remove Stock", None))
    # retranslateUi


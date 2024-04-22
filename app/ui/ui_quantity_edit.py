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
        QuantityEdit.resize(836, 67)
        QuantityEdit.setStyleSheet(u"#add_stock_button,\n"
"#remove_stock_button {\n"
"	border: 1px solid;\n"
"	margin: 0;\n"
"	font-size: 18pt;\n"
"	height: 40px;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}\n"
"\n"
"* {\n"
"	background: #fff;\n"
"	color: black;\n"
"}")
        self.horizontalLayout = QHBoxLayout(QuantityEdit)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qty_label = QLabel(QuantityEdit)
        self.qty_label.setObjectName(u"qty_label")
        self.qty_label.setMaximumSize(QSize(356356, 16777215))
        font = QFont()
        font.setPointSize(18)
        self.qty_label.setFont(font)

        self.horizontalLayout.addWidget(self.qty_label)

        self.qty_input = QLineEdit(QuantityEdit)
        self.qty_input.setObjectName(u"qty_input")
        self.qty_input.setMaximumSize(QSize(200, 16777215))
        self.qty_input.setFont(font)
        self.qty_input.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout.addWidget(self.qty_input)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.add_stock_button = QPushButton(QuantityEdit)
        self.add_stock_button.setObjectName(u"add_stock_button")
        self.add_stock_button.setMaximumSize(QSize(134, 16777215))
        self.add_stock_button.setFont(font)

        self.horizontalLayout.addWidget(self.add_stock_button)

        self.remove_stock_button = QPushButton(QuantityEdit)
        self.remove_stock_button.setObjectName(u"remove_stock_button")
        self.remove_stock_button.setMaximumSize(QSize(161, 16777215))
        self.remove_stock_button.setFont(font)

        self.horizontalLayout.addWidget(self.remove_stock_button)


        self.retranslateUi(QuantityEdit)

        QMetaObject.connectSlotsByName(QuantityEdit)
    # setupUi

    def retranslateUi(self, QuantityEdit):
        QuantityEdit.setWindowTitle(QCoreApplication.translate("QuantityEdit", u"Form", None))
        self.qty_label.setText(QCoreApplication.translate("QuantityEdit", u"Qty:", None))
        self.add_stock_button.setText(QCoreApplication.translate("QuantityEdit", u"Add Stock", None))
        self.remove_stock_button.setText(QCoreApplication.translate("QuantityEdit", u"Remove Stock", None))
    # retranslateUi


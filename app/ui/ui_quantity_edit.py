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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_QtyEdit(object):
    def setupUi(self, QtyEdit):
        if not QtyEdit.objectName():
            QtyEdit.setObjectName(u"QtyEdit")
        QtyEdit.resize(893, 87)
        QtyEdit.setStyleSheet(u"* {\n"
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
"	color: rgb(0, 159, 161);\n"
"	border-color: rgb(0, 159, 161);\n"
"	padding: 5px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: rgb(0, 159, 161);\n"
"	color: #fff;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(QtyEdit)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(QtyEdit)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setItalic(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qty_label = QLabel(QtyEdit)
        self.qty_label.setObjectName(u"qty_label")
        self.qty_label.setMaximumSize(QSize(16777215, 45))
        font1 = QFont()
        font1.setPointSize(18)
        self.qty_label.setFont(font1)
        self.qty_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.qty_label)

        self.qty_input = QLineEdit(QtyEdit)
        self.qty_input.setObjectName(u"qty_input")
        self.qty_input.setMaximumSize(QSize(16777215, 45))
        self.qty_input.setFont(font1)

        self.horizontalLayout.addWidget(self.qty_input)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.update_button = QPushButton(QtyEdit)
        self.update_button.setObjectName(u"update_button")
        self.update_button.setMaximumSize(QSize(16777215, 45))
        self.update_button.setFont(font1)

        self.horizontalLayout.addWidget(self.update_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(QtyEdit)

        QMetaObject.connectSlotsByName(QtyEdit)
    # setupUi

    def retranslateUi(self, QtyEdit):
        QtyEdit.setWindowTitle(QCoreApplication.translate("QtyEdit", u"Form", None))
        self.label.setText(QCoreApplication.translate("QtyEdit", u"Enter the new quantity of the selected item.", None))
        self.qty_label.setText(QCoreApplication.translate("QtyEdit", u"Qty", None))
        self.update_button.setText(QCoreApplication.translate("QtyEdit", u"Update Qty", None))
    # retranslateUi


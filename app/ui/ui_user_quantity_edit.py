# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_qty_edit_input.ui'
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

class Ui_UserQuantityEdit(object):
    def setupUi(self, UserQuantityEdit):
        if not UserQuantityEdit.objectName():
            UserQuantityEdit.setObjectName(u"UserQuantityEdit")
        UserQuantityEdit.resize(893, 63)
        UserQuantityEdit.setMinimumSize(QSize(0, 55))
        UserQuantityEdit.setMaximumSize(QSize(16777215, 63))
        font = QFont()
        font.setPointSize(18)
        UserQuantityEdit.setFont(font)
        UserQuantityEdit.setStyleSheet(u"* {\n"
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
        self.horizontalLayout = QHBoxLayout(UserQuantityEdit)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qty_label = QLabel(UserQuantityEdit)
        self.qty_label.setObjectName(u"qty_label")
        self.qty_label.setMaximumSize(QSize(16777215, 45))
        self.qty_label.setFont(font)
        self.qty_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.qty_label)

        self.qty_input = QLineEdit(UserQuantityEdit)
        self.qty_input.setObjectName(u"qty_input")
        self.qty_input.setMaximumSize(QSize(16777215, 45))
        self.qty_input.setFont(font)

        self.horizontalLayout.addWidget(self.qty_input)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.used_button = QPushButton(UserQuantityEdit)
        self.used_button.setObjectName(u"used_button")
        self.used_button.setMaximumSize(QSize(16777215, 45))
        self.used_button.setFont(font)

        self.horizontalLayout.addWidget(self.used_button)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 6)
        self.horizontalLayout.setStretch(3, 2)

        self.retranslateUi(UserQuantityEdit)

        QMetaObject.connectSlotsByName(UserQuantityEdit)
    # setupUi

    def retranslateUi(self, UserQuantityEdit):
        UserQuantityEdit.setWindowTitle(QCoreApplication.translate("UserQuantityEdit", u"Form", None))
        self.qty_label.setText(QCoreApplication.translate("UserQuantityEdit", u"Qty", None))
        self.used_button.setText(QCoreApplication.translate("UserQuantityEdit", u"Used", None))
    # retranslateUi


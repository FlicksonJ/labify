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
        UserQuantityEdit.resize(893, 62)
        UserQuantityEdit.setStyleSheet(u"* {\n"
"	background: #fff;\n"
"	color: black;\n"
"	font-size: 18pt;\n"
"}")
        self.horizontalLayout = QHBoxLayout(UserQuantityEdit)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qty_label = QLabel(UserQuantityEdit)
        self.qty_label.setObjectName(u"qty_label")

        self.horizontalLayout.addWidget(self.qty_label)

        self.qty_input = QLineEdit(UserQuantityEdit)
        self.qty_input.setObjectName(u"qty_input")

        self.horizontalLayout.addWidget(self.qty_input)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.used_button = QPushButton(UserQuantityEdit)
        self.used_button.setObjectName(u"used_button")

        self.horizontalLayout.addWidget(self.used_button)


        self.retranslateUi(UserQuantityEdit)

        QMetaObject.connectSlotsByName(UserQuantityEdit)
    # setupUi

    def retranslateUi(self, UserQuantityEdit):
        UserQuantityEdit.setWindowTitle(QCoreApplication.translate("UserQuantityEdit", u"Form", None))
        self.qty_label.setText(QCoreApplication.translate("UserQuantityEdit", u"Qty:", None))
        self.used_button.setText(QCoreApplication.translate("UserQuantityEdit", u"Used", None))
    # retranslateUi


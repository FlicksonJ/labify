# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'location_edit_input.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_LocationEdit(object):
    def setupUi(self, LocationEdit):
        if not LocationEdit.objectName():
            LocationEdit.setObjectName(u"LocationEdit")
        LocationEdit.resize(815, 55)
        LocationEdit.setStyleSheet(u"* {\n"
"	background: #fff;\n"
"	color: black;\n"
"}")
        self.horizontalLayout = QHBoxLayout(LocationEdit)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.location_label = QLabel(LocationEdit)
        self.location_label.setObjectName(u"location_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location_label.sizePolicy().hasHeightForWidth())
        self.location_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        self.location_label.setFont(font)

        self.horizontalLayout.addWidget(self.location_label)

        self.lab_input = QComboBox(LocationEdit)
        self.lab_input.setObjectName(u"lab_input")
        self.lab_input.setFont(font)

        self.horizontalLayout.addWidget(self.lab_input)

        self.location_input = QComboBox(LocationEdit)
        self.location_input.setObjectName(u"location_input")
        self.location_input.setFont(font)

        self.horizontalLayout.addWidget(self.location_input)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.update_location_button = QPushButton(LocationEdit)
        self.update_location_button.setObjectName(u"update_location_button")
        self.update_location_button.setFont(font)

        self.horizontalLayout.addWidget(self.update_location_button)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 3)
        self.horizontalLayout.setStretch(3, 2)

        self.retranslateUi(LocationEdit)

        QMetaObject.connectSlotsByName(LocationEdit)
    # setupUi

    def retranslateUi(self, LocationEdit):
        LocationEdit.setWindowTitle(QCoreApplication.translate("LocationEdit", u"Form", None))
        self.location_label.setText(QCoreApplication.translate("LocationEdit", u"Location:", None))
        self.update_location_button.setText(QCoreApplication.translate("LocationEdit", u"Update Location", None))
    # retranslateUi


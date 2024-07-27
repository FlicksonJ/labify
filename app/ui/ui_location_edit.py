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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from app.ui.upper_case_line_edit import UppercaseLineEdit

class Ui_LocationEdit(object):
    def setupUi(self, LocationEdit):
        if not LocationEdit.objectName():
            LocationEdit.setObjectName(u"LocationEdit")
        LocationEdit.resize(842, 95)
        LocationEdit.setMaximumSize(QSize(16777215, 100))
        LocationEdit.setStyleSheet(u"* {\n"
"       background: #fff\n"
"}\n"
"\n"
"QLabel {\n"
"       color: #fff;\n"
"       background: rgb(0, 159, 161);\n"
"       padding-left: 5px;\n"
"       padding-right: 5px;\n"
"}\n"
"\n"
"#location_label {\n"
"	background: #fff;\n"
"	color: rgb(0, 159, 161);\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit {\n"
"       border: 1px solid rgb(0, 159, 161);\n"
"       padding-left: 10px;\n"
"       color: rgb(0, 159, 161)\n"
"}\n"
"\n"
"#name_input:hover {\n"
"       border: 2px solid rgb(0, 159, 161);\n"
"}\n"
"\n"
"QPushButton {\n"
"       border: 1px solid;\n"
"       margin: 0;\n"
"       height: 40px;\n"
"       color: rgb(0, 159, 161);\n"
"       border-color: rgb(0, 159, 161);\n"
"       padding: 5px;\n"
"       border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"       background: rgb(0, 159, 161);\n"
"       color: #fff;\n"
"}\n"
"\n"
"#location_input {\n"
"       color: rgb(0, 159, 161);\n"
"}\n"
"\n"
"#location_input:hover {\n"
"       color: rgb(52, 62, 162);\n"
"}\n"
"\n"
"#location_in"
                        "put:on {\n"
"       border: 2px solid rgba(0, 159, 161, 10%);\n"
"}")
        self.verticalLayout = QVBoxLayout(LocationEdit)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(LocationEdit)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setItalic(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.location_label = QLabel(LocationEdit)
        self.location_label.setObjectName(u"location_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location_label.sizePolicy().hasHeightForWidth())
        self.location_label.setSizePolicy(sizePolicy)
        self.location_label.setMaximumSize(QSize(16777215, 45))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.location_label.setFont(font1)

        self.horizontalLayout.addWidget(self.location_label)

        self.location_input = UppercaseLineEdit(LocationEdit)
        self.location_input.setObjectName(u"location_input")
        self.location_input.setMinimumSize(QSize(0, 45))
        self.location_input.setMaximumSize(QSize(16777215, 45))
        font2 = QFont()
        font2.setPointSize(18)
        self.location_input.setFont(font2)

        self.horizontalLayout.addWidget(self.location_input)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.update_location_button = QPushButton(LocationEdit)
        self.update_location_button.setObjectName(u"update_location_button")
        self.update_location_button.setMaximumSize(QSize(16777215, 45))
        self.update_location_button.setFont(font2)

        self.horizontalLayout.addWidget(self.update_location_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(LocationEdit)

        QMetaObject.connectSlotsByName(LocationEdit)
    # setupUi

    def retranslateUi(self, LocationEdit):
        LocationEdit.setWindowTitle(QCoreApplication.translate("LocationEdit", u"Form", None))
        self.label.setText(QCoreApplication.translate("LocationEdit", u"Enter the new location in the store for the selected item", None))
        self.location_label.setText(QCoreApplication.translate("LocationEdit", u"Store Location:", None))
        self.update_location_button.setText(QCoreApplication.translate("LocationEdit", u"Update Location", None))
    # retranslateUi


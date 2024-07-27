# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'move_item_input.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from . import resources_rc

class Ui_MoveItem(object):
    def setupUi(self, MoveItem):
        if not MoveItem.objectName():
            MoveItem.setObjectName(u"MoveItem")
        MoveItem.resize(996, 77)
        MoveItem.setMaximumSize(QSize(16777215, 16777215))
        MoveItem.setStyleSheet(u"* {\n"
"       background: #fff\n"
"}\n"
"\n"
"QLabel {\n"
"       background: #fff;\n"
"       color: rgb(0, 159, 161);\n"
"       padding-left: 5px;\n"
"       padding-right: 5px;\n"
"		font-weight: bold;\n"
"}\n"
"\n"
"#label {\n"
"		font-weight: normal;\n"
"       color: #fff;\n"
"       background: rgb(0, 159, 161);\n"
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
"#location_input,\n"
"#lab_input\n"
"{\n"
"       color: rgb(0, 159, 161);\n"
"}\n"
"\n"
"#location_input:hover,\n"
"#lab_inpu"
                        "t:hover\n"
"{\n"
"       color: rgb(52, 62, 162);\n"
"}\n"
"\n"
"#location_input::drop-down,\n"
"#lab_input::drop-down\n"
"{\n"
"       border: 0px;\n"
"}\n"
"\n"
"#location_input::down-arrow,\n"
"#lab_input::down-arrow\n"
"{\n"
"       image: url(:/icon/images/down-arrow.ico);\n"
"       width: 15px;\n"
"       height: 15px;\n"
"       margin-right: 20px;\n"
"		margin-left: 20px;\n"
"}\n"
"\n"
"#location_input:on,\n"
"#lab_input:on\n"
"{\n"
"       border: 2px solid rgba(0, 159, 161, 10%);\n"
"}")
        self.verticalLayout = QVBoxLayout(MoveItem)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(MoveItem)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.item_location_label = QLabel(MoveItem)
        self.item_location_label.setObjectName(u"item_location_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_location_label.sizePolicy().hasHeightForWidth())
        self.item_location_label.setSizePolicy(sizePolicy)
        self.item_location_label.setMaximumSize(QSize(16777215, 45))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.item_location_label.setFont(font1)

        self.horizontalLayout.addWidget(self.item_location_label)

        self.qty_label = QLabel(MoveItem)
        self.qty_label.setObjectName(u"qty_label")
        self.qty_label.setMaximumSize(QSize(16777215, 45))
        self.qty_label.setFont(font1)
        self.qty_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.qty_label)

        self.qty_input = QLineEdit(MoveItem)
        self.qty_input.setObjectName(u"qty_input")
        self.qty_input.setMaximumSize(QSize(16777215, 45))
        font2 = QFont()
        font2.setPointSize(18)
        self.qty_input.setFont(font2)

        self.horizontalLayout.addWidget(self.qty_input)

        self.label_2 = QLabel(MoveItem)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.lab_input = QComboBox(MoveItem)
        self.lab_input.setObjectName(u"lab_input")
        self.lab_input.setMaximumSize(QSize(16777215, 45))
        self.lab_input.setFont(font2)

        self.horizontalLayout.addWidget(self.lab_input)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.move_item_button = QPushButton(MoveItem)
        self.move_item_button.setObjectName(u"move_item_button")
        self.move_item_button.setMaximumSize(QSize(16777215, 45))
        self.move_item_button.setFont(font2)

        self.horizontalLayout.addWidget(self.move_item_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(MoveItem)

        QMetaObject.connectSlotsByName(MoveItem)
    # setupUi

    def retranslateUi(self, MoveItem):
        MoveItem.setWindowTitle(QCoreApplication.translate("MoveItem", u"Form", None))
        self.label.setText(QCoreApplication.translate("MoveItem", u"Enter the new location for the selected item", None))
        self.item_location_label.setText(QCoreApplication.translate("MoveItem", u"Item", None))
        self.qty_label.setText(QCoreApplication.translate("MoveItem", u"Qty", None))
        self.label_2.setText(QCoreApplication.translate("MoveItem", u"Move To", None))
        self.move_item_button.setText(QCoreApplication.translate("MoveItem", u"Move Item", None))
    # retranslateUi


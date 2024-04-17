# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_entry.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_ItemEntry(object):
    def setupUi(self, ItemEntry):
        if not ItemEntry.objectName():
            ItemEntry.setObjectName(u"ItemEntry")
        ItemEntry.resize(1291, 46)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ItemEntry.sizePolicy().hasHeightForWidth())
        ItemEntry.setSizePolicy(sizePolicy)
        ItemEntry.setStyleSheet(u"* {\n"
"	background: #fff;\n"
"}\n"
"\n"
"#itemEntry {\n"
"	margin-bottom: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: rgb(0, 159, 161);\n"
"	font-size: 15pt;\n"
"	max-height: 35px;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"#add_entry_values QLabel {\n"
"	border: 1px solid rgb(0, 159, 161);\n"
"	border-radius: 10px;\n"
"}")
        self.layoutWidget = QWidget(ItemEntry)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1291, 41))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.id = QLabel(self.layoutWidget)
        self.id.setObjectName(u"id")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.id.sizePolicy().hasHeightForWidth())
        self.id.setSizePolicy(sizePolicy1)
        self.id.setMaximumSize(QSize(45, 35))

        self.horizontalLayout.addWidget(self.id)

        self.add_entry_values = QGroupBox(self.layoutWidget)
        self.add_entry_values.setObjectName(u"add_entry_values")
        self.horizontalLayoutWidget = QWidget(self.add_entry_values)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(-1, -1, 1237, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.name = QLabel(self.horizontalLayoutWidget)
        self.name.setObjectName(u"name")
        sizePolicy1.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy1)
        self.name.setMinimumSize(QSize(510, 0))
        self.name.setMaximumSize(QSize(510, 37))
        self.name.setStyleSheet(u"margin-left: 1px;")

        self.horizontalLayout_2.addWidget(self.name)

        self.qty = QLabel(self.horizontalLayoutWidget)
        self.qty.setObjectName(u"qty")
        sizePolicy1.setHeightForWidth(self.qty.sizePolicy().hasHeightForWidth())
        self.qty.setSizePolicy(sizePolicy1)
        self.qty.setMinimumSize(QSize(150, 0))
        self.qty.setMaximumSize(QSize(150, 37))

        self.horizontalLayout_2.addWidget(self.qty)

        self.lab = QLabel(self.horizontalLayoutWidget)
        self.lab.setObjectName(u"lab")
        sizePolicy1.setHeightForWidth(self.lab.sizePolicy().hasHeightForWidth())
        self.lab.setSizePolicy(sizePolicy1)
        self.lab.setMinimumSize(QSize(345, 0))
        self.lab.setMaximumSize(QSize(345, 37))

        self.horizontalLayout_2.addWidget(self.lab)

        self.location = QLabel(self.horizontalLayoutWidget)
        self.location.setObjectName(u"location")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.location.sizePolicy().hasHeightForWidth())
        self.location.setSizePolicy(sizePolicy2)
        self.location.setMinimumSize(QSize(200, 0))
        self.location.setMaximumSize(QSize(200, 37))
        self.location.setStyleSheet(u"margin-right: 10px;")

        self.horizontalLayout_2.addWidget(self.location)


        self.horizontalLayout.addWidget(self.add_entry_values)


        self.retranslateUi(ItemEntry)

        QMetaObject.connectSlotsByName(ItemEntry)
    # setupUi

    def retranslateUi(self, ItemEntry):
        ItemEntry.setWindowTitle(QCoreApplication.translate("ItemEntry", u"Form", None))
        self.id.setText(QCoreApplication.translate("ItemEntry", u"1", None))
        self.add_entry_values.setTitle(QCoreApplication.translate("ItemEntry", u"GroupBox", None))
        self.name.setText(QCoreApplication.translate("ItemEntry", u"TextLabel", None))
        self.qty.setText(QCoreApplication.translate("ItemEntry", u"TextLabel", None))
        self.lab.setText(QCoreApplication.translate("ItemEntry", u"TextLabel", None))
        self.location.setText(QCoreApplication.translate("ItemEntry", u"TextLabel", None))
    # retranslateUi


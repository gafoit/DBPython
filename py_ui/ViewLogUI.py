# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ViewLogUI.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateTimeEdit,
    QDialog, QDialogButtonBox, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(252, 132)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.dateTimeEdit_2 = QDateTimeEdit(Dialog)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setDateTime(QDateTime(QDate(2024, 12, 1), QTime(1, 0, 0)))
        self.dateTimeEdit_2.setTime(QTime(1, 0, 0))
        self.dateTimeEdit_2.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.dateTimeEdit_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label)

        self.dateTimeEdit = QDateTimeEdit(Dialog)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setDate(QDate(2024, 12, 1))
        self.dateTimeEdit.setTime(QTime(0, 0, 0))
        self.dateTimeEdit.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.dateTimeEdit)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_3.addWidget(self.comboBox)


        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e", None))
        self.dateTimeEdit_2.setDisplayFormat(QCoreApplication.translate("Dialog", u"dd.MM.yyyy HH:mm", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u043b\u043e\u0433\u0438", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0421", None))
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("Dialog", u"dd.MM.yyyy HH:mm", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u" \u0422\u0438\u043f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Insert", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Update", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Delete", None))

    # retranslateUi


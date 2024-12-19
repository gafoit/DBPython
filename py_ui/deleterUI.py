# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deleterUI.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(324, 221)
        Dialog.setStyleSheet(u"font: 9pt \"Fixedsys\";")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.spinBox = QSpinBox(Dialog)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(500000)

        self.horizontalLayout_3.addWidget(self.spinBox)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0445 \u0438\u0437 \u0442\u0430\u0431\u043b\u0438\u0446", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0443\u0441\u043b\u043e\u0432\u0438\u0435 (\u043f\u0440\u043e\u0441\u0442\u043e \u0447\u0438\u0441\u043b\u043e)", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"restraunts", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"menu", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"rate", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u043e\u043b\u0431\u0446\u0430 \u0443\u0441\u043b\u043e\u0432\u0438\u044f \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u0412\u0438\u0434 \u0438\u0442\u043e\u0433\u043e\u0432\u043e\u0433\u043e \u0437\u0430\u043f\u0440\u043e\u0441\u0430 \u0431\u0443\u0434\u0435\u0442 \u043f\u0440\u0438\u043c\u0435\u0440\u043d\u043e \u0442\u0430\u043a\u0438\u043c: </p><p><span style=\" font-weight:700;\">delete from *\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u044b*</span></p><p><span style=\" font-weight:700;\">where *\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u043e\u043b\u0431\u0446\u0430* = *\u0443\u0441\u043b\u043e\u0432\u0438\u0435*</span></p></body></html>", None))
    # retranslateUi


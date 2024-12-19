# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AirUpdateUI.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        font = QFont()
        font.setFamilies([u"Fixedsys"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"font: 9pt \"Fixedsys\";")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.spinBox_6 = QSpinBox(Dialog)
        self.spinBox_6.setObjectName(u"spinBox_6")

        self.horizontalLayout_7.addWidget(self.spinBox_6)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.spinBox = QSpinBox(Dialog)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_2.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.spinBox_2 = QSpinBox(Dialog)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.horizontalLayout_3.addWidget(self.spinBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.spinBox_3 = QSpinBox(Dialog)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.horizontalLayout_4.addWidget(self.spinBox_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.spinBox_4 = QSpinBox(Dialog)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.horizontalLayout_5.addWidget(self.spinBox_4)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.spinBox_5 = QSpinBox(Dialog)
        self.spinBox_5.setObjectName(u"spinBox_5")

        self.horizontalLayout_6.addWidget(self.spinBox_5)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u0441\u0430\u043c\u043e\u043b\u0451\u0442\u0430", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"ID \u0418\u0437\u043c\u0435\u043d\u044f\u0435\u043c\u043e\u0433\u043e \u0421\u0430\u043c\u043e\u043b\u0435\u0442\u0430", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u044b\u0439 id \u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u044b\u0439 id \u041e\u0431\u0448\u0438\u0432\u043a\u0438", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u044b\u0439 id \u043a\u043b\u0430\u0441\u0441\u0430 ", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u043e\u0435 \u041a\u043e\u043b-\u0432\u043e \u043c\u0435\u0441\u0442", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u043e\u0435 \u041a\u043e\u043b-\u0432\u043e \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u0435\u0439", None))
    # retranslateUi


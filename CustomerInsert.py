from PySide6 import QtCore, QtWidgets, QtGui
from py_ui.CustomerInsertUI import Ui_Dialog
from Connector import insert_customer, con
from ErrDialog import ErrDialog


class CustomerInsert(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def accept(self):
        try:
            insert_customer(con,
                       self.ui.lineEdit_2.text(),
                       self.ui.spinBox.value(),
                       self.ui.lineEdit.text()
                       )
        except Exception as e:
            err = ErrDialog()
            err.setErr(''.join(map(str, [i for i in e.args])))
            err.exec()
        self.accepted.emit()
        self.close()


from PySide6 import QtCore, QtWidgets, QtGui
from py_ui.OrdInsertUI import Ui_Dialog
from Connector import insert_ord, con
from ErrDialog import ErrDialog


class OrdInsert(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def accept(self):
        try:
            insert_ord(con,
                       self.ui.spinBox.value(),
                       self.ui.spinBox_2.value(),
                       self.ui.spinBox_3.value(),
                       self.ui.spinBox_4.value(),
                       self.ui.spinBox_5.value(),
                       self.ui.dateTimeEdit.text()
                       )
        except Exception as e:
            err = ErrDialog()
            err.setErr(''.join(map(str, [i for i in e.args])))
            err.exec()
        self.accepted.emit()
        self.close()


from PySide6 import QtCore, QtWidgets, QtGui
from py_ui.deleterUI import Ui_Dialog
from Connector import deleter, con
from ErrDialog import ErrDialog


class Deleter(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Удалялка')

    def accept(self):
        try:
            deleter(con,
                        self.ui.comboBox.currentText(),
                        self.ui.lineEdit.text(),
                        self.ui.spinBox.value()
                        )
        except Exception as e:
            err = ErrDialog()
            err.setErr(''.join(map(str, [i for i in e.args])))
            err.exec()
        self.accepted.emit()
        self.close()

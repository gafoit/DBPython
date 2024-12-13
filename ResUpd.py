from PySide6 import QtCore, QtWidgets, QtGui
from py_ui.resUpdUI import Ui_Dialog
from Connector import update_restraunt, con
from ErrDialog import ErrDialog


class ResUpdDialog(QtWidgets.QWidget):
    accepted = QtCore.Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Обновление существующего заведения')

    def accept(self):
        try:
            update_restraunt(con, self.ui.spinBox_2.value(), self.ui.lineEdit.text(),
                             self.ui.spinBox.value())
        except Exception as e:
            err = ErrDialog()
            err.setErr(''.join(map(str, [i for i in e.args])))
            err.exec()
        self.accepted.emit()
        self.close()

    def reject(self):
        self.close()

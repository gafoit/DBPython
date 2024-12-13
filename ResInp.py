from PySide6 import QtCore, QtWidgets, QtGui
from py_ui.ResInpUI import Ui_Dialog
from Connector import insert_restraunt, con
from ErrDialog import ErrDialog


class ResInpDialog(QtWidgets.QWidget):
    accepted = QtCore.Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Вставка нового заведения')
        self.ui.spinBox.setMinimum(1)
        self.ui.checkBox.checkStateChanged.connect(self.changeMax)

    def changeMax(self):
        if self.ui.checkBox.isChecked():
            self.ui.spinBox.setMaximum(10000)
        else:
            self.ui.spinBox.setMaximum(5)

    def accept(self):
        try:
            insert_restraunt(con, self.ui.lineEdit.text(), self.ui.spinBox.value(),
                             't' if self.ui.checkBox.isChecked() else 'f')
        except Exception as e:
            err = ErrDialog()
            err.setErr(''.join(map(str, [i for i in e.args])))
            err.exec()
        self.accepted.emit()
        self.close()

    def reject(self):
        self.close()

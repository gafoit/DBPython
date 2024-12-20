from PySide6 import QtCore, QtWidgets, QtGui
from py_ui.timeWalkUI import Ui_Dialog
from Connector import otkat, con
from ErrDialog import ErrDialog


class otkat(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('откат')

    def accept(self):
        try:
            otkat(con,
                        self.ui.spinBox.value()
                        )
        except Exception as e:
            err = ErrDialog()
            err.setErr(''.join(map(str, [i for i in e.args])))
            err.exec()
        self.accepted.emit()
        self.close()

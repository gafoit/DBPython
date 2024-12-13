from PySide6 import QtCore, QtWidgets, QtGui
from py_ui.RankUpdateUI import Ui_Dialog
from Connector import update_rank, con
from ErrDialog import ErrDialog


class RateUpdate(QtWidgets.QWidget):
    accepted = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Обновление оценки блюда')

    def accept(self):
        try:
            update_rank(con,
                        self.ui.spinBox_4.value(),
                        self.ui.spinBox_2.value(),
                        self.ui.spinBox_3.value(),
                        self.ui.spinBox.value(),
                        self.ui.dateEdit.text()
                        )
        except Exception as e:
            err = ErrDialog()
            err.setErr(''.join(map(str, [i for i in e.args])))
            err.exec()
        self.accepted.emit()
        self.close()

    def reject(self):
        self.close()

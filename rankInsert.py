from PySide6 import QtCore, QtWidgets, QtGui
from py_ui.RankInsertUI import Ui_Dialog
from Connector import insert_rank, con
from ErrDialog import ErrDialog


class RateInsert(QtWidgets.QWidget):
    accepted = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Вставка новой оценки блюда')

    def accept(self):
        try:
            insert_rank(con,
                        self.ui.spinBox_3.value(),
                        self.ui.spinBox_2.value(),
                        self.ui.spinBox.value(),
                        self.ui.dateTimeEdit.text()
                        )
        except Exception as e:
            err = ErrDialog()
            err.setErr(''.join(map(str, [i for i in e.args])))
            err.exec()
        self.accepted.emit()
        self.close()

    def reject(self):
        self.close()

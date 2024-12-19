from PySide6 import QtCore, QtWidgets, QtGui
from py_ui.SumRepUI import Ui_Dialog
from Connector import get_summary_report, con
from ErrDialog import ErrDialog


class SumRep(QtWidgets.QDialog):
    acceptedL = QtCore.Signal(str, list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Получить логи за даты')

    def accept(self):
        table = list()

        try:

            table = get_summary_report(con,
                                       't' if self.ui.checkBox.isChecked() else 'f',
                                       't' if self.ui.checkBox_2.isChecked() else 'f',
                                       't' if self.ui.checkBox_3.isChecked() else 'f'
                                       )
        except Exception as e:
            err = ErrDialog()
            err.setErr(''.join(map(str, [i for i in e.args])))
            err.exec()
        self.acceptedL.emit('Отчёт', table)
        self.accepted.emit()
        self.close()


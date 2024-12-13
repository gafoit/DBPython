from PySide6 import QtCore, QtWidgets, QtGui
from py_ui.ViewLogUI import Ui_Dialog
from Connector import get_view_logs, con
from ErrDialog import ErrDialog

class Viewlog(QtWidgets.QWidget):
    acceptedL = QtCore.Signal(str,list)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Получить логи за даты')

    def accept(self):
        table = list()
        try:
            table = get_view_logs(con, self.ui.dateTimeEdit.text(), self.ui.dateTimeEdit_2.text(),self.ui.comboBox.currentText(),'DD.MM.YYYY HH24:MI')
        except Exception as e:
            err = ErrDialog()
            err.setErr(''.join(map(str, [i for i in e.args])))
            err.exec()
        self.acceptedL.emit('Часть логов',table)
        self.close()

    def reject(self):
        self.close()

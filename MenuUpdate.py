from PySide6 import QtCore, QtWidgets, QtGui
from py_ui.MenuUpdateUI import Ui_Dialog
from Connector import update_menu, con
from ErrDialog import ErrDialog


class MenuUpdate(QtWidgets.QWidget):
    accepted = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Обновление блюда')

    def accept(self):
        try:
            update_menu(con,
                        self.ui.spinBox_2.value(),
                        self.ui.spinBox.value() if self.ui.spinBox.value()!=0 else None,
                        self.ui.lineEdit.text(),
                        self.ui.spinBox_3.value() if self.ui.spinBox_3.value()!=0 else None,
                        self.ui.spinBox_4.value() if self.ui.spinBox_4.value()!=0 else None,
                        self.ui.spinBox_5.value() if self.ui.spinBox_5.value()!=0 else None
                        )
        except Exception as e:
            err = ErrDialog()
            err.setErr(''.join(map(str, [i for i in e.args])))
            err.exec()
        self.accepted.emit()
        self.close()

    def reject(self):
        self.close()

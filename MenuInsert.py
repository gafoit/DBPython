from PySide6 import QtCore, QtWidgets, QtGui
from py_ui.MenuInsertUI import Ui_Dialog
from Connector import insert_menu, con
from ErrDialog import ErrDialog


class MenuInsert(QtWidgets.QWidget):
    accepted = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Вставка нового блюда')
        self.ui.spinBox_4.setMaximum(500000)
        self.ui.spinBox.setMaximum(500000)

    def accept(self):
        try:
            insert_menu(con,
                        self.ui.spinBox.value() if self.ui.spinBox.value()!=0 else None,
                        self.ui.lineEdit.text(),
                        self.ui.spinBox_2.value(),
                        self.ui.spinBox_3.value(),
                        self.ui.spinBox_4.value() if self.ui.spinBox_4.value()!=0 else None
                        )
        except Exception as e:
            err = ErrDialog(self.parent())
            err.setErr(''.join(map(str, [i for i in e.args])))
            err.exec()
        self.accepted.emit()
        self.close()

    def reject(self):
        self.close()

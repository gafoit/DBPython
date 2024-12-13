import PySide6.QtCore
from PySide6 import QtCore, QtWidgets, QtGui
from py_ui.ErrDialogUI import Ui_Dialog


class ErrDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def setErr(self, errMessage):
        #print(errMessage)
        self.ui.textEdit.setText(errMessage.encode('Windows-1251').decode('utf-8'))


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    dialog = ErrDialog()
    dialog.setErr("Ошибка: что-то пошло не так!")
    dialog.exec()  # Используем exec() для модального показа диалога
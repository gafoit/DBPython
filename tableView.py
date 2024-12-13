from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QHeaderView, QAbstractItemView

from py_ui.TableViewWidgetUI import Ui_Form


class TableView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.tableView.setAlternatingRowColors(True)

    def setColumns(self, column_names:list):
        self.ui.tableView.setColumnCount(len(column_names))
        self.ui.tableView.setHorizontalHeaderLabels([str(i) for i in column_names])

    def setRows(self, table:list):
        self.ui.tableView.setRowCount(len(table))
        for i in range(self.ui.tableView.rowCount()):
            for j in range(len(table[0])):
                self.ui.tableView.setItem(i, j, QtWidgets.QTableWidgetItem(str(table[i][j])))
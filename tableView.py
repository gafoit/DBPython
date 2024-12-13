from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QHeaderView, QAbstractItemView

from py_ui.TableViewWidgetUI import Ui_Form


class TableView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(
            """
                QTableWidget {
                    alternate-background-color: #C7E7C7; /* Зелёный для альтернативных строк */
                    background-color: #D8BFD8; /* Сиреневый основной фон */
                }
                QHeaderView::section {
                    background-color: #C7E7C7; /* Зелёный фон для заголовков */
                    color: #2F4F2F; /* Тёмно-зелёный текст */
                    border: 1px solid #B4D8B4;
                    padding: 4px;
                    font-weight: bold; /* Жирный текст для акцента */
                }
                QTableCornerButton::section {
                    background-color: #C7E7C7; /* Цвет фона для угловой ячейки */
                    border: 1px solid #B4D8B4; /* Граница, чтобы она соответствовала остальным */
                }
            """
        )
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.tableWidget.setAlternatingRowColors(True)

    def setColumns(self, column_names:list):
        self.ui.tableWidget.setColumnCount(len(column_names))
        self.ui.tableWidget.setHorizontalHeaderLabels([str(i) for i in column_names])

    def setRows(self, table:list):
        self.ui.tableWidget.setRowCount(len(table))
        for i in range(self.ui.tableWidget.rowCount()):
            for j in range(len(table[0])):
                self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(table[i][j])))
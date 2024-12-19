import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QHeaderView

from AirInsert import AirInsert
from AirUpdate import AirUpdate
from CustomerInsert import CustomerInsert
from CustomerUpdate import CustomerUpdate
from MenuInsert import MenuInsert
from MenuUpdate import MenuUpdate
from OrdInsert import OrdInsert
from OrdUpdate import OrdUpdate
from deleter import Deleter
from py_ui.mainframe import Ui_MainWindow
from DBTables import *
from Connector import con, get_menu, get_rate, get_restraunt, get_entity_log, commit, get_air, get_customer, get_ord
from rankUpdate import RateUpdate
from sumRep import SumRep
from tableView import TableView
from ViewLog import Viewlog
from timeWalk import otkat


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Input_Dialog = None
        self.ui.tabWidget.setCurrentIndex(0)

        self.ui.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.pushButton.clicked.connect(self.chooseDialog)
        self.ui.pushButton_2.clicked.connect(self.chooseDialog)
        self.ui.pushButton_3.clicked.connect(self.chooseDialog)
        self.ui.pushButton_4.clicked.connect(self.chooseDialog)
        self.ui.pushButton_5.clicked.connect(self.chooseDialog)
        self.ui.pushButton_6.clicked.connect(self.chooseDialog)
        self.ui.pushButton_7.clicked.connect(self.chooseDialog)
        self.ui.pushButton_8.clicked.connect(self.chooseDialog)
        self.ui.pushButton_9.clicked.connect(self.chooseDialog)
        self.ui.pushButton_10.clicked.connect(self.chooseDialog)
        self.ui.pushButton_11.clicked.connect(self.setColumns)
        self.ui.pushButton_11.clicked.connect(self.setRows)
        self.ui.tabWidget.currentChanged.connect(self.setColumns)
        self.ui.tabWidget.currentChanged.connect(self.setRows)

    def chooseDialog(self):
        if self.Input_Dialog is None:
            match self.sender():
                case self.ui.pushButton:
                    self.Input_Dialog = AirInsert(self)
                    self.Input_Dialog.accepted.connect(self.accepted)
                case self.ui.pushButton_2:
                    self.Input_Dialog = OrdInsert(self)
                    self.Input_Dialog.accepted.connect(self.accepted)
                case self.ui.pushButton_3:
                    self.Input_Dialog = CustomerInsert(self)
                    self.Input_Dialog.accepted.connect(self.accepted)
                case self.ui.pushButton_4:
                    self.Input_Dialog = AirUpdate(self)
                    self.Input_Dialog.accepted.connect(self.accepted)
                case self.ui.pushButton_5:
                    self.Input_Dialog = OrdUpdate(self)
                    self.Input_Dialog.accepted.connect(self.accepted)
                case self.ui.pushButton_6:
                    self.Input_Dialog = CustomerUpdate(self)
                    self.Input_Dialog.accepted.connect(self.accepted)
                case self.ui.pushButton_7:
                    self.Input_Dialog = Deleter(self)
                    self.Input_Dialog.accepted.connect(self.accepted)
                case self.ui.pushButton_8:
                    self.Input_Dialog = Viewlog(self)
                    self.Input_Dialog.acceptedL.connect(self.acceptedList)
                case self.ui.pushButton_9:
                    self.Input_Dialog = otkat(self)
                    self.Input_Dialog.accepted.connect(self.accepted)
                case self.ui.pushButton_10:
                    self.Input_Dialog = SumRep(self)
                    self.Input_Dialog.acceptedL.connect(self.acceptedList)
                case _:
                    self.Input_Dialog = None
            self.Input_Dialog.show()
            self.Input_Dialog.rejected.connect(self.close_dialog)
        else:
            self.Input_Dialog.close()
            self.Input_Dialog = None

    def close_dialog(self):
        self.Input_Dialog = None
    """def setColumns(self):
        self.ui.tableWidget.setColumnCount(len(restraunts))
        self.ui.tableWidget.setHorizontalHeaderLabels([str(i) for i in restraunts])
        self.ui.tableWidget_2.setColumnCount(len(menu))
        self.ui.tableWidget_2.setHorizontalHeaderLabels([str(i) for i in menu])
        self.ui.tableWidget_3.setColumnCount(len(rate))
        self.ui.tableWidget_3.setHorizontalHeaderLabels([str(i) for i in rate])
        self.ui.tableWidget_4.setColumnCount(len(entity_log))
        self.ui.tableWidget_4.setHorizontalHeaderLabels([str(i) for i in entity_log])"""

    def  setColumns(self):
        self.ui.tableWidget.setColumnCount(len(get_air(con)[0]))
        self.ui.tableWidget.setHorizontalHeaderLabels([str(i) for i in get_air(con)[0]])
        self.ui.tableWidget_2.setColumnCount(len(get_customer(con)[0]))
        self.ui.tableWidget_2.setHorizontalHeaderLabels([str(i) for i in get_customer(con)[0]])
        self.ui.tableWidget_3.setColumnCount(len(get_ord(con)[0]))
        self.ui.tableWidget_3.setHorizontalHeaderLabels([str(i) for i in get_ord(con)[0]])
        self.ui.tableWidget_4.setColumnCount(len(entity_log))
        self.ui.tableWidget_4.setHorizontalHeaderLabels([str(i) for i in entity_log])

    def setRows(self):
        table = get_air(con)[1:]
        self.ui.tableWidget.setRowCount(len(table))
        for i in range(self.ui.tableWidget.rowCount()):
            for j in range(len(table[0])):
                self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(table[i][j])))
        table = get_customer(con)[1:]
        self.ui.tableWidget_2.setRowCount(len(table))
        for i in range(self.ui.tableWidget_2.rowCount()):
            for j in range(len(table[0])):
                self.ui.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(table[i][j])))
        table = get_ord(con)[1:]
        self.ui.tableWidget_3.setRowCount(len(table))
        for i in range(self.ui.tableWidget_3.rowCount()):
            for j in range(len(table[0])):
                self.ui.tableWidget_3.setItem(i, j, QtWidgets.QTableWidgetItem(str(table[i][j])))
        table = get_entity_log(con)
        self.ui.tableWidget_4.setRowCount(len(table))
        for i in range(self.ui.tableWidget_4.rowCount()):
            for j in range(len(table[0])):
                self.ui.tableWidget_4.setItem(i, j, QtWidgets.QTableWidgetItem(str(table[i][j])))

    def accepted(self):
        commit(con)

    def acceptedList(self, lab: str, table: list):
        if self.ui.tabWidget.count() > 4:
            self.ui.tabWidget.removeTab(4)
        t = TableView()
        t.setColumns(table[0])
        t.setRows(table[1:])
        self.ui.tabWidget.addTab(t, lab)
        self.ui.tabWidget.setCurrentIndex(4)


try:
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.setWindowTitle("БДшка")
    application.setStyleSheet("""
    QMainWindow{
        background:#C7E7C7;
        
    }
    QTabWidget::pane { 
        background: #C7E7C7; /* Зелёный фон панели вкладок */
        border: 3px solid #B4D8B4;
    }
    QDialog{
        background:#D8BFD8;
        
    }

    QTabBar::tab {
        background: #D8BFD8; /* Сиреневый цвет вкладки */
        color: #4F4F4F; /* Цвет текста на вкладке */
        padding: 5px;
        border: 3px solid #B4D8B4;
        border-radius: 5px;
        margin: 2px;
    }
    QTabWidget::tab-bar {
                alignment: center;
            }
    QTabBar::tab:selected {
        background: #C7E7C7; /* Зелёный цвет активной вкладки */
        color: #2F4F2F; /* Цвет текста активной вкладки */
    }
    QTabBar::tab:hover {
        background: #B4D8B4; /* Более насыщенный зелёный при наведении */
    }
    
    QPushButton {
        background-color: #C7E7C7; /* Зелёный для кнопок */
        border: 3px solid #B4D8B4;
        border-radius: 5px;
        padding: 5px;
        color: #4F4F4F; /* Цвет текста на кнопках */
    }
    QPushButton:hover {
        background-color: #B4D8B4; /* Более насыщенный зелёный при наведении */
    }
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
""")
    application.show()
    application.setColumns()
    application.setRows()
    sys.exit(app.exec())
except Exception as e:
    with open('errors.txt', 'a') as f:
        f.write(str(e) + '\n')

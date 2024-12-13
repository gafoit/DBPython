import sys
from PySide6 import QtCore, QtWidgets, QtGui

from MenuInsert import MenuInsert
from MenuUpdate import MenuUpdate
from ResInp import ResInpDialog
from ResUpd import ResUpdDialog
from deleter import Deleter
from py_ui.mainframe import Ui_MainWindow
from DBTables import *
from Connector import con,  get_menu, get_rate, get_restraunt, get_entity_log, commit
from rankInsert import RateInsert
from rankUpdate import RateUpdate
from sumRep import SumRep
from tableView import TableView
from ViewLog import Viewlog
from timeWalk import TimeWalk


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Input_Dialog = None
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
        match self.sender():
            case self.ui.pushButton:
                self.Input_Dialog = ResInpDialog()
                self.Input_Dialog.accepted.connect(self.accepted)
            case self.ui.pushButton_2:
                self.Input_Dialog = MenuInsert()
                self.Input_Dialog.accepted.connect(self.accepted)
            case self.ui.pushButton_3:
                self.Input_Dialog = RateInsert()
                self.Input_Dialog.accepted.connect(self.accepted)
            case self.ui.pushButton_4:
                self.Input_Dialog = ResUpdDialog()
                self.Input_Dialog.accepted.connect(self.accepted)
            case self.ui.pushButton_5:
                self.Input_Dialog = MenuUpdate()
                self.Input_Dialog.accepted.connect(self.accepted)
            case self.ui.pushButton_6:
                self.Input_Dialog = RateUpdate()
                self.Input_Dialog.accepted.connect(self.accepted)
            case self.ui.pushButton_7:
                self.Input_Dialog = Deleter()
                self.Input_Dialog.accepted.connect(self.accepted)
            case self.ui.pushButton_8:
                self.Input_Dialog = Viewlog()
                self.Input_Dialog.acceptedL.connect(self.acceptedList)
            case self.ui.pushButton_9:
                self.Input_Dialog = TimeWalk()
                self.Input_Dialog.accepted.connect(self.accepted)
            case self.ui.pushButton_10:
                self.Input_Dialog = SumRep()
                self.Input_Dialog.acceptedL.connect(self.acceptedList)
            case _:
                self.Input_Dialog = None
        self.Input_Dialog.show()

    def setColumns(self):
        self.ui.tableWidget.setColumnCount(len(restraunts))
        self.ui.tableWidget.setHorizontalHeaderLabels([str(i) for i in restraunts])
        self.ui.tableWidget_2.setColumnCount(len(menu))
        self.ui.tableWidget_2.setHorizontalHeaderLabels([str(i) for i in menu])
        self.ui.tableWidget_3.setColumnCount(len(rate))
        self.ui.tableWidget_3.setHorizontalHeaderLabels([str(i) for i in rate])
        self.ui.tableWidget_4.setColumnCount(len(entity_log))
        self.ui.tableWidget_4.setHorizontalHeaderLabels([str(i) for i in entity_log])

    def setRows(self):
        table = get_restraunt(con)
        self.ui.tableWidget.setRowCount(len(table))
        for i in range(self.ui.tableWidget.rowCount()):
            for j in range(len(table[0])):
                self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(table[i][j])))
        table = get_menu(con)
        self.ui.tableWidget_2.setRowCount(len(table))
        for i in range(self.ui.tableWidget_2.rowCount()):
            for j in range(len(table[0])):
                self.ui.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(table[i][j])))
        table = get_rate(con)
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
    application.setWindowTitle("OraDB")
    application.show()
    application.setColumns()
    application.setRows()
    sys.exit(app.exec())
except Exception as e:
    with open('errors.txt', 'a') as f:
        f.write(str(e) + '\n')

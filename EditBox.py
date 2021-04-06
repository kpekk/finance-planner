import re
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QDate

##Note: instead of QTableWisget.itemAt() use item(), itemAt() uses frkn pixels!
#TODO too much code repetition, get rid of this file ((somehow...))
class EditBox(QDialog):
    def __init__(self, parent): 
        super(QDialog, self).__init__(parent)

        def changeRow():
            #Get selected values
            date = self.date.date()
            income = "+" if (self.inComing.isChecked()) else "-"
            total = self.total.text()
            category = self.type.currentText()
            description = self.description.toPlainText() #can be empty

            #Get selected row
            selectedRow = sorted(self.parent().table.selectionModel().selectedRows(),reverse=True)[0].row()

            #Update values of selected row
            self.parent().table.setItem(selectedRow,0,QTableWidgetItem(date.toString("d/MM/yyyy")))
            self.parent().table.setItem(selectedRow,1,QTableWidgetItem(income))
            self.parent().table.setItem(selectedRow,2,QTableWidgetItem(total))
            self.parent().table.setItem(selectedRow,3,QTableWidgetItem(category))
            self.parent().table.setItem(selectedRow,4,QTableWidgetItem(description))

        def validateSum():
            if re.match(r"^[1-9]\d*(\.\d+)?$", self.total.text()):
                self.okButton.setDisabled(False)
            else:
                self.okButton.setDisabled(True)

        #Removes title bar and sets this as a popup
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | Qt.Popup)
        #Set position and size
        self.setGeometry(700,400,400,400)
        layout = QGridLayout(self)

        #Get old values
        selected = sorted(self.parent().table.selectionModel().selectedRows(),reverse=True)

        #Date
        #print(QDate.fromString(self.parent().table.item(selected[0].row(),0).text(), "dd/MM/yyyy"))
        layout.addWidget(QLabel("Date"),0,0,1,1)
        self.date = QDateEdit(calendarPopup=True)
        self.date.setDate(QDate.fromString(self.parent().table.item(selected[0].row(),0).text(), "dd/MM/yyyy"))
        layout.addWidget(self.date,0,1,1,3)
        
        #Income
        layout.addWidget(QLabel("Income"),1,0,1,1)
        self.inComing = QRadioButton()
        layout.addWidget(self.inComing,1,1,1,1)

        #Expense
        self.expenseLabel = QLabel("Expense")
        self.expenseLabel.setStyleSheet("QLabel{color:red;}")
        layout.addWidget(self.expenseLabel,1,2,1,1)
        self.expense = QRadioButton()
        layout.addWidget(self.expense,1,3,1,1)

        if self.parent().table.item(selected[0].row(),1).text() == "+":
            self.inComing.setChecked(True)
        else:
            self.expense.setChecked(True)
        
        #Sum
        layout.addWidget(QLabel("Sum"),2,0,1,1)
        self.total = QLineEdit()
        self.total.setText(self.parent().table.item(selected[0].row(),2).text())
        layout.addWidget(self.total,2,1,1,3)

        #Type
        layout.addWidget(QLabel("Type"),3,0,1,1)
        self.type = QComboBox()
        self.type.addItems(["Housing","Transportation","Food","Utilities","Personal","Education","Retirement","Savings","Entertainment"])
        self.type.setCurrentText(self.parent().table.item(selected[0].row(),3).text())
        layout.addWidget(self.type,3,1,1,3)
        
        #Description
        layout.addWidget(QLabel("Description"),4,0,1,1)
        self.description = QTextEdit()
        self.description.setFixedHeight(100)
        self.description.setText(self.parent().table.item(selected[0].row(),4).text())
        layout.addWidget(self.description,4,1,1,3)

        #Confirm
        self.okButton = QPushButton("OK")
        self.okButton.clicked.connect(changeRow)
        self.okButton.setDisabled(True)
        layout.addWidget(self.okButton,5,0,1,2)

        #This needs to be connected after okButton has been defined
        self.total.textChanged.connect(validateSum)
        if re.match(r"^[1-9]\d*(\.\d+)?$", self.total.text()):
            self.okButton.setDisabled(False)

        #Cancel
        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.clicked.connect(self.close)
        layout.addWidget(self.cancelButton,5,2,1,2)     

        self.exec_()
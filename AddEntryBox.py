import re
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QDate

class addEntryBox(QDialog):
    def __init__(self, parent): 
        super(QDialog, self).__init__(parent)

        def addRow():
            #Get selected values
            date = self.date.text()
            income = "+" if (self.inComing.isChecked()) else "-"
            total = self.total.text()
            category = self.type.currentText()
            description = self.description.toPlainText() #can be empty
            rowCount = self.parent().table.rowCount()

            #Add saved values as a new row
            self.parent().table.insertRow(rowCount)
            self.parent().table.setItem(rowCount,0,QTableWidgetItem(date))
            self.parent().table.setItem(rowCount,1,QTableWidgetItem(income))
            self.parent().table.setItem(rowCount,2,QTableWidgetItem(total))
            self.parent().table.setItem(rowCount,3,QTableWidgetItem(category))
            self.parent().table.setItem(rowCount,4,QTableWidgetItem(description))

        #Checks whether "total" row is numeric
        def validateSum():
            if re.match(r"^[1-9]\d*(\.\d+)?$", self.total.text()):
                self.okButton.setDisabled(False)
            else:
                self.okButton.setDisabled(True)

        #Removes title bar and sets self as a popup
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | Qt.Popup)
        #Set position and size
        self.setGeometry(700,400,400,200)
        layout = QGridLayout(self)

        #Entry = 1)date 2)out/in 3)sum 4)desc 5)type

        #Date
        layout.addWidget(QLabel("Date"),0,0,1,1)
        self.date = QLabel(parent.currentDate[1])
        layout.addWidget(self.date,0,1,1,2)
        
        #Income
        layout.addWidget(QLabel("Income"),1,0,1,1)
        self.inComing = QRadioButton()
        self.inComing.setChecked(True)
        layout.addWidget(self.inComing,1,1,1,1)

        #Expense
        self.expenseLabel = QLabel("Expense")
        self.expenseLabel.setStyleSheet("QLabel{color:red;}")
        layout.addWidget(self.expenseLabel,1,2,1,1)
        self.expense = QRadioButton()
        layout.addWidget(self.expense,1,3,1,1)
        
        #Sum
        layout.addWidget(QLabel("Sum"),2,0,1,1)
        self.total = QLineEdit()
        self.total.textChanged.connect(validateSum)
        layout.addWidget(self.total,2,1,1,3)

        #Type
        layout.addWidget(QLabel("Type"),3,0,1,1)
        self.type = QComboBox()
        self.type.addItems(["Housing","Transportation","Food","Utilities","Personal","Education","Retirement","Savings","Entertainment"])
        layout.addWidget(self.type,3,1,1,3)
        
        #Description
        layout.addWidget(QLabel("Description"),4,0,1,1)
        self.description = QTextEdit()
        self.description.setFixedHeight(100)
        layout.addWidget(self.description,4,1,1,3)

        #Confirm
        self.okButton = QPushButton("OK")
        self.okButton.clicked.connect(addRow)
        self.okButton.setDisabled(True)
        layout.addWidget(self.okButton,5,0,1,2)

        #Cancel
        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.clicked.connect(self.close)
        layout.addWidget(self.cancelButton,5,2,1,2)

        self.exec_()
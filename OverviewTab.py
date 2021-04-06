import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDate
from PyQt5 import QtCore
#Imports from files
from ConfirmationBox import ConfirmationBox
from Table import Table
from AddEntryBox import addEntryBox
from EditBox import EditBox
from themes import dark

class OverviewTab(QWidget):
    def __init__(self, parent): 
        super(QWidget, self).__init__(parent)

        #If selected display type is month, check if the month was changed, if yes, load new rows
        def monthChanged():
            self.currentDate = ["month", self.dateSelect.date().toString("MM/yyyy")]

            #If date changes (month or year-wise), redirect to loadNewRows()
            if self.oldDate[1] != self.currentDate[1]:
                print("date was chaaaaanged")
                loadNewRows()

        def yearChanged():
            #save new date
            self.currentDate = ["year", self.dateSelect.currentText()]
            loadNewRows()

        def dayChanged():
            self.currentDate = ["day", self.dateSelect.date().toString("MM/dd/yyyy")]
            loadNewRows()

        def saveTableToFile(dateAndType, table):
            #TODO move to separate file
            dateType = dateAndType[0]
            #month | day | year
            date = dateAndType[1].split("/")

            #get data from table
            data =[""]*table.rowCount()#= [[""]*5]*table.rowCount()
            for i in range(table.rowCount()):
                row = []
                for j in range(5):
                    row.append(table.item(i,j).text())
                    #print(self.table.item(i,j).text())
                data[i] = row

            #Easiest case: 1 day
            if dateType == "day":
                #Create or navigate to 'year' directory
                pathToFile = date[2]
                if not os.path.exists(pathToFile):
                    os.mkdir(pathToFile)

                #Create or navigate to 'month' directory
                pathToFile = os.path.join(date[2],date[0])
                if not os.path.exists(pathToFile):
                    os.mkdir(pathToFile)

                #Create or navigate to 'day' .txt file
                pathToFile = os.path.join(pathToFile, date[1]+".txt")
                #if not os.path.exists(pathToFile):
                with open(pathToFile, "w+") as file:
                    for entry in data:
                        for element in entry:
                            file.write(element+" ")#delimiter set to space, since trailing spaces are removed by trim()
                        file.write("\n")
            #TODO kuu
            #TODO aasta :)


        def loadNewRows():
            #Get pre-change date
            print("old date: ",self.oldDate)

            #dont do this if we still have the initial table
            #Save current rows to old date's file
            saveTableToFile(self.oldDate, self.table)
            
            #Remove current rows
            self.table.setRowCount(0)

            #Get current date
            print("new Date: ",self.currentDate)
            currentDate = self.currentDate
            
            #Find corresponding folder or create if doesnt exist
            #TODO ERALDI MEETODISSE

            dateType = currentDate[0]
            date = currentDate[1].split("/")
         
            if dateType == "day":
                #Create or navigate to 'year' directory
                pathToFile = date[2]
                if not os.path.exists(pathToFile):
                    os.mkdir(pathToFile)

                #Create or navigate to 'month' directory
                pathToFile = os.path.join(date[2],date[0])
                if not os.path.exists(pathToFile):
                    os.mkdir(pathToFile)

                #Create or navigate to 'day' .txt file
                pathToFile = os.path.join(pathToFile, date[1]+".txt")
                if os.path.exists(pathToFile):
                    with open(pathToFile, "r") as file:
                        print("fail")
                        for line in file:
                        
                            entry = line.split(" ")
                          
                            addTableRow(self,self.table,[entry[0],entry[1],entry[2],entry[3]," ".join(entry[4:]).rstrip()])


            #Update old date
            self.oldDate = currentDate

        def addTableRow(self, table, row_data):
            row = table.rowCount()
            table.setRowCount(row+1)
            col = 0
            for item in row_data:
                cell = QTableWidgetItem(str(item))
                table.setItem(row, col, cell)
                col += 1


        def selectDateType():
            dateType = self.dateType.currentText()

            #Yearly view, combobox
            if dateType == "Year":
                options = map(str,list((range(2020,2030))))
                self.dateSelect = QComboBox()

                #Connect to changed() method
                self.dateSelect.currentTextChanged.connect(yearChanged)
                self.dateSelect.addItems(options)

                #Save the current date
                self.currentDate = ["year", self.dateSelect.currentText()]

            #Calendar view
            else:
                self.dateSelect = QDateEdit(calendarPopup=True)

                if dateType == "Month":
                    #Set display type to month
                    self.dateSelect.setDisplayFormat("MM/yyyy")

                    #Connect to changed() method
                    self.dateSelect.dateChanged.connect(monthChanged)
                    
                    #Save the current date
                    self.currentDate = ["month", QDate.currentDate().toString("MM/yyyy")]
                
                    self.dateSelect.setCurrentSection(QDateTimeEdit.MonthSection)

                else:
                    #Daily view -> signal will be sent on every change
                    self.dateSelect.dateChanged.connect(dayChanged)

                    #Save the current date
                    self.currentDate = ["day", QDate.currentDate().toString("MM/dd/yyyy")]

                self.dateSelect.setDate(QDate.currentDate())    
            
            layout.addWidget(self.dateSelect,0,2,1,1)
        #####################################################################
        def editEntry():
            #get all selected rows
            selected = sorted(self.table.selectionModel().selectedRows(),reverse=True)
            #can't edit more than 1 line at once
            if len(selected) > 1:
                #Display error message to the user
                errorBox = QMessageBox()
                errorBox.setStyleSheet(dark)
                errorBox.setWindowFlag(QtCore.Qt.FramelessWindowHint)
                errorBox.setText("Max 1 row at a time")
                errorBox.setDetailedText("Only 1 row can be edited at once")
                errorBox.exec()

            elif len(selected) == 1:
                self.editBox = EditBox(self)    

        def addEntry():
            #Initiates addEntryBox, logic located there
            self.addEntryBox = addEntryBox(self)
            
        def deleteEntry():
            selected = sorted(self.table.selectionModel().selectedRows(),reverse=True)
            #If there are selected rows, initiate confirmation box
            if not len(selected) == 0:
                self.confirmation = ConfirmationBox(self)
        ###################################################################################################
        layout = QGridLayout(self)
        
        #coordinates: (x,y,z,w)
        # X = row
        # Y = column
        # Z = rowspan
        # W = colspan 


        #Table, needs to be defined before selectDateType()
        self.table = Table(self)
        layout.addWidget(self.table,1,0,4,4)
        #initial rows from file
        #loadNewRows(True)

        #Copy of currentDate for saving to the correct file later - needed?
        self.oldDate = ["day",QDate.currentDate().toString(("MM/dd/yyyy"))]

        #date type selector
        self.dateType = QComboBox()
        self.dateType.addItems(["Day","Month","Year"])
        self.dateType.currentTextChanged.connect(selectDateType)
        layout.addWidget(self.dateType,0,1,1,1)

        #will create date selector
        selectDateType()

        #For keeping track of currently selected date (initially current date, type = day)
        self.currentDate = ["day",QDate.currentDate().toString(("MM/dd/yyyy"))]
        

        #confirm choice
        self.confirmButton = QPushButton("Select")
        layout.addWidget(self.confirmButton,0,3,1,1)
        self.confirmButton.clicked.connect(sys.exit)

        #Edit entry
        self.editEntryButton = QPushButton("Edit entry")
        self.editEntryButton.clicked.connect(editEntry)
        layout.addWidget(self.editEntryButton,6,1,1,1)

        #Add entry
        self.addEntryButton = QPushButton("Add entry")
        self.addEntryButton.clicked.connect(addEntry)
        layout.addWidget(self.addEntryButton,6,2,1,1)

        #Delete entry
        self.deleteEntryButton = QPushButton("Delete entry")
        self.deleteEntryButton.clicked.connect(deleteEntry)
        layout.addWidget(self.deleteEntryButton,6,3,1,1)

        
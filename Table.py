from PyQt5.QtWidgets import *

class Table(QTableWidget):
    def __init__(self, parent): 
        super(QTableWidget, self).__init__(parent)

        #Set cells uneditable
        self.setEditTriggers(QTableWidget.NoEditTriggers)

        #Row = 1)date 2)out/in 3)sum 4)desc 5)type
        self.setColumnCount(5)
        for i in range(5):
            self.setColumnWidth(i,193)
        
        #TODO set row count dynamically
        #self.setRowCount(1)
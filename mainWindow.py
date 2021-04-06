import sys
import re
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtCore, QtWidgets
from themes import *

from Table import Table
from AddEntryBox import addEntryBox
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #set size
        self.setFixedSize(1040,840)

        #removes title bar
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        #set stylesheet
        self.setStyleSheet(dark) 
    
        self.centralWidget = TabsWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.show()

#These imports are moved to the end of the file to avoid circular dependency
#https://stackoverflow.com/questions/894864/circular-dependency-in-python
from OverviewTab import *  
from TabsWidget import TabsWidget
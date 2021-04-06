from PyQt5.QtWidgets import *
from OverviewTab import OverviewTab
from mainWindow import *

class TabsWidget(QWidget):
    def __init__(self, parent):
        
        super(QWidget, self).__init__(parent)
        self.tabs = QTabWidget()

        #Overview tab
        self.tab1 = OverviewTab(self)
        self.tabs.addTab(self.tab1,"Overview")

        #TODO 2nd tab
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab2,"Graph")

        # Add tabs to widget
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
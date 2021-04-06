from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

class ConfirmationBox(QDialog):
    def __init__(self, parent): 
        super(QDialog, self).__init__(parent)

        def deleteSelectedRows():
            selected = sorted(self.parent().table.selectionModel().selectedRows(),reverse=True)
            for i in range(len(selected)):
                    self.parent().table.removeRow(selected[i].row())
            self.close()
        
        #Removes title bar and sets this as a popup
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | Qt.Popup)
        #Set position and size
        self.setGeometry(900,500,150,100)
        
        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(deleteSelectedRows)
        self.buttonBox.rejected.connect(self.reject)

        #HBox layout for aligning the label
        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(QLabel("Are you sure?"))
        h_box.addStretch()

        self.layout = QVBoxLayout()
        self.layout.addLayout(h_box)
        self.layout.addWidget(self.buttonBox)

        self.setLayout(self.layout)
        
        self.exec_()
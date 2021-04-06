from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


QApplication.setStyle("Fusion")

dark = """
QWidget{
    /*Will be overriden if defined below*/
    background-color: rgb(57,57,57);
    color: rgb(78,239,78);
}
QPushButton{
    background-color:rgb(53,53,53); 
}
QPushButton:pressed{
    background-color:gray;   
}
QPushButton:disabled{
    background-color:rgb(51,51,51); 
    color: red;  
}
QLineEdit{
    background-color:rgb(53,53,53);
}
QComboBox{
    background-color:rgb(51,51,51);
}
QMainWindow{
    background-color: rgb(57,57,57);
    border: 3px solid rgb(78,239,78);
}
QDialog{
    border: 1px solid green;
}
"""

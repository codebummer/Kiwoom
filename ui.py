from kiwoom.kiwoom import *
from PyQt5.QtWidgets import *
import sys



class Ui_class():
    def __init__(self):

        self.app = QApplication(sys.argv) #Initiate variables to run applications
        self.kiwoom = Kiwoom()
        self.app.exec_() #Event loop to keep the program running

from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
from config.errorCode import *


class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()

        #Event Loop
        self.login_event_loop = None
        ###########

        #Variable Collection
        self.account_num = None
        ############

        self.get_ocx_instance()
        self.event_slots()

        self.signal_login_CommConnect()
        # self.event_slots()
        self.get_account_info()
        self.detail_account_info()


    def get_ocx_instance(self):
        self.setControl('KHOPENAPI.KHOpenAPICtrl.1')

    def event_slots(self):
        self.OnEventConnect.connect(self.login_slot)

    def login_slot(self, errCode):
        print(errors(errCode))

        self.login_event_loop.exit()

    def signal_login_CommConnect(self):
        self.dynamicCall('CommConnect()')

        self.login_event_loop = QEventLoop() #An event loop executed to keep the program running
        self.login_event_loop.exec_()

    # def login_slot(self, errCode):
    #     print(errors(errCode))
    #
    #     self.login_event_loop.exit()

    def get_account_info(self):
        account_list = self.dynamicCall('GetLonginInfo(String)', 'ACCNO')
        account_num = account_list.split(';')[0]
        print(f'My account number is {account_num}')

    def detail_account_info(self):

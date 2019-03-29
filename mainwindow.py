# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget
from ui.untitled import Ui_Form
from load_from_db import mssql,MsData,TableQuery


class Db_window(QWidget,Ui_Form):
    def __init__(self, parent=None):
        super(QWidget,self).__init__(parent)
        self.setupUi(self)
        # self.setEvent()
        self.show()

    # def setEvent(self):
    #     self.comboBox.currentTextChanged.connect(self.comboBoxTextChange)
        # self.comboBox_2.clicked.connect()



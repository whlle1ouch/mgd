# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication
from mainwindow import Db_window
import sys



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Db_window()
    sys.exit(app.exec_())
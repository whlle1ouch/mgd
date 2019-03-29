# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(511, 475)
        Form.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(230, 240, 181, 41))
        self.comboBox.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.comboBox.setAcceptDrops(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "111"))
        self.comboBox.setItemText(1, _translate("Form", "New Item"))
        self.comboBox.setItemText(2, _translate("Form", "New Item"))
        self.comboBox.setItemText(3, _translate("Form", "222"))
        self.comboBox.setItemText(4, _translate("Form", "333"))
        self.comboBox.setItemText(5, _translate("Form", "444"))
        self.comboBox.setItemText(6, _translate("Form", "555"))


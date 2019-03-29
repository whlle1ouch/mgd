# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'db.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import json

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 800)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 871, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 520, 351, 100))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(380, 530, 75, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "数据库"))

        self.comboBox.setItemText(0, _translate("Form", ""))
        with open('data/config.json','r') as f:
            self.database = json.loads(f.read())

        for i,d in enumerate(self.database.keys()):
            self.comboBox.setItemText(i+1,_translate("Form",d))

        self.comboBox_2.setAcceptDrops(True)
        self.comboBox_2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.label_2.setText(_translate("Form", "数据表"))
        self.comboBox_2.setItemText(0, _translate("Form", ""))
        self.comboBox_2.setItemText(1, _translate("Form", "1"))
        self.comboBox_2.setItemText(2, _translate("Form", "2"))
        self.comboBox_2.setItemText(3, _translate("Form", "3"))
        self.comboBox_2.setItemText(4, _translate("Form", "4"))
        self.comboBox_2.setItemText(5, _translate("Form", "5"))
        self.comboBox_2.setMaxVisibleItems(10)


        # self.comboBox_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        # self.pushButton.setText(_translate("Form", "查询"))
        self.pushButton.setText(_translate("Form", "查询"))


    def comboBoxTextChange(self):
        pass
        # _translate = QtCore.QCoreApplication.translate
        # # self.comboBox_2.clear()
        # self.comboBox_2.setItemText(0, _translate("Form", ""))
        # db = self.comboBox.currentText()
        # if db != "":
        #     for i,d in enumerate(self.database[db]['TABLE'].keys()):
        #         print(i,d)
        #         self.comboBox_2.setItemText(i + 1, _translate("Form", d))
















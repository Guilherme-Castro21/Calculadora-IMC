# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(486, 363)
        MainWindow.setMinimumSize(QtCore.QSize(486, 363))
        MainWindow.setMaximumSize(QtCore.QSize(486, 363))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(30, 20, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.labelPeso = QtWidgets.QLabel(self.centralwidget)
        self.labelPeso.setGeometry(QtCore.QRect(20, 70, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.labelPeso.setFont(font)
        self.labelPeso.setObjectName("labelPeso")
        self.linePeso = QtWidgets.QLineEdit(self.centralwidget)
        self.linePeso.setGeometry(QtCore.QRect(30, 100, 331, 31))
        self.linePeso.setObjectName("linePeso")
        self.labelAlt = QtWidgets.QLabel(self.centralwidget)
        self.labelAlt.setGeometry(QtCore.QRect(20, 140, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.labelAlt.setFont(font)
        self.labelAlt.setObjectName("labelAlt")
        self.labelKg = QtWidgets.QLabel(self.centralwidget)
        self.labelKg.setGeometry(QtCore.QRect(370, 110, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.labelKg.setFont(font)
        self.labelKg.setObjectName("labelKg")
        self.lineAlt = QtWidgets.QLineEdit(self.centralwidget)
        self.lineAlt.setGeometry(QtCore.QRect(30, 170, 331, 31))
        self.lineAlt.setObjectName("lineAlt")
        self.labelM = QtWidgets.QLabel(self.centralwidget)
        self.labelM.setGeometry(QtCore.QRect(370, 180, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.labelM.setFont(font)
        self.labelM.setObjectName("labelM")
        self.btnCalcular = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalcular.setGeometry(QtCore.QRect(20, 210, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnCalcular.setFont(font)
        self.btnCalcular.setObjectName("btnCalcular")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(30, 250, 441, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.labelResult.setFont(font)
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.btnLimpar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpar.setGeometry(QtCore.QRect(260, 210, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnLimpar.setFont(font)
        self.btnLimpar.setObjectName("btnLimpar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculo do Índice de Massa Corporal (IMC)"))
        self.labelTitle.setText(_translate("MainWindow", "Calculo do Índice de Massa Corporal (IMC)"))
        self.labelPeso.setText(_translate("MainWindow", "Peso (ex.: 69,2)"))
        self.labelAlt.setText(_translate("MainWindow", "Altura (ex.: 1,70)"))
        self.labelKg.setText(_translate("MainWindow", "Kg"))
        self.labelM.setText(_translate("MainWindow", "m"))
        self.btnCalcular.setText(_translate("MainWindow", "Calcular"))
        self.btnLimpar.setText(_translate("MainWindow", "Limpar"))

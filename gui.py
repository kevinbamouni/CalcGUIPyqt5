# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowfinance.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowFinance(object):
    def setupUi(self, MainWindowFinance):
        MainWindowFinance.setObjectName("MainWindowFinance")
        MainWindowFinance.resize(1134, 144)
        self.centralWidget = QtWidgets.QWidget(MainWindowFinance)
        self.centralWidget.setObjectName("centralWidget")
        self.toolButton = QtWidgets.QToolButton(self.centralWidget)
        self.toolButton.setGeometry(QtCore.QRect(950, 10, 171, 31))
        self.toolButton.setObjectName("toolButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 921, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.Run = QtWidgets.QPushButton(self.centralWidget)
        self.Run.setGeometry(QtCore.QRect(10, 50, 181, 41))
        self.Run.setObjectName("Run")
        MainWindowFinance.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindowFinance)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1134, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFichier = QtWidgets.QMenu(self.menuBar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuEditer = QtWidgets.QMenu(self.menuBar)
        self.menuEditer.setObjectName("menuEditer")
        self.menuAide = QtWidgets.QMenu(self.menuBar)
        self.menuAide.setObjectName("menuAide")
        MainWindowFinance.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindowFinance)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindowFinance.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindowFinance)
        self.statusBar.setObjectName("statusBar")
        MainWindowFinance.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuFichier.menuAction())
        self.menuBar.addAction(self.menuEditer.menuAction())
        self.menuBar.addAction(self.menuAide.menuAction())

        self.retranslateUi(MainWindowFinance)
        QtCore.QMetaObject.connectSlotsByName(MainWindowFinance)

    def retranslateUi(self, MainWindowFinance):
        _translate = QtCore.QCoreApplication.translate
        MainWindowFinance.setWindowTitle(_translate("MainWindowFinance", "MainWindowFinance"))
        self.toolButton.setText(_translate("MainWindowFinance", "..."))
        self.Run.setText(_translate("MainWindowFinance", "Run"))
        self.menuFichier.setTitle(_translate("MainWindowFinance", "Fichier"))
        self.menuEditer.setTitle(_translate("MainWindowFinance", "Editer"))
        self.menuAide.setTitle(_translate("MainWindowFinance", "Aide"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowFinance = QtWidgets.QMainWindow()
    ui = Ui_MainWindowFinance()
    ui.setupUi(MainWindowFinance)
    MainWindowFinance.show()
    sys.exit(app.exec_())


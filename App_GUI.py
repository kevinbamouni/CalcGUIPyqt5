# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


# Les modifications les plus importantes à effectuer sur le code qui a été généré par pyuic5 (pyuic5 mainwindow.ui > mainwindowtest.py)
# 1. Ajouter la ligne "from PyQt5.QtCore import QObject, pyqtSlot"
# 2. La classe hérite de QObject et non de object
# 2. Ajouter le décorateur  #pyqtSlot() aux fonctions qui s'exécutent lors des évènements, click de boutton etc...


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot

class Ui_MainWindow(QObject): # Modification à effectuer : Ui_MainWindow hérite de QObject et non de object comme dans le code que pyuic5 génère initialement
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 820)
        MainWindow.setMinimumSize(QtCore.QSize(1130, 673))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeView = QtWidgets.QTreeView(self.centralWidget)
        self.treeView.setMaximumSize(QtCore.QSize(500, 16777215))
        self.treeView.setObjectName("treeView")
        self.horizontalLayout.addWidget(self.treeView)
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setMinimumSize(QtCore.QSize(0, 320))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.widget)
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.tab_2)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 320))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4.addWidget(self.widget_2)
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_4.addWidget(self.tableView)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1500, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFichier = QtWidgets.QMenu(self.menuBar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuEdition = QtWidgets.QMenu(self.menuBar)
        self.menuEdition.setObjectName("menuEdition")
        self.menuOutils = QtWidgets.QMenu(self.menuBar)
        self.menuOutils.setObjectName("menuOutils")
        self.menuAide = QtWidgets.QMenu(self.menuBar)
        self.menuAide.setObjectName("menuAide")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.menuBar.addAction(self.menuFichier.menuAction())
        self.menuBar.addAction(self.menuEdition.menuAction())
        self.menuBar.addAction(self.menuOutils.menuAction())
        self.menuBar.addAction(self.menuAide.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        
        #Connect l'evenement clicked sur le boutton avec le slot qui la fonction 
        self.pushButton.clicked.connect(self.addRandomTextSlot)
        
        self.treeModel = QtWidgets.QFileSystemModel()
        self.treeModel.setRootPath('')
        self.treeView.setModel(self.treeModel)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuEdition.setTitle(_translate("MainWindow", "Edition"))
        self.menuOutils.setTitle(_translate("MainWindow", "Outils"))
        self.menuAide.setTitle(_translate("MainWindow", "Aide"))
        
        # On défini la fonction qui doit être appelée lorsque l'on clique sur le boutton
        # On ajoute le décorateur @pyqtSlot() pour faire en sorte 
    @pyqtSlot()
    def addRandomTextSlot(self):
        # QFileDialog permet d'ouvrir l'explorateur de fichier et de récupérer le chemin du fichier
        # qui sera choisi et ouver
#        (nomFichierdata,filtre) = QtWidgets.QFileDialog.getOpenFileName(
#                                  self,"Ouvrir fichier de données",
#                                  filter="Bibliothèque (*.csv);; Tout (*.*)")
#        # On place le chemin du fichier dans la text box
        self.lineEdit.setText("nomFichierdata")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

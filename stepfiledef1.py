# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\stepfiledef.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot


class Ui_MainWindow(QObject):
    COUNT = 1
    my_dict = {}
    def setupUi(self, MainWindow):
        # On défini la fenètre principale, on lui donne un nom et une taille
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        # On crée un widget central destiné à apparaître au centre de la fenêtre de la fenêtre pricipale
        # Le centralwidget sera le container pricipal de tous les autres widget placé dans la fenêtre
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ### Debut demarche pour ajouter des widgets sur un container selon un layout défini
        # On ajoute un layout qui va placer automatiquement les elements sur le centralWidget
        # On crée un layout qui a pour parent le widget central, il va se placer sur le widget central
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout") # On lui donne un nom

        # On crée un tablewidget qui aura pour parent le centralwidget, c'est à dire qu'il va se placer sur le centralwidget
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout.addWidget(self.tableWidget) # le layout place le tablewidget

        ### Fin démarche pour ajouter des widget sur un container selon un layout défini

        # On crée un second tablewidget sur le centralwidget 
        self.tableWidget2 = QtWidgets.QTableWidget(self.centralwidget) # tablewidget sur le centralwidget (parent)
        self.tableWidget2.setObjectName("tableWidget2")
        self.tableWidget2.setColumnCount(0)
        self.tableWidget2.setRowCount(0)
        self.horizontalLayout.addWidget(self.tableWidget2) # place automatiquement par le layout du centralwidget

        # Ajouter un boutton sur le centralwidget.
        # Boutton par lequel on va ajouter dynamiquement des widget dans un frame créer ci dessous
        self.pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.pushbutton.setObjectName("pushbutton")
        self.pushbutton.setText("ADD...")
        self.horizontalLayout.addWidget(self.pushbutton) # Le boutton est placé automatiquement par le layout du centralwidget
        
        # On connecte le signal "clic gauche de la souris"  au slot addsomewidget, 
        # slot est une fonction qui s'exécuter suite au declenchement d'un signal auquel il est connecté
        # Pour pouvoir connecter le signal et le slot la class doit hériter de QObject
        self.pushbutton.clicked.connect(self.addsomewidget)

        # Ajout d'un deuxieme boutton
        self.pushbutton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton2.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.pushbutton2.setObjectName("pushbutton2")
        self.pushbutton2.setText("DELETE...")
        self.horizontalLayout.addWidget(self.pushbutton2)

        self.pushbutton2.clicked.connect(self.addsomewidget2)

        

        # Création et Ajout d'un frame sur le central widget(après le bouton)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(300, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # On ajoute un layout au frame créé ci-dessus
        self.VerticalLayout2 = QtWidgets.QVBoxLayout(self.frame)
        self.VerticalLayout2.setObjectName("horizontalLayout2") # On lui donne un nom

        # Ajout d'un label dans le frame
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.label.setText("TextLabel")
        self.VerticalLayout2.addWidget(self.label) # Le layout du frame place auto le label sur le frame

        self.horizontalLayout.addWidget(self.frame) # le layout du centralwidget place auto le frame sur le centralwidget
        
        # On  défini le centralwidget de la fenêtre pricipal
        MainWindow.setCentralWidget(self.centralwidget)
        # On crée la barre de menu destiné à la fenêtre principale
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        # On défini la barre de menu crée comme barre de menu de la fenêtre pricipale
        MainWindow.setMenuBar(self.menubar)
        # On crée et on défini la barre de status de la fenêtre principale comme on a fait pour la barre de menu.
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    # Fonction qui s'execute suite à un signal de clic sur le boutton : c'est un slot
    # Le décorateur se charge de le modifier pour le faire correspondre.
    # A chaque fois que l'on clique sur le boutton un textlabel s'ajoute et est automatiquement placé par le layout du
    # du container
    @pyqtSlot()
    def addsomewidget(self):
        self.COUNT += 1
        x = "TextLabel" + str(self.COUNT)
        self.my_dict[x]  = QtWidgets.QLabel(self.frame)
        self.my_dict[x].setObjectName(x)
        self.my_dict[x].setText(x)
        self.VerticalLayout2.addWidget(self.my_dict[x])
        print("add", self.COUNT, x, self.my_dict[x])

    # Supprime les textlabels ajoutés partant du plus recemment créé
    @pyqtSlot()
    def addsomewidget2(self):
        if self.COUNT >=2 :
            x = "TextLabel" + str(self.COUNT)
            self.my_dict[x].deleteLater()
            print("del", self.COUNT, x, self.my_dict[x]) # print de debugage
            self.COUNT -= 1
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

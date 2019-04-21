# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:42:10 2019

@author: work
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from var import VaR_fi
import pandas as pd

###### Source de documentation : https://pythonprogramming.net/basic-gui-pyqt-tutorial/ et qui est Sentdex
# Environnement Anaconda 2019.03

# Cette classe crée hérite de Qmainwindow et donc devient un Qmainwindow
class window(QtWidgets.QMainWindow):
    
    # Le constructeur de la classe
    def __init__(self):
        # On fait une initialisation des méthodes et propriétés de la classe parent
        # pour s'assurer qu'ils soit disponibles dans cette classe
        super(window,self).__init__()
        # On fait appel à la def ci dessous qui vas ajouter les autres widgets, boutons...
        self.setupUi() 
        
        # Code extrait à partir de qtdesigner puis transformé en python avec pycui
        # Ensuite on effectue une modification pour faire en sorte d'adapter le code à 
        # notre méthode de programmation 
        # on a essentiellement remplacé le deuxième paramètre de setupUi (d'origine) par self.
    def setupUi(self):
        
        ### Python execute le code ligne à ligne donc Les objets sont ajoutés dans cet l'ordre 
        ### 
        
        # Définition du nom et de la taille de l'objet window 
        # (qui est donc un objet QMainWindow)
        self.setObjectName("MainWindowFinance")
        self.resize(1134, 144)
        
        # On ajout un widget au QMainWindow
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        
        # Ajout de boutton
        self.toolButton = QtWidgets.QToolButton(self.centralWidget)
        # Les deux premiers chiffres représente la position sur la fen^tre et les deux derniers la taille du boutton, fin je crois.
        self.toolButton.setGeometry(QtCore.QRect(950, 10, 171, 31))
        # On donne un nom à l'objet boutton qui a été ajouté, donc deux objets ne douvent pas avoir le même nom 
        self.toolButton.setObjectName("toolButton")
        # button fonction : associe une action sur le boutton à la fonction
        self.toolButton.clicked.connect(self.on_toolButton_triggered)  #button fonction
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 921, 31))
        self.lineEdit.setObjectName("lineEdit")
        
        self.Run = QtWidgets.QPushButton(self.centralWidget)
        self.Run.setGeometry(QtCore.QRect(10, 50, 181, 41))
        self.Run.setObjectName("Run")
        # button fonction : associe une action sur le boutton à la fonction
        self.Run.clicked.connect(self.on_runbutton_triggered)  
        
        self.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(self)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1134, 21))
        self.menuBar.setObjectName("menuBar")
        
        self.menuFichier = QtWidgets.QMenu(self.menuBar)
        self.menuFichier.setObjectName("menuFichier")
        
        self.menuEditer = QtWidgets.QMenu(self.menuBar)
        self.menuEditer.setObjectName("menuEditer")
        
        self.menuAide = QtWidgets.QMenu(self.menuBar)
        self.menuAide.setObjectName("menuAide")
        
        self.setMenuBar(self.menuBar)
        
        self.mainToolBar = QtWidgets.QToolBar(self)
        self.mainToolBar.setObjectName("mainToolBar")
        
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        
        self.statusBar = QtWidgets.QStatusBar(self)
        self.statusBar.setObjectName("statusBar")
        self.setStatusBar(self.statusBar)
        
        self.menuBar.addAction(self.menuFichier.menuAction())
        self.menuBar.addAction(self.menuEditer.menuAction())
        self.menuBar.addAction(self.menuAide.menuAction())
        
        # On appelle la méthode qui permet de nommer les widgets qui ont été ajoutés
        self.retranslateUi()
        
        
        
        # Même provenance que SetupUi et même modification.
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindowFinance", "MainWindowFinance"))
        self.toolButton.setText(_translate("MainWindowFinance", "..."))
        self.Run.setText(_translate("MainWindowFinance", "Run"))
        self.menuFichier.setTitle(_translate("MainWindowFinance", "Fichier"))
        self.menuEditer.setTitle(_translate("MainWindowFinance", "Editer"))
        self.menuAide.setTitle(_translate("MainWindowFinance", "Aide"))
        self.show()
        
        
        
        
    # Méthode appelée lorsque l'on clique sur le boutton
    def on_toolButton_triggered(self):
        # QFileDialog permet d'ouvrir l'explorateur de fichier et de récupérer le chemin du fichier
        # qui sera choisi et ouver
        (nomFichierdata,filtre) = QtWidgets.QFileDialog.getOpenFileName(
                                  self,"Ouvrir fichier de données",
                                  filter="Bibliothèque (*.csv);; Tout (*.*)")
        # On place le chemin du fichier dans la text box
        self.lineEdit.setText(nomFichierdata)
        
        
        
        
    # Méthode appelée lorsque l'on clique sur le boutton
    def on_runbutton_triggered(self):
        # On appelle la fonction qui calcul la var et on exporte vers un fichier excel
        # On peut mettre du xlwings ici pour exporter les résultats vers excel de façon plus 
        # stylée, et y faire des traitements ou du reporting.
        # Tous les calculs et les traitements sont déclenchés par ce boutton
        
        # On récupère le chemin du fichier qui est dans lineEdit () après le choix permit par QFileDialog 
        # que l'on passe à la fontion qui calcul la VaR
        df = pd.DataFrame(VaR_fi(self.lineEdit.text()))
        df.to_excel('output_var.xlsx')
        #Affiche un message pour informer que le succès a été effectué avec succès
        df = QtWidgets.QMessageBox.about(self, "Etat du Run", "Run éffectué avec succès!")
        
        
# Exécution de la fenêtre
# On crée en mémoire l' application
app = QtWidgets.QApplication(sys.argv)

# On instance un objet de la classe qui a été créées ci-dessus
# cet objet va visiblement se greffer sur app créé ci-dessus
GUI = window()

# On exécute l'application qui contient desormais notre objet
# sys.exit permet de fermer l'application uniquement quand on va cliquer sur 
# le boutton fermer de la fenêtre
sys.exit(app.exec_())
        
        
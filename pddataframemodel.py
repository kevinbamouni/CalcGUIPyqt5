from PyQt5 import QtCore
import pandas as pd


# doc : https://doc.qt.io/qt-5/model-view-programming.html#model-subclassing-reference
# doc : https://doc.qt.io/qt-5/model-view-programming.html
# code inspi : https://doc.qt.io/qt-5/model-view-programming.html#creating-new-models

class pddataframemodel(QtCore.QAbstractTableModel):

    def __init__(self, df=pd.DataFrame(), parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self._df = df

    # rowCount(), columnCount(), and data()
    # Number of row of the data source
    def rowCount(self, index):
        return self._df.shape[0]

    # Number of col of the data source
    def columnCount(self, index):
        return self._df.shape[1]

    # Data source connextion
    def data(self, index, role=QtCore.Qt.DisplayRole):

        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if not index.isValid():
            return QtCore.QVariant()

        if index.row() > self._df.shape[0] or index.column() > self._df.shape[1]:
            return QtCore.QVariant
        # TODO : gerer le type de données que l'on affiche nombre et chaîne de caratère
        return QtCore.QVariant(str(self._df.iat[index.row(), index.column()]))

    # Define the column and rownames of the data structure
    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Horizontal:
            try:
                return self._df.columns.tolist()[section]
            except (IndexError,):
                return QtCore.QVariant()
        elif orientation == QtCore.Qt.Vertical:
            try:
                # return self.df.index.tolist()
                return self._df.index.tolist()[section]
            except (IndexError,):
                return QtCore.QVariant()

    # https://doc.qt.io/qt-5/qt.html#ItemFlag-enum
    def flags(self, index):
        return QtCore.Qt.ItemFlags(1 | 2 | 32)

    ###  Editable items

    ###  https://doc.qt.io/qt-5/model-view-programming.html#creating-new-models

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        # TODO : Ajouter des tests pour gerer l'intégrité de value, index
        self._df.iat[index.row(), index.column()] = str(value)      # Modifie les données
        self.dataChanged.emit(index, index, [role])                 # Pourquoi ça marche ? :-)
        # self._df.to_csv("data.csv")                               #  Ecrase le fichier avec la donnée modifiée
        return True


    def setHeaderData(self):
        pass

    ### Resizable models

    def insertRows(self):
        pass

    def removeRows(self):
        pass

    def insertColumns(self):
        pass

    def removeColumns(self):
        pass

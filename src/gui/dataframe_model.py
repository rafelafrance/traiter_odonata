"""A GUI view of the guides DB table."""

import pandas as pd
from PyQt5 import QtCore


class DataframeModel(QtCore.QAbstractTableModel):
    """use a dataframe as a model."""

    DtypeRole = QtCore.Qt.UserRole + 1000
    ValueRole = QtCore.Qt.UserRole + 1001

    def __init__(self, df=pd.DataFrame()):
        super(DataframeModel, self).__init__()
        self._dataframe = df

    @property
    def dataframe(self):
        """Dataframe getter."""
        return self._dataframe

    @dataframe.setter
    def dataframe(self, dataframe):
        """Reset the dataframe."""
        self.beginResetModel()
        self._dataframe = dataframe.copy()
        self.endResetModel()

    def data(self, index, role=QtCore.Qt.DisplayRole):
        """Get the data."""
        if (not index.isValid()
                or not (0 <= index.row() < self.rowCount()
                        and 0 <= index.column() < self.columnCount())):
            return QtCore.QVariant()
        row = self._dataframe.index[index.row()]
        col = self._dataframe.columns[index.column()]
        dt = self._dataframe[col].dtype

        val = self._dataframe.iloc[row][col]
        if role == QtCore.Qt.DisplayRole:
            return str(val)
        elif role == DataframeModel.ValueRole:
            return val
        if role == DataframeModel.DtypeRole:
            return dt
        return QtCore.QVariant()

    def rowCount(self, parent=None, *args, **kwargs):
        """The length of the outer list."""
        return len(self._dataframe.index)

    def columnCount(self, parent=None, *args, **kwargs):
        """The following takes the first sub-list."""
        return len(self._dataframe.columns)

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        """Get the row or column headers."""
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self._dataframe.columns[section]
            else:
                return str(self._dataframe.index[section])
        return QtCore.QVariant()

    def roleNames(self):
        """Custom role names."""
        return {
            QtCore.Qt.DisplayRole: b'display',
            DataframeModel.DtypeRole: b'dtype',
            DataframeModel.ValueRole: b'value'}

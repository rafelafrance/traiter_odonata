# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/gui/search_replace_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SearchReplaceDialog(object):
    def setupUi(self, SearchReplaceDialog):
        SearchReplaceDialog.setObjectName("SearchReplaceDialog")
        SearchReplaceDialog.resize(713, 261)
        self.formLayoutWidget = QtWidgets.QWidget(SearchReplaceDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 691, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.horizontalLayoutWidget = QtWidgets.QWidget(SearchReplaceDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(300, 110, 397, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout.addWidget(self.checkBox_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(SearchReplaceDialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 110, 221, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(SearchReplaceDialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 190, 221, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(SearchReplaceDialog)
        self.pushButton_5.setGeometry(QtCore.QRect(610, 220, 83, 25))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(SearchReplaceDialog)
        QtCore.QMetaObject.connectSlotsByName(SearchReplaceDialog)

    def retranslateUi(self, SearchReplaceDialog):
        _translate = QtCore.QCoreApplication.translate
        SearchReplaceDialog.setWindowTitle(_translate("SearchReplaceDialog", "Search and Replace"))
        self.label.setText(_translate("SearchReplaceDialog", "Find"))
        self.label_2.setText(_translate("SearchReplaceDialog", "Replace"))
        self.checkBox_3.setText(_translate("SearchReplaceDialog", "Case Sensitive"))
        self.checkBox_2.setText(_translate("SearchReplaceDialog", "Whole Words"))
        self.checkBox.setText(_translate("SearchReplaceDialog", "Regular Expression"))
        self.pushButton_2.setText(_translate("SearchReplaceDialog", "Findn Next"))
        self.pushButton.setText(_translate("SearchReplaceDialog", "Find Previous"))
        self.pushButton_4.setText(_translate("SearchReplaceDialog", "Replace"))
        self.pushButton_3.setText(_translate("SearchReplaceDialog", "Replace All"))
        self.pushButton_5.setText(_translate("SearchReplaceDialog", "Done"))

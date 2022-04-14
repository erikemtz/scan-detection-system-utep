from PyQt5 import QtCore, QtWidgets


class Ui_addSetNodes_window(object):
    def setupAddSetNodes(self, addSetNodes_window):
        addSetNodes_window.setObjectName("addSetNodes_window")
        addSetNodes_window.setEnabled(True)
        addSetNodes_window.resize(513, 150)
        addSetNodes_window.setMinimumSize(QtCore.QSize(513, 150))
        addSetNodes_window.setMaximumSize(QtCore.QSize(513, 150))
        self.AddSetNodesWindowLayout = QtWidgets.QGridLayout(addSetNodes_window)
        self.AddSetNodesWindowLayout.setObjectName("AddSetNodesWindowLayout")
        self.mainLayout_addSetNodesWindow = QtWidgets.QVBoxLayout()
        self.mainLayout_addSetNodesWindow.setObjectName("mainLayout_addSetNodesWindow")
        self.startingIPLayout_addSetNodesWindow = QtWidgets.QHBoxLayout()
        self.startingIPLayout_addSetNodesWindow.setObjectName("startingIPLayout_addSetNodesWindow")
        self.startingIPLabel_addSetNodesWindow = QtWidgets.QLabel(addSetNodes_window)
        self.startingIPLabel_addSetNodesWindow.setObjectName("startingIPLabel_addSetNodesWindow")
        self.startingIPLayout_addSetNodesWindow.addWidget(self.startingIPLabel_addSetNodesWindow)
        self.startingIPInput_addSetNodesWindow = QtWidgets.QLineEdit(addSetNodes_window)
        self.startingIPInput_addSetNodesWindow.setObjectName("startingIPInput_addSetNodesWindow")
        self.startingIPLayout_addSetNodesWindow.addWidget(self.startingIPInput_addSetNodesWindow)
        self.mainLayout_addSetNodesWindow.addLayout(self.startingIPLayout_addSetNodesWindow)
        self.numberVictimNodesLayout_addSetNodesWindow = QtWidgets.QHBoxLayout()
        self.numberVictimNodesLayout_addSetNodesWindow.setObjectName("numberVictimNodesLayout_addSetNodesWindow")
        self.numberVictimNodesLabel_addSetNodesWindow = QtWidgets.QLabel(addSetNodes_window)
        self.numberVictimNodesLabel_addSetNodesWindow.setObjectName("numberVictimNodesLabel_addSetNodesWindow")
        self.numberVictimNodesLayout_addSetNodesWindow.addWidget(self.numberVictimNodesLabel_addSetNodesWindow)

        self.numberVictimNodesSpinbox_addSetNodesWindow = QtWidgets.QSpinBox(addSetNodes_window)
        self.numberVictimNodesSpinbox_addSetNodesWindow.setObjectName("numberVictimNodesSpinbox_addSetNodesWindow")
        self.numberVictimNodesSpinbox_addSetNodesWindow.setValue(1)
        self.numberVictimNodesLayout_addSetNodesWindow.addWidget(self.numberVictimNodesSpinbox_addSetNodesWindow)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.numberVictimNodesLayout_addSetNodesWindow.addItem(spacerItem)
        self.mainLayout_addSetNodesWindow.addLayout(self.numberVictimNodesLayout_addSetNodesWindow)
        self.buttonsLayout_addSetNodesWindow = QtWidgets.QHBoxLayout()
        self.buttonsLayout_addSetNodesWindow.setObjectName("buttonsLayout_addSetNodesWindow")
        self.setNodesCreateButton_addSetNodesWindow = QtWidgets.QPushButton(addSetNodes_window)
        self.setNodesCreateButton_addSetNodesWindow.setObjectName("setNodesCreateButton_addSetNodesWindow")
        self.buttonsLayout_addSetNodesWindow.addWidget(self.setNodesCreateButton_addSetNodesWindow)
        self.setNodesCancelButton_addSetNodesWindow = QtWidgets.QPushButton(addSetNodes_window)
        self.setNodesCancelButton_addSetNodesWindow.setObjectName("setNodesCancelButton_addSetNodesWindow")
        self.buttonsLayout_addSetNodesWindow.addWidget(self.setNodesCancelButton_addSetNodesWindow)
        self.mainLayout_addSetNodesWindow.addLayout(self.buttonsLayout_addSetNodesWindow)
        self.AddSetNodesWindowLayout.addLayout(self.mainLayout_addSetNodesWindow, 0, 0, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(addSetNodes_window)

        _translate = QtCore.QCoreApplication.translate
        addSetNodes_window.setWindowTitle(_translate("addSetNodes_window", "Add Set of Victim Nodes"))
        self.startingIPLabel_addSetNodesWindow.setText(_translate("addSetNodes_window", "Starting IP Address:     "))
        self.numberVictimNodesLabel_addSetNodesWindow.setText(_translate("addSetNodes_window", "Number of Nodes: "))
        self.setNodesCreateButton_addSetNodesWindow.setText(_translate("addSetNodes_window", "Create"))
        self.setNodesCancelButton_addSetNodesWindow.setText(_translate("addSetNodes_window", "Cancel"))

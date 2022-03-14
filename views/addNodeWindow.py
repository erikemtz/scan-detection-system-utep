from PyQt5 import QtCore, QtWidgets


class Ui_addNode_window(object):
    def setupAddNode(self, addNode_window):
        addNode_window.setObjectName("addNode_window")
        addNode_window.setEnabled(True)
        addNode_window.resize(487, 240)
        addNode_window.setMinimumSize(QtCore.QSize(487, 240))
        addNode_window.setMaximumSize(QtCore.QSize(487, 240))
        self.AddNodeWindowLayout = QtWidgets.QGridLayout(addNode_window)
        self.AddNodeWindowLayout.setObjectName("AddNodeWindowLayout")
        self.mainLayout_addNodeWindow = QtWidgets.QVBoxLayout()
        self.mainLayout_addNodeWindow.setObjectName("mainLayout_addNodeWindow")
        self.nodeTypeLayout_addNodeWindow = QtWidgets.QHBoxLayout()
        self.nodeTypeLayout_addNodeWindow.setObjectName("nodeTypeLayout_addNodeWindow")
        self.nodeTypeLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
        self.nodeTypeLabel_addNodeWindow.setObjectName("nodeTypeLabel_addNodeWindow")
        self.nodeTypeLayout_addNodeWindow.addWidget(self.nodeTypeLabel_addNodeWindow)
        self.nodeTypeComboBox_addNodeWindow = QtWidgets.QComboBox(addNode_window)
        self.nodeTypeComboBox_addNodeWindow.setObjectName("nodeTypeComboBox_addNodeWindow")
        self.nodeTypeLayout_addNodeWindow.addWidget(self.nodeTypeComboBox_addNodeWindow)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.nodeTypeLayout_addNodeWindow.addItem(spacerItem)
        self.mainLayout_addNodeWindow.addLayout(self.nodeTypeLayout_addNodeWindow)
        self.nodeNameLayout_addNodeWindow = QtWidgets.QHBoxLayout()
        self.nodeNameLayout_addNodeWindow.setObjectName("nodeNameLayout_addNodeWindow")
        self.nodeNameLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
        self.nodeNameLabel_addNodeWindow.setObjectName("nodeNameLabel_addNodeWindow")
        self.nodeNameLayout_addNodeWindow.addWidget(self.nodeNameLabel_addNodeWindow)
        self.nodeNameInput_addNodeWindow = QtWidgets.QLineEdit(addNode_window)
        self.nodeNameInput_addNodeWindow.setObjectName("nodeNameInput_addNodeWindow")
        self.nodeNameLayout_addNodeWindow.addWidget(self.nodeNameInput_addNodeWindow)
        self.mainLayout_addNodeWindow.addLayout(self.nodeNameLayout_addNodeWindow)
        self.nodeMACAddressLayout_addNodeWindow = QtWidgets.QHBoxLayout()
        self.nodeMACAddressLayout_addNodeWindow.setObjectName("nodeMACAddressLayout_addNodeWindow")
        self.nodeMACAddressLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
        self.nodeMACAddressLabel_addNodeWindow.setObjectName("nodeMACAddressLabel_addNodeWindow")
        self.nodeMACAddressLayout_addNodeWindow.addWidget(self.nodeMACAddressLabel_addNodeWindow)
        self.nodeMACAddressInput_addNodeWindow = QtWidgets.QLineEdit(addNode_window)
        self.nodeMACAddressInput_addNodeWindow.setObjectName("nodeMACAddressInput_addNodeWindow")
        self.nodeMACAddressLayout_addNodeWindow.addWidget(self.nodeMACAddressInput_addNodeWindow)
        self.mainLayout_addNodeWindow.addLayout(self.nodeMACAddressLayout_addNodeWindow)
        self.nodeIPAddressLayout_addNodeWindow = QtWidgets.QHBoxLayout()
        self.nodeIPAddressLayout_addNodeWindow.setObjectName("nodeIPAddressLayout_addNodeWindow")
        self.nodeIPAddressLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
        self.nodeIPAddressLabel_addNodeWindow.setObjectName("nodeIPAddressLabel_addNodeWindow")
        self.nodeIPAddressLayout_addNodeWindow.addWidget(self.nodeIPAddressLabel_addNodeWindow)
        self.nodeIPAddressInput_addNodeWindow = QtWidgets.QLineEdit(addNode_window)
        self.nodeIPAddressInput_addNodeWindow.setObjectName("nodeIPAddressInput_addNodeWindow")
        self.nodeIPAddressLayout_addNodeWindow.addWidget(self.nodeIPAddressInput_addNodeWindow)
        self.mainLayout_addNodeWindow.addLayout(self.nodeIPAddressLayout_addNodeWindow)
        self.nodeScannerNodeLayout_addNodeWindow = QtWidgets.QHBoxLayout()
        self.nodeScannerNodeLayout_addNodeWindow.setObjectName("nodeScannerNodeLayout_addNodeWindow")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.nodeScannerNodeLayout_addNodeWindow.addItem(spacerItem1)
        self.nodeScannerNodeCheckBox_addNodeWindow = QtWidgets.QCheckBox(addNode_window)
        self.nodeScannerNodeCheckBox_addNodeWindow.setObjectName("nodeScannerNodeCheckBox_addNodeWindow")
        self.nodeScannerNodeLayout_addNodeWindow.addWidget(self.nodeScannerNodeCheckBox_addNodeWindow)
        self.mainLayout_addNodeWindow.addLayout(self.nodeScannerNodeLayout_addNodeWindow)

        self.addNodeButtonsLayout_addNodeWindow = QtWidgets.QHBoxLayout()
        self.addNodeButtonsLayout_addNodeWindow.setObjectName("addNodeButtonsLayout_addNodeWindow")
        self.addNodeButton_addNodeWindow = QtWidgets.QPushButton(addNode_window)
        self.addNodeButton_addNodeWindow.setObjectName("addNodeButton_addNodeWindow")
        self.addNodeButtonsLayout_addNodeWindow.addWidget(self.addNodeButton_addNodeWindow)
        self.addNodeCancelButton_addNodeWindow = QtWidgets.QPushButton(addNode_window)
        self.addNodeCancelButton_addNodeWindow.setObjectName("addNodeCancelButton_addNodeWindow")
        self.addNodeButtonsLayout_addNodeWindow.addWidget(self.addNodeCancelButton_addNodeWindow)
        self.mainLayout_addNodeWindow.addLayout(self.addNodeButtonsLayout_addNodeWindow)
        self.AddNodeWindowLayout.addLayout(self.mainLayout_addNodeWindow, 0, 0, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(addNode_window)

        _translate = QtCore.QCoreApplication.translate
        addNode_window.setWindowTitle(_translate("addNode_window", "Add New Node"))
        self.nodeTypeLabel_addNodeWindow.setText(_translate("addNode_window", "Type:                     "))
        self.nodeNameLabel_addNodeWindow.setText(_translate("addNode_window", "Node Name:          "))
        self.nodeMACAddressLabel_addNodeWindow.setText(_translate("addNode_window", "MAC Address:       "))
        self.nodeIPAddressLabel_addNodeWindow.setText(_translate("addNode_window", "IP Address:            "))
        self.nodeScannerNodeCheckBox_addNodeWindow.setText(_translate("addNode_window", "Scanner Node"))
        self.addNodeButton_addNodeWindow.setText(_translate("addNode_window", "Add Node"))
        self.addNodeCancelButton_addNodeWindow.setText(_translate("addNode_window", "Cancel"))

        self.nodeScannerNodeCheckBox_addNodeWindow.toggled.connect(lambda: self.scannerNode(addNode_window, _translate))

    def scannerNode(self, addNode_window, _translate):
        if self.nodeScannerNodeCheckBox_addNodeWindow.isChecked():
            addNode_window.resize(487, 500)
            addNode_window.setMinimumSize(QtCore.QSize(487, 450))
            addNode_window.setMaximumSize(QtCore.QSize(487, 450))

            self.addNodeButton_addNodeWindow.deleteLater()
            self.addNodeCancelButton_addNodeWindow.deleteLater()
            self.mainLayout_addNodeWindow.removeItem(self.addNodeButtonsLayout_addNodeWindow)

            self.nodeUserPassLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeUserPassLayout_addNodeWindow.setObjectName("nodeUserPassLayout_addNodeWindow")
            self.nodeUserPassLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
            self.nodeUserPassLabel_addNodeWindow.setObjectName("nodeUserPassLabel_addNodeWindow")
            self.nodeUserPassLayout_addNodeWindow.addWidget(self.nodeUserPassLabel_addNodeWindow)
            self.nodeUserPassInput_addNodeWindow = QtWidgets.QLineEdit(addNode_window)
            self.nodeUserPassInput_addNodeWindow.setObjectName("nodeUserPassInput_addNodeWindow")
            self.nodeUserPassLayout_addNodeWindow.addWidget(self.nodeUserPassInput_addNodeWindow)
            self.mainLayout_addNodeWindow.addLayout(self.nodeUserPassLayout_addNodeWindow)
            self.nodeScannerBinaryLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeScannerBinaryLayout_addNodeWindow.setObjectName("nodeScannerBinaryLayout_addNodeWindow")
            self.nodeScannerBinaryLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
            self.nodeScannerBinaryLabel_addNodeWindow.setObjectName("nodeScannerBinaryLabel_addNodeWindow")
            self.nodeScannerBinaryLayout_addNodeWindow.addWidget(self.nodeScannerBinaryLabel_addNodeWindow)
            self.nodeScannerBinaryInput_addNodeWindow = QtWidgets.QLineEdit(addNode_window)
            self.nodeScannerBinaryInput_addNodeWindow.setObjectName("nodeScannerBinaryInput_addNodeWindow")
            self.nodeScannerBinaryLayout_addNodeWindow.addWidget(self.nodeScannerBinaryInput_addNodeWindow)
            self.nodeScannerBinaryBrowseButton_addNodeWindow = QtWidgets.QPushButton(addNode_window)
            self.nodeScannerBinaryBrowseButton_addNodeWindow.setObjectName(
                "nodeScannerBinaryBrowseButton_addNodeWindow")
            self.nodeScannerBinaryLayout_addNodeWindow.addWidget(self.nodeScannerBinaryBrowseButton_addNodeWindow)
            self.mainLayout_addNodeWindow.addLayout(self.nodeScannerBinaryLayout_addNodeWindow)
            self.nodeArgumentsLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeArgumentsLayout_addNodeWindow.setObjectName("nodeArgumentsLayout_addNodeWindow")
            self.nodeArgumentsLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
            self.nodeArgumentsLabel_addNodeWindow.setObjectName("nodeArgumentsLabel_addNodeWindow")
            self.nodeArgumentsLayout_addNodeWindow.addWidget(self.nodeArgumentsLabel_addNodeWindow)
            self.nodeArgumentsInput_addNodeWindow = QtWidgets.QLineEdit(addNode_window)
            self.nodeArgumentsInput_addNodeWindow.setObjectName("nodeArgumentsInput_addNodeWindow")
            self.nodeArgumentsLayout_addNodeWindow.addWidget(self.nodeArgumentsInput_addNodeWindow)
            self.mainLayout_addNodeWindow.addLayout(self.nodeArgumentsLayout_addNodeWindow)
            self.nodeNumIterationsLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeNumIterationsLayout_addNodeWindow.setObjectName("nodeNumIterationsLayout_addNodeWindow")
            self.nodeNumIterationsLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
            self.nodeNumIterationsLabel_addNodeWindow.setObjectName("nodeNumIterationsLabel_addNodeWindow")
            self.nodeNumIterationsLayout_addNodeWindow.addWidget(self.nodeNumIterationsLabel_addNodeWindow)
            self.nodeNumIterationsSpinBox_addNodeWindow = QtWidgets.QSpinBox(addNode_window)
            self.nodeNumIterationsSpinBox_addNodeWindow.setObjectName("nodeNumIterationsSpinBox_addNodeWindow")
            self.nodeNumIterationsLayout_addNodeWindow.addWidget(self.nodeNumIterationsSpinBox_addNodeWindow)
            spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.nodeNumIterationsLayout_addNodeWindow.addItem(spacerItem2)
            self.mainLayout_addNodeWindow.addLayout(self.nodeNumIterationsLayout_addNodeWindow)
            self.nodeMaxParallelRunsLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeMaxParallelRunsLayout_addNodeWindow.setObjectName("nodeMaxParallelRunsLayout_addNodeWindow")
            self.nodeMaxParallelRunsLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
            self.nodeMaxParallelRunsLabel_addNodeWindow.setObjectName("nodeMaxParallelRunsLabel_addNodeWindow")
            self.nodeMaxParallelRunsLayout_addNodeWindow.addWidget(self.nodeMaxParallelRunsLabel_addNodeWindow)
            self.nodeMaxParallelRunsSpinBox_addNodeWindow = QtWidgets.QSpinBox(addNode_window)
            self.nodeMaxParallelRunsSpinBox_addNodeWindow.setObjectName("nodeMaxParallelRunsSpinBox_addNodeWindow")
            self.nodeMaxParallelRunsLayout_addNodeWindow.addWidget(self.nodeMaxParallelRunsSpinBox_addNodeWindow)
            spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.nodeMaxParallelRunsLayout_addNodeWindow.addItem(spacerItem3)
            self.mainLayout_addNodeWindow.addLayout(self.nodeMaxParallelRunsLayout_addNodeWindow)
            self.nodeEndConditionLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeEndConditionLayout_addNodeWindow.setObjectName("nodeEndConditionLayout_addNodeWindow")
            self.nodeEndConditionLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
            self.nodeEndConditionLabel_addNodeWindow.setObjectName("nodeEndConditionLabel_addNodeWindow")
            self.nodeEndConditionLayout_addNodeWindow.addWidget(self.nodeEndConditionLabel_addNodeWindow)
            self.nodeEndConditionInput_addNodeWindow = QtWidgets.QLineEdit(addNode_window)
            self.nodeEndConditionInput_addNodeWindow.setObjectName("nodeEndConditionInput_addNodeWindow")
            self.nodeEndConditionLayout_addNodeWindow.addWidget(self.nodeEndConditionInput_addNodeWindow)
            self.mainLayout_addNodeWindow.addLayout(self.nodeEndConditionLayout_addNodeWindow)
            self.nodeUserPassLabel_addNodeWindow.setText(_translate("addNode_window", "User/Pass:             "))
            self.nodeScannerBinaryLabel_addNodeWindow.setText(_translate("addNode_window", "Scanner-Binary:    "))
            self.nodeScannerBinaryBrowseButton_addNodeWindow.setText(_translate("addNode_window", "Browse..."))
            self.nodeArgumentsLabel_addNodeWindow.setText(_translate("addNode_window", "Arguments:            "))
            self.nodeNumIterationsLabel_addNodeWindow.setText(_translate("addNode_window", "Number-Iterations:"))
            self.nodeMaxParallelRunsLabel_addNodeWindow.setText(_translate("addNode_window", "Max-Parallel-Runs:"))
            self.nodeEndConditionLabel_addNodeWindow.setText(_translate("addNode_window", "End-Condition:       "))

            self.addNodeButtonsLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.addNodeButtonsLayout_addNodeWindow.setObjectName("addNodeButtonsLayout_addNodeWindow")
            self.addNodeButton_addNodeWindow = QtWidgets.QPushButton(addNode_window)
            self.addNodeButton_addNodeWindow.setObjectName("addNodeButton_addNodeWindow")
            self.addNodeButtonsLayout_addNodeWindow.addWidget(self.addNodeButton_addNodeWindow)
            self.addNodeCancelButton_addNodeWindow = QtWidgets.QPushButton(addNode_window)
            self.addNodeCancelButton_addNodeWindow.setObjectName("addNodeCancelButton_addNodeWindow")
            self.addNodeButtonsLayout_addNodeWindow.addWidget(self.addNodeCancelButton_addNodeWindow)
            self.mainLayout_addNodeWindow.addLayout(self.addNodeButtonsLayout_addNodeWindow)
            self.addNodeButton_addNodeWindow.setText(_translate("addNode_window", "Add Node"))
            self.addNodeCancelButton_addNodeWindow.setText(_translate("addNode_window", "Cancel"))
        else:

            addNode_window.resize(487, 240)
            addNode_window.setMinimumSize(QtCore.QSize(487, 240))
            addNode_window.setMaximumSize(QtCore.QSize(487, 240))

            self.nodeUserPassLabel_addNodeWindow.deleteLater()
            self.nodeUserPassInput_addNodeWindow.deleteLater()
            self.nodeScannerBinaryLabel_addNodeWindow.deleteLater()
            self.nodeScannerBinaryInput_addNodeWindow.deleteLater()
            self.nodeScannerBinaryBrowseButton_addNodeWindow.deleteLater()
            self.nodeArgumentsLabel_addNodeWindow.deleteLater()
            self.nodeArgumentsInput_addNodeWindow.deleteLater()
            self.nodeNumIterationsLabel_addNodeWindow.deleteLater()
            self.nodeNumIterationsSpinBox_addNodeWindow.deleteLater()
            self.nodeMaxParallelRunsLabel_addNodeWindow.deleteLater()
            self.nodeMaxParallelRunsSpinBox_addNodeWindow.deleteLater()
            self.nodeEndConditionLabel_addNodeWindow.deleteLater()
            self.nodeEndConditionInput_addNodeWindow.deleteLater()

            self.mainLayout_addNodeWindow.removeItem(self.nodeUserPassLayout_addNodeWindow)
            self.mainLayout_addNodeWindow.removeItem(self.nodeScannerBinaryLayout_addNodeWindow)
            self.mainLayout_addNodeWindow.removeItem(self.nodeArgumentsLayout_addNodeWindow)
            self.mainLayout_addNodeWindow.removeItem(self.nodeNumIterationsLayout_addNodeWindow)
            self.mainLayout_addNodeWindow.removeItem(self.nodeMaxParallelRunsLayout_addNodeWindow)
            self.mainLayout_addNodeWindow.removeItem(self.nodeEndConditionLayout_addNodeWindow)
            self.mainLayout_addNodeWindow.removeItem(self.addNodeButtonsLayout_addNodeWindow)

            self.addNodeButton_addNodeWindow.deleteLater()
            self.addNodeCancelButton_addNodeWindow.deleteLater()
            self.mainLayout_addNodeWindow.removeItem(self.addNodeButtonsLayout_addNodeWindow)

            self.addNodeButtonsLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.addNodeButtonsLayout_addNodeWindow.setObjectName("addNodeButtonsLayout_addNodeWindow")
            self.addNodeButton_addNodeWindow = QtWidgets.QPushButton(addNode_window)
            self.addNodeButton_addNodeWindow.setObjectName("addNodeButton_addNodeWindow")
            self.addNodeButtonsLayout_addNodeWindow.addWidget(self.addNodeButton_addNodeWindow)
            self.addNodeCancelButton_addNodeWindow = QtWidgets.QPushButton(addNode_window)
            self.addNodeCancelButton_addNodeWindow.setObjectName("addNodeCancelButton_addNodeWindow")
            self.addNodeButtonsLayout_addNodeWindow.addWidget(self.addNodeCancelButton_addNodeWindow)
            self.mainLayout_addNodeWindow.addLayout(self.addNodeButtonsLayout_addNodeWindow)
            self.addNodeButton_addNodeWindow.setText(_translate("addNode_window", "Add Node"))
            self.addNodeCancelButton_addNodeWindow.setText(_translate("addNode_window", "Cancel"))
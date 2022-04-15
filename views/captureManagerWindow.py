from PyQt5 import QtCore, QtWidgets


class Ui_CaptureManagerWindow(object):
    def setupCaptureManager(self, CaptureManagerWindow):
        CaptureManagerWindow.setObjectName("CaptureManagerWindow")
        CaptureManagerWindow.resize(1200, 700)
        CaptureManagerWindow.setMinimumSize(QtCore.QSize(1200, 700))
        self.CentralLayout_captureManagerWindow = QtWidgets.QWidget(CaptureManagerWindow)
        self.CentralLayout_captureManagerWindow.setObjectName("CentralLayout_captureManagerWindow")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.CentralLayout_captureManagerWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonsLayout_captureManagerWindow = QtWidgets.QHBoxLayout()
        self.buttonsLayout_captureManagerWindow.setObjectName("buttonsLayout_captureManagerWindow")

        self.projectButtonsLabel = QtWidgets.QLabel(self.CentralLayout_captureManagerWindow)
        self.projectButtonsLabel.setObjectName("projectButtonsLabel")
        self.buttonsLayout_captureManagerWindow.addWidget(self.projectButtonsLabel)
        
        self.newButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.newButton_captureManagerWindow.setObjectName("newButton_captureManagerWindow")
        self.buttonsLayout_captureManagerWindow.addWidget(self.newButton_captureManagerWindow)
        self.saveButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.saveButton_captureManagerWindow.setObjectName("saveButton_captureManagerWindow")
        self.buttonsLayout_captureManagerWindow.addWidget(self.saveButton_captureManagerWindow)
        self.importButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.importButton_captureManagerWindow.setObjectName("importButton_captureManagerWindow")
        self.buttonsLayout_captureManagerWindow.addWidget(self.importButton_captureManagerWindow)
        self.exportButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.exportButton_captureManagerWindow.setObjectName("exportButton_captureManagerWindow")
        self.buttonsLayout_captureManagerWindow.addWidget(self.exportButton_captureManagerWindow)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonsLayout_captureManagerWindow.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.buttonsLayout_captureManagerWindow, 0, 0, 1, 1)
        self.centralSectionLayout_captureManagerWindow = QtWidgets.QHBoxLayout()
        self.centralSectionLayout_captureManagerWindow.setObjectName("centralSectionLayout_captureManagerWindow")
        self.projectsList_captureManagerWindow = QtWidgets.QTreeWidget(self.CentralLayout_captureManagerWindow)
        self.projectsList_captureManagerWindow.setMinimumSize(QtCore.QSize(220, 0))
        self.projectsList_captureManagerWindow.setMaximumSize(QtCore.QSize(220, 16777215))
        self.projectsList_captureManagerWindow.setObjectName("projectsList_captureManagerWindow")
        self.centralSectionLayout_captureManagerWindow.addWidget(self.projectsList_captureManagerWindow)
        self.scenarioLayout_captureManagerWindow = QtWidgets.QVBoxLayout()
        self.scenarioLayout_captureManagerWindow.setObjectName("scenarioLayout_captureManagerWindow")
        self.scenarioRunLayout_captureManagerWindow = QtWidgets.QHBoxLayout()
        self.scenarioRunLayout_captureManagerWindow.setObjectName("scenarioRunLayout_captureManagerWindow")
        self.scenarioIterationsLabel_captureManagerWindow = QtWidgets.QLabel(self.CentralLayout_captureManagerWindow)
        self.scenarioIterationsLabel_captureManagerWindow.setObjectName("scenarioIterationsLabel_captureManagerWindow")
        self.scenarioRunLayout_captureManagerWindow.addWidget(self.scenarioIterationsLabel_captureManagerWindow)

        self.scenarioIterationsSpinbox_captureManagerWindow = QtWidgets.QSpinBox(self.CentralLayout_captureManagerWindow)
        self.scenarioIterationsSpinbox_captureManagerWindow.setObjectName("scenarioIterationsSpinbox_captureManagerWindow")
        self.scenarioIterationsSpinbox_captureManagerWindow.setValue(1)
        self.scenarioRunLayout_captureManagerWindow.addWidget(self.scenarioIterationsSpinbox_captureManagerWindow)

        self.startVirtualMachineButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.startVirtualMachineButton_captureManagerWindow.setObjectName("startVirtualMachineButton_captureManagerWindow")
        self.scenarioRunLayout_captureManagerWindow.addWidget(self.startVirtualMachineButton_captureManagerWindow)

        self.shutdownVMButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.shutdownVMButton_captureManagerWindow.setObjectName("shutdownVMButton_captureManagerWindow")
        self.scenarioRunLayout_captureManagerWindow.addWidget(self.shutdownVMButton_captureManagerWindow)

        self.runScenarioButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.runScenarioButton_captureManagerWindow.setObjectName("runScenarioButton_captureManagerWindow")
        self.scenarioRunLayout_captureManagerWindow.addWidget(self.runScenarioButton_captureManagerWindow)

        self.stopRestoreScenarioButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.stopRestoreScenarioButton_captureManagerWindow.setObjectName("stopScenarioButton_captureManagerWindow")
        self.scenarioRunLayout_captureManagerWindow.addWidget(self.stopRestoreScenarioButton_captureManagerWindow)

        # self.restoreScenarioButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        # self.restoreScenarioButton_captureManagerWindow.setObjectName("restoreScenarioButton_captureManagerWindow")
        # self.scenarioRunLayout_captureManagerWindow.addWidget(self.restoreScenarioButton_captureManagerWindow)

        self.closeWorkspaceButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.closeWorkspaceButton_captureManagerWindow.setObjectName("closeWorkspaceButton_captureManagerWindow")
        self.scenarioRunLayout_captureManagerWindow.addWidget(self.closeWorkspaceButton_captureManagerWindow)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.scenarioRunLayout_captureManagerWindow.addItem(spacerItem1)
        self.scenarioLayout_captureManagerWindow.addLayout(self.scenarioRunLayout_captureManagerWindow)
        self.nodesList_captureManagerWindow = QtWidgets.QTreeWidget(self.CentralLayout_captureManagerWindow)
        self.nodesList_captureManagerWindow.setObjectName("nodesList_captureManagerWindow")
        self.scenarioLayout_captureManagerWindow.addWidget(self.nodesList_captureManagerWindow)
        self.nodeLayout_captureManagerWindow = QtWidgets.QHBoxLayout()
        self.nodeLayout_captureManagerWindow.setObjectName("nodeLayout_captureManagerWindow")
        self.scenarioStatusLabel_captureManagerWindow = QtWidgets.QLabel(self.CentralLayout_captureManagerWindow)
        self.scenarioStatusLabel_captureManagerWindow.setObjectName("scenarioStatusLabel_captureManagerWindow")
        self.nodeLayout_captureManagerWindow.addWidget(self.scenarioStatusLabel_captureManagerWindow)
        self.scenarioStatus_captureManagerWindow = QtWidgets.QLabel(self.CentralLayout_captureManagerWindow)
        self.scenarioStatus_captureManagerWindow.setObjectName("scenarioStatus_captureManagerWindow")
        self.nodeLayout_captureManagerWindow.addWidget(self.scenarioStatus_captureManagerWindow)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.nodeLayout_captureManagerWindow.addItem(spacerItem2)
        self.addNodeButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.addNodeButton_captureManagerWindow.setObjectName("addNodeButton_captureManagerWindow")
        self.nodeLayout_captureManagerWindow.addWidget(self.addNodeButton_captureManagerWindow)
        self.addSetNodeButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.addSetNodeButton_captureManagerWindow.setObjectName("addSetNodeButton_captureManagerWindow")
        self.nodeLayout_captureManagerWindow.addWidget(self.addSetNodeButton_captureManagerWindow)
        self.scenarioLayout_captureManagerWindow.addLayout(self.nodeLayout_captureManagerWindow)
        self.centralSectionLayout_captureManagerWindow.addLayout(self.scenarioLayout_captureManagerWindow)
        self.gridLayout_2.addLayout(self.centralSectionLayout_captureManagerWindow, 1, 0, 1, 1)
        CaptureManagerWindow.setCentralWidget(self.CentralLayout_captureManagerWindow)
        self.exportButton_captureManagerWindow.setEnabled(False)

        QtCore.QMetaObject.connectSlotsByName(CaptureManagerWindow)

        _translate = QtCore.QCoreApplication.translate
        CaptureManagerWindow.setWindowTitle(_translate("CaptureManagerWindow", "Scan Detection System"))
        self.newButton_captureManagerWindow.setToolTip(_translate("CaptureManagerWindow", "New Project"))
        self.projectButtonsLabel.setText(_translate("CaptureManagerWindow", "  Project Functions  "))
        self.newButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "  New  "))
        self.saveButton_captureManagerWindow.setToolTip(_translate("CaptureManagerWindow", "Save Project"))
        self.saveButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "  Save  "))
        self.importButton_captureManagerWindow.setToolTip(_translate("CaptureManagerWindow", "Import Project"))
        self.importButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Import"))
        self.exportButton_captureManagerWindow.setToolTip(_translate("CaptureManagerWindow", "Export Project"))
        self.exportButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Export"))
        self.projectsList_captureManagerWindow.headerItem().setText(0, _translate("CaptureManagerWindow", "Projects"))
        __sortingEnabled = self.projectsList_captureManagerWindow.isSortingEnabled()
        self.projectsList_captureManagerWindow.setSortingEnabled(False)
        self.projectsList_captureManagerWindow.setSortingEnabled(__sortingEnabled)
        self.scenarioIterationsLabel_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Scenario Iterations:   "))

        self.startVirtualMachineButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Start VM"))
        self.shutdownVMButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Shutdown VM"))

        self.runScenarioButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Run Scenario"))
        self.stopRestoreScenarioButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Stop/Restore Scenario"))
        #self.restoreScenarioButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Restore State"))
        self.closeWorkspaceButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Close Workspace"))
        self.nodesList_captureManagerWindow.headerItem().setText(0, _translate("CaptureManagerWindow", "Log Net Traffic"))
        self.nodesList_captureManagerWindow.headerItem().setText(1, _translate("CaptureManagerWindow", "Type"))
        self.nodesList_captureManagerWindow.headerItem().setText(2, _translate("CaptureManagerWindow", "Name"))
        self.nodesList_captureManagerWindow.headerItem().setText(3, _translate("CaptureManagerWindow", "MAC"))
        self.nodesList_captureManagerWindow.headerItem().setText(4, _translate("CaptureManagerWindow", "IP"))
        #self.nodesList_captureManagerWindow.headerItem().setText(6, _translate("CaptureManagerWindow", "Port"))
        self.nodesList_captureManagerWindow.headerItem().setText(5, _translate("CaptureManagerWindow", "Scanner/Victim"))
        self.scenarioStatusLabel_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Status:"))
        self.scenarioStatus_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Active"))
        self.addNodeButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "    Add Node    "))
        self.addSetNodeButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Set of Victim Nodes"))

        # Temporarily having all buttons enabled
        # self.startVirtualMachineButton_captureManagerWindow.setEnabled(False)
        # self.runScenarioButton_captureManagerWindow.setEnabled(False)
        # self.stopScenarioButton_captureManagerWindow.setEnabled(False)
        # self.restoreScenarioButton_captureManagerWindow.setEnabled(False)
        self.addNodeButton_captureManagerWindow.setEnabled(False)
        self.addSetNodeButton_captureManagerWindow.setEnabled(False)

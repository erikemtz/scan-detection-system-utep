from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupMainWindowUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1131, 747)
        MainWindow.setMinimumSize(QtCore.QSize(812, 580))
        self.CentralLayout_mainWindow = QtWidgets.QWidget(MainWindow)
        self.CentralLayout_mainWindow.setObjectName("CentralLayout_mainWindow")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.CentralLayout_mainWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonsLayout_mainWindow = QtWidgets.QHBoxLayout()
        self.buttonsLayout_mainWindow.setObjectName("buttonsLayout_mainWindow")
        self.newButton_mainWindow = QtWidgets.QPushButton(self.CentralLayout_mainWindow)
        self.newButton_mainWindow.setObjectName("newButton_mainWindow")
        self.buttonsLayout_mainWindow.addWidget(self.newButton_mainWindow)
        self.saveButton_mainWindow = QtWidgets.QPushButton(self.CentralLayout_mainWindow)
        self.saveButton_mainWindow.setObjectName("saveButton_mainWindow")
        self.buttonsLayout_mainWindow.addWidget(self.saveButton_mainWindow)
        self.importButton_mainWindow = QtWidgets.QPushButton(self.CentralLayout_mainWindow)
        self.importButton_mainWindow.setObjectName("importButton_mainWindow")
        self.buttonsLayout_mainWindow.addWidget(self.importButton_mainWindow)
        self.exportButton_mainWindow = QtWidgets.QPushButton(self.CentralLayout_mainWindow)
        self.exportButton_mainWindow.setObjectName("exportButton_mainWindow")
        self.buttonsLayout_mainWindow.addWidget(self.exportButton_mainWindow)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonsLayout_mainWindow.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.buttonsLayout_mainWindow, 0, 0, 1, 1)
        self.centralSectionLayout_mainWindow = QtWidgets.QHBoxLayout()
        self.centralSectionLayout_mainWindow.setObjectName("centralSectionLayout_mainWindow")
        self.projectsList_mainWindow = QtWidgets.QTreeWidget(self.CentralLayout_mainWindow)
        self.projectsList_mainWindow.setMinimumSize(QtCore.QSize(220, 0))
        self.projectsList_mainWindow.setMaximumSize(QtCore.QSize(220, 16777215))
        self.projectsList_mainWindow.setObjectName("projectsList_mainWindow")
        self.centralSectionLayout_mainWindow.addWidget(self.projectsList_mainWindow)
        self.scenarioLayout_mainWindow = QtWidgets.QVBoxLayout()
        self.scenarioLayout_mainWindow.setObjectName("scenarioLayout_mainWindow")
        self.scenarioRunLayout_mainWindow = QtWidgets.QHBoxLayout()
        self.scenarioRunLayout_mainWindow.setObjectName("scenarioRunLayout_mainWindow")
        self.scenarioIterationsLabel_mainWindow = QtWidgets.QLabel(self.CentralLayout_mainWindow)
        self.scenarioIterationsLabel_mainWindow.setObjectName("scenarioIterationsLabel_mainWindow")
        self.scenarioRunLayout_mainWindow.addWidget(self.scenarioIterationsLabel_mainWindow)
        self.scenarioIterationsSpinbox_mainWindow = QtWidgets.QSpinBox(self.CentralLayout_mainWindow)
        self.scenarioIterationsSpinbox_mainWindow.setObjectName("scenarioIterationsSpinbox_mainWindow")
        self.scenarioIterationsSpinbox_mainWindow.setValue(1)
        self.scenarioRunLayout_mainWindow.addWidget(self.scenarioIterationsSpinbox_mainWindow)
        self.startScenarioButton_mainWindow = QtWidgets.QPushButton(self.CentralLayout_mainWindow)
        self.startScenarioButton_mainWindow.setObjectName("startScenarioButton_mainWindow")
        self.scenarioRunLayout_mainWindow.addWidget(self.startScenarioButton_mainWindow)
        self.runScenarioButton_mainWindow = QtWidgets.QPushButton(self.CentralLayout_mainWindow)
        self.runScenarioButton_mainWindow.setObjectName("runScenarioButton_mainWindow")
        self.scenarioRunLayout_mainWindow.addWidget(self.runScenarioButton_mainWindow)
        self.stopScenarioButton_mainWindow = QtWidgets.QPushButton(self.CentralLayout_mainWindow)
        self.stopScenarioButton_mainWindow.setObjectName("stopScenarioButton_mainWindow")
        self.scenarioRunLayout_mainWindow.addWidget(self.stopScenarioButton_mainWindow)
        self.restoreScenarioButton_mainWindow = QtWidgets.QPushButton(self.CentralLayout_mainWindow)
        self.restoreScenarioButton_mainWindow.setObjectName("restoreScenarioButton_mainWindow")
        self.scenarioRunLayout_mainWindow.addWidget(self.restoreScenarioButton_mainWindow)
        self.spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.scenarioRunLayout_mainWindow.addItem(self.spacerItem3)
        self.closeWorkspaceButton_mainWindow = QtWidgets.QPushButton(self.CentralLayout_mainWindow)
        self.closeWorkspaceButton_mainWindow.setObjectName("closeWorkspaceButton_mainWindow")
        self.scenarioRunLayout_mainWindow.addWidget(self.closeWorkspaceButton_mainWindow)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.scenarioRunLayout_mainWindow.addItem(spacerItem1)
        self.scenarioLayout_mainWindow.addLayout(self.scenarioRunLayout_mainWindow)
        self.servicesLayout_mainWindow = QtWidgets.QVBoxLayout()
        self.servicesLayout_mainWindow.setObjectName("servicesLayout_mainWindow")
        self.coreSdsServiceLayout_mainWindow = QtWidgets.QHBoxLayout()
        self.coreSdsServiceLayout_mainWindow.setObjectName("coreSdsServiceLayout_mainWindow")
        self.coreSdsServiceLabel_mainWindow = QtWidgets.QLabel(self.CentralLayout_mainWindow)
        self.coreSdsServiceLabel_mainWindow.setObjectName("coreSdsServiceLabel_mainWindow")
        self.coreSdsServiceLayout_mainWindow.addWidget(self.coreSdsServiceLabel_mainWindow)
        self.coreSdsServiceInput_mainWindow = QtWidgets.QLineEdit(self.CentralLayout_mainWindow)
        self.coreSdsServiceInput_mainWindow.setObjectName("coreSdsServiceInput_mainWindow")
        self.coreSdsServiceLayout_mainWindow.addWidget(self.coreSdsServiceInput_mainWindow)
        self.servicesLayout_mainWindow.addLayout(self.coreSdsServiceLayout_mainWindow)
        self.corePortNumberLayout_mainWindow = QtWidgets.QHBoxLayout()
        self.corePortNumberLayout_mainWindow.setObjectName("corePortNumberLayout_mainWindow")
        self.corePortNumberLabel_mainWindow = QtWidgets.QLabel(self.CentralLayout_mainWindow)
        self.corePortNumberLabel_mainWindow.setObjectName("corePortNumberLabel_mainWindow")
        self.corePortNumberLayout_mainWindow.addWidget(self.corePortNumberLabel_mainWindow)
        self.corePortNumberInput_mainWindow = QtWidgets.QLineEdit(self.CentralLayout_mainWindow)
        self.corePortNumberInput_mainWindow.setObjectName("corePortNumberInput_mainWindow")
        self.corePortNumberLayout_mainWindow.addWidget(self.corePortNumberInput_mainWindow)
        self.servicesLayout_mainWindow.addLayout(self.corePortNumberLayout_mainWindow)
        self.vmSdsServiceLayout_mainWindow = QtWidgets.QHBoxLayout()
        self.vmSdsServiceLayout_mainWindow.setObjectName("vmSdsServiceLayout_mainWindow")
        self.vmSdsServiceLabel_mainWindow = QtWidgets.QLabel(self.CentralLayout_mainWindow)
        self.vmSdsServiceLabel_mainWindow.setObjectName("vmSdsServiceLabel_mainWindow")
        self.vmSdsServiceLayout_mainWindow.addWidget(self.vmSdsServiceLabel_mainWindow)
        self.vmSdsServiceInput_mainWindow = QtWidgets.QLineEdit(self.CentralLayout_mainWindow)
        self.vmSdsServiceInput_mainWindow.setObjectName("vmSdsServiceInput_mainWindow")
        self.vmSdsServiceLayout_mainWindow.addWidget(self.vmSdsServiceInput_mainWindow)
        self.servicesLayout_mainWindow.addLayout(self.vmSdsServiceLayout_mainWindow)
        self.dockerSdsServiceLayout_mainWindow = QtWidgets.QHBoxLayout()
        self.dockerSdsServiceLayout_mainWindow.setObjectName("dockerSdsServiceLayout_mainWindow")
        self.dockerSdsServiceLabel_mainWindow = QtWidgets.QLabel(self.CentralLayout_mainWindow)
        self.dockerSdsServiceLabel_mainWindow.setObjectName("dockerSdsServiceLabel_mainWindow")
        self.dockerSdsServiceLayout_mainWindow.addWidget(self.dockerSdsServiceLabel_mainWindow)
        self.dockerSdsServiceInput_mainWindow = QtWidgets.QLineEdit(self.CentralLayout_mainWindow)
        self.dockerSdsServiceInput_mainWindow.setObjectName("dockerSdsServiceInput_mainWindow")
        self.dockerSdsServiceLayout_mainWindow.addWidget(self.dockerSdsServiceInput_mainWindow)
        self.servicesLayout_mainWindow.addLayout(self.dockerSdsServiceLayout_mainWindow)
        self.scenarioLayout_mainWindow.addLayout(self.servicesLayout_mainWindow)
        self.nodesList_mainWindow = QtWidgets.QTreeWidget(self.CentralLayout_mainWindow)
        self.nodesList_mainWindow.setObjectName("nodesList_mainWindow")
        self.scenarioLayout_mainWindow.addWidget(self.nodesList_mainWindow)
        self.nodeLayout_mainWindow = QtWidgets.QHBoxLayout()
        self.nodeLayout_mainWindow.setObjectName("nodeLayout_mainWindow")
        self.scenarioStatusLabel_mainWindow = QtWidgets.QLabel(self.CentralLayout_mainWindow)
        self.scenarioStatusLabel_mainWindow.setObjectName("scenarioStatusLabel_mainWindow")
        self.nodeLayout_mainWindow.addWidget(self.scenarioStatusLabel_mainWindow)
        self.scenarioStatus_mainWindow = QtWidgets.QLabel(self.CentralLayout_mainWindow)
        self.scenarioStatus_mainWindow.setObjectName("scenarioStatus_mainWindow")
        self.nodeLayout_mainWindow.addWidget(self.scenarioStatus_mainWindow)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.nodeLayout_mainWindow.addItem(spacerItem2)
        self.addNodeButton_mainWindow = QtWidgets.QPushButton(self.CentralLayout_mainWindow)
        self.addNodeButton_mainWindow.setObjectName("addNodeButton_mainWindow")
        self.nodeLayout_mainWindow.addWidget(self.addNodeButton_mainWindow)
        self.setupScenarioButton_mainWindow = QtWidgets.QPushButton(self.CentralLayout_mainWindow)
        self.setupScenarioButton_mainWindow.setObjectName("setupScenarioButton_mainWindow")
        self.nodeLayout_mainWindow.addWidget(self.setupScenarioButton_mainWindow)
        self.scenarioLayout_mainWindow.addLayout(self.nodeLayout_mainWindow)
        self.centralSectionLayout_mainWindow.addLayout(self.scenarioLayout_mainWindow)
        self.gridLayout_2.addLayout(self.centralSectionLayout_mainWindow, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.CentralLayout_mainWindow)
        self.exportButton_mainWindow.setEnabled(False)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scan Detection System"))
        self.newButton_mainWindow.setToolTip(_translate("MainWindow", "New Project"))
        self.newButton_mainWindow.setText(_translate("MainWindow", "  New  "))
        self.saveButton_mainWindow.setToolTip(_translate("MainWindow", "Save Project"))
        self.saveButton_mainWindow.setText(_translate("MainWindow", "  Save  "))
        self.importButton_mainWindow.setToolTip(_translate("MainWindow", "Import Project"))
        self.importButton_mainWindow.setText(_translate("MainWindow", "Import"))
        self.exportButton_mainWindow.setToolTip(_translate("MainWindow", "Export Project"))
        self.exportButton_mainWindow.setText(_translate("MainWindow", "Export"))
        self.projectsList_mainWindow.headerItem().setText(0, _translate("MainWindow", "Projects"))
        __sortingEnabled = self.projectsList_mainWindow.isSortingEnabled()
        self.projectsList_mainWindow.setSortingEnabled(False)
        self.projectsList_mainWindow.setSortingEnabled(__sortingEnabled)
        self.scenarioIterationsLabel_mainWindow.setText(_translate("MainWindow", "Scenario Iterations:   "))
        self.startScenarioButton_mainWindow.setText(_translate("MainWindow", "   Start   "))
        self.runScenarioButton_mainWindow.setText(_translate("MainWindow", "    Run    "))
        self.stopScenarioButton_mainWindow.setText(_translate("MainWindow", "   Stop   "))
        self.restoreScenarioButton_mainWindow.setText(_translate("MainWindow", " Restore "))
        self.closeWorkspaceButton_mainWindow.setText(_translate("MainWindow", " Close Workspace "))
        self.coreSdsServiceLabel_mainWindow.setText(_translate("MainWindow", "CORE SDS Service:   "))
        self.corePortNumberLabel_mainWindow.setText(_translate("MainWindow", "CORE Port Number:  "))
        self.vmSdsServiceLabel_mainWindow.setText(_translate("MainWindow", "SDS VM Service:       "))
        self.dockerSdsServiceLabel_mainWindow.setText(_translate("MainWindow", "SDS Docker Service:"))
        self.nodesList_mainWindow.headerItem().setText(0, _translate("MainWindow", "Log Net Traffic"))
        self.nodesList_mainWindow.headerItem().setText(1, _translate("MainWindow", "Type"))
        self.nodesList_mainWindow.headerItem().setText(2, _translate("MainWindow", "Name"))
        self.nodesList_mainWindow.headerItem().setText(3, _translate("MainWindow", "MAC"))
        self.nodesList_mainWindow.headerItem().setText(4, _translate("MainWindow", "IP"))
        self.nodesList_mainWindow.headerItem().setText(5, _translate("MainWindow", "Port"))
        self.nodesList_mainWindow.headerItem().setText(6, _translate("MainWindow", "Scan/Victim"))
        self.scenarioStatusLabel_mainWindow.setText(_translate("MainWindow", "Status:"))
        self.scenarioStatus_mainWindow.setText(_translate("MainWindow", "Active"))
        self.addNodeButton_mainWindow.setText(_translate("MainWindow", "    Add Node    "))
        self.setupScenarioButton_mainWindow.setText(_translate("MainWindow", "Set up Scenario"))

        self.startScenarioButton_mainWindow.setEnabled(False)
        self.runScenarioButton_mainWindow.setEnabled(False)
        self.stopScenarioButton_mainWindow.setEnabled(False)
        self.restoreScenarioButton_mainWindow.setEnabled(False)
        #self.addNodeButton_mainWindow.setEnabled(False)

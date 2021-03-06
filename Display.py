#  Copyright (c) 2021 Beaker Labs LLC.
#  This software the GNU LGPLv3.0 License

import pickle
import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QDialog, QApplication, QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        screen_dimensions_file = open("dimensions.pkl", "rb")
        screen_dimensions = pickle.load(screen_dimensions_file)
        screen_dimensions_file.close()

        work_area = screen_dimensions

        size_factor = 0.85

        adjusted_width = work_area[2] * size_factor  # for non full screen sizing
        adjusted_height = work_area[3] * size_factor

        screen_dimensions_file = open("dimensions.pkl", "wb")
        dimensions = [work_area, [0, 0, adjusted_width, adjusted_height]]

        pickle.dump(dimensions, screen_dimensions_file)
        screen_dimensions_file.close()

        MainWindow.resize(adjusted_width, adjusted_height)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        altSizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

        # MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(int(adjusted_width * 0.8), int(adjusted_height * 0.80)))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))

        # Central Widget --> verticalLayout --> horizontal layout
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("Centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)

        # horizontalLayout --> Static Label -- variable label
        self.SpotlightSpacer = QtWidgets.QSpacerItem(75, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(self.SpotlightSpacer)

        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 10, 0, 10)

        self.labelStaticTN = QtWidgets.QLabel()
        self.labelStaticTN.setObjectName("labelStaticTN")
        self.labelStaticTN.setText("Place Holder")
        self.labelStaticTN.setSizePolicy(altSizePolicy)
        self.horizontalLayout.addWidget(self.labelStaticTN)

        self.SpotlightSpacer2 = QtWidgets.QSpacerItem(75, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(self.SpotlightSpacer2)

        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName("mdiArea")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.mdiArea.setSizePolicy(sizePolicy)
        self.mdiArea.setEnabled(True)

        self.mdiArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mdiArea.setActivationOrder(QtWidgets.QMdiArea.StackingOrder)
        self.mdiArea.setViewMode(QtWidgets.QMdiArea.TabbedView)
        self.mdiArea.setTabsClosable(True)
        self.mdiArea.setTabsMovable(True)
        self.verticalLayout.addWidget(self.mdiArea)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 18))
        self.menubar.setObjectName("menubar")
        font = self.menubar.font()
        font.setPixelSize(14)
        self.menubar.setFont(font)
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAssets = QtWidgets.QMenu(self.menubar)
        self.menuAssets.setObjectName("menuAssets")
        self.menuLiabilities = QtWidgets.QMenu(self.menubar)
        self.menuLiabilities.setObjectName("menuLiabilities")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)

        self.actionProfile = QtWidgets.QWidgetAction(MainWindow)
        self.actionProfile.setObjectName("actionProfile")
        self.actionSummary = QtWidgets.QWidgetAction(MainWindow)
        self.actionSummary.setObjectName("actionSummary")
        self.actionGenerate = QtWidgets.QWidgetAction(MainWindow)
        self.actionGenerate.setObjectName("actionGenerate")
        self.actionNWG = QtWidgets.QWidgetAction(MainWindow)
        self.actionNWG.setObjectName("actionNWG")
        self.actionExport = QtWidgets.QWidgetAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionSave = QtWidgets.QWidgetAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionClose = QtWidgets.QWidgetAction(MainWindow)
        self.actionClose.setObjectName("actionClose")

        self.actionBank = QtWidgets.QWidgetAction(MainWindow)
        self.actionBank.setObjectName("actionBank")
        self.actionCash = QtWidgets.QWidgetAction(MainWindow)
        self.actionCash.setObjectName("actionCash")
        self.actionCertificate_of_Deposit = QtWidgets.QWidgetAction(MainWindow)
        self.actionCertificate_of_Deposit.setObjectName("actionCertificate_of_Deposit")
        self.actionEquity = QtWidgets.QWidgetAction(MainWindow)
        self.actionEquity.setObjectName("actionEquity")
        self.actionProperty = QtWidgets.QWidgetAction(MainWindow)
        self.actionProperty.setObjectName("actionProperty")
        self.actionTreasury_Bonds = QtWidgets.QWidgetAction(MainWindow)
        self.actionTreasury_Bonds.setObjectName("actionTreasury_Bonds")
        self.actionRetirement = QtWidgets.QWidgetAction(MainWindow)
        self.actionRetirement.setObjectName("actionRetirement")

        self.actionDebt = QtWidgets.QWidgetAction(MainWindow)
        self.actionDebt.setObjectName("actionDebt")
        self.actionCredit_Cards = QtWidgets.QWidgetAction(MainWindow)
        self.actionCredit_Cards.setObjectName("actionCredit_Cards")

        self.actionUserManual = QtWidgets.QWidgetAction(MainWindow)
        self.actionUserManual.setObjectName("actionUserManual")
        self.actionAbout = QtWidgets.QWidgetAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.actionArchive = QtWidgets.QWidgetAction(MainWindow)
        self.actionArchive.setObjectName("actionArchive")
        self.actionReports_Future = QtWidgets.QWidgetAction(MainWindow)
        self.actionReports_Future.setObjectName("actionReports_Future")
        self.actionBudgeting_Future = QtWidgets.QWidgetAction(MainWindow)
        self.actionBudgeting_Future.setObjectName("actionBudgeting_Future")

        submenu_lst = [self.actionSummary, self.actionGenerate, self.actionNWG, self.actionExport, self.actionSave,
                       self.actionClose, self.actionBank, self.actionCash, self.actionCertificate_of_Deposit,
                       self.actionEquity, self.actionProperty, self.actionRetirement, self.actionTreasury_Bonds,
                       self.actionDebt, self.actionCredit_Cards, self.actionCredit_Cards, self.actionUserManual,
                       self.actionAbout, self.actionArchive, self.actionReports_Future, self.actionBudgeting_Future,
                       self.actionProfile]

        for submenu in submenu_lst:
            font = submenu.font()
            font.setPixelSize(12)
            submenu.setFont(font)

        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuFile.addAction(self.actionProfile)
        self.menuFile.addAction(self.actionSummary)
        self.menuFile.addAction(self.actionGenerate)
        self.menuFile.addAction(self.actionNWG)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose)

        self.menuAssets.addAction(self.actionBank)
        self.menuAssets.addAction(self.actionCash)
        self.menuAssets.addAction(self.actionCertificate_of_Deposit)
        self.menuAssets.addAction(self.actionEquity)
        self.menuAssets.addAction(self.actionProperty)
        self.menuAssets.addAction(self.actionTreasury_Bonds)
        self.menuAssets.addAction(self.actionRetirement)

        self.menuLiabilities.addAction(self.actionDebt)
        self.menuLiabilities.addAction(self.actionCredit_Cards)

        self.menuTools.addAction(self.actionArchive)
        self.menuTools.addAction(self.actionBudgeting_Future)
        self.menuAbout.addAction(self.actionUserManual)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAssets.menuAction())
        self.menubar.addAction(self.menuLiabilities.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Artifact from a previous version of this program. My First version was built using the Qt Designer with a Ui to py.
    # I should stop being lazy and remove this and just build this in manually and correctly above
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('MainWindow', "Alchemical Finances - GUI DEMO", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAssets.setTitle(_translate("MainWindow", "Assets", None))
        self.menuLiabilities.setTitle(_translate("MainWindow", "Liabilities", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuAbout.setTitle(_translate("MainWindow", "Other", None))
        self.actionSummary.setText(_translate("MainWindow", "Summary", None))
        self.actionExport.setText(_translate("MainWindow", "Export [Future]", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionBank.setText(_translate("MainWindow", "Bank", None))
        self.actionEquity.setText(_translate("MainWindow", "Equity", None))
        self.actionEquity.setToolTip(_translate("MainWindow", "Equity", None))
        self.actionProperty.setText(_translate("MainWindow", "Property", None))
        self.actionProperty.setToolTip(_translate("MainWindow", "Property", None))
        self.actionCertificate_of_Deposit.setText(_translate("MainWindow", "Certificate of Deposit", None))
        self.actionRetirement.setText(_translate("MainWindow", "Retirement", None))
        self.actionRetirement.setToolTip(_translate("MainWindow", "Retirement", None))
        self.actionTreasury_Bonds.setText(_translate("MainWindow", "Treasury Bonds", None))
        self.actionDebt.setText(_translate("MainWindow", "Debt", None))
        self.actionCredit_Cards.setText(_translate("MainWindow", "Credit Cards", None))
        self.actionCash.setText(_translate("MainWindow", "Cash", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionUserManual.setText(_translate("MainWindow", "User Manual", None))
        self.actionUserManual.setToolTip(_translate("MainWindow", "User Manual", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionAbout.setToolTip(_translate("MainWindow", "Other", None))
        self.actionArchive.setText(_translate("MainWindow", "Archive", None))
        self.actionBudgeting_Future.setText(_translate("MainWindow", "Budgeting [Future]", None))
        self.actionGenerate.setText(_translate("MainWindow", "Generate Report", None))
        self.actionNWG.setText(_translate("MainWindow", "Net Worth Graph", None))
        self.actionProfile.setText(_translate("MainWindow", "User Profile", None))


# This Dialog is a Subwindow for the Mainwindow MdiArea
# Ledger 2 is used for Equity Accounts.

class Ui_Ledger2(object):
    def setupUi(self, Dialog):
        # Dialog settings
        Dialog.setObjectName("Ledger2")
        Dialog.setWindowTitle("Ledger2")  # Will be dynamically changed in the backend

        # Dialog size
        screen_dimensions_file = open("dimensions.pkl", "rb")
        screen_dimensions = pickle.load(screen_dimensions_file)
        screen_dimensions_file.close()

        work_area = screen_dimensions[1]

        size_factor_a = 0.45
        size_factor_b = 0.50

        if 3840 <= work_area[2]:
            size_factor_NA = size_factor_a

        if 2560 <= work_area[2] < 3840:
            size_factor_NA = (3840 * size_factor_a)/2560

        if 1920 <= work_area[2] < 2560:
            size_factor_NA = (3840 * size_factor_a)/1920

        if 1600 <= work_area[2] < 1920:
            size_factor_NA = (3840 * size_factor_a)/1600

        if work_area[2] < 1600:
            size_factor_NA = (3840 * size_factor_a)/1366

        size_factor_NB = (size_factor_b * size_factor_NA)/size_factor_a

        adjusted_width = work_area[2] * size_factor_NA  # for non full screen sizing
        adjusted_height = work_area[3] * size_factor_NB
        Dialog.resize(adjusted_width, adjusted_height)

        # Font and Size Policy
        header_font = QtGui.QFont()
        header_font.setPixelSize(18)
        header_font.setBold(True)

        graph_header_font = QtGui.QFont()
        graph_header_font.setPixelSize(14)
        graph_header_font.setBold(True)

        general_font = QtGui.QFont()
        general_font.setPixelSize(12)
        general_font.setBold(False)

        pushButton_font = QtGui.QFont()
        pushButton_font.setPixelSize(12)
        pushButton_font.setBold(False)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        altSizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

        # Core GridLayout
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")

        # Row 1 --  hVSpacer (C1) -- hSpacer (C2) -- hSpacer3 (C3)
        self.hVSpacer1 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(self.hVSpacer1, 1, 1, 1, 1)

        width_wo_border = adjusted_width - 50
        ledger_width = width_wo_border * 0.80
        category_width = width_wo_border * 0.20

        self.hSpacer1 = QtWidgets.QSpacerItem(ledger_width, 0, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(self.hSpacer1, 1, 2, 1, 1)

        self.hSpacer2 = QtWidgets.QSpacerItem(category_width, 0, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(self.hSpacer2, 1, 3, 1, 1)

        # Row 2 -- QFrame1 (C2) -- QFrame 2 (C3)
        self.ledgerFrame = QtWidgets.QFrame()
        self.ledgerFrame.setObjectName("ledgerFrame")
        scrollFrame_sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.ledgerFrame.setSizePolicy(scrollFrame_sizePolicy)
        self.gridLayout.addWidget(self.ledgerFrame, 2, 2, 1, 1)

        self.outerScrollLayout = QtWidgets.QVBoxLayout(self.ledgerFrame)
        self.outerScrollLayout.setObjectName("outerScrollLayout")

        self.ledgerScroll = QtWidgets.QScrollArea()
        self.ledgerScroll.horizontalScrollBar().setEnabled(True)
        self.ledgerScroll.verticalScrollBar().setEnabled(True)
        self.ledgerScroll.setGeometry(0, 0, self.ledgerFrame.width(), self.ledgerFrame.height())
        self.ledgerScroll.setWidgetResizable(True)
        self.ledgerScroll.setFrameStyle(0)
        self.outerScrollLayout.addWidget(self.ledgerScroll)

        widget = QtWidgets.QWidget()
        widget.setObjectName("scrollWidget")
        self.ledgerScroll.setWidget(widget)

        self.vBLayout1 = QtWidgets.QVBoxLayout(widget)
        self.vBLayout1.setObjectName("vBLayout1")

        self.categoryFrame = QtWidgets.QFrame()
        self.categoryFrame.setObjectName("categoryFrame")
        # self.categoryFrame.setFrameShape(QtWidgets.QFrame.Panel)
        # self.categoryFrame.setLineWidth(1)
        self.categoryFrame.setFixedWidth(category_width)
        self.gridLayout.addWidget(self.categoryFrame, 2, 3, 1, 1)

        self.vBLayout2 = QtWidgets.QVBoxLayout(self.categoryFrame)
        self.vBLayout2.setObjectName("vBLayout2")

        # LedgerFrame -- vBLayout1 -- hbLayout1
        self.hBLayout1 = QtWidgets.QHBoxLayout()
        self.hBLayout1.setObjectName("hBlayout1")
        self.vBLayout1.addLayout(self.hBLayout1)

        self.staticAccount = QtWidgets.QLabel()
        self.staticAccount.setObjectName("staticAccount")
        self.staticAccount.setText("Active Account: ")
        self.staticAccount.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.staticAccount.setFont(header_font)
        self.staticAccount.setFixedWidth(200)
        self.staticAccount.setFixedHeight(40)
        self.staticAccount.setSizePolicy(sizePolicy)
        self.hBLayout1.addWidget(self.staticAccount)

        self.comboBLedger2 = QtWidgets.QComboBox()
        self.comboBLedger2.setObjectName("comboBLedger2")
        self.comboBLedger2.setFont(header_font)
        self.comboBLedger2.setFixedWidth(ledger_width / 3)
        self.comboBLedger2.setFixedHeight(40)
        self.comboBLedger2.setSizePolicy(sizePolicy)
        self.hBLayout1.addWidget(self.comboBLedger2)

        self.pBModAccount = QtWidgets.QPushButton()
        self.pBModAccount.setObjectName("pBModAccount")
        self.pBModAccount.setText("Modify")
        self.pBModAccount.setFont(pushButton_font)
        self.pBModAccount.setFixedWidth(150)
        self.pBModAccount.setFixedHeight(40)
        self.pBModAccount.setSizePolicy(sizePolicy)
        self.hBLayout1.addWidget(self.pBModAccount)

        self.hSpacer3 = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.hBLayout1.addSpacerItem(self.hSpacer3)

        # LedgerFrame --  vBLayout1 -- hbLayout2
        self.vSpacer2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.vBLayout1.addSpacerItem(self.vSpacer2)

        self.hBLayout2 = QtWidgets.QHBoxLayout()
        self.hBLayout2.setObjectName("hBlayout2")
        self.vBLayout1.addLayout(self.hBLayout2)

        self.vSpacer3 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.vBLayout1.addSpacerItem(self.vSpacer3)

        # LedgerFrame --> vBLayout1 --> hBLayout2 --> hSpacer -- LFrame -- CFrame -- RFrame -- hSpacer
        self.hSpacer4 = QtWidgets.QSpacerItem(25, 60, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.hBLayout2.addSpacerItem(self.hSpacer4)

        self.leftDisplayFrame = QtWidgets.QFrame()
        self.leftDisplayFrame.setObjectName("leftFrame")
        self.leftDisplayFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.leftDisplayFrame.setLineWidth(1)
        self.leftDisplayFrame.setFixedWidth((ledger_width - 40) / 3)
        self.leftDisplayFrame.setFixedHeight(60)
        self.hBLayout2.addWidget(self.leftDisplayFrame)

        self.centerDisplayFrame = QtWidgets.QFrame()
        self.centerDisplayFrame.setObjectName("centerFrame")
        self.centerDisplayFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.centerDisplayFrame.setLineWidth(1)
        self.centerDisplayFrame.setFixedWidth((ledger_width - 350) / 3)
        self.centerDisplayFrame.setFixedHeight(60)
        self.hBLayout2.addWidget(self.centerDisplayFrame)

        self.rightDisplayFrame = QtWidgets.QFrame()
        self.rightDisplayFrame.setObjectName("rightFrame")
        self.rightDisplayFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.rightDisplayFrame.setLineWidth(1)
        self.rightDisplayFrame.setFixedWidth((ledger_width - 350) / 3)
        self.rightDisplayFrame.setFixedHeight(60)
        self.hBLayout2.addWidget(self.rightDisplayFrame)

        self.hSpacer5 = QtWidgets.QSpacerItem(25, 60, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.hBLayout2.addSpacerItem(self.hSpacer5)

        # LedgerFrame --  vBLayout1 -- hbLayout2 -- leftDisplayFrame --> hblayout2A --> --> StaticLabel -- Label
        self.hBLayout2A = QtWidgets.QHBoxLayout(self.leftDisplayFrame)
        self.hBLayout2A.setObjectName("hBLayout2A")

        self.lStaticAccountBalance = QtWidgets.QLabel()
        self.lStaticAccountBalance.setObjectName("lStaticAccountBalance")
        self.lStaticAccountBalance.setText("Account Balance: ")
        self.lStaticAccountBalance.setFont(header_font)
        self.lStaticAccountBalance.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.hBLayout2A.addWidget(self.lStaticAccountBalance)

        self.lAccountBalance = QtWidgets.QLabel()
        self.lAccountBalance.setObjectName("lAccountBalance")
        self.lAccountBalance.setText("$ 0.00")
        self.lAccountBalance.setFont(header_font)
        self.lAccountBalance.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.hBLayout2A.addWidget(self.lAccountBalance)

        # LedgerFrame --  vBLayout1 -- hbLayout2 -- CenterDisplayFrame  --> hbLayout2B --> --> StaticLabel -- Label
        self.hBLayout2B = QtWidgets.QHBoxLayout(self.centerDisplayFrame)
        self.hBLayout2B.setObjectName("hBLayout2B")

        self.lStaticShareBal = QtWidgets.QLabel()
        self.lStaticShareBal.setObjectName("lStaticShareBal")
        self.lStaticShareBal.setText("Share Balance: ")
        self.lStaticShareBal.setFont(header_font)
        self.lStaticShareBal.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.hBLayout2B.addWidget(self.lStaticShareBal)

        self.lShareBalance = QtWidgets.QLabel()
        self.lShareBalance.setObjectName("lShareBalance")
        self.lShareBalance.setText("0.0000")
        self.lShareBalance.setFont(header_font)
        self.lShareBalance.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.hBLayout2B.addWidget(self.lShareBalance)

        # LedgerFrame --  vBLayout1 -- hbLayout2 -- RightDisplayFrame  --> hbLayout2C --> --> StaticLabel -- Label
        self.hBLayout2C = QtWidgets.QHBoxLayout(self.rightDisplayFrame)
        self.hBLayout2C.setObjectName("hBLayout2C")

        self.lStaticVariable1 = QtWidgets.QLabel()
        self.lStaticVariable1.setObjectName("lstaticVariable1")
        self.lStaticVariable1.setText("Share Price: ")
        self.lStaticVariable1.setFont(header_font)
        self.lStaticVariable1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.hBLayout2C.addWidget(self.lStaticVariable1)

        self.lVariable1 = QtWidgets.QLabel()
        self.lVariable1.setObjectName("lVariable1")
        self.lVariable1.setText("0.0000")
        self.lVariable1.setFont(header_font)
        self.lVariable1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.hBLayout2C.addWidget(self.lVariable1)

        # LedgerFrame --  vBLayout1 -- hbLayout3 --> hSpacer -- lInputFrame -- rInputFrame -- hSpacer
        self.hBLayout3 = QtWidgets.QHBoxLayout()
        self.hBLayout3.setObjectName("hBlayout3")
        self.hBLayout3.setSpacing(0)
        self.vBLayout1.addLayout(self.hBLayout3)

        self.hSpacer6 = QtWidgets.QSpacerItem(25, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.hBLayout3.addSpacerItem(self.hSpacer6)

        inputFrameWidth = (ledger_width - 250) / 2

        self.lInputFrame = QtWidgets.QFrame()
        self.lInputFrame.setObjectName("lInputFrame")
        self.lInputFrame.setFixedWidth(inputFrameWidth)
        # self.lInputFrame.setFrameShape(QtWidgets.QFrame.Panel)
        # self.lInputFrame.setLineWidth(1)
        self.hBLayout3.addWidget(self.lInputFrame)

        self.rInputFrame = QtWidgets.QFrame()
        self.rInputFrame.setObjectName("rInputFrame")
        self.rInputFrame.setFixedWidth(inputFrameWidth)
        # self.rInputFrame.setFrameShape(QtWidgets.QFrame.Panel)
        # self.rInputFrame.setLineWidth(1)
        self.hBLayout3.addWidget(self.rInputFrame)

        self.hSpacer7 = QtWidgets.QSpacerItem(25, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.hBLayout3.addSpacerItem(self.hSpacer7)

        # LedgerFrame -- VBlayout1 -- hbLayout3 -- lInputFrame --> gridlayout2 --> --> Inputs A
        self.gridLayout2 = QtWidgets.QGridLayout(self.lInputFrame)
        self.gridLayout2.setObjectName("gridLayout2")

        # Inputs A - Row # 1 -- hspacer (C1) hSpacer9  (c2) -- hSpacer 10 (c4) -- hSpacer(C5)
        self.hSpacer13 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout2.addItem(self.hSpacer13, 1, 1, 1, 1)

        self.hSpacer9 = QtWidgets.QSpacerItem(inputFrameWidth - 600, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout2.addItem(self.hSpacer9, 1, 2, 1, 1)

        self.hSpacer10 = QtWidgets.QSpacerItem(100, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout2.addItem(self.hSpacer10, 1, 4, 1, 1)

        # Inputs A - Row # 2 -- Label (c2) -- ComboBox (C3-4)
        self.lTransDate = QtWidgets.QLabel()
        self.lTransDate.setObjectName("lTransDate")
        self.lTransDate.setText("Trans. Date: ")
        self.lTransDate.setFont(general_font)
        self.lTransDate.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lTransDate.setSizePolicy(altSizePolicy)
        self.gridLayout2.addWidget(self.lTransDate, 2, 2, 1, 1)

        self.DateEditTransDate = QtWidgets.QDateEdit()
        self.DateEditTransDate.setObjectName("DateEditTransDate")
        self.DateEditTransDate.setFont(general_font)
        self.DateEditTransDate.setSizePolicy(altSizePolicy)
        self.DateEditTransDate.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.DateEditTransDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.DateEditTransDate.setDisplayFormat("MM/dd/yyyy")
        self.DateEditTransDate.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.DateEditTransDate.setCalendarPopup(True)
        self.DateEditTransDate.setFixedHeight(33)
        self.gridLayout2.addWidget(self.DateEditTransDate, 2, 3, 1, 1)

        # Inputs A - Row # 3 -- Label (c1) -- LineEdit (C2-3)
        self.lTransDesc = QtWidgets.QLabel()
        self.lTransDesc.setObjectName("lTransDesc")
        self.lTransDesc.setText("Trans. Description: ")
        self.lTransDesc.setFont(general_font)
        self.lTransDesc.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lTransDesc.setSizePolicy(altSizePolicy)
        self.gridLayout2.addWidget(self.lTransDesc, 3, 2, 1, 1)

        self.lEditTransDesc = QtWidgets.QLineEdit()
        self.lEditTransDesc.setObjectName("lEditTransDesc")
        self.lEditTransDesc.setPlaceholderText(" (Max 40 Characters)")
        self.lEditTransDesc.setMaxLength(40)
        self.lEditTransDesc.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lEditTransDesc.setFont(general_font)
        self.lEditTransDesc.setSizePolicy(altSizePolicy)
        self.gridLayout2.addWidget(self.lEditTransDesc, 3, 3, 1, 2)

        # Inputs A - Row # 4 -- Label (c1) -- Combobox  (C2) -- pB (C3)
        self.lCategory = QtWidgets.QLabel()
        self.lCategory.setObjectName("lCategory")
        self.lCategory.setText("Category: ")
        self.lCategory.setFont(general_font)
        self.lCategory.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lCategory.setSizePolicy(altSizePolicy)
        self.gridLayout2.addWidget(self.lCategory, 4, 2, 1, 1)

        self.comboBCategory = QtWidgets.QComboBox()
        self.comboBCategory.setObjectName("comboBTCategory")
        self.comboBCategory.setFont(general_font)
        self.comboBCategory.setSizePolicy(altSizePolicy)
        self.comboBCategory.setFixedHeight(33)
        self.gridLayout2.addWidget(self.comboBCategory, 4, 3, 1, 1)

        self.pBCatModify = QtWidgets.QPushButton()
        self.pBCatModify.setObjectName("pBCatModify")
        self.pBCatModify.setText("Modify")
        self.pBCatModify.setFont(pushButton_font)
        self.pBCatModify.setFixedWidth(150)
        self.pBCatModify.setFixedHeight(33)
        self.pBCatModify.setSizePolicy(altSizePolicy)
        self.gridLayout2.addWidget(self.pBCatModify, 4, 4, 1, 1)

        # Inputs A - Row # 5 -- Label (c1) -- LineEdit (C2-3)
        self.lDebit = QtWidgets.QLabel()
        self.lDebit.setObjectName("lDebit")
        self.lDebit.setText("Debit (-): ")
        self.lDebit.setFont(general_font)
        self.lDebit.setAlignment(QtCore.Qt.AlignLeft)
        self.lDebit.setSizePolicy(altSizePolicy)
        self.gridLayout2.addWidget(self.lDebit, 5, 2, 1, 1)

        self.lEditDebit = QtWidgets.QLineEdit()
        self.lEditDebit.setObjectName("lEditDebit")
        self.lEditDebit.setPlaceholderText("0.00 ")
        self.lEditDebit.setAlignment(QtCore.Qt.AlignRight)
        self.lEditDebit.setFont(general_font)
        self.lEditDebit.setSizePolicy(altSizePolicy)
        self.gridLayout2.addWidget(self.lEditDebit, 5, 3, 1, 1)

        # Inputs A - Row # 6 -- Label (c1) -- LineEdit (C2-3)
        self.lCredit = QtWidgets.QLabel()
        self.lCredit.setObjectName("lCredit")
        self.lCredit.setText("Credit (+): ")
        self.lCredit.setFont(general_font)
        self.lCredit.setAlignment(QtCore.Qt.AlignLeft)
        self.lCredit.setSizePolicy(altSizePolicy)
        self.gridLayout2.addWidget(self.lCredit, 6, 2, 1, 1)

        self.lEditCredit = QtWidgets.QLineEdit()
        self.lEditCredit.setObjectName("lEditCredit")
        self.lEditCredit.setPlaceholderText("0.00 ")
        self.lEditCredit.setAlignment(QtCore.Qt.AlignRight)
        self.lEditCredit.setFont(general_font)
        self.lEditCredit.setSizePolicy(altSizePolicy)
        self.gridLayout2.addWidget(self.lEditCredit, 6, 3, 1, 1)

        # Inputs A - Row # 7 -- Label (c1) -- LineEdit (C2-3)
        self.lSharePrice = QtWidgets.QLabel()
        self.lSharePrice.setObjectName("lSharePrice")
        self.lSharePrice.setText("Price per Share: ")
        self.lSharePrice.setFont(general_font)
        self.lSharePrice.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lSharePrice.setSizePolicy(altSizePolicy)
        self.gridLayout2.addWidget(self.lSharePrice, 7, 2, 1, 1)

        self.lEditSharePrice = QtWidgets.QLineEdit()
        self.lEditSharePrice.setObjectName("lEditSharePrice")
        self.lEditSharePrice.setPlaceholderText(" 0.0000")
        self.lEditSharePrice.setMaxLength(20)
        self.lEditSharePrice.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.lEditSharePrice.setFont(general_font)
        self.lEditSharePrice.setSizePolicy(altSizePolicy)
        self.gridLayout2.addWidget(self.lEditSharePrice, 7, 3, 1, 1)

        # Inputs A - Row # 8 -- hSpacer12
        self.hSpacer12 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout2.addItem(self.hSpacer10, 8, 5, 1, 1)

        # LedgerFrame -- VBlayout1 -- hbLayout3 -- rInputFrame --> gridlayout3 --> --> Inputs B
        self.gridLayout3 = QtWidgets.QGridLayout(self.rInputFrame)
        self.gridLayout3.setObjectName("gridLayout3")

        # Inputs B -- Row# 1 - hSpacer3(C1) -- hSpacer15 (C2)
        self.hVSpacer3 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout3.addItem(self.hVSpacer3, 1, 1, 1, 1)

        self.hSpacer14 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout3.addItem(self.hSpacer14, 1, 3, 1, 1)

        # Inputs B -- Row# 2 -- Label -- lEdit Purchase -- Label -- lEdit Sold
        self.lSharesPurchased = QtWidgets.QLabel()
        self.lSharesPurchased.setObjectName("lSharesPurchased")
        self.lSharesPurchased.setText("Shares Purchased:")
        self.lSharesPurchased.setFont(general_font)
        self.lSharesPurchased.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lSharesPurchased.setSizePolicy(altSizePolicy)
        self.gridLayout3.addWidget(self.lSharesPurchased, 2, 2, 1, 1)

        self.lEditSharePurch = QtWidgets.QLineEdit()
        self.lEditSharePurch.setObjectName("lEditSharePurch")
        self.lEditSharePurch.setPlaceholderText(" 0.0000")
        self.lEditSharePurch.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.lEditSharePurch.setFont(general_font)
        self.lEditSharePurch.setFixedWidth(125)
        self.lEditSharePurch.setSizePolicy(altSizePolicy)
        self.gridLayout3.addWidget(self.lEditSharePurch, 2, 4, 1, 1)

        self.lSharesSold = QtWidgets.QLabel()
        self.lSharesSold.setObjectName("lSharesSold")
        self.lSharesSold.setText("Sold: ")
        self.lSharesSold.setFont(general_font)
        self.lSharesSold.setAlignment(QtCore.Qt.AlignRight)
        self.lSharesSold.setSizePolicy(altSizePolicy)
        self.gridLayout3.addWidget(self.lSharesSold, 2, 5, 1, 1)

        self.lEditShareSold = QtWidgets.QLineEdit()
        self.lEditShareSold.setObjectName("lEditShareSold")
        self.lEditShareSold.setPlaceholderText(" 0.0000")
        self.lEditShareSold.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.lEditShareSold.setFont(general_font)
        self.lEditShareSold.setFixedWidth(125)
        self.lEditShareSold.setSizePolicy(altSizePolicy)
        self.gridLayout3.addWidget(self.lEditShareSold, 2, 6, 1, 1)

        # Inputs B -- Row# 3 - label (C2) -- TextEdit (C4-7)
        self.lAddNotes = QtWidgets.QLabel()
        self.lAddNotes.setObjectName("lAddNotes")
        self.lAddNotes.setText("Additional Notes: ")
        self.lAddNotes.setFont(general_font)
        self.lAddNotes.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lAddNotes.setSizePolicy(altSizePolicy)
        self.lAddNotes.setFixedHeight(80)
        self.gridLayout3.addWidget(self.lAddNotes, 3, 2, 1, 1)

        self.textEditAddNotes = QtWidgets.QTextEdit()
        self.textEditAddNotes.setObjectName("textEditAddNotes")
        self.textEditAddNotes.setPlaceholderText(" (Max 150 Characters)")
        self.textEditAddNotes.setFont(general_font)
        self.textEditAddNotes.setMaximumHeight(80)
        self.textEditAddNotes.setSizePolicy(altSizePolicy)
        self.gridLayout3.addWidget(self.textEditAddNotes, 3, 4, 1, 4)

        # Inputs B -- Row# 4 - label (C2) -- QRadiobutton (C4) -- QRadioButton - (C5)
        self.lTransStatus = QtWidgets.QLabel()
        self.lTransStatus.setObjectName("lTransStatus")
        self.lTransStatus.setText("Transaction Status: ")
        self.lTransStatus.setFont(general_font)
        self.lTransStatus.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lTransStatus.setSizePolicy(altSizePolicy)
        self.gridLayout3.addWidget(self.lTransStatus, 4, 2, 1, 1)

        self.rBPending = QtWidgets.QRadioButton()
        self.rBPending.setObjectName("rBPending")
        self.rBPending.setText("Pending")
        self.rBPending.setFont(general_font)
        self.rBPending.setChecked(True)
        self.gridLayout3.addWidget(self.rBPending, 4, 4, 1, 1)

        self.rBPosted = QtWidgets.QRadioButton()
        self.rBPosted.setObjectName("rBPosted")
        self.rBPosted.setText("Posted")
        self.rBPosted.setFont(general_font)
        self.rBPosted.setChecked(False)
        self.gridLayout3.addWidget(self.rBPosted, 4, 5, 1, 1)

        # Inputs B -- Row# 5 - label (C2) -- LineEdit (C3-6)
        self.lReceipt = QtWidgets.QLabel()
        self.lReceipt.setObjectName("lReceipt")
        self.lReceipt.setText("Receipt: ")
        self.lReceipt.setFont(general_font)
        self.lReceipt.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lReceipt.setSizePolicy(altSizePolicy)
        self.gridLayout3.addWidget(self.lReceipt, 5, 2, 1, 1)

        self.lEditReceipt = QtWidgets.QLineEdit()
        self.lEditReceipt.setObjectName("lEditReceipt")
        self.lEditReceipt.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lEditReceipt.setFont(general_font)
        self.lEditReceipt.setSizePolicy(altSizePolicy)
        self.lEditReceipt.setEnabled(False)
        self.gridLayout3.addWidget(self.lEditReceipt, 5, 4, 1, 4)

        # Inputs B -- Row# 6 - blank (C2-3) pushButtons x4 (C3-7)
        self.receptHBLayout = QtWidgets.QHBoxLayout()
        self.receptHBLayout.setObjectName("receiptHBLayout")
        self.gridLayout3.addLayout(self.receptHBLayout, 6, 4, 1, 4, alignment=QtCore.Qt.Alignment())

        self.pBUpload = QtWidgets.QPushButton()
        self.pBUpload.setObjectName("pBUpload")
        self.pBUpload.setText("Upload")
        self.pBUpload.setFont(pushButton_font)
        self.pBUpload.setFixedHeight(30)
        self.pBUpload.setSizePolicy(altSizePolicy)
        self.receptHBLayout.addWidget(self.pBUpload)

        self.pBDisplay = QtWidgets.QPushButton()
        self.pBDisplay.setObjectName("pBDisplay")
        self.pBDisplay.setText("Display")
        self.pBDisplay.setFont(pushButton_font)
        self.pBDisplay.setFixedHeight(30)
        self.pBDisplay.setSizePolicy(altSizePolicy)
        self.receptHBLayout.addWidget(self.pBDisplay)

        self.pBClear = QtWidgets.QPushButton()
        self.pBClear.setObjectName("pBClear")
        self.pBClear.setText("Clear")
        self.pBClear.setFont(pushButton_font)
        self.pBClear.setFixedHeight(30)
        self.pBClear.setSizePolicy(altSizePolicy)
        self.receptHBLayout.addWidget(self.pBClear)

        self.pBDeleteReceipt = QtWidgets.QPushButton()
        self.pBDeleteReceipt.setObjectName("pBDeleteReceipt")
        self.pBDeleteReceipt.setText("Delete")
        self.pBDeleteReceipt.setFont(pushButton_font)
        self.pBDeleteReceipt.setFixedHeight(30)
        self.pBDeleteReceipt.setSizePolicy(altSizePolicy)
        self.receptHBLayout.addWidget(self.pBDeleteReceipt)

        # Inputs B -- Row# 7 - hVSpacer (C8)
        self.hvSpacer4 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout3.addItem(self.hvSpacer4, 7, 8, 1, 1)

        # LedgerFrame --  vBLayout1 --> hbLayout4 --> --> hspacer -- 5x buttons
        self.vSpacer5 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.vBLayout1.addSpacerItem(self.vSpacer5)

        self.hBLayout4 = QtWidgets.QHBoxLayout()
        self.hBLayout4.setObjectName("hBlayout4")
        self.vBLayout1.addLayout(self.hBLayout4)

        self.comboBPeriod = QtWidgets.QComboBox()
        self.comboBPeriod.setObjectName("comboBLedger1")
        self.comboBPeriod.setFont(general_font)
        self.comboBPeriod.setFixedWidth(300)
        self.comboBPeriod.setFixedHeight(33)
        self.comboBPeriod.setSizePolicy(sizePolicy)
        self.hBLayout4.addWidget(self.comboBPeriod)

        self.hSpacer8 = QtWidgets.QSpacerItem(25, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.hBLayout4.addSpacerItem(self.hSpacer8)

        self.pBAddTransaction = QtWidgets.QPushButton()
        self.pBAddTransaction.setObjectName("pBAddTransaction")
        self.pBAddTransaction.setText("Add Transaction")
        self.pBAddTransaction.setFont(pushButton_font)
        self.pBAddTransaction.setFixedWidth(250)
        self.pBAddTransaction.setFixedHeight(40)
        self.pBAddTransaction.setSizePolicy(sizePolicy)
        self.hBLayout4.addWidget(self.pBAddTransaction)

        self.pBSelect = QtWidgets.QPushButton()
        self.pBSelect.setObjectName("pBSelect")
        self.pBSelect.setText("Select")
        self.pBSelect.setFont(pushButton_font)
        self.pBSelect.setFixedWidth(125)
        self.pBSelect.setFixedHeight(40)
        self.pBSelect.setSizePolicy(sizePolicy)
        self.hBLayout4.addWidget(self.pBSelect)

        self.pBUpdate = QtWidgets.QPushButton()
        self.pBUpdate.setObjectName("pBUpdate")
        self.pBUpdate.setText("Update")
        self.pBUpdate.setFont(pushButton_font)
        self.pBUpdate.setFixedWidth(125)
        self.pBUpdate.setFixedHeight(40)
        self.pBUpdate.setSizePolicy(sizePolicy)
        self.hBLayout4.addWidget(self.pBUpdate)

        self.pBDelete = QtWidgets.QPushButton()
        self.pBDelete.setObjectName("pBDelete")
        self.pBDelete.setText("Delete")
        self.pBDelete.setFont(pushButton_font)
        self.pBDelete.setFixedWidth(125)
        self.pBDelete.setFixedHeight(40)
        self.pBDelete.setSizePolicy(sizePolicy)
        self.hBLayout4.addWidget(self.pBDelete)

        self.pBClearInputs = QtWidgets.QPushButton()
        self.pBClearInputs.setObjectName("pBClearInputs")
        self.pBClearInputs.setText("Clear Inputs")
        self.pBClearInputs.setFont(pushButton_font)
        self.pBClearInputs.setFixedWidth(125)
        self.pBClearInputs.setFixedHeight(40)
        self.pBClearInputs.setSizePolicy(sizePolicy)
        self.hBLayout4.addWidget(self.pBClearInputs)

        self.pBUStockPrice = QtWidgets.QPushButton()
        self.pBUStockPrice.setObjectName("pBUStockPrice")
        self.pBUStockPrice.setText("Update Stock Price")
        self.pBUStockPrice.setFont(pushButton_font)
        self.pBUStockPrice.setFixedWidth(250)
        self.pBUStockPrice.setFixedHeight(40)
        self.pBUStockPrice.setSizePolicy(sizePolicy)
        self.hBLayout4.addWidget(self.pBUStockPrice)

        # LedgerFrame -->  vBLayout1 --> hbLayout5 --> --> vSpacer -- QTableWidget
        self.hBLayout5 = QtWidgets.QHBoxLayout()
        self.hBLayout5.setObjectName("hBlayout5")
        self.vBLayout1.addLayout(self.hBLayout5)

        self.vSpacer1 = QtWidgets.QSpacerItem(0, adjusted_height / 2, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        self.hBLayout5.addSpacerItem(self.vSpacer1)

        self.tableWLedger2 = QtWidgets.QTableWidget()
        self.tableWLedger2.setObjectName("tableWLedger2")
        self.tableWLedger2.setLineWidth(2)
        self.tableWLedger2.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWLedger2.setShowGrid(False)
        self.tableWLedger2.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWLedger2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWLedger2.setAlternatingRowColors(True)
        self.tableWLedger2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWLedger2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWLedger2.verticalHeader().setStretchLastSection(False)
        self.tableWLedger2.horizontalHeader().setStretchLastSection(True)
        self.tableWLedger2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWLedger2.setColumnCount(0)
        self.tableWLedger2.setRowCount(0)
        self.hBLayout5.addWidget(self.tableWLedger2)

        # This Frame 'Functions' separately to the LedgerFrame. Intended to provide a breakdown of investments by Type
        # Investment Break down will function on all Ledger2 instances equally regardless of active account.
        # This is not a by transaction component
        # CategoryFrame --> vBLayout2 --> --> QTabWidget w/ 2 Tabs
        self.tabWidgetLedger2 = QtWidgets.QTabWidget()
        self.tabWidgetLedger2.setObjectName("tabWidgetLedger2")
        self.vBLayout2.addWidget(self.tabWidgetLedger2)

        self.tab1Ledger2 = QtWidgets.QWidget()
        self.tab1Ledger2.setObjectName("SubTypeTab")

        self.tabWidgetLedger2.addTab(self.tab1Ledger2, "Type")  # Grouped by Account Type Determined by user.

        self.tab1Ledger2.hBLayout1 = QtWidgets.QHBoxLayout()
        self.tab1Ledger2.setLayout(self.tab1Ledger2.hBLayout1)

        # self.tab1Ledger2.hBlayout1 -- Breakdown by Type
        self.hvSpacer5 = QtWidgets.QSpacerItem(10, 25, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.tab1Ledger2.hBLayout1.addItem(self.hvSpacer5)

        self.lTab1vBLayout = QtWidgets.QVBoxLayout()
        self.lTab1vBLayout.setObjectName("lTab1vBLayout")
        self.tab1Ledger2.hBLayout1.addLayout(self.lTab1vBLayout)

        self.hvSpacer6 = QtWidgets.QSpacerItem(10, 25, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.tab1Ledger2.hBLayout1.addItem(self.hvSpacer6)

        # self.tab1Ledger2.hBlayout1 --> self.lTab1vBlayout --> --> Label -- hSpacer -- frame -- hblayout - hblayout
        self.vSpacer7 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.lTab1vBLayout.addItem(self.vSpacer7)

        self.lTypeBreakdown = QtWidgets.QLabel()
        self.lTypeBreakdown.setObjectName("lTypeBreakdown")
        self.lTypeBreakdown.setText(f"Breakdown by Investment Type")
        self.lTypeBreakdown.setFont(graph_header_font)
        self.lTypeBreakdown.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.lTypeBreakdown.setSizePolicy(altSizePolicy)
        self.lTab1vBLayout.addWidget(self.lTypeBreakdown)

        self.typeFrame = QtWidgets.QFrame()
        self.typeFrame.setObjectName("typeFrame")
        self.typeFrame.setSizePolicy(altSizePolicy)
        self.typeFrame.setFixedHeight(300)
        self.typeFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.typeFrame.setLineWidth(1)
        self.lTab1vBLayout.addWidget(self.typeFrame)

        self.tab1HBLayout1 = QtWidgets.QHBoxLayout()
        self.tab1HBLayout1.setObjectName("tab1HBLayout1")
        self.lTab1vBLayout.addLayout(self.tab1HBLayout1)

        self.tab1HBLayout2 = QtWidgets.QHBoxLayout()
        self.tab1HBLayout2.setObjectName("tab1HBLayout2")
        self.lTab1vBLayout.addLayout(self.tab1HBLayout2)

        # self.tab1Ledger2.hBlayout1 --> self.lTab1vBlayout --> tab1HBLayout1 -- hSpacer -- pbButton toggle
        self.hSpacer11 = QtWidgets.QSpacerItem(10, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.tab1HBLayout1.addItem(self.hSpacer11)

        # self.tab1Ledger2.hBlayout1 --> self.lTab1vBlayout --> tab1HBLayout2 -- vSpacer -- DataScrollArea
        self.vSpacer8 = QtWidgets.QSpacerItem(0, 25, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        self.tab1HBLayout2.addItem(self.vSpacer8)

        self.typeScroll = QtWidgets.QScrollArea()
        self.typeScroll.setObjectName("typeScroll")
        self.typeScroll.horizontalScrollBar().setEnabled(False)
        self.typeScroll.setFrameStyle(0)
        self.tab1HBLayout2.addWidget(self.typeScroll)

        widget = QtWidgets.QWidget()
        self.typeScroll.setWidget(widget)
        self.typeScroll.setWidgetResizable(True)
        self.typeScrollLayout = QtWidgets.QVBoxLayout(widget)

        # Row Last -- hVSpacer (C4)
        self.hVSpacer2 = QtWidgets.QSpacerItem(5, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(self.hVSpacer2, 3, 4, 1, 1)


class initialize_subwindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Ledger2()
        self.ui.setupUi(self)
        self.show()


class initialize(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        subwindow = initialize_subwindow()
        self.ui.mdiArea.addSubWindow(subwindow)
        subwindow.showMaximized()


def main():

    app = QApplication(sys.argv)

    f = open("dimensions.pkl", "wb")
    screen = app.primaryScreen()
    size = screen.size()
    dimensions = [0, 0, size.width(), size.height()]
    pickle.dump(dimensions, f)
    f.close()

    mainwindow = initialize()
    mainwindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/newgui.ui'
#
# Created: Mon Mar 10 15:58:12 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(979, 737)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cbShowLangBoxes = QtGui.QCheckBox(self.centralwidget)
        self.cbShowLangBoxes.setObjectName(_fromUtf8("cbShowLangBoxes"))
        self.horizontalLayout.addWidget(self.cbShowLangBoxes)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 979, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuPoject = QtGui.QMenu(self.menubar)
        self.menuPoject.setObjectName(_fromUtf8("menuPoject"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuInfo = QtGui.QMenu(self.menubar)
        self.menuInfo.setObjectName(_fromUtf8("menuInfo"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuWindow = QtGui.QMenu(self.menubar)
        self.menuWindow.setObjectName(_fromUtf8("menuWindow"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(16, 16))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget_2 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.dockWidgetContents_2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.list_parsingstatus = QtGui.QListWidget(self.dockWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_parsingstatus.sizePolicy().hasHeightForWidth())
        self.list_parsingstatus.setSizePolicy(sizePolicy)
        self.list_parsingstatus.setObjectName(_fromUtf8("list_parsingstatus"))
        self.horizontalLayout_5.addWidget(self.list_parsingstatus)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.teConsole = QtGui.QTextEdit(self.dockWidgetContents)
        self.teConsole.setReadOnly(True)
        self.teConsole.setObjectName(_fromUtf8("teConsole"))
        self.verticalLayout.addWidget(self.teConsole)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        self.actionImport = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-import"))
        self.actionImport.setIcon(icon)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionRandomDel = QtGui.QAction(MainWindow)
        self.actionRandomDel.setObjectName(_fromUtf8("actionRandomDel"))
        self.actionUndoRandomDel = QtGui.QAction(MainWindow)
        self.actionUndoRandomDel.setObjectName(_fromUtf8("actionUndoRandomDel"))
        self.actionOpen = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-open"))
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-save"))
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionNew = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-new"))
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionRun = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("system-run"))
        self.actionRun.setIcon(icon)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.actionSelect_font = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("fonts"))
        self.actionSelect_font.setIcon(icon)
        self.actionSelect_font.setObjectName(_fromUtf8("actionSelect_font"))
        self.actionParse_Tree = QtGui.QAction(MainWindow)
        self.actionParse_Tree.setCheckable(False)
        self.actionParse_Tree.setChecked(False)
        self.actionParse_Tree.setObjectName(_fromUtf8("actionParse_Tree"))
        self.actionAbout = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("help-about"))
        self.actionAbout.setIcon(icon)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionStateGraph = QtGui.QAction(MainWindow)
        self.actionStateGraph.setObjectName(_fromUtf8("actionStateGraph"))
        self.actionUndo = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("undo"))
        self.actionUndo.setIcon(icon)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionRedo = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("redo"))
        self.actionRedo.setIcon(icon)
        self.actionRedo.setObjectName(_fromUtf8("actionRedo"))
        self.actionCut = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("editcut"))
        self.actionCut.setIcon(icon)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionCopy = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("editcopy"))
        self.actionCopy.setIcon(icon)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionPaste = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("editpaste"))
        self.actionPaste.setIcon(icon)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionSave_as = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-save-as"))
        self.actionSave_as.setIcon(icon)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionAdd_language_box = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("insert-text"))
        self.actionAdd_language_box.setIcon(icon)
        self.actionAdd_language_box.setObjectName(_fromUtf8("actionAdd_language_box"))
        self.actionSelect_next_language_box = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("forward"))
        self.actionSelect_next_language_box.setIcon(icon)
        self.actionSelect_next_language_box.setObjectName(_fromUtf8("actionSelect_next_language_box"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuOptions.addAction(self.actionRandomDel)
        self.menuOptions.addAction(self.actionUndoRandomDel)
        self.menuOptions.addAction(self.actionSelect_font)
        self.menuPoject.addAction(self.actionRun)
        self.menuView.addAction(self.actionParse_Tree)
        self.menuView.addAction(self.actionStateGraph)
        self.menuInfo.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionAdd_language_box)
        self.menuEdit.addAction(self.actionSelect_next_language_box)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuPoject.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAdd_language_box)
        self.toolBar.addAction(self.actionSelect_next_language_box)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRun)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSelect_font)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Eco - Editor for language composition", None))
        self.cbShowLangBoxes.setText(_translate("MainWindow", "Show language boxes", None))
        self.label.setText(_translate("MainWindow", "Valid tokens:", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuOptions.setTitle(_translate("MainWindow", "Options", None))
        self.menuPoject.setTitle(_translate("MainWindow", "Project", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuInfo.setTitle(_translate("MainWindow", "Help", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuWindow.setTitle(_translate("MainWindow", "Window", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.dockWidget_2.setWindowTitle(_translate("MainWindow", "Parsing Status", None))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Console", None))
        self.actionImport.setText(_translate("MainWindow", "Import...", None))
        self.actionRandomDel.setText(_translate("MainWindow", "Delete random chars", None))
        self.actionUndoRandomDel.setText(_translate("MainWindow", "Undo random deletion", None))
        self.actionOpen.setText(_translate("MainWindow", "Open...", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionRun.setText(_translate("MainWindow", "Run", None))
        self.actionSelect_font.setText(_translate("MainWindow", "Select font..", None))
        self.actionParse_Tree.setText(_translate("MainWindow", "Tree", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionStateGraph.setText(_translate("MainWindow", "StateGraph", None))
        self.actionUndo.setText(_translate("MainWindow", "Undo", None))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z", None))
        self.actionRedo.setText(_translate("MainWindow", "Redo", None))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z", None))
        self.actionCut.setText(_translate("MainWindow", "Cut", None))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X", None))
        self.actionCopy.setText(_translate("MainWindow", "Copy", None))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C", None))
        self.actionPaste.setText(_translate("MainWindow", "Paste", None))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V", None))
        self.actionSave_as.setText(_translate("MainWindow", "Save as...", None))
        self.actionSave_as.setShortcut(_translate("MainWindow", "Ctrl+Shift+S", None))
        self.actionAdd_language_box.setText(_translate("MainWindow", "Add language box", None))
        self.actionAdd_language_box.setShortcut(_translate("MainWindow", "Ctrl+Space", None))
        self.actionSelect_next_language_box.setText(_translate("MainWindow", "Select next language box", None))
        self.actionSelect_next_language_box.setShortcut(_translate("MainWindow", "Ctrl+Shift+Space", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))


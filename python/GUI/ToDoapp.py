
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    num = -1
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(787, 558)
        MainWindow.setMouseTracking(True)
        MainWindow.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 241, 191))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(80, 230, 88, 34))
        self.run.setObjectName("run")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(60, 270, 131, 16))
        self.line_2.setAutoFillBackground(True)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(260, 30, 511, 221))
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setPlaceholderText("")
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 0, 81, 20))
        self.label_2.setObjectName("label_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(260, 260, 521, 241))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 511, 201))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 0, 511, 201))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 310, 191, 20))
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName("label")
        self.bal = QtWidgets.QCheckBox(self.centralwidget)
        self.bal.setGeometry(QtCore.QRect(60, 360, 151, 20))
        self.bal.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.bal.setObjectName("bal")
        self.tan = QtWidgets.QCheckBox(self.centralwidget)
        self.tan.setGeometry(QtCore.QRect(60, 340, 151, 22))
        self.tan.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tan.setObjectName("tan")
        self.message_crazy = QtWidgets.QLabel(self.centralwidget)
        self.message_crazy.setGeometry(QtCore.QRect(10, 390, 201, 20))
        self.message_crazy.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.message_crazy.setText("")
        self.message_crazy.setObjectName("message_crazy")
        self.database = QtWidgets.QRadioButton(self.centralwidget)
        self.database.setGeometry(QtCore.QRect(50, 430, 161, 22))
        self.database.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.database.setObjectName("database")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.run.clicked.connect(self.data)
        self.tan.stateChanged['int'].connect(self.message_tanbal)
        self.bal.stateChanged['int'].connect(self.check_button)
        self.database.clicked.connect(self.databases)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def data(self):
        self.num += 1
        text = f'task {self.num} : \n{self.plainTextEdit.toPlainText()}'
        self.textBrowser.append(text)
        self.textBrowser.append("----------------------------------------------------------------------")
        self.plainTextEdit.clear()

    def check_button(self , checked):
        
        if checked == Qt.Checked:

            self.textBrowser_2.append(self.textBrowser.toPlainText())
            self.textBrowser.clear()

    def message_tanbal(self , stat):

        if stat == Qt.Checked:

            self.message_crazy.setText("بدو منتظر چی پس؟/:")


    def databases(self):
        #coming soon!
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do app"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", "please Enter your Task"))
        self.run.setText(_translate("MainWindow", "Register"))
        self.label_2.setText(_translate("MainWindow", "کار های پیشرو"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "کار های تمام شده"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "تسک های قدیمی - دیتابیس"))
        self.label.setText(_translate("MainWindow", "کار های پیشروت تموم نشد:("))
        self.bal.setText(_translate("MainWindow", "پس چی, فکردی تنبلم"))
        self.tan.setText(_translate("MainWindow", "تنبلم"))
        self.database.setText(_translate("MainWindow", "اتمام تسک های قدیمی"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

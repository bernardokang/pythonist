


#세상에 내 프로그레스바에 내 인덱스핑거값을 넣었다




from PyQt5 import QtCore, QtGui, QtWidgets

SIMPLE_STYLESHEET = """
QProgressBar{
    border: 2px dotted moccasin;
    border-radius: 5px;
    text-align: center
}

QProgressBar::chunk {
    background-color: lightpink;
    width: 1px;
    margin: 1px;
}
"""


class Ui_MainWindow(object):
    indexfinger = 0


    def plus(self):
        your.indexfinger += 10
        #세상에 내 프로그레스바에 내 인덱스핑거값을 넣었다
        self.progressBar.setValue(your.indexfinger)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 130, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 180, 60, 16))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(250, 90, 118, 23))
        self.progressBar.setProperty("value", self.indexfinger)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setStyleSheet(SIMPLE_STYLESHEET)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.plus)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    your = Ui_MainWindow()
    your.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


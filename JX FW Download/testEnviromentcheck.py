import time
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from Common.function_CheckIP import get_Windows_ip
from Common.function_checkDriver_Ella import checkChromeDriverUpdate
from newGUIui import Ui_JX_FW, main


# global file

class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str) #定义一个发送str的信号
    def write(self, text):
      self.textWritten.emit(str(text))

class checkGoogleDriver(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        checkChromeDriverUpdate()

class runthemainwindow(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        # TesteEnviromentCheck.close()
        import sys
        app2 = QtWidgets.QApplication(sys.argv)
        JX_FW = QtWidgets.QWidget()
        jx = Ui_JX_FW()
        jx.setupUi(JX_FW)
        JX_FW.show()
        sys.exit(app2.exec_())

class Ui_TesteEnviromentCheck(object):
    def __init__(self):
        sys.stdout = EmittingStr(textWritten=self.onUpdateText)
        sys.stderr = EmittingStr(textWritten=self.onUpdateText)

    def onUpdateText(self, text):
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()

    def slot_btn_chooseDir(self):
        dir_choose = QFileDialog.getExistingDirectory()  # 起始路径
        file = dir_choose
        if dir_choose == " ":
            file = "./"
            saveDir = open("saveDir.txt", "wt")
            saveDir.write(file)
            saveDir.close()
            # print(file)
            # print("Your have choose the "+file+"as save location")
        else:
            saveDir = open("saveDir.txt", "wt")
            saveDir.write(file)
            saveDir.close()

    def gotomainwindow(self):
        TesteEnviromentCheck.close()
        import sys
        app2 = QtWidgets.QApplication(sys.argv)
        JX_FW = QtWidgets.QWidget()
        jx = Ui_JX_FW()
        jx.setupUi(JX_FW)
        JX_FW.show()
        sys.exit(app2.exec_())



    def setupUi(self, TesteEnviromentCheck):
        TesteEnviromentCheck.setObjectName("TesteEnviromentCheck")
        TesteEnviromentCheck.resize(362, 307)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(TesteEnviromentCheck)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(TesteEnviromentCheck)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.chooseSaveDir = QtWidgets.QPushButton(TesteEnviromentCheck)
        self.chooseSaveDir.setMinimumSize(QtCore.QSize(0, 40))
        self.chooseSaveDir.setObjectName("next")
        self.chooseSaveDir2 = QtWidgets.QPushButton(TesteEnviromentCheck)
        self.chooseSaveDir2.setMinimumSize(QtCore.QSize(0, 40))
        self.chooseSaveDir2.setObjectName("chooseSaveDir")
        self.verticalLayout.addWidget(self.chooseSaveDir)
        self.verticalLayout.addWidget(self.chooseSaveDir2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.chooseSaveDir.clicked.connect(lambda:self.slot_btn_chooseDir())
        self.chooseSaveDir2.clicked.connect(lambda:self.gotomainwindow())
        self.retranslateUi(TesteEnviromentCheck)
        QtCore.QMetaObject.connectSlotsByName(TesteEnviromentCheck)

    def retranslateUi(self, TesteEnviromentCheck):
        _translate = QtCore.QCoreApplication.translate
        TesteEnviromentCheck.setWindowTitle(_translate("TesteEnviromentCheck", "Test Enviroment check"))
        TesteEnviromentCheck.setWindowIcon(QIcon('jabra.ico'))
        self.chooseSaveDir.setText(_translate("TesteEnviromentCheck", "Select the folder to save test package"))
        self.chooseSaveDir2.setText(_translate("TesteEnviromentCheck", "Go to the Main Window"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TesteEnviromentCheck = QtWidgets.QWidget()
    ui = Ui_TesteEnviromentCheck()
    ui.setupUi(TesteEnviromentCheck)
    TesteEnviromentCheck.show()
    #Check network
    ipaddress=get_Windows_ip()
    print("Check Network : ")

    if ipaddress==True:
        print("Supported network")
        print("\n")
        print("Start check Google Chrome driver....")
        checkDriver=checkGoogleDriver()
        checkDriver.start()

    else:
        print("Unsupported netwrok")
        print("Supported network list:")
        print("   -Intra-gnn.com")
        print("   -Rand-gnn.com")
        print("   -GN-Wifi")
        print("Please Switch to the Supported network and restart the APP")

    sys.exit(app.exec_())

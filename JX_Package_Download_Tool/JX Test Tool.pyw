import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog
from multiprocessing import  process

from Common.function_CheckIP import get_Windows_ip
from Common.function_checkDriver_Ella import checkChromeDriverUpdate

from TestCase_Linux.case10312_L import testcase10312l
from TestCase_Linux.case16991 import testcase16991
from TestCase_Linux.case7692 import testcase7692
from TestCase_Linux.case6134 import testcase6134
from TestCase_Linux.case7551 import testcase7551
from TestCase_Linux.case7695 import testcase7695
from TestCase_Linux.case7555 import testcase7555
from TestCase_Linux.case7556 import testcase7556
from TestCase_Linux.case16990 import testcase16990
from TestCase_Linux.case6098 import testcase6098
from TestCase_Windows.case10449 import testcase10449
from TestCase_Windows.case3961 import testcase3961
from TestCase_Windows.case3965 import testcase3965
from TestCase_Windows.case3965_32b import testcase3965_32b
from TestCase_Windows.case3966 import testcase3966
from TestCase_Windows.case3968 import testcase3968
from TestCase_Windows.case3969 import testcase3969
from TestCase_Windows.case4090 import testcase4090
from TestCase_Windows.case4090_32b import testcase4090_32b
from TestCase_Windows.case4128_1 import testcase4128_1
from TestCase_Windows.case4128_2 import testcase4128_2
from TestCase_Windows.case4128_3 import testcase4128_3
from TestCase_Windows.case4153_1 import testcase4153_1
from TestCase_Windows.case4153_2 import testcase4153_2
from TestCase_Windows.case5509 import testcase5509
from TestCase_Windows.case5509_32b import testcase5509_32b
from TestCase_Windows.case5664 import testcase5664
from TestCase_Windows.case5665 import testcase5665
from TestCase_Windows.case7195 import testcase7195
from TestCase_Windows.case7196 import testcase7196
from TestCase_Windows.case3966_32b import testcase3966_32b
from TestCase_Windows.case5664_32b import testcase5664_32b
from TestCase_Windows.case5665_32b import testcase5665_32b
from TestCase_Windows.case10312_w import testcase10312w
from Common.function_Configure import getLocation
from Common.function_GetInfo import getXpressVersion
items_list=[
'Jabra BIZ 1500 MS USB Duo',
'Jabra BIZ 1500 MS USB Mono',
'Jabra BIZ 1500 USB Duo',
'Jabra BIZ 1500 USB Mono',
'Jabra BIZ 2300 USB Duo',
'Jabra BIZ 2300 USB Mono',
'Jabra BIZ 2400 II CC USB Mono',
'Jabra BIZ 2400 II CC USB Stereo',
'Jabra BIZ 2400 II Duo',
'Jabra EVOLVE2 75',
'Jabra BIZ 2400 II Mono',
'Jabra BIZ 2400 USB Duo',
'Jabra BIZ 2400 USB Mono',
'Jabra DIAL 550',
'Jabra Engage 50',
'Jabra PanaCast 20',
'Jabra Engage 65',
'Jabra Engage 75',
'Jabra EVOLVE 20 Mono',
'Jabra EVOLVE 20 SE Mono',
'Jabra EVOLVE 20 SE Stereo',
'Jabra EVOLVE 20 Stereo',
'Jabra EVOLVE 30 II Mono',
'Jabra EVOLVE 30 II Stereo',
'Jabra EVOLVE 30 Mono',
'Jabra EVOLVE 30 Stereo',
'Jabra EVOLVE 40 Mono',
'Jabra EVOLVE 40/80 Stereo',
'Jabra EVOLVE 65 Mono',
'Jabra EVOLVE 65 Stereo',
'Jabra Evolve 65e',
'Jabra Evolve 75',
'Jabra Evolve 75e',
'Jabra EVOLVE2 40',
'Jabra Evolve2 65 Deskstand',
'Jabra EVOLVE2 65 Mono',
'Jabra EVOLVE2 65 Stereo',
'Jabra EVOLVE2 85',
'Jabra Evolve2 85 Deskstand',
'Jabra GN2000 MS USB Mono / Duo',
'Jabra GN2000 USB Mono / Duo',
'Jabra GO 6470',
'Jabra HANDSET 450',
'Jabra LINK 220 QD to USB Adapter',
'Jabra LINK 220a QD to USB Adapter',
'Jabra LINK 230 QD to USB Adapter',
'Jabra LINK 260 MS QD to USB Adapter',
'Jabra LINK 260 QD to USB Adapter',
'Jabra LINK 265 QD to USB Training Adapter',
'Jabra LINK 280 QD to USB Adapter',
'Jabra LINK 350 (GO 6430)',
'Jabra LINK 360',
'Jabra LINK 370',
'Jabra LINK 370 MS Teams',
'Jabra Link 380a',
'Jabra LINK 380c',
'Jabra LINK 850',
'Jabra LINK 860',
'Jabra LINK 950',
'Jabra MOTION OFFICE',
'Jabra MOTION UC',
'Jabra PRO 925 Dual Connectivity',
'Jabra PRO 925 Single Connectivity',
'Jabra PRO 930',
'Jabra PRO 935 Dual Connectivity',
'Jabra PRO 935 Single Connectivity',
'Jabra PRO 9450 Series',
'Jabra PRO 9460 Series',
'Jabra PRO 9465 / 9470',
'Jabra SPEAK 410',
'Jabra SPEAK 450 Cisco',
'Jabra SPEAK 510',
'Jabra SPEAK 710',
'Jabra SPEAK 750 MS Teams',
'Jabra SPEAK 750 UC',
'Jabra SPEAK 810',
'Jabra STEALTH UC',
'Jabra SUPREME UC',
'Jabra UC VOICE 150a Duo (Version A)',
'Jabra UC VOICE 150a Mono (Version A)',
'Jabra UC VOICE 150a MS Duo (Version A)',
'Jabra UC VOICE 150a MS Mono (Version A)',
'Jabra UC VOICE 250a (Version A)',
'Jabra UC VOICE 250a MS (Version A)',
'Jabra UC VOICE 550a Duo (Version A)',
'Jabra UC VOICE 550a Mono (Version A)',
'Jabra UC VOICE 550a MS Duo (Version A)',
'Jabra UC VOICE 550a MS Mono (Version A)',
'Jabra UC VOICE 750a Duo (Version A)',
'Jabra UC VOICE 750a Mono (Version A)',
'Jabra UC VOICE 750a MS Duo (Version A)',
'Jabra UC VOICE 750a MS Mono (Version A)',
'Jabra EVOLVE2 30'
]


class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str) #定义一个发送str的信号
    def write(self, text):
      self.textWritten.emit(str(text))

class EmittingStr2(QtCore.QObject):
    textWritten2 = QtCore.pyqtSignal(str) #定义一个发送str的信号
    def write(self, text):
      self.textWritten2.emit(str(text))

class checkGoogleDriver(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        checkChromeDriverUpdate()
        print("\n")
        print("Please click the 1st button to choose the location that test package should save.")
        print("Then click the 2nd button to the main windows - choose what case want test.")


class startdownloadThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        testcaselist = Ui_JX_FW.excuteTestCase
        for testcase in testcaselist:
            testcase = "test" + testcase
            print('Start configure '+testcase)
            eval(testcase)()
        print("All the test package that you choose is downloaded!")

class getXpressVersionThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        # global xpress_version
        getXpressVersion()


class saveLocation(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        print("Wait a few second.....")
        dir_choose = QFileDialog.getExistingDirectory()  # 起始路径
        file = dir_choose
        if dir_choose == " ":
            file = "./"
            saveDir = open("saveDir.txt", "wt")
            saveDir.write(file)
            saveDir.close()
            print("You have choose this location that test package will keep:"+file)
        else:
            saveDir = open("saveDir.txt", "wt")
            saveDir.write(file)
            saveDir.close()
            print("You have choose this location that test package will keep:"+file)
            # self.chooseSaveDir2.setEnabled(True)

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
        print("\n")
        print("Wait a few second.....")
        dir_choose = QFileDialog.getExistingDirectory()  # 起始路径
        file = dir_choose
        if dir_choose == " ":
            file = "./"
            saveDir = open("saveDir.txt", "wt")
            saveDir.write(file)
            saveDir.close()
            print("You have choose this location that test package will keep:"+file)
        else:
            saveDir = open("saveDir.txt", "wt")
            saveDir.write(file)
            saveDir.close()
            print("You have choose this location that test package will keep:"+file)
            self.chooseSaveDir2.setEnabled(True)
        try:
            currentversion = getXpressVersionThread()
            currentversion.run()
        except Exception as e:
            print(e)


    def gotomainwindow(self):
        TesteEnviromentCheck.close()
        time.sleep(0.5)
        jx = Ui_JX_FW()
        jx.setupUi(JX_FW)
        JX_FW.show()

    def setupUi(self, TesteEnviromentCheck):
        TesteEnviromentCheck.setObjectName("TesteEnviromentCheck")
        TesteEnviromentCheck.setStyleSheet("background-color: rgb(255, 255, 222);")
        TesteEnviromentCheck.resize(600, 400)
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
        self.chooseSaveDir2.setEnabled(False)
        self.font=QtGui.QFont()
        self.font.setPointSize(10)
        self.font.setFamily("SimHei")
        self.textBrowser.setFont(self.font)
        self.retranslateUi(TesteEnviromentCheck)
        QtCore.QMetaObject.connectSlotsByName(TesteEnviromentCheck)

    def retranslateUi(self, TesteEnviromentCheck):
        _translate = QtCore.QCoreApplication.translate
        TesteEnviromentCheck.setWindowTitle(_translate("TesteEnviromentCheck", "Test Enviroment check"))
        TesteEnviromentCheck.setWindowIcon(QIcon('jabra.ico'))
        self.chooseSaveDir.setText(_translate("TesteEnviromentCheck", "Select the folder to save test package"))
        self.chooseSaveDir2.setText(_translate("TesteEnviromentCheck", "Go to the Main Window"))
        TesteEnviromentCheck.setWindowIcon(QIcon('jabra.ico'))


class Ui_JX_FW(object):
    def __init__(self):
        sys.stdout = EmittingStr2(textWritten2=self.onUpdateText2)
        sys.stderr = EmittingStr2(textWritten2=self.onUpdateText2)

    def onUpdateText2(self, text):
        cursor = self.textbox_progress.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textbox_progress.setTextCursor(cursor)
        self.textbox_progress.ensureCursorVisible()

    excuteTestCase = []


    #Add test case that user select to Ui_JX_FW.excuteTestCase
    def addCase(self,testcase):
        testcase = testcase
        if (testcase in Ui_JX_FW.excuteTestCase):
            Ui_JX_FW.excuteTestCase.remove(testcase)
            # print(Ui_JX_FW.excuteTestCase)
        elif(testcase=='case4128'):
            Ui_JX_FW.excuteTestCase.append('case4128_1')
            Ui_JX_FW.excuteTestCase.append('case4128_2')
            Ui_JX_FW.excuteTestCase.append('case4128_3')
        elif(testcase=='case4153'):
            Ui_JX_FW.excuteTestCase.append('case4153_1')
            Ui_JX_FW.excuteTestCase.append('case4153_2')
        else:
            Ui_JX_FW.excuteTestCase.append(testcase)
            # print(Ui_JX_FW.excuteTestCase)

    #Define the download function - - Start the new Thread.
    def startNewThread(self):
        self.startNewThread=startdownloadThread()
        # print("thread created")
        self.startNewThread.start()

    def saveDeviceName(self):
        DeviceName = self.combox_chooseDevice.currentText()
        print("Test device is " + DeviceName)
        fo = open("device.txt", "wt")
        fo.write(DeviceName)
        fo.close()

    def startbuttonevent(self):
        self.button_start.setEnabled(False)
        self.saveDeviceName()
        print("Download will start......")
        self.startNewThread()
        # self.currentversion()


    def setupUi(self, JX_FW):
        JX_FW.setObjectName("JX_FW")
        JX_FW.resize(800, 879)
        JX_FW.setStyleSheet("background-color: rgb(255, 255, 222);")
        self.Layout_global = QtWidgets.QVBoxLayout(JX_FW)
        self.Layout_global.setObjectName("Layout_global")
        self.HLayout_first = QtWidgets.QHBoxLayout()
        self.HLayout_first.setObjectName("HLayout_first")
        self.label_theCurrentVersion = QtWidgets.QLabel(JX_FW)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_theCurrentVersion.setFont(font)
        self.label_theCurrentVersion.setObjectName("label_theCurrentVersion")
        self.HLayout_first.addWidget(self.label_theCurrentVersion)
        self.label_theCurrentVersionSet = QtWidgets.QLabel(JX_FW)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_theCurrentVersionSet.setFont(font)
        self.label_theCurrentVersionSet.setObjectName("label_theCurrentVersionSet")
        self.HLayout_first.addWidget(self.label_theCurrentVersionSet)
        self.Layout_global.addLayout(self.HLayout_first)
        self.HLayout_second = QtWidgets.QHBoxLayout()
        self.HLayout_second.setObjectName("HLayout_second")
        self.label_empty_1 = QtWidgets.QLabel(JX_FW)
        self.label_empty_1.setText("")
        self.label_empty_1.setObjectName("label_empty_1")
        self.HLayout_second.addWidget(self.label_empty_1)
        self.label_empty_2 = QtWidgets.QLabel(JX_FW)
        self.label_empty_2.setText("")
        self.label_empty_2.setObjectName("label_empty_2")
        self.HLayout_second.addWidget(self.label_empty_2)
        self.Layout_global.addLayout(self.HLayout_second)
        self.HLayout_third = QtWidgets.QHBoxLayout()
        self.HLayout_third.setObjectName("HLayout_third")
        self.label_empty_3 = QtWidgets.QLabel(JX_FW)
        self.label_empty_3.setEnabled(False)
        self.label_empty_3.setText("")
        self.label_empty_3.setObjectName("label_empty_3")
        self.HLayout_third.addWidget(self.label_empty_3)
        self.label_chooseDevice = QtWidgets.QLabel(JX_FW)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_chooseDevice.setFont(font)
        self.label_chooseDevice.setWordWrap(True)
        self.label_chooseDevice.setObjectName("label_chooseDevice")
        self.HLayout_third.addWidget(self.label_chooseDevice)
        self.combox_chooseDevice = QtWidgets.QComboBox(JX_FW)
        self.combox_chooseDevice.setMinimumSize(QtCore.QSize(0, 35))
        self.combox_chooseDevice.setEditable(True)
        self.combox_chooseDevice.setObjectName("combox_chooseDevice")
        self.HLayout_third.addWidget(self.combox_chooseDevice)
        self.label_empty_4 = QtWidgets.QLabel(JX_FW)
        self.label_empty_4.setEnabled(False)
        self.label_empty_4.setText("")
        self.label_empty_4.setObjectName("label_empty_4")
        self.HLayout_third.addWidget(self.label_empty_4)
        self.Layout_global.addLayout(self.HLayout_third)
        self.HLayout_forth = QtWidgets.QGridLayout()
        self.HLayout_forth.setContentsMargins(-1, -1, 200, -1)
        self.HLayout_forth.setObjectName("HLayout_forth")
        self.label_Windows = QtWidgets.QLabel(JX_FW)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Windows.sizePolicy().hasHeightForWidth())
        self.label_Windows.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Windows.setFont(font)
        self.label_Windows.setToolTipDuration(0)
        self.label_Windows.setObjectName("label_Windows")
        self.HLayout_forth.addWidget(self.label_Windows, 0, 0, 1, 1)
        # self.label_empty_5 = QtWidgets.QLabel(JX_FW)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_empty_5.sizePolicy().hasHeightForWidth())
        # self.label_empty_5.setSizePolicy(sizePolicy)
        # self.label_empty_5.setMinimumSize(QtCore.QSize(20, 10))
        # self.label_empty_5.setText("")
        # self.label_empty_5.setObjectName("label_empty_5")
        # self.HLayout_forth.addWidget(self.label_empty_5, 0, 1, 1, 1)
        self.label_Linux = QtWidgets.QLabel(JX_FW)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Linux.sizePolicy().hasHeightForWidth())
        self.label_Linux.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Linux.setFont(font)
        self.label_Linux.setToolTipDuration(0)
        self.label_Linux.setObjectName("label_Linux")
        self.HLayout_forth.addWidget(self.label_Linux, 0, 1, 1, 1)
        self.HLayout_forth.setColumnMinimumWidth(0, 5)
        self.HLayout_forth.setColumnMinimumWidth(1, 1)
        self.HLayout_forth.setColumnMinimumWidth(2, 5)
        self.HLayout_forth.setColumnStretch(0, 3)
        self.HLayout_forth.setColumnStretch(1, 1)
        self.HLayout_forth.setColumnStretch(2, 3)
        self.Layout_global.addLayout(self.HLayout_forth)
        self.HLayout_fifth = QtWidgets.QHBoxLayout()
        self.HLayout_fifth.setObjectName("HLayout_fifth")
        self.VLayout_win = QtWidgets.QVBoxLayout()
        self.VLayout_win.setObjectName("VLayout_win")
        self.checkBox_checkAll_win = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_checkAll_win.setObjectName("checkBox_checkAll_win")
        self.VLayout_win.addWidget(self.checkBox_checkAll_win)
        self.checkBox_case3961 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case3961.setObjectName("checkBox_case3961")
        self.VLayout_win.addWidget(self.checkBox_case3961)
        self.checkBox_case3965 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case3965.setObjectName("checkBox_case3965")
        self.VLayout_win.addWidget(self.checkBox_case3965)
        self.checkBox_case3966 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case3966.setObjectName("checkBox_case3966")
        self.VLayout_win.addWidget(self.checkBox_case3966)
        self.checkBox_case3968 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case3968.setObjectName("checkBox_case3968")
        self.VLayout_win.addWidget(self.checkBox_case3968)
        self.checkBox_case3969 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case3969.setObjectName("checkBox_case3969")
        self.VLayout_win.addWidget(self.checkBox_case3969)
        self.checkBox_case4090 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case4090.setObjectName("checkBox_case4090")
        self.VLayout_win.addWidget(self.checkBox_case4090)
        self.checkBox_case4128 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case4128.setObjectName("checkBox_case4128")
        self.VLayout_win.addWidget(self.checkBox_case4128)
        self.checkBox_case4153 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case4153.setObjectName("checkBox_case4153")
        self.VLayout_win.addWidget(self.checkBox_case4153)
        self.checkBox_case5509 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case5509.setObjectName("checkBox_case5509")
        self.VLayout_win.addWidget(self.checkBox_case5509)
        self.checkBox_case7196 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case7196.setObjectName("checkBox_case7196")
        self.VLayout_win.addWidget(self.checkBox_case7196)
        self.checkBox_case5665 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case5665.setObjectName("checkBox_case5665")
        self.VLayout_win.addWidget(self.checkBox_case5665)
        self.checkBox_case7195 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case7195.setObjectName("checkBox_case7195")
        self.VLayout_win.addWidget(self.checkBox_case7195)
        self.checkBox_case10449 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case10449.setObjectName("checkBox_case10449")
        self.VLayout_win.addWidget(self.checkBox_case10449)
        self.checkBox_case10312 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case10312.setObjectName("checkBox_case10312")
        self.VLayout_win.addWidget(self.checkBox_case10312)
        self.checkBox_case3965_32b = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case3965_32b.setObjectName("checkBox_case3965_32b")
        self.VLayout_win.addWidget(self.checkBox_case3965_32b)
        self.checkBox_case3966_32b = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case3966_32b.setObjectName("checkBox_case3966_32b")
        self.VLayout_win.addWidget(self.checkBox_case3966_32b)
        self.checkBox_case4090_32b = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case4090_32b.setObjectName("checkBox_case4090_32b")
        self.VLayout_win.addWidget(self.checkBox_case4090_32b)
        self.checkBox_case5664_32b = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case5664_32b.setObjectName("checkBox_case5664_32b")
        self.VLayout_win.addWidget(self.checkBox_case5664_32b)
        self.checkBox_case5509_32b = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case5509_32b.setObjectName("checkBox_case5509_32b")
        self.VLayout_win.addWidget(self.checkBox_case5509_32b)
        self.checkBox_case5665_32b = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case5665_32b.setObjectName("checkBox_case5665_32b")
        self.VLayout_win.addWidget(self.checkBox_case5665_32b)
        self.HLayout_fifth.addLayout(self.VLayout_win)
        self.VLayout_linux = QtWidgets.QVBoxLayout()
        self.VLayout_linux.setObjectName("VLayout_linux")
        self.checkbox_selectAll_linux = QtWidgets.QCheckBox(JX_FW)
        self.checkbox_selectAll_linux.setObjectName("checkbox_selectAll_linux")
        self.VLayout_linux.addWidget(self.checkbox_selectAll_linux)
        self.checkBox_case6098 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case6098.setObjectName("checkBox_case6098")
        self.VLayout_linux.addWidget(self.checkBox_case6098)
        self.checkBox_case6134 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case6134.setObjectName("checkBox_case6134")
        self.VLayout_linux.addWidget(self.checkBox_case6134)
        self.checkBox_case7555 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case7555.setObjectName("checkBox_case7555")
        self.VLayout_linux.addWidget(self.checkBox_case7555)
        self.checkBox_case7695 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case7695.setObjectName("checkBox_case7695")
        self.VLayout_linux.addWidget(self.checkBox_case7695)
        self.checkBox_case7692 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case7692.setObjectName("checkBox_case7692")
        self.VLayout_linux.addWidget(self.checkBox_case7692)
        self.checkBox_case7551 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case7551.setObjectName("checkBox_case7551")
        self.VLayout_linux.addWidget(self.checkBox_case7551)
        self.checkBox_case7556 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case7556.setObjectName("checkBox_case7556")
        self.VLayout_linux.addWidget(self.checkBox_case7556)
        self.checkBox_case10312_2 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case10312_2.setObjectName("checkBox_case10312_2")
        self.VLayout_linux.addWidget(self.checkBox_case10312_2)
        self.checkBox_case16990 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case16990.setObjectName("checkBox_case16990")
        self.VLayout_linux.addWidget(self.checkBox_case16990)
        self.checkBox_case16991 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_case16991.setObjectName("checkBox_case16991")
        self.VLayout_linux.addWidget(self.checkBox_case16991)
        self.HLayout_fifth.addLayout(self.VLayout_linux)
        self.Layout_global.addLayout(self.HLayout_fifth)
        self.HLayout_sixth = QtWidgets.QHBoxLayout()
        self.HLayout_sixth.setObjectName("HLayout_sixth")
        self.label_8 = QtWidgets.QLabel(JX_FW)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.HLayout_sixth.addWidget(self.label_8)
        self.button_start = QtWidgets.QPushButton(JX_FW)
        self.button_start.setMinimumSize(QtCore.QSize(10, 40))
        self.button_start.setObjectName("button_start")
        self.HLayout_sixth.addWidget(self.button_start)
        self.label_9 = QtWidgets.QLabel(JX_FW)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.HLayout_sixth.addWidget(self.label_9)
        self.Layout_global.addLayout(self.HLayout_sixth)
        self.HLayout_seventh = QtWidgets.QVBoxLayout()
        self.HLayout_seventh.setObjectName("HLayout_seventh")
        self.label = QtWidgets.QLabel(JX_FW)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.HLayout_seventh.addWidget(self.label)
        self.textbox_progress = QtWidgets.QTextBrowser(JX_FW)
        self.textbox_progress.setObjectName("textbox_progress")
        self.HLayout_seventh.addWidget(self.textbox_progress)
        self.Layout_global.addLayout(self.HLayout_seventh)
        self.actionCheckall = QtWidgets.QAction(JX_FW)
        self.actionCheckall.setObjectName("actionCheckall")
        self.font=QtGui.QFont()
        self.font.setPointSize(12)
        self.font.setFamily("SimHei")
        self.textbox_progress.setFont(self.font)
        # self.combox_chooseDevice.setCurrentText("Choose test device")
        from Common.function_GetInfo import xpress_version
        self.label_theCurrentVersionSet.setText(xpress_version)
        self.retranslateUi(JX_FW)
        QtCore.QMetaObject.connectSlotsByName(JX_FW)

        # Define widget function
        i = 0
        while i < len(items_list):
            self.combox_chooseDevice.addItem(items_list[i])
            i=i+1
        # Define check all button - windows
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case3961.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case3965.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case3966.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case3969.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case4090.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case4128.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case3968.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case4153.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case5509.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case7196.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case5665.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case7195.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case10449.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case10312.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case3965_32b.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case3966_32b.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case4090_32b.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case5664_32b.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case5509_32b.click)
        self.checkBox_checkAll_win.clicked.connect(self.checkBox_case5665_32b.click)
        # # Define check all button - Linux
        self.checkbox_selectAll_linux.clicked.connect(self.checkBox_case6098.click)
        self.checkbox_selectAll_linux.clicked.connect(self.checkBox_case6134.click)
        self.checkbox_selectAll_linux.clicked.connect(self.checkBox_case7555.click)
        self.checkbox_selectAll_linux.clicked.connect(self.checkBox_case7695.click)
        self.checkbox_selectAll_linux.clicked.connect(self.checkBox_case7692.click)
        self.checkbox_selectAll_linux.clicked.connect(self.checkBox_case7551.click)
        self.checkbox_selectAll_linux.clicked.connect(self.checkBox_case7556.click)
        self.checkbox_selectAll_linux.clicked.connect(self.checkBox_case10312_2.click)
        self.checkbox_selectAll_linux.clicked.connect(self.checkBox_case16990.click)
        self.checkbox_selectAll_linux.clicked.connect(self.checkBox_case16991.click)
        # Define function for Windows case checkbox
        self.checkBox_case3961.clicked.connect(lambda:self.addCase(self.checkBox_case3961.text()))
        self.checkBox_case3965.clicked.connect(lambda:self.addCase(self.checkBox_case3965.text()))
        self.checkBox_case3966.clicked.connect(lambda:self.addCase(self.checkBox_case3966.text()))
        self.checkBox_case3969.clicked.connect(lambda:self.addCase(self.checkBox_case3969.text()))
        self.checkBox_case3968.clicked.connect(lambda:self.addCase(self.checkBox_case3968.text()))
        self.checkBox_case4153.clicked.connect(lambda:self.addCase(self.checkBox_case4153.text()))
        self.checkBox_case4090.clicked.connect(lambda:self.addCase(self.checkBox_case4090.text()))
        self.checkBox_case4128.clicked.connect(lambda:self.addCase(self.checkBox_case4128.text()))
        self.checkBox_case5509.clicked.connect(lambda:self.addCase(self.checkBox_case5509.text()))
        self.checkBox_case7195.clicked.connect(lambda:self.addCase(self.checkBox_case7195.text()))
        self.checkBox_case10449.clicked.connect(lambda:self.addCase(self.checkBox_case10449.text()))
        self.checkBox_case10312.clicked.connect(lambda:self.addCase(self.checkBox_case10312.text()))
        self.checkBox_case3965_32b.clicked.connect(lambda:self.addCase(self.checkBox_case3965_32b.text()))
        self.checkBox_case3966_32b.clicked.connect(lambda:self.addCase(self.checkBox_case3966_32b.text()))
        self.checkBox_case4090_32b.clicked.connect(lambda:self.addCase(self.checkBox_case4090_32b.text()))
        self.checkBox_case5664_32b.clicked.connect(lambda:self.addCase(self.checkBox_case5664_32b.text()))
        self.checkBox_case5509_32b.clicked.connect(lambda:self.addCase(self.checkBox_case5509_32b.text()))
        self.checkBox_case5665_32b.clicked.connect(lambda:self.addCase(self.checkBox_case5664_32b.text()))
        # Define function for Linux case checkbox
        self.checkBox_case6098.clicked.connect(lambda:self.addCase(self.checkBox_case6098.text()))
        self.checkBox_case6134.clicked.connect(lambda:self.addCase(self.checkBox_case6134.text()))
        self.checkBox_case7555.clicked.connect(lambda:self.addCase(self.checkBox_case7555.text()))
        self.checkBox_case7695.clicked.connect(lambda:self.addCase(self.checkBox_case7695.text()))
        self.checkBox_case7692.clicked.connect(lambda:self.addCase(self.checkBox_case7692.text()))
        self.checkBox_case7551.clicked.connect(lambda:self.addCase(self.checkBox_case7551.text()))
        self.checkBox_case7556.clicked.connect(lambda:self.addCase(self.checkBox_case7556.text()))
        self.checkBox_case10312_2.clicked.connect(lambda:self.addCase(self.checkBox_case10312_2.text()))
        self.checkBox_case16990.clicked.connect(lambda:self.addCase(self.checkBox_case16990.text()))
        self.checkBox_case16991.clicked.connect(lambda:self.addCase(self.checkBox_case16991.text()))

        self.button_start.clicked.connect(lambda:self.startbuttonevent())


    def retranslateUi(self, JX_FW):
        _translate = QtCore.QCoreApplication.translate
        JX_FW.setWindowTitle(_translate("JX_FW", "Jabra Xpress Downlod tool"))
        self.label_theCurrentVersion.setText(_translate("JX_FW", "            The current version of Jabra Xpress    :"))
        # self.label_theCurrentVersionSet.setText(_translate("JX_FW", "TextLabel"))
        self.label_chooseDevice.setText(_translate("JX_FW", "Choose Device   :"))
        self.combox_chooseDevice.setCurrentText(_translate("JX_FW", "Choose test device"))
        self.label_Windows.setText(_translate("JX_FW", "Windows Cases"))
        self.label_Linux.setText(_translate("JX_FW", "                                          Linux Cases "))
        self.checkBox_checkAll_win.setText(_translate("JX_FW", "Select All"))
        self.checkBox_case3961.setText(_translate("JX_FW", "case3961"))
        self.checkBox_case3961.setToolTip(_translate("JX_FW", "FW:leaveunchage;Setings:All defualt value;JD install:Yes;Protect:Yes"))
        self.checkBox_case3965.setText(_translate("JX_FW", "case3965"))
        self.checkBox_case3965.setToolTip(_translate("JX_FW", "FW:leaveunchage;Setings:leaveunchage;JD install:Yes;Protect:Yes"))
        self.checkBox_case3966.setText(_translate("JX_FW", "case3966"))
        self.checkBox_case3966.setToolTip(_translate("JX_FW", "FW:higer version;Setings:leaveunchage;JD install:Yes;Protect:leaveunchage"))
        self.checkBox_case3968.setText(_translate("JX_FW", "case3968"))
        self.checkBox_case3968.setToolTip(_translate("JX_FW", "Manage by Jabra"))
        self.checkBox_case3969.setText(_translate("JX_FW", "case3969"))
        self.checkBox_case3969.setToolTip(_translate("JX_FW", "FW:leaveunchage;Setings:Random;JD install:Yes;Protect:leaveunchage"))
        self.checkBox_case4090.setText(_translate("JX_FW", "case4090"))
        self.checkBox_case4090.setToolTip(_translate("JX_FW", "FW:higer version;Setings:diff from default;JD install:not;Protect:not"))
        self.checkBox_case4128.setText(_translate("JX_FW", "case4128"))
        self.checkBox_case4128.setToolTip(_translate("JX_FW", "FW:leaveunchage;Setings:default/leaveunchage/diff from default;JD install:not."))
        self.checkBox_case4153.setText(_translate("JX_FW", "case4153"))
        self.checkBox_case4153.setToolTip(_translate("JX_FW", "2/3 packages FW:all avaliable;Setings:leaveunchage;JD install:not;Protect:not"))
        self.checkBox_case5509.setText(_translate("JX_FW", "case5509"))
        self.checkBox_case5509.setToolTip(_translate("JX_FW", "FW:higer version;Setings:leaveunchage;JD install:Yes;Protect:not"))
        self.checkBox_case7196.setText(_translate("JX_FW", "case7196"))
        self.checkBox_case7196.setToolTip(_translate("JX_FW", "FW:leaveunchage;Setings:random;JD install:Yes;Protect:not"))
        self.checkBox_case5665.setText(_translate("JX_FW", "case5665"))
        self.checkBox_case5665.setToolTip(_translate("JX_FW", "FW:leaveunchage;Setings:Min;JD install:Yes;Protect:Yes"))
        self.checkBox_case7195.setText(_translate("JX_FW", "case7195"))
        self.checkBox_case7195.setToolTip(_translate("JX_FW", "FW:lower version;Setings:random;JD install:Yes;Protect:random"))
        self.checkBox_case10449.setText(_translate("JX_FW", "case10449"))
        self.checkBox_case10449.setToolTip(_translate("JX_FW", "FW:leaveunchage;Setings:leaveunchage;JD install:Yes;Protect:Yes"))
        self.checkBox_case10312.setText(_translate("JX_FW", "case10312"))
        self.checkBox_case10312.setToolTip(_translate("JX_FW", "Language case,will download all language if device has languange setting"))
        self.checkBox_case3965_32b.setText(_translate("JX_FW", "case3965_32b"))
        self.checkBox_case3965_32b.setToolTip(_translate("JX_FW", "FW:leaveunchage;Setings:leaveunchage;JD install:Yes;Protect:Yes"))
        self.checkBox_case3966_32b.setText(_translate("JX_FW", "case3966_32b"))
        self.checkBox_case3966_32b.setToolTip(_translate("JX_FW", "FW:higer version;Setings:leaveunchage;JD install:Yes;Protect:leaveunchage"))
        self.checkBox_case4090_32b.setText(_translate("JX_FW", "case4090_32b"))
        self.checkBox_case4090_32b.setToolTip(_translate("JX_FW", "FW:higer version;Setings:diff from default;JD install:not;Protect:not"))
        self.checkBox_case5664_32b.setText(_translate("JX_FW", "case5664_32b"))
        self.checkBox_case5664_32b.setToolTip(_translate("JX_FW", "FW:leaveunchage;Setings:MAX;JD install:Yes;Protect:Yes"))
        self.checkBox_case5509_32b.setText(_translate("JX_FW", "case5509_32b"))
        self.checkBox_case5509_32b.setToolTip(_translate("JX_FW", "FW:higer version;Setings:leaveunchage;JD install:Yes;Protect:not"))
        self.checkBox_case5665_32b.setText(_translate("JX_FW", "case5665_32b"))
        self.checkBox_case5665_32b.setToolTip(_translate("JX_FW", "FW:leaveunchage;Setings:Min;JD install:Yes;Protect:Yes"))
        self.checkbox_selectAll_linux.setText(_translate("JX_FW", "Select All"))
        self.checkBox_case6098.setText(_translate("JX_FW", "case6098"))
        self.checkBox_case6098.setToolTip(_translate("JX_FW", "Verify zip package content and JXDU version by creating a ZIP file."))
        self.checkBox_case6134.setText(_translate("JX_FW", "case6134"))
        self.checkBox_case6134.setToolTip(_translate("JX_FW", "FW:leaveunchage;Setings:leaveunchage;Protect:Yes"))
        self.checkBox_case7555.setText(_translate("JX_FW", "case7555"))
        self.checkBox_case7555.setToolTip(_translate("JX_FW", "FW:higer version;Setings:leaveunchage;Protect:Yes"))
        self.checkBox_case7695.setText(_translate("JX_FW", "case7695"))
        self.checkBox_case7695.setToolTip(_translate("JX_FW", "FW:leaveunchage;Setings:MAX;Protect:not"))
        self.checkBox_case7692.setText(_translate("JX_FW", "case7692"))
        self.checkBox_case7692.setToolTip(_translate("JX_FW", "FW:leaveunchage;Setings:Min;Protect:Yes"))
        self.checkBox_case7551.setText(_translate("JX_FW", "case7551"))
        self.checkBox_case7551.setToolTip(_translate("JX_FW", "FW:higer version;Setings:differ from default;Protect:Yes"))
        self.checkBox_case7556.setText(_translate("JX_FW", "case7556"))
        self.checkBox_case7556.setToolTip(_translate("JX_FW", "FW:higer version;Setings:default value;Protect:not"))
        self.checkBox_case10312_2.setText(_translate("JX_FW", "case10312l"))
        self.checkBox_case10312_2.setToolTip(_translate("JX_FW", "Language case,will download all language if device has languange setting"))
        self.checkBox_case16990.setText(_translate("JX_FW", "case16990"))
        self.checkBox_case16990.setToolTip(_translate("JX_FW", "FW:higer version;Setings:leaveunchage;Protect:not;Allow downgrade"))
        self.checkBox_case16991.setText(_translate("JX_FW", "case16991"))
        self.checkBox_case16991.setToolTip(_translate("JX_FW", "FW:higer version;Setings:leaveunchage;Protect:not;not Allow downgrade"))
        self.button_start.setText(_translate("JX_FW", "Start"))
        self.label.setText(_translate("JX_FW", "Download Progress"))
        self.actionCheckall.setText(_translate("JX_FW", "Checkall"))
        JX_FW.setWindowIcon(QIcon('jabra.ico'))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TesteEnviromentCheck = QtWidgets.QWidget()
    ui = Ui_TesteEnviromentCheck()
    ui.setupUi(TesteEnviromentCheck)
    TesteEnviromentCheck.show()

    # Get the xpress version nned.


    #Define the Main Window
    app2 = QtWidgets.QApplication(sys.argv)
    JX_FW = QtWidgets.QWidget()

    #Check network
    ipaddress=get_Windows_ip()
    print("This Software is a test tool to help tester download the package that testcase required.")
    print("This windows will check whether the current network environment meets the requirements of software operation.")
    print("\n")
    # time.sleep(1)
    print("Check Network : ")

    if ipaddress==True:
        print("Supported network")
        print("\n")
        print("Start check Google Chrome driver....")
        # currentversion = getXpressVersionThread()
        # currentversion.run()
        checkDriver=checkGoogleDriver()
        checkDriver.start()
        # currentversion = getXpressVersionThread()
        # currentversion.run()

    else:
        print("Unsupported netwrok")
        print("Supported network list:")
        print("   -Intra-gnn.com")
        print("   -Rand-gnn.com")
        print("   -GN-Wifi")
        print("Please Switch to the Supported network and restart the APP")
        print("\n")
        # checkDriver=checkGoogleDriver()
        # checkDriver.start()




    sys.exit(app.exec_())
    sys.exit(app2.exec_())


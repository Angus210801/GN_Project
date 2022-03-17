
#Import PyQt5
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QWidget,QCompleter
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow
#Import Testcase
from  TestCase_Windows import case3965
from  TestCase_Windows import case3961
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


from Common.CheckIP import get_Windows_ip
from Common.checkChromeDriverwithoutLoging import checkChromeDriverUpdate

items_list=['Jabra BIZ 1500 MS USB Duo',
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

# 定义一个发送信号的类，发送log函数1
class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str) #定义一个发送str的信号
    def write(self, text):
      self.textWritten.emit(str(text))

class Ui_JX_FW(object):

    excuteTestCase = []

#捕捉信号，发送log函数2
    def __init__(self):
        sys.stdout = EmittingStr(textWritten=self.onUpdateText)
        sys.stderr = EmittingStr(textWritten=self.onUpdateText)

#输入到文本框，发送log函数3
    def onUpdateText(self, text):
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()

    def pushbuttonEvent(self):
        self.saveDeviceName()
        self.startDownload()

    def saveDeviceName(self):
        DeviceName = self.input_choosedevice.text()
        print("Test device is " + DeviceName)
        fo = open("device.txt", "wt")
        fo.write(DeviceName)
        fo.close()

    def addCase(self,testcase):
        testcase = testcase
        print(testcase)
        if (testcase in Ui_JX_FW.excuteTestCase):
            Ui_JX_FW.excuteTestCase.remove(testcase)
            print(Ui_JX_FW.excuteTestCase)
        else:
            Ui_JX_FW.excuteTestCase.append(testcase)
            print(Ui_JX_FW.excuteTestCase)

    def checkIP(self):
        get_Windows_ip()

    def checkChromeDriver(self):
        checkChromeDriverUpdate()


    def startDownload(self):
        testcaselist=Ui_JX_FW.excuteTestCase
        for testcase in testcaselist:
            testcase = "test"+testcase
            print(testcase)
            eval(testcase)()

    def init_input_choosedevice(self):
        # 增加自动补全
        self.completer = QCompleter(items_list)
        # 设置匹配模式 有三种： Qt.MatchStartsWith 开头匹配（默认） Qt.MatchContains 内容匹配 Qt.MatchEndsWith 结尾匹配
        self.completer.setFilterMode(Qt.MatchContains)
        # 设置补全模式 有三种： QCompleter.PopupCompletion（默认） QCompleter.InlineCompletion  QCompleter.UnfilteredPopupCompletion
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        # 给lineedit设置补全器
        self.input_choosedevice.setCompleter(self.completer)


    def setupUi(self, JX_FW):
        JX_FW.setObjectName("JX_FW")
        JX_FW.resize(600, 830)
        self.label_chooseDevice = QtWidgets.QLabel(JX_FW)
        self.label_chooseDevice.setGeometry(QtCore.QRect(60, 60, 200, 60))

        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_chooseDevice.setFont(font)
        self.label_chooseDevice.setWordWrap(True)
        self.label_chooseDevice.setObjectName("label_chooseDevice")
        self.input_choosedevice = QtWidgets.QLineEdit(JX_FW)
        self.input_choosedevice.setGeometry(QtCore.QRect(290, 70, 300, 50))
        self.input_choosedevice.setObjectName("input_choosedevice")
        self.label_Windows = QtWidgets.QLabel(JX_FW)
        self.label_Windows.setGeometry(QtCore.QRect(0, 140, 300, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Windows.setFont(font)
        self.label_Windows.setToolTipDuration(0)
        self.label_Windows.setObjectName("label_Windows")
        self.label_Linux = QtWidgets.QLabel(JX_FW)
        self.label_Linux.setGeometry(QtCore.QRect(300, 140, 300, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Linux.setFont(font)
        self.label_Linux.setToolTipDuration(0)
        self.label_Linux.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_Linux.setTextFormat(QtCore.Qt.PlainText)
        self.label_Linux.setObjectName("label_Linux")
        self.checkBox = QtWidgets.QCheckBox(JX_FW)
        self.checkBox.setGeometry(QtCore.QRect(20, 180, 271, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 200, 271, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 220, 271, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 240, 271, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 260, 271, 20))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_6.setGeometry(QtCore.QRect(20, 300, 271, 20))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_7.setGeometry(QtCore.QRect(20, 320, 271, 20))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_8.setGeometry(QtCore.QRect(20, 340, 271, 20))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_9.setGeometry(QtCore.QRect(20, 280, 271, 20))
        self.checkBox_9.setObjectName("checkBox_9")
        self.CheckNetwork = QtWidgets.QPushButton(JX_FW)
        self.CheckNetwork.setGeometry(QtCore.QRect(20, 10, 250, 40))
        self.CheckNetwork.setIconSize(QtCore.QSize(130, 30))
        self.CheckNetwork.setObjectName("CheckNetwork")
        self.checkChromeDriverBtn = QtWidgets.QPushButton(JX_FW)
        self.checkChromeDriverBtn.setGeometry(QtCore.QRect(310, 10, 250, 40))
        self.checkChromeDriverBtn.setIconSize(QtCore.QSize(130, 30))
        self.checkChromeDriverBtn.setObjectName("checkChromeDriverBtn")
        self.checkBox_10 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_10.setGeometry(QtCore.QRect(20, 360, 271, 20))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_11.setGeometry(QtCore.QRect(20, 380, 271, 20))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_12.setGeometry(QtCore.QRect(20, 400, 271, 20))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_13.setGeometry(QtCore.QRect(20, 420, 271, 20))
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_14.setGeometry(QtCore.QRect(20, 440, 271, 20))
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_15.setGeometry(QtCore.QRect(20, 460, 271, 20))
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_16 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_16.setGeometry(QtCore.QRect(20, 480, 271, 20))
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_17 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_17.setGeometry(QtCore.QRect(20, 500, 271, 20))
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_18 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_18.setGeometry(QtCore.QRect(20, 520, 271, 20))
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_19 = QtWidgets.QCheckBox(JX_FW)
        self.checkBox_19.setGeometry(QtCore.QRect(20, 540, 271, 20))
        self.checkBox_19.setObjectName("checkBox_19")
        self.pushButton = QtWidgets.QPushButton(JX_FW)
        self.pushButton.setGeometry(QtCore.QRect(250, 560, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(JX_FW)
        self.textBrowser.setGeometry(QtCore.QRect(10, 650, 581, 161))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.ensureCursorVisible()
        self.lineEdit = QtWidgets.QLabel(JX_FW)
        self.lineEdit.setGeometry(QtCore.QRect(10, 610, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.case6134 = QtWidgets.QCheckBox(JX_FW)
        self.case6134.setGeometry(QtCore.QRect(350, 220, 271, 20))
        self.case6134.setObjectName("case6134")
        self.case7555 = QtWidgets.QCheckBox(JX_FW)
        self.case7555.setGeometry(QtCore.QRect(350, 240, 271, 20))
        self.case7555.setObjectName("case7555")
        self.Linux_selectAll_chkbox = QtWidgets.QCheckBox(JX_FW)
        self.Linux_selectAll_chkbox.setGeometry(QtCore.QRect(350, 180, 271, 20))
        self.Linux_selectAll_chkbox.setObjectName("Linux_selectAll_chkbox")
        self.case7692 = QtWidgets.QCheckBox(JX_FW)
        self.case7692.setGeometry(QtCore.QRect(350, 260, 271, 20))
        self.case7692.setObjectName("case7692")
        self.case7695 = QtWidgets.QCheckBox(JX_FW)
        self.case7695.setGeometry(QtCore.QRect(350, 280, 271, 20))
        self.case7695.setObjectName("case7695")
        self.case7551 = QtWidgets.QCheckBox(JX_FW)
        self.case7551.setGeometry(QtCore.QRect(350, 300, 271, 20))
        self.case7551.setObjectName("case7551")
        self.case7556 = QtWidgets.QCheckBox(JX_FW)
        self.case7556.setGeometry(QtCore.QRect(350, 320, 271, 20))
        self.case7556.setObjectName("case7556")
        self.case10312 = QtWidgets.QCheckBox(JX_FW)
        self.case10312.setGeometry(QtCore.QRect(350, 340, 271, 20))
        self.case10312.setObjectName("case10312")
        self.case16990 = QtWidgets.QCheckBox(JX_FW)
        self.case16990.setGeometry(QtCore.QRect(350, 360, 271, 20))
        self.case16990.setObjectName("case16990")
        self.case16991 = QtWidgets.QCheckBox(JX_FW)
        self.case16991.setGeometry(QtCore.QRect(350, 380, 271, 20))
        self.case16991.setObjectName("case16991")
        self.case6098 = QtWidgets.QCheckBox(JX_FW)
        self.case6098.setGeometry(QtCore.QRect(350, 200, 271, 20))
        self.case6098.setObjectName("case6098")

        self.actionCheckall = QtWidgets.QAction(JX_FW)
        self.actionCheckall.setObjectName("actionCheckall")


        self.retranslateUi(JX_FW)
        self.init_input_choosedevice()
        self.CheckNetwork.clicked.connect(lambda:self.checkIP())
        self.checkChromeDriverBtn.clicked.connect(lambda:self.checkChromeDriver())
        #处理Windwows case全选
        self.checkBox.clicked.connect(self.checkBox_2.click)
        self.checkBox.clicked.connect(self.checkBox_3.click)
        self.checkBox.clicked.connect(self.checkBox_4.click)
        self.checkBox.clicked.connect(self.checkBox_5.click)
        self.checkBox.clicked.connect(self.checkBox_6.click)
        self.checkBox.clicked.connect(self.checkBox_7.click)
        self.checkBox.clicked.connect(self.checkBox_8.click)
        self.checkBox.clicked.connect(self.checkBox_9.click)
        self.checkBox.clicked.connect(self.checkBox_10.click)
        self.checkBox.clicked.connect(self.checkBox_11.click)
        self.checkBox.clicked.connect(self.checkBox_12.click)
        self.checkBox.clicked.connect(self.checkBox_13.click)
        self.checkBox.clicked.connect(self.checkBox_14.click)
        self.checkBox.clicked.connect(self.checkBox_15.click)
        self.checkBox.clicked.connect(self.checkBox_16.click)
        self.checkBox.clicked.connect(self.checkBox_17.click)
        self.checkBox.clicked.connect(self.checkBox_18.click)
        self.checkBox.clicked.connect(self.checkBox_19.click)
        #处理Linux case全选
        self.Linux_selectAll_chkbox.clicked.connect(self.case6098.click)
        self.Linux_selectAll_chkbox.clicked.connect(self.case7556.click)
        self.Linux_selectAll_chkbox.clicked.connect(self.case7551.click)
        self.Linux_selectAll_chkbox.clicked.connect(self.case6134.click)
        self.Linux_selectAll_chkbox.clicked.connect(self.case7692.click)
        self.Linux_selectAll_chkbox.clicked.connect(self.case7695.click)
        self.Linux_selectAll_chkbox.clicked.connect(self.case7555.click)
        self.Linux_selectAll_chkbox.clicked.connect(self.case10312.click)
        self.Linux_selectAll_chkbox.clicked.connect(self.case16991.click)
        self.Linux_selectAll_chkbox.clicked.connect(self.case16990.click)

        #发送选中Windows Case到列表中
        self.checkBox_2.clicked.connect(lambda:self.addCase(self.checkBox_2.text()))
        self.checkBox_3.clicked.connect(lambda:self.addCase(self.checkBox_3.text()))
        self.checkBox_4.clicked.connect(lambda:self.addCase(self.checkBox_4.text()))
        self.checkBox_5.clicked.connect(lambda:self.addCase(self.checkBox_5.text()))
        self.checkBox_6.clicked.connect(lambda:self.addCase(self.checkBox_6.text()))
        self.checkBox_7.clicked.connect(lambda:self.addCase(self.checkBox_7.text()))
        self.checkBox_8.clicked.connect(lambda:self.addCase(self.checkBox_8.text()))
        self.checkBox_9.clicked.connect(lambda:self.addCase(self.checkBox_9.text()))
        self.checkBox_10.clicked.connect(lambda:self.addCase(self.checkBox_10.text()))
        self.checkBox_11.clicked.connect(lambda:self.addCase(self.checkBox_11.text()))
        self.checkBox_12.clicked.connect(lambda:self.addCase(self.checkBox_12.text()))
        self.checkBox_13.clicked.connect(lambda:self.addCase(self.checkBox_13.text()))
        self.checkBox_14.clicked.connect(lambda:self.addCase(self.checkBox_14.text()))
        self.checkBox_15.clicked.connect(lambda:self.addCase(self.checkBox_15.text()))
        self.checkBox_16.clicked.connect(lambda:self.addCase(self.checkBox_16.text()))
        self.checkBox_17.clicked.connect(lambda:self.addCase(self.checkBox_17.text()))
        self.checkBox_18.clicked.connect(lambda:self.addCase(self.checkBox_18.text()))
        self.checkBox_19.clicked.connect(lambda:self.addCase(self.checkBox_19.text()))
        #发送选中Linux Case到列表中
        self.case6098.clicked.connect(lambda:self.addCase(self.case6098.text()))
        self.case7556.clicked.connect(lambda:self.addCase(self.case7556.text()))
        self.case7551.clicked.connect(lambda:self.addCase(self.case7551.text()))
        self.case6134.clicked.connect(lambda:self.addCase(self.case6134.text()))
        self.case7692.clicked.connect(lambda:self.addCase(self.case7692.text()))
        self.case7695.clicked.connect(lambda:self.addCase(self.case7695.text()))
        self.case7555.clicked.connect(lambda:self.addCase(self.case7555.text()))
        self.case10312.clicked.connect(lambda:self.addCase(self.case10312.text()))
        self.case16991.clicked.connect(lambda:self.addCase(self.case16991.text()))
        self.case16990.clicked.connect(lambda:self.addCase(self.case16990.text()))

        self.pushButton.clicked.connect(lambda:self.pushbuttonEvent())


        QtCore.QMetaObject.connectSlotsByName(JX_FW)

    def retranslateUi(self, JX_FW):
        _translate = QtCore.QCoreApplication.translate
        JX_FW.setWindowTitle(_translate("JX_FW", "Jabra Xpress Downlod tool"))
        JX_FW.setWindowIcon(QIcon('jabra.ico'))
        self.label_chooseDevice.setText(_translate("JX_FW", "Choose Device :"))
        self.label_Windows.setText(_translate("JX_FW", "                     Windows Cases"))
        self.label_Linux.setText(_translate("JX_FW", "                            Linux Cases"))
        self.checkBox.setText(_translate("JX_FW", "Select All"))
        self.checkBox_2.setText(_translate("JX_FW", "case3961"))
        self.checkBox_3.setText(_translate("JX_FW", "case3965"))
        self.checkBox_4.setText(_translate("JX_FW", "case3966"))
        self.checkBox_5.setText(_translate("JX_FW", "case3969"))
        self.checkBox_6.setText(_translate("JX_FW", "case4128"))
        self.checkBox_7.setText(_translate("JX_FW", "case5509"))
        self.checkBox_8.setText(_translate("JX_FW", "case5665"))
        self.checkBox_9.setText(_translate("JX_FW", "case4090"))
        self.CheckNetwork.setText(_translate("JX_FW", "CheckNetwork"))
        self.checkChromeDriverBtn.setText(_translate("JX_FW", "Check Chrome Driver"))
        self.checkBox_10.setText(_translate("JX_FW", "case7195"))
        self.checkBox_11.setText(_translate("JX_FW", "case7196"))
        self.checkBox_12.setText(_translate("JX_FW", "case10449"))
        self.checkBox_13.setText(_translate("JX_FW", "case10312"))
        self.checkBox_14.setText(_translate("JX_FW", "case3965_32b"))
        self.checkBox_15.setText(_translate("JX_FW", "case3966_32b"))
        self.checkBox_16.setText(_translate("JX_FW", "case4090_32b"))
        self.checkBox_17.setText(_translate("JX_FW", "case3965_32b"))
        self.checkBox_18.setText(_translate("JX_FW", "case3965_32b"))
        self.checkBox_19.setText(_translate("JX_FW", "case3965_32b"))
        self.pushButton.setText(_translate("JX_FW", "Start"))
        self.lineEdit.setText(_translate("JX_FW", "Download progress"))
        self.case6134.setText(_translate("JX_FW", "Case6134"))
        self.case7555.setText(_translate("JX_FW", "Case7555"))
        self.Linux_selectAll_chkbox.setText(_translate("JX_FW", "Select All"))
        self.case7692.setText(_translate("JX_FW", "Case7692"))
        self.case7695.setText(_translate("JX_FW", "Case7695"))
        self.case7551.setText(_translate("JX_FW", "Case7551"))
        self.case7556.setText(_translate("JX_FW", "Case7556"))
        self.case10312.setText(_translate("JX_FW", "Case10312"))
        self.case16990.setText(_translate("JX_FW", "Case16990"))
        self.case16991.setText(_translate("JX_FW", "Case16991"))
        self.case6098.setText(_translate("JX_FW", "Case6098"))
        self.actionCheckall.setText(_translate("JX_FW", "Checkall"))



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    QApplication.processEvents()
    Form = QtWidgets.QWidget()
    ui = Ui_JX_FW()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


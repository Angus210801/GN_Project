import sys

from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QWidget,QCompleter
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow

from main import Ui_JX_FW


class EmittingStr(QtCore.QObject):
    textWritten=QtCore.pyqtSignal(str)
    def write(self,text):
        self.textWritten.emit(str(text))


class ControlBoard(QMainWindow,Ui_JX_FW):
    def __init__(self):
        super(ControlBoard, self).__init__()
        self.setupUi(self)
        # 下面将输出重定向到textBrowser中
        sys.stdout = EmittingStr(textWritten=self.outputWritten)
        sys.stderr = EmittingStr(textWritten=self.outputWritten)
        self.th=MyThread()
        self.th.signalForText.connect(self.outputWritten)
        self.pushButton.clicked.connect(self.bClicked)


    def outputWritten(self, text):
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.append(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()

    def bClicked(self):
        """Runs the main function."""
        print('Begin')

        self.printABCD()

        print("End")



class MyThread(QThread):
    signalForText = pyqtSignal(str)

    def __init__(self,data=None, parent=None):
        super(MyThread, self).__init__(parent)
        self.data = data

    def write(self, text):
        self.signalForText.emit(str(text))  # 发射信号


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_JX_FW()
    ui.setupUi(Form)
    # win = ControlBoard()
    # win.show()
    Form.show()
    sys.exit(app.exec_())

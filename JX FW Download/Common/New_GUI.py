import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication, QHBoxLayout, QVBoxLayout, QPlainTextEdit)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # hbox = QHBoxLayout()
        # hbox.addStretch(1)


        vbox = QVBoxLayout()
        vbox.addStretch(4)
        iPbox = QPlainTextEdit('Network')
        vbox.addWidget(iPbox)


        self.setLayout(vbox)
        #setGeometry(A,B,C,D)
        #从屏幕上（A，B）位置开始（即为最左上角的点），显示一C*D的界面（宽C，高D）
        self.setGeometry(626, 126, 800, 800)
        self.setWindowTitle('Jabra Xpress Test tool - Download the package that test need')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
import sys
import sys
import os
from time import time, sleep
import shutil

from PyQt5.QtWidgets import QApplication
from Common.Cases import Windows_cases,Linux_cases
from Common.getDevice import Widget

if __name__ == '__main__':

     #Begin time
     time_begin=time()
     #author
     print('*Target:Download the FW package what Jabra Xpress 1.0 test case need')
     print('*Author:Angus Lin')
     print('*Email:extalin@jabra.com')
     print('*Data:12/30/2020')

     dFile="device.txt"
     pFile="platform.txt"
     if os.path.exists(dFile):
          os.remove(dFile)
     if os.path.exists(pFile):
          os.remove(pFile)

     #GUI
     app = QApplication(sys.argv)
     JX_FW_download = Widget()
     JX_FW_download.show()
     app.exec_()

     try:
          platformfile=open("platform.txt", "rt")
          fo = open("device.txt", "rt")
          lastingDevicename = fo.read()
          file = "C:\\download\\" + lastingDevicename
          if os.path.exists(file):
               shutil.rmtree(file)
          platform=platformfile.read()

          if platform=='Windows':
               windowsCases = Windows_cases()
          elif platform=="Linux":
               linuxCases = Linux_cases()
          else:
               linuxCases = Linux_cases()
               windowsCases = Windows_cases()

          #End time
          time_end=time()

          cost=time_end-time_begin
          print('Cost time: %.1f'%cost+'s')
     except Exception as e:
          print(e)
          print('Not choose device,application will exit.')
          sleep(15)
          sys.exit()


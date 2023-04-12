import os
import sys 
from Common.function_basic import GoToPCSoftwarePage 
from Common.function_basic import GoToPCSoftwarePage
from time import sleep
from selenium import webdriver
import Common.function_basic
from Common.function_basic import borwserConfigure, getLocation

def configureFinish():
    print(os.path.basename(sys.argv[0]).split('.')[0])

def renameSummary(testcase,file,testDeviceName):
    summary = file + '\\summary.html'
    summary_rename = file + '\\'+testcase+'.html'
    try:
        while os.path.exists(summary) == False:
            sleep(8)
        os.rename(summary, summary_rename)
        print(testDeviceName + testcase+' summary download successful')
    except:
        os.remove(summary_rename)
        os.rename(summary, summary_rename)

def renameMsiFile(self,file,testcaseName,testDeviceName):
    msiFile = file + '\\JabraXPRESSx64.msi'
    msiFile_rename = file + '\\'+testcaseName+'.msi'

    try:
        while os.path.exists(msiFile) == False:
            sleep(8)
        os.rename(msiFile, msiFile_rename)
        self.close()

    except Exception as e:
        print(e)
        self.close()
    print(testDeviceName+ ' '+testcaseName+' download successful.')
    print('\n')


def setup_driver():
    # 读取设备名称
    with open("device.txt", "rt") as f:
        testDeviceName = f.read()

    # 获取文件位置并构建选项
    file = getLocation() + testDeviceName
    options = borwserConfigure()

    with open("saveDir.txt", "rt") as f:
        file = f.read()
        file = file.replace('/', '\\')+'\\'+ testDeviceName

    # 创建并返回WebDriver对象和windowsPage对象
    driver = webdriver.Chrome(chrome_options=options)
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior',
              'params': {'behavior': 'allow', 'downloadPath': file}}
    driver.execute("send_command", params=params)

    windowsTrack = Common.function_basic.windowsPage(driver)
    return driver, windowsTrack,testDeviceName,file

import sys
import os
import sys
from time import sleep

from selenium import webdriver


class baseConfigure(object):
    def __init__(self, driver):
        self.driver = driver

    def click(self, *button):
        self.driver.find_element(*button).click()

    def click(self, *device):
        self.driver.find_element(*device).click()

    def windowPosition(self) -> object:
        self.update_idletasks()
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.geometry("+%d+%d" % (x, y))
        self.mainloop()

# def getDeivceName():
#     fo = open("device.txt", "rt")
#     lastingDevicename = fo.read()
#     file = getLocation() +lastingDevicename
#     options = borwserConfigure()

def getLocation():
    fo=open("saveDir.txt","rt")
    saveDir=fo.read()+"/"
    saveDir=saveDir.replace('/','\\\\')
    return saveDir

def borwserConfigure():
    fo = open("device.txt", "rt")
    lastingDevicename = fo.read()
    file = getLocation()
    file=file.replace('\\\\','\\')
    file= file+lastingDevicename
    # file2="C:\\download\\" +lastingDevicename
    options = webdriver.ChromeOptions()
    # print(file2)
    # print(file)
    prefs = {"download.default_directory": file, "download.prompt_for_download": False}
    options.add_experimental_option('prefs', prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--headless')
    return options




def renameAndclose(self, summary, renamesummary):
    try:
        while os.path.exists(summary) == False:
            sleep(10)
        os.rename(summary, renamesummary)
        self.close()
    except Exception as e:
        print(e)
        self.close()


def configureFinish():
    print(os.path.basename(sys.argv[0]).split('.')[0])

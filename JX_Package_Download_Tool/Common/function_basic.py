import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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


class linuxindexPage(baseConfigure):
    def __init__(self,driver):
        baseConfigure.__init__(self,driver)
        driver.get('http://dkcphweb15/')
        testadress=driver.find_element(By.LINK_TEXT,'Start Page').get_attribute("href")
        driver.get(testadress+'/thin-client')

    def clickNextButton(self):
        button = (By.CLASS_NAME, 'button-container')
        self.click(*button)

    def chooseDevice(self):
        fo = open("device.txt", "rt")
        lastingDevicename = fo.read()
        device=(By.XPATH,"//label[contains(text(),'" + lastingDevicename+ "')]")
        self.click(*device)
        self.driver.find_element(By.ID,'btnAdd').send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH,"//input[@value='NEXT >']").click()

class windowsPage(baseConfigure):

    def __init__(self,driver):
        baseConfigure.__init__(self,driver)
        driver.get('http://dkcphweb15/')
        testadress=driver.find_element(By.LINK_TEXT,'Start Page').get_attribute("href")
        # testadress="http://dkcphweb15/Xpress/36.X.Development/MDCT"
        driver.get(testadress+'/windows-desktop')

    def clickNextButton(self):
        ''' Click the next button'''
        button = (By.CLASS_NAME, 'button-container')
        self.click(*button)

    def chooseDevice(self):
        fo = open("device.txt", "rt")
        lastingDevicename = fo.read()
        device=(By.XPATH,"//label[contains(text(),'" + lastingDevicename+ "')]")
        self.click(*device)
        self.driver.find_element(By.ID,'btnAdd').send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH,"//input[@value='NEXT >']").click()


def borwserConfigure():
    fo = open("device.txt", "rt")
    lastingDevicename = fo.read()
    file = getLocation()
    file = file.replace('\\\\', '\\')
    file = file + lastingDevicename
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": file, "download.prompt_for_download": False, 'safebrowsing.enabled': True}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return options


def get_Windows_ip():
    try:
        http = urllib3.PoolManager()
        http.request('GET', 'http://dkcphweb15.corp.intra-gnn.com/')
        return True
    except:
        return False


def getLocation():
    fo = open("saveDir.txt", "rt")
    saveDir = fo.read() + "/"
    saveDir = saveDir.replace('/', '\\\\')
    return saveDir

def gotosummaryPage(driver):
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    #跳转到Summary下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()

def downloadmsi(driver):
    # 返回到下载页
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # 勾选同意协议
    driver.find_element_by_id('eulaOk').click()
    # #点击下载
    driver.find_element_by_id('download64bit').click()
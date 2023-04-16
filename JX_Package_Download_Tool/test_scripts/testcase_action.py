import os
import sys
from time import sleep

import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BaseConfigure(object):
    def __init__(self, driver):
        self.driver = driver

    def click(self, *button):
        self.driver.find_element(*button).click()

    def click(self, *device):
        self.driver.find_element(*device).click()

    def window_position(self) -> object:
        self.update_idletasks()
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.geometry("+%d+%d" % (x, y))
        self.mainloop()


class InitLinuxTrack(BaseConfigure):
    def __init__(self, driver):
        BaseConfigure.__init__(self, driver)
        driver.get('http://dkcphweb15/')
        test_address = driver.find_element(By.LINK_TEXT, 'Start Page').get_attribute("href")
        driver.get(test_address + '/thin-client')

    def click_next_button(self):
        button = (By.CLASS_NAME, 'button-container')
        self.click(*button)

    def select_device(self):
        fo = open("device.txt", "rt")
        test_device_name = fo.read()
        device = (By.XPATH, "//label[contains(text(),'" + test_device_name + "')]")
        self.click(*device)
        self.driver.find_element(By.ID, 'btnAdd').send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, "//input[@value='NEXT >']").click()


class InitWindowsTrack(BaseConfigure):

    def __init__(self, driver):
        BaseConfigure.__init__(self, driver)
        driver.get('http://dkcphweb15/')
        test_address = driver.find_element(By.LINK_TEXT, 'Start Page').get_attribute("href")
        # test_address="http://dkcphweb15/Xpress/36.X.Development/MDCT"
        driver.get(test_address + '/windows-desktop')

    def goto_selectdevice_page(self):
        """ Click the New button go to select device page """
        button = (By.CLASS_NAME, 'button-container')
        self.click(*button)

    def action_selectdevice_page(self):
        """ Select device and click next button """
        fo = open("device.txt", "rt")
        test_device_name = fo.read()
        device = (By.XPATH, "//label[contains(text(),'" + test_device_name + "')]")
        self.click(*device)
        self.driver.find_element(By.ID, 'btnAdd').send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, "//input[@value='NEXT >']").click()


def browser_configure():
    """ Configure the browser"""
    fo = open("device.txt", "rt")
    test_device_name = fo.read()
    file = get_save_dir()
    file = file.replace('\\\\', '\\')
    file = file + test_device_name
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": file, "download.prompt_for_download": False, 'safebrowsing.enabled': True}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return options


def check_network_access():
    try:
        http = urllib3.PoolManager()
        http.request('GET', 'http://dkcphweb15.corp.intra-gnn.com/')
        return True
    except:
        return False


def get_save_dir():
    # 获取保存路径
    fo = open("saveDir.txt", "rt")
    saveDir = fo.read() + "/"
    saveDir = saveDir.replace('/', '\\\\')
    return saveDir


def goto_pcsoftware_page(driver):
    # 跳转到PC Software下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()


def action_download_jd(driver):
    # Choose JD
    driver.find_element_by_xpath("//input[@value='true']").click()


def goto_summary_page_and_download(driver):
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 跳转到Summary下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()


def action_download_msi(driver):
    # 返回到下载页
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # 勾选同意协议
    driver.find_element_by_id('eulaOk').click()
    # #点击下载
    driver.find_element_by_id('download64bit').click()


def configure_finish():
    print(os.path.basename(sys.argv[0]).split('.')[0])


def rename_summary(testcase, file, testDeviceName):
    summary = file + '\\summary.html'
    summary_rename = file + '\\' + testcase + '.html'
    try:
        while not os.path.exists(summary):
            sleep(8)
        os.rename(summary, summary_rename)
        print(testDeviceName + testcase + ' summary download successful')
    except:
        os.remove(summary_rename)
        os.rename(summary, summary_rename)


def rename_msi_file(self, file, testcaseName, testDeviceName):
    msiFile = file + '\\JabraXPRESSx64.msi'
    msiFile_rename = file + '\\' + testcaseName + '.msi'

    try:
        while not os.path.exists(msiFile):
            sleep(8)
        os.rename(msiFile, msiFile_rename)
        self.close()

    except Exception as e:
        print(e)
        self.close()
    print(testDeviceName + ' ' + testcaseName + ' download successful.')
    print('\n')


def setup_driver():
    with open("device.txt", "rt") as f:
        testDeviceName = f.read()

    # 获取文件位置并构建选项
    file = get_save_dir() + testDeviceName
    options = browser_configure()

    with open("saveDir.txt", "rt") as f:
        file = f.read()
        file = file.replace('/', '\\') + '\\' + testDeviceName

    # 创建并返回WebDriver对象和windowsPage对象
    driver = webdriver.Chrome(chrome_options=options)
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior',
              'params': {'behavior': 'allow', 'downloadPath': file}}
    driver.execute("send_command", params=params)

    windowsTrack = InitWindowsTrack(driver)
    return driver, windowsTrack, testDeviceName, file

import sys
import os
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from Common.function_configure import renameMsiFile, getLocation, renameSummary, setup_driver
from Common.function_basic import gotosummaryPage,downloadmsi


#Jabra Direct Diagnostic Report plug-in version and s/n verification(not FW, settings=default）
def testcase3961():
    #Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    #Configure driver
    driver, windowsTrack,testDeviceName,file = setup_driver()
    # Go to device page
    windowsTrack.clickNextButton()
    # Choose device
    windowsTrack.chooseDevice()
    # Configure the device page with all settings as default
    driver.find_element_by_xpath("//input[@value='SET ALL TO DEFAULT VALUES']").click()
    setting = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[0].SelectedValue']")
    Select(setting).select_by_index("1")

    print(testDeviceName+' '+currentTestcaseName+' Configure finish')
    #Goto SP page
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    #勾选下载JD
    driver.find_element_by_xpath("//input[@value='true']").click()
    # Go to summary page
    gotosummaryPage(driver)
    # Download summary
    renameSummary(currentTestcaseName, file, testDeviceName)
    # Go back to download page
    downloadmsi(driver)
    #调用重命名函数
    renameMsiFile(driver, file, currentTestcaseName,testDeviceName)

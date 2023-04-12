import sys 
from Common.function_basic import GoToPCSoftwarePage
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from Common.function_configure import renameMsiFile
from Common.function_basic import borwserConfigure, getLocation


#Verification of all available firmware version to a device
def testcase4153_1():
    #Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    #Configure driver
    driver, windowsTrack,testDeviceName,file = setup_driver()
    # 进入到选择device页
    windowsTrack.GoToSelectDevice()
    #输入Device
    windowsTrack.SelectDevicePageAction()
    #选择FW
    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    Select(fw_select).select_by_index("1")
    driver.find_element_by_css_selector("input[name='configurationViewModel.Devices[0].Downgrade']").click()
    print(testDeviceName+' '+sys._getframe().f_code.co_name+' Configure finish')
    # #进入softphone配置页
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    #跳转到.msi下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    #跳转到Summary下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件
    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\4153_1.html'
    try:
        os.rename(summary, renamesummary)
        print(testDeviceName+ ' testcase4153_1 summary download successful')
        summary = file + '\\JabraXPRESSx64.msi'
        renamesummary = file + '\\4153_1.msi'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXPRESSx64.msi'
        renamesummary = file + '\\4153_1.msi'
    # 返回到下载页
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # 勾选同意协议
    driver.find_element_by_id('eulaOk').click()
    # #点击下载
    driver.find_element_by_id('download64bit').click()
    #调用重命名函数
    renameMsiFile(driver, summary, renamesummary)
    print(testDeviceName+ ' testcase4153_1 download successful')
    print('\n')
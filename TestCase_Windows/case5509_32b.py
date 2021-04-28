import sys
import os
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from Common.configure import renameAndclose,borwserConfigure


# Make a package with higher FW version, DU settings as leave uncaged.(DUT has lower version).
def testcase5509_32b():
    fo = open("device.txt", "rt")
    lastingDevicename = fo.read()
    file = "C:\\download\\" +lastingDevicename
    options=borwserConfigure()
    global driver
    driver = webdriver.Chrome(chrome_options=options)
    from Page.indexPage import windowsPage
    windowsPage = windowsPage(driver)
    # 进入到选择device页
    windowsPage.clickNextButton()
    #输入Device
    windowsPage.chooseDevice()
    #选择FW
    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    Select(fw_select).select_by_index("1")
    print(lastingDevicename+' '+sys._getframe().f_code.co_name+' Configure finish')
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
    renamesummary = file + '\\5509_32bit.html'
    try:
        os.rename(summary, renamesummary)
        print(lastingDevicename+ ' testcase5509 summary download successful')
        summary = file + '\\JabraXPRESSx86.msi'
        renamesummary = file + '\\5509_32bit.msi'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXPRESSx86.msi'
        renamesummary = file + '\\5509_32bit.msi'
    # 返回到下载页
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # 勾选同意协议
    driver.find_element_by_id('eulaOk').click()
    # #点击下载
    driver.find_element_by_id('download32bit').click()
    #调用重命名函数
    renameAndclose(driver,summary,renamesummary)
    print(lastingDevicename+ ' testcase5509_32bit download successful')
    print('\n')
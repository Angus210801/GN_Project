import sys
import os
import shutil
import zipfile
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

from Common.function_Configure import renameAndclose,borwserConfigure,getLocation,getLocation


def testcase6134():
    fo = open("device.txt", "rt")
    lastingDevicename = fo.read()
    file = getLocation() +lastingDevicename
    options = borwserConfigure()
    global driver
    driver = webdriver.Chrome(chrome_options=options)
    from Common.function_Basic import linuxindexPage
    linuxindexPage = linuxindexPage(driver)
    #Select device页
    linuxindexPage.clickNextButton()
    #输入设备名
    linuxindexPage.chooseDevice()
    #选择FW
    setting = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[0].SelectedValue']")
    Select(setting).select_by_index("1")



    print(lastingDevicename+' '+sys._getframe().f_code.co_name+' Configure finish')
    # #进入softphone配置页
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()

    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件

    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\6134.html'
    try:
        os.rename(summary, renamesummary)
        print(lastingDevicename+ ' testcase6134 summary download successful')
        summary = file + '\\JabraXpressFiles.zip'
        renamesummary = file + '\\6134'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXpressFiles.zip'
        renamesummary = file + '\\6134'
    # 返回到下载页
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # 勾选同意协议
    driver.find_element_by_id('eulaOk').click()
    # 输入网址：
    driver.find_element_by_css_selector("input[name='localServerUrl']").send_keys('http://my.gn.com/')
    # #点击下载
    driver.find_element_by_id('downloadZip').click()
    sleep(20)
    try:
        while os.path.exists(summary)==False:
            sleep(10)
        with zipfile.ZipFile(summary, "r") as zip_ref:
            zip_ref.extractall(file)
        summary = file + '\\Files_to_place_on_local_server'
        os.rename(summary, renamesummary)
        shutil.rmtree(file + '\\Files_to_install_on_end-user_computers')
        os.remove(file + '\\JabraXpressFiles.zip')
        os.remove(file + '\\readme.txt')
        print(lastingDevicename+ ' testcase6134 download successful')
        print('\n')

    except Exception as e:
        sleep(40)
        os.rename(summary, renamesummary)
        print('rename success')
        driver.close()

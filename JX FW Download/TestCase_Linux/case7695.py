import sys
import os
import shutil
import zipfile
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

from Common.configure import borwserConfigure

#  All settings in the device an be hange from default value to max value with installation of zip file at the end user PC,no FW change.
from Page.configurationPage import isElementExist, isInputExist


def testcase7695():
    fo = open("device.txt", "rt")
    lastingDevicename = fo.read()
    file = "C:\\download\\" +lastingDevicename
    options = borwserConfigure()
    global driver
    driver = webdriver.Chrome(chrome_options=options)
    from Page.indexPage import linuxindexPage
    linuxindexPage = linuxindexPage(driver)
    # 进入到选择device页
    linuxindexPage.clickNextButton()
    #输入设备名
    linuxindexPage.chooseDevice()

   #  fw_select = driver.find_element_by_css_selector(
   #      "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
   # # fw_verision = Select(fw_select).options
   #  Select(fw_select).select_by_index("1")

    set_table = driver.find_element_by_class_name('settings-table')
    td_content = set_table.find_elements_by_tag_name('tr')
    set_content = driver.find_element_by_class_name("setting-name")
    table_tr_number = len(td_content)

    i = 0
    while i < table_tr_number:
        flag = isElementExist(driver,
            "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(i) + "].SelectedValue']")
        if flag:
            setting = driver.find_element_by_css_selector(
                "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                    i) + "].SelectedValue']")
            if Select(setting):
                select = Select(setting)
                selectlen = len(select.options)
                Select(setting).select_by_index(selectlen-1)
                i = i + 1
                continue
        elif isInputExist(driver,
                "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                    i) + "].SelectedValue']"):
            try:
                driver.find_element_by_css_selector(
                    "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                        i) + "].SelectedValue']").send_keys('2020')
                i = i + 1
                continue
            except:
                i = i + 1
                continue
        else:
            i = i + 1
            continue

    # fw_selected = Select(fw_select).first_selected_option
    # print(fw_selected.text)
    print(lastingDevicename+' '+sys._getframe().f_code.co_name+' Configure finish')
    # #进入softphone配置页
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()

    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件
    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\7695.html'
    try:
        os.rename(summary, renamesummary)
        print(lastingDevicename+ ' testcase7695 summary download successful')
        summary = file + '\\JabraXpressFiles.zip'
        renamesummary = file + '\\7695'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
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
        print(lastingDevicename+ ' testcase7695 download successful')
        print('\n')
        driver.close()
    except Exception as e:
        print(e)


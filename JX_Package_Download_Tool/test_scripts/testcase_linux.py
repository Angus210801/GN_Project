import random
import shutil
import sys
import zipfile

import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from test_scripts.testcase_action import browser_configure, get_save_dir
from test_scripts.testcase_element_exist import isElementExist, isInputExist, isUploadButton



def testcase6098():
    """ 6098: Install a Zip file on end user environment with a later FW and no setting change."""
    fo = open("device.txt", "rt")
    lastingDevicename = fo.read()
    file = get_save_dir() + lastingDevicename
    options = browser_configure()
    global driver
    driver = webdriver.Chrome(chrome_options=options)
    from test_scripts.testcase_action import InitLinuxTrack
    linuxindexPage = InitLinuxTrack(driver)
    # 进入到选择device页
    linuxindexPage.click_next_button()
    #输入Device
    linuxindexPage.select_device()
    #选择FW
    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    fw_verision = Select(fw_select).options
    Select(fw_select).select_by_index("1")

    set_table = driver.find_element_by_class_name('settings-table')
    td_content = set_table.find_elements_by_tag_name('tr')
    set_content = driver.find_element_by_class_name("setting-name")
    table_tr_number = len(td_content)

    i = 0
    while i < table_tr_number:
        flag = isElementExist(driver,
                              "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                  i) + "].SelectedValue']")
        if flag:
            setting = driver.find_element_by_css_selector(
                "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                    i) + "].SelectedValue']")
            if Select(setting):
                select = Select(setting)
                selectlen = len(select.options)
                Select(setting).select_by_index(selectlen - 1)
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

    print(lastingDevicename+' '+sys._getframe().f_code.co_name+' Configure finish')
    # #进入softphone配置页
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()

    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件
    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\6098.html'
    try:
        os.rename(summary, renamesummary)
        print(lastingDevicename+ ' testcase6098 summary download successful')
        summary = file + '\\JabraXpressFiles.zip'
        renamesummary = file + '\\6098.zip'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXpressFiles.zip'
        renamesummary = file + '\\6098.zip'
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
        os.rename(summary, renamesummary)
        print(lastingDevicename+ ' testcase6098 download successful')
        print('\n')
        driver.close()
    except Exception as e:
        sleep(40)
        os.rename(summary, renamesummary)
        print('rename success')
        driver.close()


def testcase6134():
    fo = open("device.txt", "rt")
    lastingDevicename = fo.read()
    file = get_save_dir() + lastingDevicename
    options = browser_configure()
    global driver
    driver = webdriver.Chrome(chrome_options=options)
    from test_scripts.testcase_action import InitLinuxTrack
    linuxindexPage = InitLinuxTrack(driver)
    #Select device页
    linuxindexPage.click_next_button()
    #输入设备名
    linuxindexPage.select_device()
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


def testcase7551():
    fo = open("device.txt", "rt")
    lastingDevicename = fo.read()
    file = get_save_dir() + lastingDevicename
    options = browser_configure()
    global driver
    driver = webdriver.Chrome(chrome_options=options)
    from test_scripts.testcase_action import InitLinuxTrack
    linuxindexPage = InitLinuxTrack(driver)
    # 进入到选择device页
    linuxindexPage.click_next_button()
    #输入设备名
    linuxindexPage.select_device()
    #选择FW
    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    Select(fw_select).select_by_index("1")

    set_table = driver.find_element_by_class_name('settings-table')
    td_content = set_table.find_elements_by_tag_name('tr')
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
                Select(setting).select_by_index(random.randint(1, selectlen - 1))
                i = i + 1
                continue
        elif isInputExist(driver,
                "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                    i) + "].SelectedValue']"):
            try:
                driver.find_element_by_css_selector(
                    "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                        i) + "].SelectedValue']").send_keys('2021')
            except:
                i = i + 1
                continue
            i = i + 1
            continue
        else:
            i = i + 1
            continue
    #判断按钮是否可用
    nextButton=driver.find_element_by_xpath("//input[@value='NEXT >']")
    isNextButtonEnable=nextButton.is_enabled()
    if isNextButtonEnable==False:
        i = 0
        while i < table_tr_number:
            flag = isElementExist(driver,
                                  "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                      i) + "].SelectedValue']")
            if flag:
                setting = driver.find_element_by_css_selector(
                    "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                        i) + "].SelectedValue']")
                if Select(setting):
                    i = i + 1
                    continue
            elif isInputExist(driver,
                             "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                 i) + "].SelectedValue']"):
                try:
                    driver.find_element_by_css_selector(
                        "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                            i) + "].SelectedValue']").send_keys('2021')
                    i = i + 1
                    continue
                except Exception as e:
                    i=i+1
                    continue
            elif isUploadButton(driver,"input[value='Upload']"):
                try:
                    driver.find_element_by_css_selector("input[id='configurationViewModel.Devices[0].SelectedFirmware.Settings[36].fileinputId']").send_keys("C:\\download\\bat.bmp")
                    sleep(5)
                    i=i+1
                    continue
                except Exception as e:
                    print(e)
            else:
                i=i+1
                continue
    print(lastingDevicename+' '+sys._getframe().f_code.co_name+' Configure finish')
    # #进入softphone配置页
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()

    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件
    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\7551.html'
    try:
        os.rename(summary, renamesummary)
        print(lastingDevicename+ ' testcase7551 summary download successful')
        summary = file + '\\JabraXpressFiles.zip'
        renamesummary = file + '\\7551'
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
        print(lastingDevicename+ ' testcase7551 download successful')
        print('\n')
        driver.close()
    except Exception as e:
        sleep(40)
        os.rename(summary, renamesummary)
        print('rename success')
        driver.close()


def testcase7555():
    fo = open("device.txt", "rt")
    lastingDevicename = fo.read()
    file = get_save_dir() + lastingDevicename
    options = browser_configure()
    global driver
    driver = webdriver.Chrome(chrome_options=options)
    from test_scripts.testcase_action import InitLinuxTrack
    linuxindexPage = InitLinuxTrack(driver)
    # 进入到选择device页
    linuxindexPage.click_next_button()
    #输入Device
    linuxindexPage.select_device()
    #选择FW
    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    fw_verision = Select(fw_select).options
    Select(fw_select).select_by_index("1")

    print(lastingDevicename+' '+sys._getframe().f_code.co_name+' Configure finish')
    # #进入softphone配置页
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()

    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件
    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\7555.html'
    try:
        os.rename(summary, renamesummary)
        print(lastingDevicename+ ' testcase7555 summary download successful')
        summary = file + '\\JabraXpressFiles.zip'
        renamesummary = file + '\\7555'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXpressFiles.zip'
        renamesummary = file + '\\7555.zip'
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
        print(lastingDevicename+ ' testcase7555 download successful')
        print('\n')
        driver.close()
    except Exception as e:
        sleep(40)
        os.rename(summary, renamesummary)
        print('rename success')
        driver.close()


def testcase7556():
    fo = open("device.txt", "rt")
    lastingDevicename = fo.read()
    file = get_save_dir() + lastingDevicename
    options = browser_configure()
    global driver
    driver = webdriver.Chrome(chrome_options=options)
    from test_scripts.testcase_action import InitLinuxTrack
    linuxindexPage = InitLinuxTrack(driver)
    # 进入到选择device页
    linuxindexPage.click_next_button()
    #输入Device
    linuxindexPage.select_device()
    #选择FW
    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    fw_verision = Select(fw_select).options
    Select(fw_select).select_by_index("1")

    #配置设置项为Default
    driver.find_element_by_xpath("//input[@value='SET ALL TO DEFAULT VALUES']").click()

    print(lastingDevicename+' '+sys._getframe().f_code.co_name+' Configure finish')
    # #进入softphone配置页
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()

    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件
    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\7556.html'
    try:
        os.rename(summary, renamesummary)
        print(lastingDevicename+ ' testcase7556 summary download successful')
        summary = file + '\\JabraXpressFiles.zip'
        renamesummary = file + '\\7556'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXpressFiles.zip'
        renamesummary = file + '\\7556'
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
        print(lastingDevicename+ ' testcase7556 download successful')
        print('\n')
        driver.close()
    except Exception as e:
        sleep(40)
        os.rename(summary, renamesummary)
        print('rename success')
        driver.close()


def testcase7556p():
    fo = open("device.txt", "rt")
    lastingDevicename = fo.read()
    file = get_save_dir() + lastingDevicename
    options = browser_configure()
    global driver
    driver = webdriver.Chrome(chrome_options=options)
    from test_scripts.testcase_action import InitLinuxTrack
    linuxindexPage = InitLinuxTrack(driver)
    # 进入到选择device页
    linuxindexPage.click_next_button()
    #输入Device
    linuxindexPage.select_device()
    #选择FW
    #配置设置项为Default
    set_table = driver.find_element_by_class_name('settings-table')
    td_content = set_table.find_elements_by_tag_name('tr')
    table_tr_number = len(td_content)

    i = 1
    while i < table_tr_number:
        flag = isElementExist(driver,
                              "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                  i) + "].SelectedValue']")
        if flag:
            setting = driver.find_element_by_css_selector(
                "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                    i) + "].SelectedValue']")
            if Select(setting):
                select = Select(setting)
                selectlen = len(select.options)
                Select(setting).select_by_index(random.randint(1, selectlen - 1))
                default = "*"
                selectedValue = Select(setting).first_selected_option.text
                chooseNotDefault = default in selectedValue
                while chooseNotDefault:
                    Select(setting).select_by_index(random.randint(1, selectlen - 1))
                    selectedValue = Select(setting).first_selected_option.text
                    chooseNotDefault = default in selectedValue
                i = i + 1
                continue
        elif isInputExist(driver,
                          "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                              i) + "].SelectedValue']"):
            try:
                driver.find_element_by_css_selector(
                    "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                        i) + "].SelectedValue']").send_keys('2021')
            except:
                i = i + 1
                continue
            i = i + 1
            continue
        else:
            i = i + 1
            continue

    # 判断按钮是否可用
    nextButton = driver.find_element_by_xpath("//input[@value='NEXT >']")
    isNextButtonEnable = nextButton.is_enabled()
    if isNextButtonEnable == False:
        i = 0
        while i < table_tr_number:
            flag = isElementExist(driver,
                                  "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                      i) + "].SelectedValue']")
            if flag:
                setting = driver.find_element_by_css_selector(
                    "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                        i) + "].SelectedValue']")
                if Select(setting):
                    i = i + 1
                    continue
            elif isInputExist(driver,
                              "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                  i) + "].SelectedValue']"):
                try:
                    driver.find_element_by_css_selector(
                        "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                            i) + "].SelectedValue']").send_keys('2021')
                    i = i + 1
                    continue
                except Exception as e:
                    i = i + 1
                    continue
            elif isUploadButton(driver, "input[value='Upload']"):
                try:
                    driver.find_element_by_css_selector(
                        "input[id='configurationViewModel.Devices[0].SelectedFirmware.Settings[36].fileinputId']").send_keys(
                        "C:\\download\\bat.bmp")
                    sleep(5)
                    i = i + 1
                    continue
                except Exception as e:
                    print(e)
            else:
                i = i + 1
                continue
    print(lastingDevicename + ' ' + sys._getframe().f_code.co_name + ' Configure finish')
    # Go to the package download page
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # Go to the summary download page
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # Download summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件
    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\7556B.html'
    try:
        os.rename(summary, renamesummary)
        print(lastingDevicename+ ' testcase7556B summary download successful')
        summary = file + '\\JabraXpressFiles.zip'
        renamesummary = file + '\\7556B'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXpressFiles.zip'
        renamesummary = file + '\\7556B'
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
        print(lastingDevicename+ ' testcase7556B download successful')
        print('\n')
        driver.close()
    except Exception as e:
        sleep(40)
        os.rename(summary, renamesummary)
        print('rename success')
        driver.close()


def testcase7692():
    fo = open("device.txt", "rt")
    lastingDevicename = fo.read()
    file = get_save_dir() + lastingDevicename
    options = browser_configure()
    global driver
    driver = webdriver.Chrome(chrome_options=options)
    from test_scripts.testcase_action import InitLinuxTrack
    linuxindexPage = InitLinuxTrack(driver)
    # 进入到选择device页
    linuxindexPage.click_next_button()
    #输入设备名
    linuxindexPage.select_device()

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
                Select(setting).select_by_index("1")
                i = i + 1
                continue
        elif isInputExist(driver,
                "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                    i) + "].SelectedValue']"):
            getInputName=driver.find_element_by_css_selector("input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(i) + "].SelectedValue']")
            if getInputName.get_attribute('data-val-regex')=='[\s\S]':
                try:
                    driver.find_element_by_css_selector(
                        "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                            i) + "].SelectedValue']").send_keys('J2½§!"@#£$¤*%&/\<>[]()=?')
                    i = i + 1
                    continue
                except:
                    i = i + 1
                    continue
            else:
                try:
                    driver.find_element_by_css_selector(
                        "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                            i) + "].SelectedValue']").send_keys('1*#959932881')
                    i = i + 1
                    continue
                except:
                    i = i + 1
                    continue
        else:
            i = i + 1
            continue


    #判断按钮是否可用
    nextButton=driver.find_element_by_xpath("//input[@value='NEXT >']")
    isNextButtonEnable=nextButton.is_enabled()
    if isNextButtonEnable==False:
        i = 0
        while i < table_tr_number:
            flag = isElementExist(driver,
                                  "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                      i) + "].SelectedValue']")
            if flag:
                setting = driver.find_element_by_css_selector(
                    "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                        i) + "].SelectedValue']")
                if Select(setting):
                    i = i + 1
                    continue
            elif isInputExist(driver,
                             "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                                 i) + "].SelectedValue']"):
                try:
                    driver.find_element_by_css_selector(
                        "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                            i) + "].SelectedValue']").send_keys('2021')
                    i = i + 1
                    continue
                except Exception as e:
                    i=i+1
                    continue
            elif isUploadButton(driver,"input[value='Upload']"):
                try:
                    driver.find_element_by_css_selector("input[id='configurationViewModel.Devices[0].SelectedFirmware.Settings[36].fileinputId']").send_keys("C:\\download\\bat.bmp")
                    sleep(5)
                    i=i+1
                    continue
                except Exception as e:
                    print(e)
            else:
                i=i+1
                continue
    print(lastingDevicename+' '+sys._getframe().f_code.co_name+' Configure finish')
    # #进入softphone配置页
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()

    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件
    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\7692.html'
    try:
        os.rename(summary, renamesummary)
        print(lastingDevicename+ ' testcase7692 summary download successful')
        summary = file + '\\JabraXpressFiles.zip'
        renamesummary = file + '\\7692'
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
        readme=file + '\\readme.txt'
        while os.path.exists(readme):
            os.remove(readme)
        print(lastingDevicename+ ' testcase7692 download successful')
        print('\n')
        driver.close()
    except Exception as e:
        print(e)


def testcase7695():
    fo = open("device.txt", "rt")
    lastingDevicename = fo.read()
    file = get_save_dir() + lastingDevicename
    options = browser_configure()
    global driver
    driver = webdriver.Chrome(chrome_options=options)
    from test_scripts.testcase_action import InitLinuxTrack
    linuxindexPage = InitLinuxTrack(driver)
    # 进入到选择device页
    linuxindexPage.click_next_button()
    #输入设备名
    linuxindexPage.select_device()

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


def testcase10312l():
    i=1
    while i<=6:
        fo = open("device.txt", "rt")
        lastingDevicename = fo.read()
        file = get_save_dir() + lastingDevicename
        options = browser_configure()
        global driver
        driver = webdriver.Chrome(chrome_options=options)
        from test_scripts.testcase_action import InitLinuxTrack
        linuxindexPage = InitLinuxTrack(driver)
        #Select device页
        linuxindexPage.click_next_button()
        #输入设备名
        linuxindexPage.select_device()
        #选择FW
        fw_select = driver.find_element_by_css_selector(
            "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
        Select(fw_select).select_by_index("1")


        #判断是否存在Language setting
        try:
            language_region_select = driver.find_element_by_css_selector("select[name='configurationViewModel.Devices[0].SelectedFirmware.TunePackRegionSettings.SelectedTunePackRegionId']")
            Select(language_region_select).select_by_index("1")
            language_select=driver.find_element_by_css_selector("select[name='configurationViewModel.Devices[0].SelectedFirmware.TunePackRegionSettings.SelectedTunePackRegionLanguageId']")
            languageList=Select(language_select)
            languageNum=len(languageList.options)
            Select(language_select).select_by_index(i)
            language_select=Select(language_select).first_selected_option.text

            #配置完成后打印提醒消息
            print(lastingDevicename+' '+sys._getframe().f_code.co_name+' Configure finish')
            # #进入softphone配置页
            driver.find_element_by_xpath("//input[@value='NEXT >']").click()

            driver.find_element_by_xpath("//input[@value='NEXT >']").click()
            # 下载Summary
            driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
            # 重命名summary文件
            sleep(5)
            summary = file + '\\summary.html'
            renamesummary = file + '\\10312'+language_select+'.html'
            try:
                os.rename(summary, renamesummary)
                print(lastingDevicename+ ' testcase10312 summary download successful')
                summary = file + '\\JabraXpressFiles.zip'
                renamesummary = file + '\\10312_'+language_select
            except Exception as e:
                os.remove(renamesummary)
                os.rename(summary, renamesummary)
                summary = file + '\\JabraXpressFiles.zip'
                renamesummary = file + '\\10312'+language_select
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
                print(lastingDevicename+ ' testcase10312 '+language_select+'download successful')
                print('\n')
                i = i + 1
                driver.close()

            except Exception as e:
                sleep(40)
                os.rename(summary, renamesummary)
                print('rename success')
                i=i+1
        except:
            print("There is no language setting for this device")
            driver.close()
            break


def testcase16990():
    fo = open("device.txt", "rt")
    lastingDevicename = fo.read()
    file = get_save_dir() + lastingDevicename
    options = browser_configure()
    global driver
    driver = webdriver.Chrome(chrome_options=options)
    from test_scripts.testcase_action import InitLinuxTrack
    linuxindexPage = InitLinuxTrack(driver)
    # 进入到选择device页
    linuxindexPage.click_next_button()
    #输入设备名
    linuxindexPage.select_device()

    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    Select(fw_select).select_by_index("1")

    driver.find_element_by_css_selector("input[name='configurationViewModel.Devices[0].Downgrade']").click()

    print(lastingDevicename+' '+sys._getframe().f_code.co_name+' Configure finish')
    # #进入softphone配置页
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()

    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件
    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\16990.html'
    try:
        os.rename(summary, renamesummary)
        print(lastingDevicename+ ' testcase16990 summary download successful')
        summary = file + '\\JabraXpressFiles.zip'
        renamesummary = file + '\\16990'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXpressFiles.zip'
        renamesummary = file + '\\16990.zip'
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
        print(lastingDevicename+ ' testcase16990 download successful')
        print('\n')
        driver.close()
    except Exception as e:
        sleep(40)
        os.rename(summary, renamesummary)
        print('rename success')
        driver.close()


def testcase16991():
    fo = open("device.txt", "rt")
    lastingDevicename = fo.read()
    file = get_save_dir() + lastingDevicename
    options = browser_configure()
    global driver
    driver = webdriver.Chrome(chrome_options=options)
    from test_scripts.testcase_action import InitLinuxTrack
    linuxindexPage = InitLinuxTrack(driver)
    # 进入到选择device页
    linuxindexPage.click_next_button()
    #输入设备名
    linuxindexPage.select_device()

    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    Select(fw_select).select_by_index("1")

    print(lastingDevicename+' '+sys._getframe().f_code.co_name+' Configure finish')
    # #进入softphone配置页
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()

    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件
    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\16991.html'
    try:
        os.rename(summary, renamesummary)
        print(lastingDevicename+ ' testcase16991 summary download successful')
        summary = file + '\\JabraXpressFiles.zip'
        renamesummary = file + '\\16991'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXpressFiles.zip'
        renamesummary = file + '\\16991.zip'
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
        print(lastingDevicename+ ' testcase16991 download successful')
        print('\n')
        driver.close()
    except Exception as e:
        sleep(40)
        os.rename(summary, renamesummary)
        print('rename success')
        driver.close()

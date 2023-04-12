import sys
import os
import shutil
import zipfile
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from Common.function_configure import renameMsiFile, getLocation
from Common.function_basic import borwserConfigure, getLocation
from Common.function_Judge import isElementExist, isInputExist,isUploadButton

#JX-ThinC:All settings in the device can be change from default value to min.value with installation of .zip file at the end user PC,no FW change.

def testcase7692():
    fo = open("device.txt", "rt")
    lastingDevicename = fo.read()
    file = getLocation() +lastingDevicename
    options = borwserConfigure()
    global driver
    driver = webdriver.Chrome(chrome_options=options)
    from Common.function_basic import linuxindexPage
    linuxindexPage = linuxindexPage(driver)
    # 进入到选择device页
    linuxindexPage.clickNextButton()
    #输入设备名
    linuxindexPage.chooseDevice()

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
                    driver.find_element_by_css_selector("input[id='configurationViewModel.Devices[0].SelectedFirmware.Settings[36].fileinputId']").send_keys("C:\\download\\001.bmp")
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


import sys
import os
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from Common.configure import renameAndclose,borwserConfigure
from Page.configurationPage import isElementExist, isInputExist, isUploadButton


#JX-JDU: [DUT in Power OFF Mode] Make a package for both FW upgrade/downgrade and DUT settings configuration.
def testcase7195():
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

    #选择FW为低版本
    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    fwList=Select(fw_select)
    fwNum=len(fwList.options)
    i=3
    if i != fwNum-1 :
        i=fwNum-1
        Select(fw_select).select_by_index(i)
        driver.find_element_by_css_selector("input[name='configurationViewModel.Devices[0].Downgrade']").click()

    #配置设置项为随机项
    set_table = driver.find_element_by_class_name('settings-table')
    td_content = set_table.find_elements_by_tag_name('tr')
    table_tr_number = len(td_content)

    i = 1
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
                default="*"
                selectedValue=Select(setting).first_selected_option.text
                chooseNotDefault=default in selectedValue
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
                        "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                            i) + "].SelectedValue']").send_keys(
                        "C:\\download\\cat.bmp")
                    sleep(5)
                    i = i + 1
                    continue
                except Exception as e:
                    print(e)
            else:
                i = i + 1
                continue
    print(lastingDevicename + ' ' + sys._getframe().f_code.co_name + ' Configure finish')
    # #进入softphone配置页
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    #勾选下载JD
    driver.find_element_by_xpath("//input[@value='true']").click()
     ## 选择1个随机的Preferred softphone
    setting = driver.find_element_by_css_selector(
        "select[name='PcSoftwareViewModel.DeploymentOptionGroups[2].DeploymentOptions[19].Value']")
    if Select(setting):
        select = Select(setting)
        selectlen = len(select.options)
        Select(setting).select_by_index(random.randint(0, selectlen - 1))
    #跳转到.msi下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    #跳转到Summary下载页面
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    # 下载Summary
    driver.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
    # 重命名summary文件
    sleep(5)
    summary = file + '\\summary.html'
    renamesummary = file + '\\7195.html'
    try:
        os.rename(summary, renamesummary)
        print(lastingDevicename+ ' testcase7195 summary download successful')
        summary = file + '\\JabraXPRESSx64.msi'
        renamesummary = file + '\\7195.msi'
    except Exception as e:
        os.remove(renamesummary)
        os.rename(summary, renamesummary)
        summary = file + '\\JabraXPRESSx64.msi'
        renamesummary = file + '\\7195.msi'
    # 返回到下载页
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # 勾选同意协议
    driver.find_element_by_id('eulaOk').click()
    # #点击下载
    driver.find_element_by_id('download64bit').click()
    #调用重命名函数
    renameAndclose(driver,summary,renamesummary)
    print(lastingDevicename+ ' testcase7195 download successful')
    print('\n')
import random
import sys 
from Common.function_basic import GoToPCSoftwarePage

from selenium.webdriver.support.select import Select

from Common.function_configure import renameMsiFile, setup_driver, renameSummary


# Device settings configuration with all setings as LEAVE UNCHANGED and a specific and password as leave Unchnaged
def testcase3966():
    currentTestcaseName = sys._getframe().f_code.co_name
    driver, windowsTrack,testDeviceName,file = setup_driver()
    # 进入到选择device页
    windowsTrack.GoToSelectDevice()
    #输入Device
    windowsTrack.SelectDevicePageAction()
    #选择FW
    fw_select = driver.find_element_by_css_selector(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
    Select(fw_select).select_by_index("1")
    print(testDeviceName+' '+sys._getframe().f_code.co_name+' Configure finish')
    # #进入softphone配置页
    driver.find_element_by_xpath("//input[@value='NEXT >']").click()
    #勾选下载JD
        # Go to PC software page
    GoToPCSoftwarePage(driver)
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
    renameSummary(currentTestcaseName, file, testDeviceName)
    # 返回到下载页
    driver.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
    # 勾选同意协议
    driver.find_element_by_id('eulaOk').click()
    # #点击下载
    driver.find_element_by_id('download64bit').click()
    #调用重命名函数
    renameMsiFile(driver, file, currentTestcaseName)
    print(testDeviceName+ ' testcase3966 download successful')
    print('\n')
import sys 
from Common.function_basic import GoToPCSoftwarePage
from selenium.webdriver.support.select import Select
from Common.function_configure import renameMsiFile, renameSummary, setup_driver
from Common.function_basic import gotosummaryPage,downloadmsi,GoToPCSoftwarePage,DownloadJabraDirect

#Jabra Direct Diagnostic Report plug-in version and s/n verification(not FW, settings=default）
def testcase3961():
    #Get current function name
    currentTestcaseName = sys._getframe().f_code.co_name
    #Configure driver
    driver, windowsTrack, testDeviceName, file = setup_driver()
    # Go to device page
    windowsTrack.GoToSelectDevice()
    # Choose device
    windowsTrack.SelectDevicePageAction()
    # Configure the device page with all settings as default
    driver.find_element_by_xpath("//input[@value='SET ALL TO DEFAULT VALUES']").click()
    setting = driver.find_element_by_css_selector("select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[0].SelectedValue']")
    Select(setting).select_by_index("1")
    # Print the configured finish message
    print(testDeviceName+' '+currentTestcaseName+' Configure finish')
    # Go to PC software page
    GoToPCSoftwarePage(driver)
    # Download Jabra Direct
    DownloadJabraDirect(driver)
    # Go to summary page
    gotosummaryPage(driver)
    # Download summary
    renameSummary(currentTestcaseName, file, testDeviceName)
    # Go back to download page
    downloadmsi(driver)
    # Rename msi file
    renameMsiFile(driver, file, currentTestcaseName,testDeviceName)

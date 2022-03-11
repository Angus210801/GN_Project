from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://dkcphweb15/Xpress/35.X.Development/MDCT/select-devices")

if __name__ == '__main__':
    i=0
    while i<=90:
        driver.find_element_by_xpath("//p[@data-order=\""+str(i)+"\"]").click()
        i=i+1
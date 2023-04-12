from TestCase_Linux.case7556_pre import testcase7556p
from TestCase_Windows.case3961 import testcase3961
from TestCase_Windows.case3966 import testcase3966
from Common.function_basic import get_Windows_ip
from Common.function_check_chromedriver import checkChromeDriverUpdate

if __name__ == '__main__':
    # testcase7556p()
    # testcase3966()
    # ip_access=get_Windows_ip()
    # print(ip_access)
    testcase3961()

    # with open("saveDir.txt", "rt") as f:
    #     file = f.read() + '/' + 'Jabra spk240'
    # print(file)
    # checkChromeDriverUpdate()
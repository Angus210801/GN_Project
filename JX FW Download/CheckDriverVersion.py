import requests,winreg,zipfile,re,os
url='http://npm.taobao.org/mirrors/chromedriver/' # chromedriver download link
def get_Chrome_version():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Google\Chrome\BLBeacon')
    version, types = winreg.QueryValueEx(key, 'version')
    return version

def get_latest_version(url):
    '''查询最新的Chromedriver版本'''
    rep = requests.get(url).text
    time_list = []                                          # 用来存放版本时间
    time_version_dict = {}                                  # 用来存放版本与时间对应关系
    result = re.compile(r'\d.*?/</a>.*?Z').findall(rep)     # 匹配文件夹（版本号）和时间
    for i in result:
        time = i[-24:-1]                                    # 提取时间
        version = re.compile(r'.*?/').findall(i)[0]         # 提取版本号
        time_version_dict[time] = version                   # 构建时间和版本号的对应关系，形成字典
        time_list.append(time)                              # 形成时间列表
    latest_version = time_version_dict[max(time_list)][:-1] # 用最大（新）时间去字典中获取最新的版本号
    return latest_version
def get_server_chrome_versions():
    '''return all versions list'''
    versionList=[]
    url="https://chromedriver.storage.googleapis.com/index.html"
    rep = requests.get(url).text
    result = re.compile(r'\d.*?/</a>.*?Z').findall(rep)
    for i in result:                                 # 提取时间
        version = re.compile(r'.*?/').findall(i)[0]         # 提取版本号
        versionList.append(version[:-1])                  # 将所有版本存入列表
    return versionList


def download_driver(download_url):
    '''下载文件'''
    file = requests.get(download_url)
    with open("chromedriver.zip", 'wb') as zip_file:        # 保存文件到脚本所在目录
        zip_file.write(file.content)
        print('Download driver successfully')

def get_version():
    '''查询系统内的Chromedriver版本'''
    outstd2 = os.popen('chromedriver --version').read()
    return outstd2.split(' ')[1]


def unzip_driver(path):
    '''解压Chromedriver压缩包到指定目录'''
    f = zipfile.ZipFile("chromedriver.zip",'r')
    for file in f.namelist():
        f.extract(file, path)

def check_update_chromedriver():
    # The program enterance
    print("Pre-condition:check the chromedriver...")
    chromeVersion=get_Chrome_version()
    chrome_main_version=int(chromeVersion.split(".")[0]) # chrome主版本号
    driverVersion=get_version()
    driver_main_version=int(driverVersion.split(".")[0]) # chromedriver主版本号
    download_url=""
    if driver_main_version!=chrome_main_version:
        print("chromedriver is old，updating>>>")
        versionList=get_server_chrome_versions()
        if chromeVersion in versionList:
            download_url=f"{url}{chromeVersion}/chromedriver_win32.zip"
        else:
            for version in versionList:
                if version.startswith(str(chrome_main_version)):
                    download_url=f"{url}{version}/chromedriver_win32.zip"
                    break
            if download_url=="":
                print("Can't find the chromedriver version match the browser , please go to the http://npm.taobao.org/mirrors/chromedriver/ verify")

        download_driver(download_url=download_url)
        path = "C:\Program Files (x86)\Google\Chrome\Application"
        unzip_driver(path)
        os.remove("chromedriver.zip")
        print('The driver has been update to：', get_version())
    else:
       print("chromedriver is match browser, go ahead!")

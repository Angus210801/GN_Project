import os
import re
import winreg
import zipfile
import time
import requests

# from Common.sel_def_logger import Log

# Mylog=Log()
base_url = 'http://npm.taobao.org/mirrors/chromedriver/'
version_re = re.compile(r'^[1-9]\d*\.\d*.\d*')  # 匹配前3位版本号的正则表达式

def onefloat(num):
    return '{:.1f}'.format(num)

def getChromeVersion():
    """通过注册表查询chrome版本"""
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Google\\Chrome\\BLBeacon')
        value, t = winreg.QueryValueEx(key, 'version')
        return version_re.findall(value)[0]  # 返回前3位版本号
    except WindowsError as e:
        # 没有安装chrome浏览器
        return "1.1.1"


def getChromeDriverVersion():
    """查询Chromedriver版本"""
    outstd2 = os.popen('chromedriver --version').read()
    try:
        version = outstd2.split(' ')[1]
        version = ".".join(version.split(".")[:-1])
        return version
    except Exception as e:
        return "0.0.0"


def getLatestChromeDriver(version):
    # 获取该chrome版本的最新driver版本号
    url = f"{base_url}LATEST_RELEASE_{version}"
    latest_version = requests.get(url).text
    # Mylog.info(f"与当前chrome匹配的最新chromedriver版本为: {latest_version}")
    # 下载chromedriver
    # Mylog.info("开始下载chromedriver...")
    download_url = f"{base_url}{latest_version}/chromedriver_win32.zip"
    with requests.get(download_url,stream=True) as file, open(r'chromedriver.zip', 'wb') as zip_file:# 保存文件到脚本所在目录
        total_size = int(file.headers['content-length'])
        # 请求文件的大小单位字节B
        total_size = int(file.headers['content-length'])
        # 以下载的字节大小
        content_size = 0
        # 进度下载完成的百分比
        plan = 0
        # 请求开始的时间
        start_time = time.time()
        # 上秒的下载大小
        temp_size = 0
        # 开始下载每次请求1024字节
        for content in file.iter_content(chunk_size=1024):
            zip_file.write(content)
            # 统计以下载大小
            content_size += len(content)
            # 计算下载进度
            plan = (content_size / total_size) * 100
            # 每一秒统计一次下载量
            if time.time() - start_time > 1:
                # 重置开始时间
                start_time = time.time()
                # 每秒的下载量
                speed = content_size - temp_size
                # KB级下载速度处理
                if 0 <= speed < (1024 ** 2):
                    print('\r',onefloat(plan), '%', onefloat(speed / 1024), 'KB/s', end='', flush=True,)
                # MB级下载速度处理
                elif (1024 ** 2) <= speed < (1024 ** 3):
                    print('\r', onefloat(plan), '%', onefloat(speed / (1024 ** 2)), 'MB/s', end='', flush=True)
                # 重置以下载大小
                temp_size = content_size
    print('\n')
    # Mylog.info("100%,下载完成.")
    # 解压
    f = zipfile.ZipFile("chromedriver.zip", 'r')
    for file in f.namelist():
        f.extract(file)
    # Mylog.info("解压完成.")


def checkChromeDriverUpdate():
    chrome_version = getChromeVersion()
    # Mylog.info(f'当前chrome版本: {chrome_version}')
    driver_version = getChromeDriverVersion()
    # Mylog.info(f'当前chromedriver版本: {driver_version}')
    if chrome_version == driver_version:
        # Mylog.info("版本兼容，无需更新.")
        return
    # Mylog.info("chromedriver版本与chrome浏览器不兼容，更新中>>>")
    try:
        getLatestChromeDriver(chrome_version)
        # Mylog.info("chromedriver更新成功!")
    except requests.exceptions.Timeout:
        print("chromedriver未知原因更新失败: {e}")
    except Exception as e:
        print("chromedriver未知原因更新失败: {e}")
        # Mylog.error(f"chromedriver未知原因更新失败: {e}")


if __name__ == "__main__":
    checkChromeDriverUpdate()


import os
import socket

def get_window_ip1():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        print(s.getsockname())
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

def get_window_ip2():
    # 获取本机计算机名称
    hostname = socket.gethostname()
    # 需要注意的是，如果本机有多网卡，比如说安装的有虚拟机，则此ip可能是虚拟机VMnet8的ip，而你真正的内网IP可能是物理无线适配器wlan的IP
    ip = socket.gethostbyname(hostname)

    #这种情况下，首先需要获取所有网卡的ip地址，然后人为进行筛选
    ipList = socket.gethostbyname_ex(hostname)
    return ipList[2][-1]

def get_window_ip3():
    return [a for a in os.popen('route print').readlines() if ' 0.0.0.0 ' in a][0].split()[-2]

def get_window_ip4():
    # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.connect(('baidu.com', 0))
    # ipaddr = s.getsockname()[0]
    # return ipaddr
    IP = socket.gethostbyname(socket.gethostname())
    return IP

def get_Windows_ip():
    iPv4=get_window_ip4()
    if iPv4[0:5]=='10.86':
        return True
    else:
        return False



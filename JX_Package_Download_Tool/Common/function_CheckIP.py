import socket

def get_Windows_ip():
    try:
        domain='http://dkcphweb15.corp.intra-gnn.com/'
        socket.gethostbyname(domain)
        return True
    except socket.error:
        return False


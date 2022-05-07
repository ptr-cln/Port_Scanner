import json
import socket

def extractJsonData(filename):
    with open(filename , "r") as file:
        data = json.load(file)
    return data

def getHostIpAddr(target):
    try:
        ip_addr = socket.gethostbyname(target)
        print("Ip address of " + (target) + " = " + ip_addr)
    except socket.gaierror as e:
        print(f"ERROR: {e}")
    else:
        return ip_addr

def isPortOpen(ip,port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(1.0)
    conn_status = sock.connect_ex((ip,port))
    if conn_status == 0:
        return True
    sock.close()
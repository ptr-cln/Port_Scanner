import socket
from JsonUtils import extractJsonData

PORTS_DATA_FILE = "./resources/Common_Used_Ports.json"
open_ports = []
ports_info = {}

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

if __name__ == "__main__":
    extractJsonData(PORTS_DATA_FILE)
    target = input("Insert target: ")
    ip_addr = getHostIpAddr(target)
    ports_info = extractJsonData(PORTS_DATA_FILE)

    for el in ports_info:
        try:

            #Input Checker
            try:
                port_to_scan = int(el['Port_Number'])
            except ValueError:
                continue


            print(f"Scanning :  {ip_addr} : {port_to_scan} | Protocol: {el['Transport_Protocol']}")
            if(isPortOpen(ip_addr,port_to_scan)):
                open_ports.append(el)
            
        except KeyboardInterrupt:
            print("Execution interrupted")
            break
    
    print("Open Ports:")
    for openPort in open_ports:
        print(str(openPort['Port_Number']) , " | " , openPort['Description'] , " | " , "Protocol: " , openPort['Transport_Protocol'])
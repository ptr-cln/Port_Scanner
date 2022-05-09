import json
import socket
import re

def extractJsonData(filename):
    with open(filename , "r") as file:
        data = json.load(file)
    return data

def getHostIpAddr(target):
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", str(target)):
        return target
    
    try:
        ipAddr = socket.gethostbyname(target)
        print("Ip address of " + (target) + " = " + ipAddr)
    except socket.gaierror as e:
        print(f"ERROR: {e}")
    else:
        return ipAddr

def isPortOpen(ip,port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(1.0)
    conn_status = sock.connect_ex((ip,port))
    if conn_status == 0:
        return True
    sock.close()

# Returns a list of lists
def splitListOfPorts(portsList,totalThreads):
    
    output = []
    
    listLen = len(portsList)
    elForEachThread = int(listLen / totalThreads)
    
    startsFrom = 0
    endTo = elForEachThread
    for x in range (0 , totalThreads):
        
        if(x == (totalThreads -1 )):
            output.append(portsList[startsFrom:])
        else:
            output.append(portsList[startsFrom:endTo])
            startsFrom = startsFrom + elForEachThread
            endTo = endTo + elForEachThread
    return output
    
# Work in progress
def orderListOfDict(listOfDict):
    return listOfDict



       


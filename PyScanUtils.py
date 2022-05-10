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

def printFile(openPort,ipAddr):
    file = open("./Scan_" + str(ipAddr) + ".txt","a")
    file.write(str(ipAddr) + " : " + (str(openPort['Port_Number']) + " | " + openPort['Description'] + "\n"))
    file.close
            
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
    
# Removes duplicates and sorts the list of ports (Ascending order)
def prettifyOutput(listOfDict):
    
    output=[]
    portsTmp=[]
    
    for port in listOfDict:
        if port['Port_Number'] not in portsTmp:
            portsTmp.append(port['Port_Number'])
        
    sortArr(portsTmp)
    
    for port in portsTmp:
        portInDict = next((item for item in listOfDict if item['Port_Number'] == port), None)
        output.append(portInDict)
    
    return output

def sortArr(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

       


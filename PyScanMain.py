from PyScanThread import *
from PyScanUtils import *

PORTS_DATA_FILE = "./resources/Common_Used_Ports.json"

# Number of how many threads will be used 
totalThreads = 10

threads = []

if __name__ == "__main__":
    target = input("Insert target: ")
    ipAddr = getHostIpAddr(target)
    portsList = extractJsonData(PORTS_DATA_FILE)

# Balancing the thread charge
    balancedPortsList = splitListOfPorts(portsList,totalThreads)

# Creating and starting all threads
    for x in range(0,totalThreads):
        threads.append(PyScanThread(("Thread" + str(x)),ipAddr,balancedPortsList[x]))
        threads[x].start()

# Waiting for all of them to finish
    for thread in threads:
        thread.join()

# Printing all open ports

    print("\n----------------------------------------------------------------------------")
    
    print("Open Ports:")
    for openPort in PyScanThread.OPEN_PORTS:
        print(str(ipAddr) + ":" + (str(openPort['Port_Number']) + " | " + openPort['Description'] + " | " + "Protocol: " + openPort['Transport_Protocol']))
    
    print("\n----------------------------------------------------------------------------")
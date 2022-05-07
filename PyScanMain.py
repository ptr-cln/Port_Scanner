from PyScanThread import *
from PyScanUtils import *
from collections import OrderedDict
from operator import itemgetter

PORTS_DATA_FILE = "./resources/Common_Used_Ports.json"

threads = []

if __name__ == "__main__":
    extractJsonData(PORTS_DATA_FILE)
    target = input("Insert target: ")
    ip_addr = getHostIpAddr(target)
    ports_info = extractJsonData(PORTS_DATA_FILE)

# Create and start all threads
    for x in range(0,10):
        threads.append(PyScanThread(("Thread" + str(x)),ip_addr,(ports_info[(x * 30):(x*30 + 30)])))
        threads[x].start()

# Wait for all of them to finish
    for thread in threads:
        thread.join()

# Sort and print all open ports
    PyScanThread.OPEN_PORTS =  orderListOfDict(PyScanThread.OPEN_PORTS)

    print("Open Ports:")
    for openPort in PyScanThread.OPEN_PORTS:
        print(str(openPort['Port_Number']) , " | " , openPort['Description'] , " | " , "Protocol: " , openPort['Transport_Protocol'])
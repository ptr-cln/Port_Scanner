from threading import *
from PyScanUtils import *

class PyScanThread (Thread):

   OPEN_PORTS = []
   LOCK = Lock()
    
   def printWithLock(self,msg):
        with self.LOCK:
            print(msg)
            
            
   def printFileWithLock(self,openPort,ipAddr):
        with self.LOCK:
            file = open("./Scan_" + str(ipAddr) + ".txt","a")
            file.write(str(ipAddr) + ":" + (str(openPort['Port_Number']) + " | " + openPort['Description'] + " | " + "Protocol: " + openPort['Transport_Protocol']) + "\n")
            file.close
        
        
   def __init__(self, threadId, ip_addr,ports_info):
      Thread.__init__(self)
      self.threadId = threadId
      self.ip_addr = ip_addr
      self.ports_info = ports_info
      
    

   def run(self):
       for el in self.ports_info:
        try:
            #Input Checker
            try:
                port_to_scan = int(el['Port_Number'])
            except ValueError:
                continue
            
            self.printWithLock(f"Scanning :  {self.ip_addr} : {port_to_scan} | Protocol: {el['Transport_Protocol']} | ThreadID: {self.threadId}")
            if(isPortOpen(self.ip_addr,port_to_scan)):
                self.OPEN_PORTS.append(el)
                self.printFileWithLock(el,self.ip_addr)
            
        except KeyboardInterrupt:
            print("Execution interrupted")
            break
    
from threading import *
from PyScanUtils import *

class PyScanThread (Thread):

   OPEN_PORTS = []
   LOCK = Lock()
    
   def printWithLock(self,msg):
        with self.LOCK:
            print(msg)
            
            

            
   def appendWithLock(self,el):
        with self.LOCK:
            self.OPEN_PORTS.append(el)
        
        
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
            
            self.printWithLock(f"Scanning :  {self.ip_addr} : {port_to_scan} | ThreadID: {self.threadId}")
            if(isPortOpen(self.ip_addr,port_to_scan)):
                self.appendWithLock(el)
            
        except KeyboardInterrupt:
            print("Execution interrupted")
            break
    
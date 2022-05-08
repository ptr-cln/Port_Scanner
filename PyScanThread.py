from threading import Thread
from PyScanUtils import *

class PyScanThread (Thread):

   OPEN_PORTS = []

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

            print(f"\nScanning :  {self.ip_addr} : {port_to_scan} | Protocol: {el['Transport_Protocol']} | ThreadID: {self.threadId}")
            if(isPortOpen(self.ip_addr,port_to_scan)):
                self.OPEN_PORTS.append(el)
                printFile(el,self.ip_addr)
            
        except KeyboardInterrupt:
            print("Execution interrupted")
            break
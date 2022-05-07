from threading import Thread
from PyScanUtils import *

class PyScanThread (Thread):

   def __init__(self, threadId, ip_addr,ports_info):
      Thread.__init__(self)
      self.threadId = threadId
      self.ip_addr = ip_addr
      self.ports_info = ports_info

      self.open_ports = []


   def run(self):
       for el in self.ports_info:
        try:
            #Input Checker
            try:
                port_to_scan = int(el['Port_Number'])
            except ValueError:
                continue

            print(f"Scanning :  {self.ip_addr} : {port_to_scan} | Protocol: {el['Transport_Protocol']} \n")
            if(isPortOpen(self.ip_addr,port_to_scan)):
                self.open_ports.append(el)
            
        except KeyboardInterrupt:
            print("Execution interrupted")
            break
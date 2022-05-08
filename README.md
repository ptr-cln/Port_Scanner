# Port Scanner
Hello there!<br>
This is a simple port scanner, written in <b>Python3</b>.<br>
It reads a json file that contains a lot of commonly used ports,then it will list what of those ports are open on a specific hostname (Given in input)<br><br>

It is multithread.<br>
It balances each thread charge dynamically at runtime.<br> 
For example, given 1000 ports to scan and 10 threads to use, it will assign 100 ports to scan for each thread.<br>
Given 5000 ports to scan and 20 threads to use, it will assign 250 ports to scan for each thread.<br>
I assume a different amount of ports to scan because you can edit <b>"Common_Used_Ports.json"</b> and let it scan only the ports you want<br>
You can change the amount of threads to use changing <b>"totalThreads"</b> in <b>"PyScanMain.py"</b><br>

![Alt text](https://raw.githubusercontent.com/ptr-cln/Port_Scanner/main/resources/screenshots/Screenshot.JPG)<br>


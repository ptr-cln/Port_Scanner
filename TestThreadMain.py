from random import randint
from PyScanThread import *

# Creazione dei thread
thread1 = PyScanThread("Thread#1", randint(1,20))
thread2 = PyScanThread("Thread#2", randint(1,20))
thread3 = PyScanThread("Thread#3", randint(1,20))
# Avvio dei thread
thread1.start()
thread2.start()
thread3.start()
# Join
thread1.join()
thread2.join()
thread3.join()
# Fine dello script
print("Fine")
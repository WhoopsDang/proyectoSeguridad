import threading
import time
from sensorHumedad_obj import sensorHumedad
from sensorTemperatura_obj import sensorTemperatura
from sensorMovimiento_obj import PIR
from sensorhumoyGas_obj import SmokeGasSensor
from Actuadores import Actuadores

def thread1():
    humedad = sensorHumedad(11)
    
    # execute script 1 here
    humedad.read()

def thread2():
    humo = SmokeGasSensor(18)

    # execute script 2 here
    humo.read()
        

def thread3():
    mov = PIR(23)
    while True:
        
        # execute script 3 here
        mov.connect()
        c = mov.read()
        if c == True:
            print(c)
        mov.disconnect()
        time.sleep(.5)
        
def thread4():
    temperatura = sensorTemperatura(11)
    temperatura.read()
    
def thread5():
    act = Actuadores()
    act.run()

# create threads for each script
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)
t3 = threading.Thread(target=thread3)
t4 = threading.Thread(target=thread4)
t5 = threading.Thread(target=thread5)

# start each thread
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

# wait for each thread to finish
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
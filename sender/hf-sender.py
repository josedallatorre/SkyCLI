from LoRaRaspberryPi import loralib                                                          
import time

loralib.init(0, 868000000, 7)

for i in range(0,10000000):
    loralib.send(b'hello%s',i)
    time.sleep(0.001)
from LoRaRaspberryPi import loralib                                                          
import time

loralib.init(0, 868000000, 7)

for i in range(0,1000):
    loralib.send(b'hello')
    time.sleep(0.001)
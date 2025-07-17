from LoRaRaspberryPi import loralib                                                          
import time

loralib.init(1, 868000000, 7)

for i in range(0,10000000):
  msg=loralib.recv()
  if msg[5] == 0 and msg[1] > 0:
    print(msg)
  time.sleep(0.001)
from LoRaRaspberryPi import loralib                                                          
import time

loralib.init(1, 868000000, 7)

for i in range(0,10000000):
  msg=loralib.recv()
  print("%06d, frame=" % i, end='')
  print(msg)
  time.sleep(1)
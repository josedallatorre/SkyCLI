from LoRaRaspberryPi import loralib                                                          
import time
from utils.logging import create_logger

loralib.init(0, 868000000, 7)
logger = create_logger('sender')

counter = [0, 0, 0]

for i in range(0,12000):
    temp = i
    #TODO: substitute the magic number with index of 
    #the list
    counter[0] = temp // (255**2)
    temp -= counter[0] * (255**2)
    counter[1] = temp // (255**1) 
    temp -= counter[1] * (255**1)
    counter[2] = temp 
    temp -= counter[2] 
    assert temp == 0
    print(counter, temp, i)
    loralib.send(b'counter:' + bytes(counter) + b': hello')
    logger.info(f"Sent message {i}: hello")
    time.sleep(0.01)
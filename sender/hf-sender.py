from LoRaRaspberryPi import loralib                                                          
import time
from utils.logging import create_logger

loralib.init(0, 868000000, 7)

logger = create_logger('hf-sender')

counter = [0, 0, 0]

for i in range(0,10000000):
    temp = i
    counter[2] = i // 255
    temp -= counter[2] * 255
    counter[1] = i // (255**2) 
    temp -= counter[1] * (255**2)
    counter[0] = i // (255**3)
    temp -= counter[0] * (255**3)
    loralib.send(b'counter:' + bytes(counter) + b': hello')
    logger.info(f"Sent message {i}: hello")
    time.sleep(0.001)
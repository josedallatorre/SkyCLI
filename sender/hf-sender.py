from LoRaRaspberryPi import loralib                                                          
import time
from utils.logging import create_logger

loralib.init(0, 868000000, 7)

logger = create_logger('hf-sender')

for i in range(0,10000000):
    loralib.send(f"{i}: hello".encode())
    logger.info(f"Sent message {i}: hello")
    time.sleep(0.001)
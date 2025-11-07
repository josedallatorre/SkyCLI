from LoRaRaspberryPi import loralib                                                          
import time
from utils.logging import create_logger

loralib.init(0, 868000000, 7)
logger = create_logger('sender')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

for i in range(0,10000000):
    loralib.send(f"{i}: hello".encode())
    logger.info(f"Sent message {i}: hello")
    time.sleep(1)
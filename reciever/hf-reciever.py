from LoRaRaspberryPi import loralib                                                          
import time
from utils.logging import create_logger

loralib.init(1, 868000000, 7)

logger = create_logger('hf-reciever')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

for i in range(0,10000000):
  msg=loralib.recv()
  if msg[5] == 0 and msg[1] > 0:
    print(msg)
  time.sleep(0.001)
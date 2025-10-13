from LoRaRaspberryPi import loralib                                                          
import time
from utils.logging import create_logger

loralib.init(1, 868000000, 7)
logger = create_logger('reciever')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

for i in range(0,10000000):
  msg=loralib.recv()
  print("%06d, frame=" % i, end='')
  print(msg)
  time.sleep(1)
from LoRaRaspberryPi import loralib                                                          
import time
from utils.logging import create_logger

loralib.init(1, 868000000, 7) #init LoRa in receiver mode, freq 868MHz, spread factor 7
logger = create_logger('hfreceiver')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

for i in range(0,10000000):
  msg=loralib.recv()
  # check if valid message received
  if msg[5] == 0:
    if msg[1] > 0:
      logger.info(f"valid msg: %s", msg)
    else:
      logger.info(f"empty msg: %s", msg)
  else:
    logger.warning(f"invalid msg: %s", msg)
  print(msg)
  time.sleep(0.001)
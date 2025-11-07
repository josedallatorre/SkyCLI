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
  # check if valid message received
  if msg[5] == 0:
    if msg[1] > 0:
      logger.info(f"Counter: {i}, valid msg: %s", msg)
      msg_str = msg[0].decode("utf-8", errors='ignore')
      x = msg_str.split(':')[1].split(':')[0]
      print(f"Counter value: {int.from_bytes(x.encode())}, {msg_str}, {x}")
    else:
      logger.info(f"Counter: {i}, empty msg: %s", msg)
  else:
    logger.warning(f"Counter: {i}, invalid msg: %s", msg)
  print("%06d, frame=" % i, end='')
  print(msg)
  time.sleep(0.01)
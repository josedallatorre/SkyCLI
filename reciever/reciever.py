from LoRaRaspberryPi import loralib                                                          
from datetime import datetime
import logging 
import time
from pathlib import Path

#create log directory
Path("./log/reciever").mkdir(exist_ok=True, parents=True)

#create logger
logger = logging.getLogger('reciever')
logger.setLevel(logging.DEBUG)


fh = logging.FileHandler(filename='./log/reciever/{:%Y-%m-%d}.log'.format(datetime.now()), mode='w')
fh.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(fh)
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

loralib.init(1, 868000000, 7)

for i in range(0,10000000):
  msg=loralib.recv()
  print("%06d, frame=" % i, end='')
  print(msg)
  time.sleep(1)
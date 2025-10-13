from LoRaRaspberryPi import loralib                                                          
import logging 
import time

#create logger
logging.basicConfig(filename='./log/%d-%m-%y.log', filemode='w')
logger = logging.getLogger('reciever')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
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
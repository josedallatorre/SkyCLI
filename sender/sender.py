from LoRaRaspberryPi import loralib                                                          
from utils.logging import create_logger

loralib.init(0, 868000000, 7)
logger = create_logger('sender')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

loralib.send(b'hello')
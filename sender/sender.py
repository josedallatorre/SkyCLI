from LoRaRaspberryPi import loralib
import time
from utils.logging import create_logger
from utils.conversion import toDigits

loralib.init(0, 868000000, 7)
logger = create_logger('sender')

for i in range(0,12000):
    temp = i
    # since lora send bytes of data we need to convert the counter to a list of digits in base 255
    digits = toDigits(temp, 255) 
    print(digits, temp, i)
    loralib.send(b'counter:' + bytes(digits) + b': hello')
    logger.info(f"Sent message {i} in digits {digits}: hello")
    time.sleep(0.01)
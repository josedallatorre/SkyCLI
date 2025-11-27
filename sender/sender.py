from LoRaRaspberryPi import loralib
import time
from utils.logging import create_logger
from utils.conversion import toDigits
import sys

loralib.init(0, 868000000, 7) # init LoRa in sender mode, freq 868MHz, spread factor 7
logger = create_logger('sender')

for i in range(0,12000):
    temp = i
    # since lora send bytes of data we need to convert the counter to a list of digits in base 255
    digits = toDigits(temp, 255) 
    print(digits, temp, i)
    msg = b'counter:' + bytes(digits) + b': hello'
    loralib.send(msg)
    print(sys.getsizeof(msg))
    logger.info(f"Sent message {i} in digits {digits} in bytes {bytes(digits)}: hello")
    time.sleep(0.01)
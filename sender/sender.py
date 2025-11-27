from LoRaRaspberryPi import loralib
import time
from utils.logging import create_logger
from utils.conversion import toDigits
from math import ceil
import sys

loralib.init(0, 868000000, 7) # init LoRa in sender mode, freq 868MHz, spread factor 7
logger = create_logger('sender')

def calculate_airtime(SF, BW, PL, H, DE, CR, n_preamble):
    Tsym = 2**SF / BW
    time_preamble = (n_preamble + 4.25)  * Tsym
    payloadSymbNb = 8 + max(ceil((8*PL - 4*SF + 28 + 16 - 20*H) / (4*(SF - 2*DE))) * (CR + 4), 0)
    time_payload = payloadSymbNb * Tsym
    time_packet = time_preamble + time_payload
    return time_packet

time_start = time.perf_counter()
time_elapsed = 0
i = 0
while(time_elapsed  < 120): # send for 2 minutes
    i += 1
    # since lora send bytes of data we need to convert the counter to a list of digits in base 255
    digits = toDigits(i, 255) 
    print(digits, i)
    msg = b'counter:' + bytes(digits) + b': hello'
    size_msg = sys.getsizeof(msg)
    airtime = calculate_airtime(SF=7, BW=125000, PL=size_msg, H=0, DE=0, CR=1, n_preamble=8)
    loralib.send(msg)
    logger.info(f"Sent message {i} in digits {digits} in bytes {bytes(digits)}: hello")
    time.sleep(airtime)
    time_elapsed = time.perf_counter() - time_start


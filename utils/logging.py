from datetime import datetime
import logging 
from pathlib import Path

# Function to create a logger
# communicator: str - name of the communicator (e.g., 'reciever', 'transmitter')
def create_logger(communicator: str):
  #create log directory
  path = "./log/{}".format(communicator)
  Path(path).mkdir(exist_ok=True, parents=True)

  #create logger
  logger = logging.getLogger(communicator)
  logger.setLevel(logging.DEBUG)

  fh = logging.FileHandler(filename='./log/{}/{:%Y-%m-%d}.log'.format(communicator, datetime.now()), mode='w')
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
  return logger
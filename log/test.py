import logging
import logging.handlers
import time

logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.handlers.TimedRotatingFileHandler(filename='log/123.log',when='M',interval=1)
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

while True:
# 'application' code
  logger.debug('debug message')
  
  time.sleep(1)

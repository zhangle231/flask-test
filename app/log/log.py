import logging
import logging.config
import yaml

#logging.config.fileConfig('logging.conf')

with open('logging.yaml','r') as f:
    log_cfg = yaml.safe_load(f.read())

logging.config.dictConfig(log_cfg)
'''
logging.basicConfig(
        format='%(asctime)s %(levelname)s %(module)s %(name)s:%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG)
'''

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch= logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('ch %(asctime)s %(name)s %(levelname)s: %(message)s')

ch.setFormatter(formatter)

logger.addHandler(ch)


logger.debug('123')
#logger.warning('is when this event was logged.')

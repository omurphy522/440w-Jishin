__author__ = 'owen'
import logging

logger = logging.getLogger('Jishin')
logger.setLevel(logging.DEBUG)
# create file handler which logs even info and more messages
ah = logging.FileHandler('..\Audit.log')
ah.setLevel(logging.INFO)
# create file handler which logs only Error and Critical messages
eh = logging.FileHandler('..\Error.log')
eh.setLevel(logging.ERROR)
# create console handler with a higher log level
# ch = logging.StreamHandler()
# ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ah.setFormatter(formatter)
eh.setFormatter(formatter)
# add the handlers to logger

logger.addHandler(ah)
logger.addHandler(eh)
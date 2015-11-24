import logging

# create logger with 'error_application'
logger = logging.getLogger('Jishin')
logger.setLevel(logging.DEBUG)

# create file handler which logs info and debug messages
fh = logging.FileHandler('/tmp/jishin/logging/Error.log')
fh.setLevel(logging.ERROR)
ch = logging.FileHandler('/tmp/jishin/logging/Audit.log')
ch.setLevel(logging.INFO)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)


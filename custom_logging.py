import logging

logger = logging.getLogger("testlogger")
logger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler(filename='advanced_logging.log')
fileHandler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

# adding formatter to consolehandle
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

logger.debug("This is debug message") # 10
logger.info("This is info message")   # 20
logger.warning("This is warning message") # 30
logger.error("This is error message")  # 40
logger.critical("This is critical message") # 50
#helps to understand flow of the program
#Debug, info, warning, error and critical
import logging

#to send all the logs to file
# to get the debug and info logs mention log level
logging.basicConfig(filename="test.log",format= '%(asctime)s: %(levelname)s: %(message)s',datefmt= '%m/%d/%Y %I:%M:%S %p')

logger= logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is a debug message")
logger.info("This is a info message")
logger.warning("This is a warning message")
logger.error("This is a error message")
logger.critical("This is a critical message")


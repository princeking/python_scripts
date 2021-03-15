import logging
import logging_example1
logger = logging.getLogger(__name__)

logger.setLevel(logging.WARNING)
file_handler = logging.FileHandler('test2.log')

format= "%(asctime)s : %(levelname)s: %(name)s: %(message)s"

formatter = logging.Formatter(format)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.warning("This is a warning from logging_example2.py")
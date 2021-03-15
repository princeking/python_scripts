import logging

logging.basicConfig(level = logging.DEBUG, filename='test.log',
                    filemode='w', format='%(asctime)s :: %(funcName)s :: %(lineno)d :: %(message)s')
#by default only warning, error, critical error are loged

def test():
    logging.debug("This is a debug message")
    logging.info("This is a info message")
    logging.warning("This is a warning")
    logging.error("This is a error")
    logging.critical("This is highly critical")

test()
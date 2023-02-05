import logging


# class Logger(object):

def logger():
    # level = logging.DEBUG,

    logging.basicConfig(
        filename="C:\\Users\\saurabhd\\PycharmProjects\\API_Automation_Practice\\api_framework\\src\\utilities\\app_1.log",
        filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # logging.basicConfig(filename="python.log",
    #                      format='%(asctime)s %(message)s',
    #                      filemode='w')

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    return logger
# logging.debug("This is debug message")
# logging.info("This is debug message")
# logging.warning("This is debug message")
# logging.error("This is debug message")
# logging.critical("This is debug message")

# log = Logger()
# log.logger_level()

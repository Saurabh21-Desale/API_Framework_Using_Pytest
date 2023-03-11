# import logging.config
#
#
# logging.config.fileConfig('logger.ini', disable_existing_loggers=False)
# logger = logging.getLogger('Logger')
#
# def test_hello():
#     logger.info("Hi")
import logging


#C:\\Users\\saurabhd\\pythonProject\\API_Framework_Using_Pytest\\api_framework\\src\\utilities\\
class Log():
    def custome_log(self, loglevel):

        #print(logging.__file__)
        logging.basicConfig(
            filename="python.log",
            format='%(asctime)s %(message)s',
            filemode='w')

        logger = logging.getLogger()
        logger.setLevel(loglevel)
        return logger

#return logger

#logger.info("this is demo")
#print(logging.__file__)
# Setting the threshold of logger to INFO
# logger.setLevel(logging.INFO)
# logging.info("this is demo")
# return logger

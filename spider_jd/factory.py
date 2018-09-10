
import logging

class logger_factory(object):

    def get_logger(self, clazz='spider_jd', filename='test.log'):
        LOGGER = logging.getLogger(clazz)
        LOGGER.setLevel(logging.DEBUG)

        fh = logging.FileHandler(filename, encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        formatter = logging.Formatter('【%(asctime)s】[%(name)s](%(levelname)s)：\r%(message)s \r\n')

        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        LOGGER.addHandler(fh)
        LOGGER.addHandler(ch)
        return LOGGER
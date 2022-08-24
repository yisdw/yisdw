import logging
import time
def logger():
    logger=logging.getLogger()
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        fromatter=logging.Formatter('%(asctime)s-%(filename)s-%(lineno)s-%(levelname)s-(Message)')
        fs=time.strftime('%Y%m%d')+'.log'
        console=logging.StreamHandler()
        files=logging.FileHandler(fs,encoding='utf-8')
        console.setFormatter(fromatter)
        files.setFormatter(fromatter)
        logger.addHandler(console)
        logger.addFilter(files)
        console.close()
        files.close()
    return logger

logger().info('可以')




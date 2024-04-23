import time
from functools import wraps

from logger.logger import LogFactory
logger = LogFactory('Utils')


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logger.info(f"Time taken to execute {func.__name__}: {elapsed_time:.6f} seconds")
        return result
    return wrapper

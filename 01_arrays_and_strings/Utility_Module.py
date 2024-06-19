''''
This class will define the utility modules.
'''
import logging as log
def utility_decorator(func):
    def wrapper(*args, **kwargs):
        log.info("-" * 60)
        log.info(f"Started {func.__name__} method")
        # store the inner function valuecd 
        value = func(*args, **kwargs)
        log.info(f"Ended {func.__name__} message")
        # return the inner func value 
        log.info("-" * 60)
        return value
    return wrapper

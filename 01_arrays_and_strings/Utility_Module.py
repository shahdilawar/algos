''''
This class will define the utility modules.
'''
import logging as log
def utility_decorator(func):
    def wrapper(*args, **kwargs):
        log.info("-" * 60)
        log.info(f"Started {func.__name__} method")
        value = func(*args, **kwargs)
        log.info(f"Ended {func.__name__} message")
        log.info("-" * 60)
        return value
    return wrapper

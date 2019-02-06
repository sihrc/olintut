import time
import random

from .utils import logger


@logger
def long_running_magic_number_generator():
    """
    Magical numbers are conjured through black magic
    """
    time.sleep(2)
    return random.random()


if __name__ == "__main__":
    magic_number = long_running_magic_number_generator()
    print(f"Generated magic number {magic_number}")
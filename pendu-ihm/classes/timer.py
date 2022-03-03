from time import time


def start_time():
    """
    Function used to get the time elapsed in seconds between the 1st January of 1970 and the current date
    :return: the time elapsed
    """
    start_timer = time()
    return start_timer


def get_time(time1, time2):
    """
    Function to get the time elapsed between 2 times
    :param time1: a time
    :param time2: a time
    :return: the time elapsed
    """
    return time2 - time1

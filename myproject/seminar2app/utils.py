import random
# from datetime import datetime as _dt
from datetime import timedelta


def get_random_date(start, end):
    delta = end - start
    return start + timedelta(random.randint(0, delta.days))





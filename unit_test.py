import unittest

class T:
    def __init__(self):
        self.x = 1.000


def add_x_and_k(x, k):
    if isinstance(x, str):
        return x + str(k)
    elif isinstance(x, int):
        return x + int(k)
    elif isinstance(x, float):
        return x + float(k)
    else:
        return "this would be an error"

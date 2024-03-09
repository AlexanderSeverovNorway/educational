import math


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self, a):
        self.a = a

    def get_area_square(self):
        return self.a ** 2


class Round:
    def __init__(self, R):
        self.R = R

    def get_area_round(self):
        math.pi = 3.14
        return math.pi * (self.R ** 2)

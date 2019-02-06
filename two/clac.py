import math

from two.point import Point


class Calc:

    @staticmethod
    def getDist(p1: Point, p2: Point)-> float:
        return math.sqrt(pow((p2.lon - p1.lon), 2) + (p2.lat - p2.lat) ** 2)
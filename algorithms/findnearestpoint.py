__author__ = 'tingxxu'
import math


class FindNearestPoint:

    def __init__(self):
        pass

    def normal(self, points):
        target1 = None
        target2 = None
        mini = 1000000000
        for index in range(0, len(points)-1):
            for index_inner in range(index+1, len(points)):
                dis = FindNearestPoint.distance(points[index], points[index_inner])
                if dis < mini:
                    mini = dis
                    target1 = points[index]
                    target2 = points[index_inner]

        return target1, target2


    def imporve(self, points):
        target1 = None
        target2 = None
        mini = 1000000000
        for index in range(0, len(points)-1):
            for index_inner in range(index+1, len(points)):
                dis = FindNearestPoint.distance(points[index], points[index_inner])
                if dis < mini:
                    mini = dis
                    target1 = points[index]
                    target2 = points[index_inner]

        return target1, target2

    @staticmethod
    def distance(point1, point2):
        return math.pow(point1.x - point2.x, 2) + math.pow(point1.y - point2.y, 2)

    @staticmethod
    def distance2(point1, point2):
        return abs(point1.x - point2.x) + abs(point1.y - point2.y)

    @staticmethod
    def print_method(name, result, cost):
        print("%s result is [(%d, %d),(%d, %d)], cost time is %s" % (name, result[0].x, result[0].y,
                                                                     result[1].x, result[1].y, cost))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

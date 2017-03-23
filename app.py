__author__ = 'tingxxu'

from algorithms.fibonaccipro import FibonacciPro
from algorithms.fibonacci import Fibonacci
from algorithms.findnearestpoint import FindNearestPoint, Point
from algorithms.sort import Sort
from algorithms.findsum import FindSum
from algorithms.findmaxchildren import FindMaxChildren
from algorithms.redundant import Redundant

from compare import compare, compare_pro, compare_times
import random

import timeit

def test_fib():
    test1 = Fibonacci()
    compare(50, Fibonacci.print_method, test1.improve, test1.improve2, test1.improve3, test1.improve5)


def test_nearest():
    test = FindNearestPoint()
    data = []
    for index in range(0, random.randint(4, 6)):
        point = Point(random.randint(0, 1000), random.randint(0, 1000))
        data.append(point)
        print("create point at (%d, %d) " % (point.x, point.y))

    compare(data, FindNearestPoint.print_method, test.normal, test.imporve)


def test_sort():
    test = Sort()
    data = []
    for index in range(0, random.randint(2000,3000)):
        point = random.randint(0, 1000)
        data.append(point)
        # print("create data at %d " % point)

    compare_pro(data, Sort.print_method, test.quick, test.bubble)


def test_find_sum():

    data = []
    for index in range(0, random.randint(20000, 20050)):
        point = random.randint(0, 10000)
        data.append(point)

    test = FindSum(10000)
    compare_pro(data, Sort.print_method, test.normal, test.improve)


def test_find_max_children():
    data = [1, -2, 3, 5, -3, 2]
    for index in range(0, random.randint(2000, 2050)):
        point = random.randint(-10000, 10000)
        data.append(point)
    test = FindMaxChildren()

    compare(data, FindMaxChildren.print_method, test.common, test.improve, test.improve2, test.improve3)

def test_redundant():
    data = []
    for index in range(0, random.randint(5, 7)):
        point = random.randint(0, 1000000)
        data.append(point)

    test = Redundant()

    compare_times(data, Redundant.print_method, 1000, test.common, test.brief, test.improve)

def test_n():
    from algorithms.less_than_n import LessThanN
    test = LessThanN(73, 32)
    compare(6600000, LessThanN.print_method, test.common, test.improve2, test.improve3)

if __name__ == '__main__':
    # test_fib()
    test_n()




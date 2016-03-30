__author__ = 'tingxxu'

from algorithms.fibonaccipro import FibonacciPro
from algorithms.fibonacci import Fibonacci

import datetime


def compare(parameter, *function_array):
    for function in function_array:
        start = datetime.datetime.now()
        print("function name is %s" % function.__name__)
        result = function(parameter)
        end = datetime.datetime.now()
        cost = end-start
        print("%s result is %f, cost time is %s" % (function.__name__, result, str(cost)))

if __name__ == '__main__':
    test1 = FibonacciPro(0.7, 2.53)

    compare(25, test1.common, test1.improve)
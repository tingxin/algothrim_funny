import datetime
import copy
import cProfile


def compare(parameter, print_method, *function_array):
    for function in function_array:
        start = datetime.datetime.now()
        result = function(parameter)
        end = datetime.datetime.now()
        cost = end-start
        print_method(function.__name__, result, str(cost))


def compare_pro(parameter, print_method, *function_array):
    for function in function_array:
        new_parameter = copy.copy(parameter)
        start = datetime.datetime.now()
        result = function(new_parameter)
        end = datetime.datetime.now()
        cost = end-start
        print_method(function.__name__, result, str(cost))

def compare_times(parameter, print_method, times, *function_array):
    for function in function_array:
        new_parameter = copy.copy(parameter)
        start = datetime.datetime.now()
        for index in range(0, times):
            result = function(new_parameter)
        end = datetime.datetime.now()
        cost = end-start
        print_method(function.__name__, result, str(cost))
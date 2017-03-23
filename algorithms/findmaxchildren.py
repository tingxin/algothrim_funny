__author__ = 'tingxxu'
import sys
sys.setrecursionlimit(100000)

class FindMaxChildren:

    def __init__(self):
        self.__start = []
        self.__Aii = []

    def common(self, input_array):
        count = len(input_array)
        max_number = -10000000
        for index in range(0, count-1):
            summary = 0
            for inner in range(index, count):
                summary += input_array[inner]
                if max_number < summary:
                    max_number = summary
        return max_number

    def __improve_outer(self, input_array, from_index, from_end):
        check = from_end - from_index
        if check > 1:
            split = (from_index + from_end)/2

            left = split-1

            test_number = input_array[split]
            cross_max = test_number

            while left >= from_index:
                test_number += input_array[left]
                left -= 1
                if test_number > cross_max:
                    cross_max = test_number

            right = split+1
            test_number = cross_max
            while right <= from_end:
                test_number += input_array[right]
                right += 1
                if test_number > cross_max:
                    cross_max = test_number

            left_value = self.__improve_outer(input_array, from_index, split)
            right_value = self.__improve_outer(input_array, split+1, from_end)
            max_number = max(left_value, right_value)

            return max(cross_max, max_number)

        elif check == 1:
            sum_number = input_array[from_end] + input_array[from_index]

            max_1 = max(input_array[from_end], input_array[from_index])
            max_2 = max(max_1, sum_number)
            return max_2
        else:
            return input_array[from_end]

    def improve(self, input_array):
        return self.__improve_outer(input_array, 0, len(input_array)-1)

    def improve2(self, input_array):
        count = len(input_array)

        start = input_array[count-1]

        input_max = input_array[count-1]

        index = count - 2
        while index >= 0:
            start = max(input_array[index], input_array[index] + start)
            input_max = max(start, input_max)
            index -= 1

        return input_max

    def improve3(self, input_array):

        max_number = input_array[0]
        start = input_array[0]
        for index in range(0, len(input_array)):
            start = max(input_array[index], input_array[index] + start)
            max_number = max(max_number, start)

        return max_number




    @staticmethod
    def print_method(name, result, cost):
        print("%s result is %s, cost time is %s" % (name, str(result), cost))

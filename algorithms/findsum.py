__author__ = 'tingxxu'
from sort import Sort

class FindSum:

    def __init__(self, number):
        self.number = number
        self.sorter = Sort()

    def normal(self, array):
        count = len(array)
        for index in range(0, count-1):
            for inner in range(index, count):
                if array[index] + array[inner] == self.number:
                    return array[index], array[inner]
        return None

    def improve(self, array):
        sort_array = self.sorter.quick(array)
        count = len(sort_array)
        start = 0
        end = count - 1
        while end > start:
            value = sort_array[start] + sort_array[end]
            if value > self.number:
                end -= 1
            elif value < self.number:
                start += 1
            else:
                return sort_array[start], sort_array[end]

        return None

    @staticmethod
    def print_method(name, result, cost):
        print("%s cost time is %s" % (name, cost))
        if result is None:
            print("can't find result")
        else:
            print(result)



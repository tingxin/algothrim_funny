__author__ = 'tingxxu'

import sys
import math
sys.setrecursionlimit(100000)

class Sort:

    def __init__(self):
        pass

    def bubble(self, input_array):
        count = len(input_array)
        for index in range(0, count - 1):
            for inner in range(index, count):
                if input_array[index] > input_array[inner]:
                   self.swap(input_array, index, inner)

        return input_array

    def quick(self, array):
        self.qsort(array, 0, len(array)-1)
        return array

    def qsort(self, arr, left, right):
        if right > left:
            pivot = right
            pivot_new = self.partition(arr, left, right, pivot)
            self.qsort(arr, left, pivot_new -1)
            self.qsort(arr, pivot_new + 1, right)

    def partition(self, array, left, right, pivot):
        pivot_value = array[pivot]
        self.swap(array, pivot, right)

        store_index = left
        for i in range(left, right):
            if array[i] <= pivot_value:
                if store_index != i:
                    self.swap(array, store_index, i)
                store_index += 1

        self.swap(array, right, store_index)
        return store_index

    def swap(self, array, index1, index2):
        temp = array[index1]
        array[index1] = array[index2]
        array[index2] = temp

    # def heap_sort(self, array):
    #     array_length = len(array)
    #     self.build_heap(array)
    #     for i in range(array_length-1, 0, -1):
    #         self.swap(array, 0, i)
    #         self.build_heap()
    #
    # def build_heap(self, array):
    #     array_length = len(array)
    #     last_dad = int(math.ceil(array_length/2.0)) - 1
    #     for i in range(last_dad, 0, -1):
    #         self.arrange_heap(array, i)
    #
    #
    # def arrange_heap(self, array, dad):
    #     son_one = dad * 2 + 1
    #     max_value_son = son_one
    #     while son_one <= len(array):
    #         son_two = son_one + 1
    #         if son_two <= len(array):
    #             if array[son_two] > array[son_one]:
    #                 max_value_son = son_two
    #         if array[dad] < array[max_value_son]:
    #             self.swap(array, dad, max_value_son)
    #             dad = max_value_son
    #             son_one = dad * 2 + 1
    #             max_value_son = son_one






    @staticmethod
    def print_method(name, result, cost):
        print("%s cost time is %s, result is:" % (name, cost))
        print(result)


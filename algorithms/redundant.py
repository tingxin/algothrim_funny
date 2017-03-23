__author__ = 'tingxxu'


class Redundant:

    def __init__(self):
        pass

    def common(self, input_array):
        result = []

        for item in input_array:
            if item not in result:
                result.append(item)

        return result

    def brief(self, input_array):
        return list(set(input_array))

    def improve(self, input_array):
        result = {}
        for item in input_array:
            result[item] = 0
        return result.keys()


    @staticmethod
    def print_method(name, result, cost):
        print("%s cost time is %s" % (name, cost))
        if result is None:
            print("can't find result")
        else:
            print(result)


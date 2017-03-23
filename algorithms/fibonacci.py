# ----------original-----------
# fn = fn-1 + fn-2


class Fibonacci:

    def __init__(self):
        self.global_map = {}
        self.global_map[0] = 0
        self.global_map[1] = 1

    def common(self, number):
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            return self.common(number-1) + self.common(number - 2)

    def improve(self, number):
        record = {}
        for i in range(0, number+1):
            if i == 0:
                record[i] = 0
            elif i == 1:
                record[i] = 1
            else:
                record[i] = record[i-1] + record[i-2]

        return record[number]

    def improve2(self, number):
        times = 0
        for i in range(0, number+1):
            for inner in range(0, number+1 - i):

                value = i + inner * 2
                if number - value == 1:
                    # print("%d and %d to %d ok" % (i, inner, value))
                    times += self.range(i, inner)
                elif number - value == 0:
                    # print("%d and %d to %d failed" % (i, inner, value))
                    pass
                elif number - value < 0:
                    break
        return times


    def steps(self, num):
        result = 1
        for i in range(1, num+1):
            result *= i
        return result

    def range(self, category1, category2):
        num1 = self.steps(category1 + category2)
        category1N = self.steps(category1)
        category2N = self.steps(category2)
        result = num1/category1N/category2N
        return result

    def improve_in_wiki(self, number):
        if number not in self.global_map:
            self.global_map[number] = self.improve_in_wiki(number - 1) + self.improve_in_wiki(number - 2)
        return self.global_map[number]

    def improve3(self, number):
        def fab_i(a, b, count):
            if count == 0:
                return b
            return fab_i(a + b, a, count - 1)

        return fab_i(1, 0, number)

    def improve5(self, number):
        t = (0, 1)
        for i in range(2, number + 1):
            t = (t[1], t[0] + t[1])
        return t[1]


    @staticmethod
    def print_method(name, result, cost):
        print("%s result is %s, cost time is %s" % (name, str(result), cost))
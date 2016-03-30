__author__ = 'tingxxu'
# fn= f(n-a)+f(n-b), a, b >0 and a, b can be float
# fn = 0 if n<=0 fn=1 if 0<n<=1


class FibonacciPro:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.global_map = {}
        self.global_map[0] = 1
        self.global_map[1] = 1
        self.limited = 1

    def common(self, number):
        if 0<number <=1:
            return 1
        elif number <= 0:
            return 0
        else:
            return self.common(number-self.a) + self.common(number - self.b)

    def improve(self, number):
        loop1 = int(number/self.a) + 1
        loop2 = int(number/self.b) + 1

        mini = min(min(self.a, self.b), self.limited)
        times = 0
        for index in range(0, loop1):
            for inn in range(0, loop2):
                value = number - index * self.a - inn * self.b
                if 0 < value <= mini:
                    # print("%d and %d to %d ok" % (index, inn, value))
                    times += self.range(index, inn)
                elif value <= 0:
                    # print("%d and %d to %d failed" % (index, inn, value))
                    pass
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
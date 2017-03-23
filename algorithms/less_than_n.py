import math
class LessThanN:

    def __init__(self, test_number1, test_number2):
        self.test_number_1 = test_number1
        self.test_number2 = test_number2

    def common(self, number):
        summary = 0
        for i in range(min(self.test_number_1, self.test_number2), number):
            if i % self.test_number_1 == 0 or i % self.test_number2 ==0:
                summary += i
        return summary


    def improve2(self, number):
        summary = 0
        multiple = [self.test_number_1, self.test_number2]
        min_test_number = min(self.test_number_1, self.test_number2)
        for mul in multiple:
            for index in range(1, number/min_test_number+1):
                test_number = mul * index
                if test_number >= number:
                    break
                summary += test_number
        min_multiple = self.get_min_multiple(self.test_number_1, self.test_number2)
        for index in range(1, number / min_multiple + 1):
            double_added_number = min_multiple * index
            summary -= double_added_number

        return summary

    def improve3(self, number):
        count_number_1 = int(math.floor(number/self.test_number_1))
        count_number_2 = int(math.floor(number/self.test_number2))
        min_multiple = self.get_min_multiple(self.test_number_1, self.test_number2)
        count_min_multiple = math.floor(number/min_multiple)
        return (self.test_number_1 * count_number_1 * (count_number_1 + 1) +
                self.test_number2 * count_number_2 * (count_number_2 + 1) -
                min_multiple * count_min_multiple * (count_min_multiple + 1)) / 2;

    def get_divisor(self, number1, number2):
        if number1 > number2:
            number1 -= number2
        elif number1 < number2:
            number2 -=  number1
        else:
            return number1
        return self.get_divisor(number1, number2)

    def get_min_multiple(self, num1, num2):
        divisor = self.get_divisor(num1, num2)
        return num1*num2 / divisor

    @staticmethod
    def print_method(name, result, cost):
        print("%s cost time is %s, result is:" % (name, cost))
        print(result)
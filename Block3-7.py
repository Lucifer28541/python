import math
import random


class Calculator():
    def plus(self, args, other):
        self.args = args
        self.other = other
        return self.args + self.other

    def minus(self, args, other):
        self.args = args
        self.other = other
        return args - self.other

    def mult(self, args, other):
        self.args = args
        self.other = other
        return args * self.other

    def div(self, args, other):
        self.args = args
        self.other = other
        return args / self.other

    def grade(self, args, other):
        self.args = args
        self.other = other
        return self.args ** self.other

    def factorial(self, args):
        self.args = args
        return math.factorial(self.args)

    def arccos(self, args):
        self.args = args
        return math.degrees(math.acos(self.args))


calc = Calculator()

g = 1
while g != 0:
    print("Введите произвольное число")
    a = float(input())

    b = 0
    while b != 1 and b != 2 and b != 3 and b != 4 and b != 5 and b != 6 and b != 7:
        print("\nВведите номер операции с числом\n")
        print(
            "1. +\n2. -\n3. *\n4. /\n5. Возведение в степень\n6. Вычислить факториал\n7. Вычислить Арккосинус - значение должно быть задано в диапазоне от -1 до 1 \n")
        b = int(input())
        y = b
        if b == 7:
            while a > 1 or a < -1:
                print("\nДля вычисления арккосинуса введите число в диапазоне от -1 до 1")
                a = float(input())
            continue
    c = 0
    if b != 6 and b != 7:
        while c != 1 and c != 2:
            print("\nВведите число: 1 - ваше число; 2 - рандомное число (1-100)")
            c = int(input())

    if c == 1:
        print("\nВведите произвольное число")
        d = float(input())
    if c == 2:
        print("\nРандомное число от 1 до 100")
        d = float(random.randint(1, 100))
        print(d, "\n")

    if b == 1:
        print("\n", a, '+', d, '=', (calc.plus(a, d)))

    if b == 2:
        print("\n", a, '-', d, '=', calc.minus(a, d))

    if b == 3:
        print("\n", a, '*', d, '=', calc.mult(a, d))

    if b == 4:
        print("\n", a, '/', d, '=', calc.div(a, d))

    if b == 5:
        print("\n", a, '^', d, '=', calc.grade(a, d))

    if b == 6:
        d = int(a)
        print("\nФакториал", a, "равен", calc.factorial(d))

    if b == 7:
        print("\nАрккосинус", a, "равен", calc.arccos(a), "градуса")

    print("\nХотите завершить?: 0 - Да; \nНачать сначала: любая клавиша + Enter\n")
    g = int(input())
    continue
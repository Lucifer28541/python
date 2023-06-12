print("Введите 3 произвольных слова")
print("Первое слово:")
a1 = str(input())
print("\nВторое слово:")
a2 = str(input())
print("\nТретье слово:")
a3 = str(input())
string = a1 + ' ' + a2 + ' ' + a3

allwds = string.lower()
print("\nВывод слов в нижнем регистре:")
print(allwds)
allwds = string.upper()
print("\nВывод слов в Верхнем регистре:")
print(allwds)
allwds = string.title()
print("\nВыводим первый символ в верхнем регистре:")
print(allwds)

print("\nВведите количество для:")
print("", a1, ":")
b1 = int(input())
print("\n", a2, ":")
b2 = int(input())
print("\n", a3, ":")
b3 = int(input())
print('Овощей всего: {0} - {3}шт.; {1} - {4}шт.; {2} - {5}шт.\n'.format(a1.title(), a2.title(), a3.title(), b1, b2, b3))



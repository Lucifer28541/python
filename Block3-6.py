def first(**test): return test
first = input("Введите список слов через запятую: ").split(",")
first_set = set(first)
print("Количество слов:", len(first))

def second(**test): return test
second = input("Введите второй список с тем же количеством слов через запятую: ").split(",")

dictionary = dict(zip(first_set, second))
print(dictionary)

# Задача_1

def my_func(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "y не может быть 0"
    except ValueError:
        return "Введите цифру"


print(my_func(int(input("Введите число x = ")), int(input("Введите число y = "))))

print('___________')


# Задача_3

def my_func(x, y, z):
    sequence = [x, y, z]
    total = []
    max_1 = max(sequence)
    total.append(max_1)
    sequence.remove(max_1)
    max_2 = max(sequence)
    total.append(max_2)
    print(sum(total))


my_func(-7, 4, 2)

print('___________')


# Задача_5

import sys

result = 0
while True:
    line = input("Введите числа через пробел: ")
    tokens = line.split(" ")
    for token in tokens:
        try:
            number = float(token)
            result += number
        except:
            if token == 'q':
                print(f"Сумма равна {result}. Завершение")
                exit(0)
            else:
                print(f"Сумма равна {result}. Ошибка ввода", file=sys.stderr)
                exit(1)

print('___________')
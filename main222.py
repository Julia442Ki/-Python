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
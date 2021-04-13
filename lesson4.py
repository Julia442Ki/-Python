# Задача_1

def simple_calc():
    x = float(input('Введите количество отработанных часов : '))
    y = float(input('Введите сумму оплаты труда за 1 час : '))
    c = float(input('Укажите размер премии - '))
    pay = x * y
    return pay + c
print(f'Размер заработной платы составил: {simple_calc() }')

print('___________')

# Задача_2

my_list = [4, 222, 17, 4, 1, 2, 42, 7, 14, 4, 24]
new = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new)

print('___________')

# Задача_3

numbers = range(20, 241)
new_list = [el for el in numbers if el%20==0 or el%21==0]
print(new_list)

print('___________')

# Задача_4

my_list = [11, 24, 24, 33, 40, 1, 1, 4]
new = [el for el in my_list if my_list.count(el)==1]
print(new)

print('___________')

# Задача_5

from functools import reduce
my_list = [el for el in range(100, 1000) if el % 2 == 0]
def my_func(prev_el, el):
    return prev_el * el

print(reduce(my_func, my_list))

print('___________')

# Задача_7

def fibo_gen(number):
    count = 1
    while count <= number:
        yield count
        count += 1
i = 1
my_fifteen = []
for el in fibo_gen(5):
    if i > 15:
        break
    else:
        my_fifteen.append(el)
        i += 1
print(my_fifteen)

print('___________')
# Задача_1

my_int = 5
my_float = 1.2
my_str = "Hello World"
my_list = ['a', '4']
my_tuple = ('b', '7')
my_dict = {'город': 'Москва', 'страна': 'Россия'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')

print('___________')

# Задача_2

my_list = ['2', '5', '4', '7', '9']
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = el
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
print(my_list)

print('___________')

# Задача_3

number = int(input("Введите число месяца: "))
if number <= 12 and number >= 1:
    month_dict = {1: 'Январь',
                  2: 'Февраль',
                  3: 'Март',
                  4: 'Апрель',
                  5: 'Май',
                  6: 'Июнь',
                  7: 'Июль',
                  8: 'Август',
                  9: 'Сентябрь',
                  10: 'Октябрь',
                  11: 'Ноябрь',
                  12: 'Декабрь'}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == number-1:
            print(f"Месяц: {month_list[i]}")
            break
    print(f"Месяц: {month_dict[number]}")
else:
    print("К сожалению, вы допустили ошибку. Попробуйте ещё раз.")

print('___________')

# Задача_4

my_str = input("Введите текст: ")
a = my_str.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")

print('___________')

# Задача_5

number = int(input("Введите число: "))
my_list = [7, 4, 4, 3, 2]
c = my_list.count(number)
for element in my_list:
    if c > 0:
        i = my_list.index(number)
        my_list.insert(i+c, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)

print('___________')
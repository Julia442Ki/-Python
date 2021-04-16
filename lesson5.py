# Задача_1

my_list = []
while True:
    line = input("Введите данные: ")
    if line == '':
        print(my_list)
        exit()
    else:
        newline = line + '\n'
        my_list.append(newline)

    with open("test_1.txt", "w") as file_obj:
        file_obj.writelines(my_list)

print('___________')

# Задача_3

firm = {'Харрисон': 40, 'Хэтфилд': 19, 'Меркури': 17, 'Джексон': 15, 'Плант': 25}
try:
    file_obj = open("test_3.txt", 'w')
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка")
finally:
    file_obj.close()
summa = 0
count = 0
persons = []
with open("test_3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 20:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"persons: {persons}")
print(f"averate: {result}")

print('___________')

# Задача_4

translater = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []
result = []
try:
    file_obj = open("test_4_output.txt", 'r')
    for line in file_obj:
        tokens = line.split(" - ")
        print(tokens)
        if tokens[0] in translater:
            word = translater[tokens[0]]
            result.append(word +' - '+ tokens[1])
    print(result)
except IOError:
    print("Ошибка ввода-вывода")
finally:
    file_obj.close()

try:
    file_input = open("test_4_input.txt", "w")
    file_input.writelines(result)
except IOError:
    print("Ошибка ввода-вывода")
finally:
    file_input.close()

print('___________')

# Задача_5

def summary():
    try:
        with open('file_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()

print('___________')

# Задача_6

subj = {}
with open('file_6.txt', 'r') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
print(f'Общее количество часов по предмету - \n {subj}')

print('___________')

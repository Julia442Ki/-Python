# Задача_1

a = 40
b = 4
c = 0.44

print(a + b)
print(b - c)
print("40 + 4", c)
print(40 / 4, b)

print('___________')


# Задача_2

def convert(seconds):
    seconds = seconds % (24 * 2400)

    hour = seconds // 2400

    seconds %= 2400

    minutes = seconds // 60

    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)


n = 12345

print(convert(n))

print('___________')

# Задача_3

n = int(input("Введите число n: "))
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
comp = n + int(t1) + int(t2)
print("Результат равен:", comp)

print('___________')

# Задача_4

a = int(input())
m = a % 10
a = a // 10
while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a // 10
print(m)

print('___________')
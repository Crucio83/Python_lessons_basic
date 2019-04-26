from random import randint

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):

    row_fib = []
    a, b = 0, 1
    for num in range(m):
        row_fib.append(b)
        a, b = b, a + b
    print(row_fib)

    n -= 1
    return ([row_fib[i] for i in range(n, m)])

print("-"*3 , "задачка №1", "-"*3)
print(fibonacci(1, 5))
print(fibonacci(75, 80))
print(fibonacci(15, 20))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
#

def sort_to_max_bubble(origin_list):
    for i in range(len(origin_list) - 1):
        for j in range(len(origin_list) - i - 1):
            if origin_list[j] > origin_list[j + 1]:
                buff = origin_list[j]
                origin_list[j] = origin_list[j + 1]
                origin_list[j + 1] = buff


a = [randint(-100, 100) for i in range(15)]

print("-"*3 , "задачка №2", "-"*3)
print(a)
sort_to_max_bubble(a)
print(a)


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def custom_filter(flt, itr):

    new_itr = [index for index in itr if flt(index)]
    return new_itr


lst = [randint(-100, 100) for j in range(15)]


print("-"*3 , "задачка №3", "-"*3)
print(lst)
print(custom_filter(lambda x: x > 50, lst))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def check_parall(a, b, c, d):

    check1 = False
    check2 = False

    # Противополжные стороны параллельны и равны

    ab = ((b[0] - a[0])**2 + (b[1] - a[1])**2)**0.5
    bc = ((b[0] - c[0])**2 + (b[1] - c[1])**2)**0.5
    cd = ((d[0] - c[0])**2 + (d[1] - c[1])**2)**0.5
    ad = ((d[0] - a[0])**2 + (d[1] - a[1])**2)**0.5
    if ab == cd and bc == ad:
        check1 = True

    # Диагонали O1 и O2 в точках пересечения делятся пополам и равны

    O1 = ((a[0] + c[0])/2, (a[1] + c[1])/2)
    O2 = ((b[0] + d[0])/2, (b[1] + d[1])/2)

    if O1 == O2:
        check2 = True

    if check1 and check2:
        print('Вершины A1{}, A2{}, A3{}, A4{}\n являются вершинами параллелограмма' .format(a, b, c, d))
    else:
        print('Вершины A1{}, A2{}, A3{}, A4{}\n НЕ образуют параллелограмм'.format(a, b, c, d))


print("-"*3 , "задачка №4", "-"*3)
A, B, C, D = (-9, 0), (-3, 6), (3, 4), (6, -3)
check_parall(A, B, C, D)

A, B, C, D = (-4, -2), (-3, 2), (7, -1), (6, -5)
check_parall(A, B, C, D)



# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]

max_len = 0
for item in fruits:
    if len(item) > max_len:
        max_len = len(item)

for i in range(len(fruits)):
    print('{}. {}'.format(i+1, fruits[i].rjust(max_len, ' ')))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

from random import randint
lst1 = [randint(-10, 10) for i in range(10)]
lst2 = [randint(-10, 10) for i in range(5)]

print(lst1)
print(lst2)

lst1 = [item for item in lst1 if item not in lst2]

print(lst1)
print(lst2)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

lst1 = [randint(0, 100) for i in range(15)]
print(lst1)
lst2 = []
for item in lst1:
    if (item % 2 == 0):
        lst2.append(item / 4)
    else:
        lst2.append(item * 2)

print(lst2)
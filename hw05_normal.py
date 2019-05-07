# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import commands

def menu():
    print('Выберете действие (1-4) или выход из программы "q":')
    print('1 - Перейти в папку')
    print('2 - Просмотреть содержимое текущей папки')
    print('3 - Удалить папку')
    print('4 - Создать папку')
    print('q - Выход из программы')
    action = input()
    return action


def processing(action):
    if action == 'q':
        print('Выход из программы')
        return
    action_item = {
        '1': commands.change_dir,
        '2': commands.dir_list,
        '3': commands.del_dir,
        '4': commands.make_dir
        }
    item = None
    try:
        item = int(action)
        if item in range(1,5):
            for item, key in action_item.items():
                if item == action:
                    key()
        else:
            print(f'{action} - некорректная команда!')

    except ValueError:
        print(f"{action} - некорректная команда!")

    answer = input('Продолжить работу с программой?\n"y" - Да: ')

    processing(menu()) if answer == 'y' else processing('q')


processing(menu())

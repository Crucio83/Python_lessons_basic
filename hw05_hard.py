# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import shutil

print('INFO: ', sys.argv)
print(os.getcwd())

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создание копии указанного файла")
    print("rm <file_name> - удаление указанного файла")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")
    print("files - содержимое текущей папки")


def make_dir():
    if not second_argument:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), second_argument)
    try:
        os.mkdir(dir_path)
        print(f'директория {second_argument} создана')
    except FileExistsError:
        print(f'директория {second_argument} уже существует')


def ping():
    print("pong")

def copy_file():
    if not second_argument:
        print("Необходимо указать имя копируемого файла вторым параметром")
        return

    fileToCopy = second_argument.split('.py').pop(0) + '_copy.py'
    curent_path_file = os.path.join(os.getcwd(), second_argument)
    copy_path_file = os.path.join(os.getcwd(), fileToCopy)

    try:
        if os.path.isfile(copy_path_file) == False:
            shutil.copy(curent_path_file, copy_path_file)
            print(f'Файл: {copy_path_file} скопирован!')
        else:
            print(f'Копия файла: {copy_path_file} уже существует!')
    except FileNotFoundError:
        print(f'файл {second_argument} не найден!')

def remove_file():
    if not second_argument:
        print("Необходимо указать имя удаляемого файла вторым параметром")
        return
    answer = input(f'Вы действительно хотите удалить {second_argument}\n? y/n:')

    if answer == 'y':
        rm_file_path = os.path.join(os.getcwd(), second_argument)
        try:
            os.remove(rm_file_path)
            print(f'Файл {second_argument} успешно удалён')
        except WindowsError:
            print(f'Невозможно удалить файл {second_argument}! Файла не существует')

def change_dir():
    if not second_argument:
        print("Необходимо указать полный или относительный путь к необходимой директории вторым параметром")
        return

    if os.path.exists(second_argument):
        new_cwd = second_argument
    else:
        new_cwd = os.path.join(os.getcwd(), second_argument)

    try:
        print("Текущая директория = ", os.getcwd())
        os.chdir(new_cwd)
        print(f'Директория изменена на {os.getcwd()}')
    except WindowsError:
        print(f'Директория {new_cwd} не найдена!')

def full_path():
    path = os.path.realpath(os.getcwd())
    print(f'Полный путь:{path}')


def list_files():
    list_dir = os.listdir(os.getcwd())
    print(f"содержимое текущей папки: {list_dir}")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": full_path,
    "files": list_files
}

try:
    second_argument = sys.argv[2]
except IndexError:
    second_argument = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

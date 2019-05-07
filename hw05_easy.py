import os
import sys
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

for i in range(9):
    dir_path = os.path.join(os.getcwd(), 'dir_'+ str(i+1))
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print(f'Такая директория {dir_path} уже существует')

for i in range(9):
    dir_path = os.path.join(os.getcwd(), 'dir_'+ str(i+1))
    try:
        os.removedirs(dir_path)
    except FileNotFoundError:
        print(f'Такая директория {dir_path} НЕ существует')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

folders = [file for file in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(), file))]
print(folders)

# Задача-3
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


if os.path.isfile(os.path.realpath(__file__) + '.copy') == False:
    shutil.copy(os.path.realpath(__file__), os.path.realpath(__file__) + '.copy')
    print(f'Файл скопирован: {os.path.realpath(__file__)}')
else:
    print(f'Копия файла: {os.path.realpath(__file__)} уже существует!')

# или так...

file_name =os.path.realpath(__file__)
fileToCopy = file_name.split('.py').pop(0) + '_copy.py'


if os.path.isfile(fileToCopy) == False:
    shutil.copy(file_name, fileToCopy)
    print(f'Файл: {fileToCopy} скопирован!')
else:
    print(f'Копия файла: {fileToCopy} уже существует!')


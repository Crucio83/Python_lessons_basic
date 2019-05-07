import os

def dir_list():

    # Функция для вывода списка файлов в текущей директории

    list_dir = os.listdir(os.getcwd())
    print(list_dir)


def change_dir():

    # Функция смены директории
    # исходный каталог

    print("Текущая директория = ", os.getcwd())
    result = input('Для перехода на уровень выше, введите "+", иначе введите название папки, куда следует перейти\n')

    if result == "+":
        new_cwd = (os.getcwd().split('\\') if os.name == 'nt' else os.getcwd().split('/'))
        new_cwd.pop() #убираем последнюю папку
        new_cwd = ('\\'.join(new_cwd) if os.name == 'nt' else '/'.join(new_cwd)) #склеиваем новый путь
    else:
        new_cwd = os.path.join(os.getcwd(), result)

    try:
        os.chdir(new_cwd)
        print(f'Директория изменена на {new_cwd}')
    except WindowsError:
        print(f'Директория {new_cwd} не найдена!')


def make_dir():
    # Функция для создания директории
    name_dir = input('Введите название новой Директории(папки):\n')
    cur_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.mkdir(cur_path)
        print(f'Директория(папка){name_dir} успешно создана!')
    except WindowsError:
        print(f'Директория(папка) с именем {name_dir} уже существует!')


def del_dir():
    # Функция для удаления директории
    name_dir = input('Введите название Директории(папки) для удаления:\n')
    cur_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.removedirs(cur_path)
        print(f'Директория(папка) {name_dir} успешно удалена')
    except WindowsError:
        print(f'Не удаётся найти Директорию(папку) {name_dir}')



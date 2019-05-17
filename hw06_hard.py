# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

class Person:
    def __init__(self, string):
        self._full_name = {
            'name': string.split()[0],
            'last_name': string.split()[1]
        }

    @property
    def get_full_name(self):
        return self._full_name['name'] + ' ' + self._full_name['last_name']


class Person_Card(Person):
    def __init__(self, string):
        Person.__init__(self, string)
        self._data = {
            'cash': string.split()[2],
            'job': string.split()[3],
            'norm': string.split()[4],
            'real_cash': None
        }

    @property
    def get_card(self):
        return self._data

    def get_real_cash(self):
        return self._data['real_cash']


class Person_Work(Person):
    def __init__(self, string):
        Person.__init__(self, string)
        self._fact_work = {
            'worked': string.split()[2]
            }

    @property
    def get_fact_work(self):
        return self._fact_work


def parse_file(file, obj):
    # Возвращает список из объектов, из каждой строки файла
    with open(file, encoding='UTF-8') as lister:
        elems = [obj(elem) for elem in lister][1:]
        return elems


def join_tab(elems1, elems2):
    # Общий объект из соответсвующих друг другу объектов из двух списков

    join_obj = [elems for elems in elems1]
    for elem in join_obj:
        for el in elems2:
            if elem.get_full_name == el.get_full_name:
                elem.get_card.update(el.get_fact_work)
    return join_obj



def string_result(res):
    # Вывод результата
    return '{0:<16} {1} руб.'.format(res.get('name'), res.get('real_cash'))


def res_pay(obj):
    # словарь с именем и расчётом по сотруднику

    cash = float(obj.get_card['cash'])  # зарплата
    norm = float(obj.get_card['norm'])  # норма
    worked = float(obj.get_card['worked'])  # отработано
    norm_cash_h = cash / norm  # норма в час

    obj.get_card['real_cash'] = round(norm_cash_h * worked if
                                      norm > worked else
                                      cash + (worked - norm) * (norm_cash_h * 2), 2)

    return {'name': obj.get_full_name,
            'real_cash': obj.get_real_cash()
            }


workers = parse_file('workers.txt', Person_Card)
fact = parse_file('hourse_of.txt', Person_Work)
workers_cash = list(map(res_pay, join_tab(workers, fact)))

print('РАСЧЁТ СОТРУДНИКОВ:')
print('\n'.join(list(map(string_result, workers_cash))))

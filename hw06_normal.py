# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class School:
    def __init__(self, school_name, teachers, students):
        self.school_name = school_name
        self.teachers = teachers
        self.students = students

    def get_all_classes(self):
        classes = set([student.get_class_room for student in self.students])
        return list(sorted(classes, key=lambda x: int(x[:-1])))

    def get_students(self, class_room):
        return [student.get_short_name for student in self.students if
                class_room == student.get_class_room]

    def get_teachers(self, class_room):
        return [teacher.get_short_name for teacher in self.teachers if
                class_room in teacher.get_classes]

    def find_student(self, student_full_name):
        for person in self.students:
            if student_full_name == person.get_full_name:
                Xteachers = [teachers.get_short_name for teachers in
                            self.teachers if person.get_class_room in
                            teachers.get_classes]
                Xlessons = [teachers.get_courses for teachers in
                           self.teachers if person.get_class_room in
                           teachers.get_classes]
                Xparents = person.get_parents

                return {
                    'full_name': student_full_name,
                    'class_room': person.get_class_room,
                    'teachers': Xteachers,
                    'lessons': Xlessons,
                    'parents': Xparents
                }

    @property
    def name(self):
        return self.school_name



class People:
    def __init__(self, last_name, first_name, middle_name):
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name

    @property
    def get_full_name(self):
        return '{0} {1} {2}'.format(self._last_name,
                                    self._first_name,
                                    self._middle_name)

    @property
    def get_short_name(self):
        return '{0} {1}.{2}.'.format(self._last_name,
                                     self._first_name[:1],
                                     self._middle_name[:1])


class Student(People):
    def __init__(self, last_name, first_name, middle_name, class_room, mather, father):
        People.__init__(self, last_name, first_name, middle_name)
        self.class_room = class_room
        self.parents = {
            'mather': mather,
            'father': father
            }

    @property
    def get_class_room(self):
        return self.class_room

    @property
    def get_parents(self):
        return self.parents


class Teacher(People):
    def __init__(self, last_name, first_name, middle_name,
                 courses, classes):
        People.__init__(self, last_name, first_name, middle_name)
        self._courses = courses
        self._classes = classes

    @property
    def get_courses(self):
        return self._courses

    @property
    def get_classes(self):
        return self._classes


list_teachers = [
    Teacher('Пажинская','Арина','Михаиловна','Алгебра', ['9В', '7А', '8А', '11Б', '6Г']),
    Teacher('Бернацкая','Полина','Никитична','Геометрия', ['9Б', '11А', '8В', '10А']),
    Teacher('Разумовская','Ольга','Матвеевна','Русский язык', ['8В', '7А', '10Б', '10В', '11Г', '6Г', '5В']),
    Teacher('Березина','Юлия','Романовна','Литература', ['11Г', '10Г', '11В', '9А', '8Б', '11В', '9А', '9Г']),
    Teacher('Бестужев','Петр','Егорович','Биология', ['10А', '10В', '8Б', '6А', '10Б']),
    Teacher('Вишневецкий','Арсений','Александрович','Информатика', ['9А', '6Г', '6Б']),
    Teacher('Воронина','Виктория','Ивановна','История', ['7Б', '6В']),
    Teacher('Воронцова','Елизавета','Денисовна','География', ['6Б', '6А', '7Г', '9В', '9Б']),
    Teacher('Булгакова','Ксения','Петровна','Химия', ['7Б', '8В', '5Г', '5А']),
    Teacher('Островская','Алиса','Тимофеевна','ОБЖ', ['6В', '5Б', '5Г'])
]

list_students = [
    Student('Андреев','Егор','Борисович','9В','Андреев Б.Р.','Андреевa В.P.'),
    Student('Захаров','Дмитрий','Владимирович','5В','Захаров В.В.','Захаровa Б.Ф.'),
    Student('Соловьев','Даниил','Вадимович','8Б','Соловьев В.Ч.','Соловьевa К.М.'),
    Student('Смирнов','Александр','Анатольевич','11А','Смирнов А.К.','Смирновa Н.Н.'),
    Student('Кузьмин','Руслан','Богданович','8А','Кузьмин Б.Г.','Кузьминa Р.Ж.'),
    Student('Федоров','Евгений','Георгиевич','9Г','Федоров Г.Г.','Федоровa Б.У.'),
    Student('Волков','Иван','Вячеславович','8Г','Волков В.М.','Волковa Б.В.'),
    Student('Смирнов','Денис','Александрович','10А','Смирнов А.К.','Смирновa К.Б.'),
    Student('Петров','Владислав','Анатольевич','7Г','Петров А.П.','Петровa Ч.М.'),
    Student('Сергеев','Владимир','Васильевич','11В','Сергеев В.М.','Сергеевa К.Б.'),
    Student('Степанов','Павел','Богданович','8Г','Степанов Б.М.','Степановa Н.С.'),
    Student('Сергеев','Владислав','Андреевич','11Г','Сергеев А.К.','Сергеевa К.П.'),
    Student('Новиков','Игорь','Борисович','8А','Новиков Б.Н.','Новиковa В.Д.'),
    Student('Егоров','Никита','Евгеньевич','11В','Егоров Е.Н.','Егоровa И.И.'),
    Student('Попов','Максим','Афанасьевич','5Г','Попов А.Ц.','Поповa М.Я.'),
    Student('Смирнов','Евгений','Арсеньевич','10Б','Смирнов А.Ц.','Смирновa С.А.'),
    Student('Андреев','Даниил','Борисович','5А','Андреев Б.В.','Андреевa С.М.'),
    Student('Павлов','Тимофей','Антонович','9Б','Павлов А.С.','Павловa Б.С.'),
    Student('Соловьев','Евгений','Емельянович','10А','Соловьев Е.У.','Соловьевa Р.М.'),
    Student('Федоров','Егор','Арсеньевич','9Б','Федоров А.А.','Федоровa З.П.'),
    Student('Никитин','Максим','Иванович','11Г','Никитин И.С.','Никитинa Ч.М.'),
    Student('Кузнецов','Павел','Данилович','8Г','Кузнецов Д.М.','Кузнецовa М.Б.'),
    Student('Воробьев','Игорь','Глебович','8А','Воробьев Г.Б.','Воробьевa С.Б.'),
    Student('Смирнов','Владислав','Гаврилович','9В','Смирнов Г.М.','Смирновa П.В.'),
    Student('Николаев','Игорь','Ефимович','10Г','Николаев Е.Н.','Николаевa М.Н.'),
    Student('Соловьев','Тимофей','Афанасьевич','10Г','Соловьев А.П.','Соловьевa О.Н.'),
    Student('Андреев','Матвей','Денисович','6Б','Андреев Д.Ф.','Андреевa А.А.'),
    Student('Макаров','Даниил','Васильевич','9А','Макаров В.Ц.','Макаровa О.К.'),
    Student('Смирнов','Евгений','Афанасьевич','6А','Смирнов А.И.','Смирновa З.А.'),
    Student('Попов','Владимир','Антонович','7Г','Попов А.Ч.','Поповa В.Ф.')
]


school = School('Гимназия №1', list_teachers, list_students)

print(school.name)
print('\n1. Полный список всех классов школы:\n', ', '.join(school.get_all_classes()))
print('\n2. Список всех учеников в классе "8Г":\n')
print('\n'.join(school.get_students('8Г')))
print('\n3&4. Cписок всех предметов ученика Попов Максим Афанасьевич:\n')

XStudent = school.find_student('Попов Максим Афанасьевич')

print('Ученик: {0}\nУчебный класс: "{1}"\n'
      'Учителя: {2}\nПредметы: {3}\n'
      'Родители: {4}, {5}'.format(XStudent['full_name'],
                            XStudent['class_room'],
                            ', '.join(XStudent['teachers']),
                            ', '.join(XStudent['lessons']),
                                 XStudent['parents']['mather'],
                                 XStudent['parents']['father']))

print('\n5. Cписок всех Учителей, преподающих в 11Г классе:\n', '{0}'.format(', '.join(school.get_teachers('11Г'))))



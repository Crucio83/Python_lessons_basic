import re

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
#
line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'
#---------------------------
pattern = re.compile('([a-z]+)[A-Z]|[A-Z]([a-z]+)')
found = [''.join(item) for item in pattern.findall(line)]
print("-"*3, "задачка №1", "-"*3, "\nСпособ с re:\nСимволы в нижнем регистре, которые находятся вокруг 1 или более символов в верхнем регистре\n" , found)

#---------------------------
CapLetters = list(map(lambda x: chr(x), list(range(65, 91))))  # из chr выбираем заглавные буквы в список
line_new = list(line)       # из строки делаем список

for i, element in enumerate(line_new[:]):
       for let in CapLetters:
              if element == let:
                     line_new[i] = ' '    #если нашли заглавную - зануляем

# соединяем буквы
line_new = ''.join(line_new).split(' ')
# убираем пустоты
found2 = [i for i in line_new if i != '']

print("-"*3, "задачка №1", "-"*3, "\nСпособ БЕЗ re:\nСимволы в нижнем регистре, которые находятся вокруг 1 или более символов в верхнем регистре\n" , found2)

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'
#---------------------------
pattern = re.compile('[a-z]{2}([A-Z]+)[A-Z]{2}')
found = [''.join(item) for item in pattern.findall(line_2)]
print("-"*3, "задачка №2", "-"*3, "\nСпособ с re\nСимволы в верхнем регистре, слева от которых находятся  \ "
                                  "два символа в нижнем регистре, а справа - два символа в верхнем регистре\n" , found)

#---------------------------

CapLetters = list(map(lambda x: chr(x), list(range(65, 91))))  # Преобразуем список из кодов ANSI в список букв A-Z
lowLetter = list(map(lambda x: chr(x), list(range(97, 123))))  # Преобразуем список из кодов ANSI в список букв a-z
line_new = list(line_2)

lst = []
i = len(line_new) - 1
# бежим в обратном порядке
while i >= 0:
       if line_new[i] in lowLetter:
              lst.append(line_new[i])
       elif line_new[i] in CapLetters and i <= len(line_new) - 3 and line_new[i + 1] in CapLetters and line_new[i + 2] in CapLetters:
              lst.append(line_new[i])
       else:
              lst.append(' ')
       i -= 1
lst.reverse()  # Переворачиваем список

i = 0
lst2 = []
flag = True
# Фильтрация списка.
while i <= len(lst) - 1:
       if lst[i] in lowLetter:
              flag = True
       if lst[i] in CapLetters and lst[i - 1] in lowLetter and lst[i - 2] in lowLetter:
              lst2.append(lst[i])
              flag = False
       elif lst[i] in CapLetters and flag == False:
              lst2.append(lst[i])
       else:
              lst2.append(' ')
       i += 1

lst2 = ''.join(lst2).split(' ')  # соединяем буквы

found2 = [i for i in lst2 if i != '']  # убираем пустоты
print("-"*3, "задачка №2", "-"*3, "\nСпособ БЕЗ re\nСимволы в верхнем регистре, слева от которых находятся  \ "
                                  "два символа в нижнем регистре, а справа - два символа в верхнем регистре\n" , found2)

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
from random import randint

with open('testRegular.txt', 'w', encoding='UTF-8') as file:
       Xstr = [str(randint(0, 9)) for i in range(2500)]
       Xstr = ''.join(Xstr)
       file.write(Xstr)

with open('testRegular.txt', 'r', encoding='UTF-8') as file:
       listNum = file.readline()
       pattern = re.compile('[0]+|[1]+|[3]+|[4]+|[5]+|[6]+|[7]+|[8]+|[9]+')
       listX = set(pattern.findall(listNum))
       result = [item for item in listX if len(item) == len(max(listX, key=len))]
       print(f"--- задачка №3 ---\nСамая длинная последовательность: {result}")


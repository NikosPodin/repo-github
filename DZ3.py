# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

print('Задание 1\n')
def separate(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('на ноль не делится')

a = int(input('введите число, которое будем делить:  '))
b = int(input('введите число на которое будем делить:  '))
print(separate(a,b))

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
print('\nЗадание 2\n')
human = ['имя', 'фамилия', 'год рождения', 'город проживания', 'email', 'телефон']
hunam = []
def my_f():
    for i in human:
        hunam.append(input(f'введите {i}: '))
my_f()
print(dict(zip(human, hunam)))

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает
# сумму наибольших двух аргументов.

print('\nЗадание 3\n')
def my_func(a,b,c):
    if a+b>b+c and a+b>a+c:
        return a+b
    elif a+c>b+c and a+c>a+b:
        return a+c
    else:
        return b+c

u_i1 = int(input('Введите число: '))
u_i2 = int(input('Введите число: '))
u_i3 = int(input('Введите число: '))
print('из введенных Вами чисел - наибольшая комбинация получается: {}'.format(my_func(u_i1,u_i2,u_i3)))

# z = lambda: int(input('a:')), int(input('b:')), int(input('c:')) # Почему-то всегда с b начинается
# z = lambda: a, b = map(int, input().split())

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде
# функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения
# числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью
# оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

print('Задание 4')
def my_func(x, y):
    return x**y
    #return pow(x,y)
x = int(input('Введите положительное число :'))
y = int(input('введите число положительное (а мы при помощи магии сделаем его отрицательным) :'))
print('если {} будет в степеи -{} получится: {}'.format(x,y,my_func(x, -y)))

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter
# должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и
# снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

b = 0
while True:
    a = input('Введите числа через пробел :')
    #print(a.count('q'))
    if  a.count('q') != 1:
        b += sum(map(int,a.split(' ')))
        print(f'Промежуточная сумма: {b}')
    elif a.count('q') == 1 or a.count('Q') == 1:
        a = a[:(a.find('q')-1)]
        b += sum(map(int, a.split(' ')))
        print(f'Итоговая сумма равна: {b}')
        break


# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую
# его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое
# слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

print('Задание 6')
def int_func(t):
    return t.capitalize()
print(int_func('text'))
a = ('it a good day to die')
print(list(map(int_func, a.split())))
a = input('Сами введите предложение: ')
print(list(map(int_func, a.split())))
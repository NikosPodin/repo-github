# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
import random
import sys
from random import random
print(sys.argv, 'Введите h или help, чтобы рассчитать з/п')

def zp(hours):
    return (int(input('Введите ставку за час: '))*hours)*(1+(int(input('Введите % премии: '))/100))
    #(1500*int(hours*(random()))) #вариант рандомная премия

argv = sys.argv[1:]
if 'h' in argv or 'help' in argv:
    print(zp(int(input('Введите число отработанных часов: '))), 'рублей заработано за месяц')

# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых
# больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка
# использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
print('\nЗадание 2')
prime_s1 = list(map(int, input('Введите несколько цифр через пробел: ').split(' ')))
print('из введенных цифр элементы больше предыдущих будут {}'.format(list(b for a,b in enumerate(prime_s1) if a>0 and prime_s1[a]>prime_s1[a-1])))

prime_s = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print('из имеющихся в примере цифр элементы больше предыдущих будут {}'.format(list(b for a,b in enumerate(prime_s) if a>0 and prime_s[a]>prime_s[a-1])))

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание
# в одну строку. Подсказка: использовать функцию range() и генератор.
print('\nЗадание 3')
print('из имеющихся чисел кратные 20 или 21 будут {}'.format(list(el for el in range(20,241) if el%20==0 or el%21==0)))

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать
# итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]
print('\nЗадание 4')
numb = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print("из диапазона {}\nНе повторяюшиеся элементы будут : {}".format(numb, list(i for i in numb if numb.count(i) == 1)))

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
print('\nЗадание 5')
from functools import reduce
print('Из диапазона 100/1000 умноженные чётные числа дадут: {}'.format(reduce(lambda x, y: x * y, list(range(100,1001,2)))))
print('Из диапазона 100/1000 сумма чётных чисел будет: {}'.format(reduce(lambda x, y: x + y, list(range(100,1001,2)))))
#Не знаю что значит произведение, поэтому и умножил и сложил на всякий случай

# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
#     Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
print('\nЗадание 6')
from itertools import count, cycle
from time import sleep
new_n = []
while True:
    if input('Выход - Q, \nЛюбая клавиша - продолжить: ').upper() == 'Q':
        break
    st = list(map(int, input('Введите две числа через пробел: начало отсчёта и конец: ').split(' ')))
    print(st[0], st[1])
    if st[1]>st[0]:
        for i in count(start=st[0], step=3):
            new_n.append(i)
            print(f'цифра {i} с шагом 3')
            if i >= st[1]:
                break

    else:
        print("Первая введённая цифра должна быть меньше втрой цифры)")
print(new_n)
for number in cycle(new_n):
    sleep(1)
    print(f'в цикле были цифры {number} и цикл закончится на {new_n[-1]} вы ввели её последней')
    if number == new_n[-1]:
        break
print('I love python')


# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
#     При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим
# образом: for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо
# выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
print('\nЗадание 7')
def factor(n):
    numbers = 1
    for i in range(1, n+1):
        numbers=numbers*i
        yield numbers
for a in factor(int(input('Введите число, к которому будем расписывать факториал: '))):
    print(f'числа в факториале получаются: {a}')


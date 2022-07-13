#Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
#не использовать random.randint и вообще библиотеку random
#Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

from time import time

x = int(input('Введите число от 1 до 1 000 000 000: '))

n = time()
strNunber = str(n)                      #Переводим полученное число в строку (для того что бы избавится от запятой)
strNunber = strNunber.replace('.','')   #Избавляемся от запятой
number = int(strNunber)                 #Переводим строку в число типа int

random_number = number // x

print(random_number, type(random_number))
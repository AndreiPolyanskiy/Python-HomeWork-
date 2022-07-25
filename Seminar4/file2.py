# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. 
# Посмотрели, что такое множество? Вот здесь его не используйте.

from math import factorial

number = int(input('Enter number N: '))

list_number = []
i = 1

while i < number:
    list_number.append(factorial(i)) 
    i += 1

print(list_number)
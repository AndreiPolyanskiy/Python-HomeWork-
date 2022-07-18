#Задайте список из нескольких чисел. Напишите программу, 
#которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random

list_of_number = []

n = int (input("Enter the number of items: "))

for i in range(n):
    list_of_number.append(random.randint(1, 10))
print(list_of_number)

def sum(list_of_number):
    sum_number = 0
    for i in range(len(list_of_number)):
        if i%2!=0:
            sum_number += list_of_number[i]
    return sum_number
    
print(sum(list_of_number))

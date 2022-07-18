# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

list_of_number = []

n = int (input("Enter the number of items: "))

for i in range(n):
    list_of_number.append(random.randint(1, 10))
print(list_of_number)

def multiplication_list(list_of_number):
    new_list = []
    i = 0
    j = n-1
    if n % 2 == 0:
        while i < n:
            new_list.append(list_of_number[i] * list_of_number[j])
            i+=1
            j-=1
            if i == n/2:
                break
    else:
        while i < n:
            new_list.append(list_of_number[i] * list_of_number[j])
            i+=1
            j-=1
            if i > j:
                break
            
    return new_list

print(multiplication_list(list_of_number))
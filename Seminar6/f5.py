#  Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

list_of_number = [i for i in range(1, random.randint(1, random.randint(5, 11)))]
print(list_of_number)

def multiplication_list(data):
    new_list = []
    n = len(data)
    i = 0
    j = n-1
    if n % 2 == 0:
        while i < n:
            new_list.append(data[i] * data[j])
            i+=1
            j-=1
            if i == n/2: break
    else:
        while i < n:
            new_list.append(data[i] * data[j])
            i+=1
            j-=1
            if i > j: break
            
    return new_list

print(multiplication_list(list_of_number))
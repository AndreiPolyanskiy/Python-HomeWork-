#  Определить, присутствует ли в заданном списке строк, некоторое число

import random 

lst_num = [i for i in range(random.randint(1, random.randint(2, 11)))]
print(lst_num)
filter_number = int(input('Enter number: '))

lst2 = list(filter(lambda x: x == filter_number, lst_num))
print(lst2)
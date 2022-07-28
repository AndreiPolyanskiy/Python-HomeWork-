# Найти сумму чисел списка стоящих на нечетной позиции

import functools
import random 

lst_num = [i for i in range(random.randint(1, random.randint(2, 11)))]
print(lst_num)

def filter_list (data):
    return (data[0::2])
summ = functools.reduce((lambda a, b: a+b), filter_list(lst_num))    
print('Сумма: ', summ)
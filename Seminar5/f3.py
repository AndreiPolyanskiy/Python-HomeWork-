# Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]

from functools import reduce


lst_leng = []
with open("programming_language.txt", "r") as data:
    lst_leng = data.read().splitlines()

#print(lst_leng)

lst_numbers = []
for i in range(1, len(lst_leng)+1):
    lst_numbers.append(i)
#print(lst_numbers)

def cortege_lists(list1, list2):
    list2 = [x.upper() for x in list2]
    list3 = list(zip(list1, list2))
    return list3

cort_lst = cortege_lists(lst_numbers, lst_leng)
print(cort_lst)

def filter_list(list1):
    result_list = []
    result = 0
    for number, lenguage in list1:
        point = reduce(lambda a, b: a+b, [ord(char) for char in lenguage])
        if point % number == 0:
            result += point
            result_list.append((point, lenguage))
    del list1
    return result, result_list

print(filter_list(cort_lst))


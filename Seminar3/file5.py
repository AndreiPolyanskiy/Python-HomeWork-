# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

number = int(input('Введите число: '))

def fibonachi(number):
    
    n1 = 0 
    n2 = 1
    list_fibonachi = [n1, n2]

    for i in range(1, number):
        n3 = n2 + n1
        list_fibonachi.append(n3)
        n1 = n2
        n2 = n3
    
    n1 = 0 
    n2 = 1
    for i in range (1, number):
        n3 = n1 - n2
        list_fibonachi.insert(0, n3)
        n1 = n2
        n2 = n3

    return list_fibonachi

print(fibonachi(number))



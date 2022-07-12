#Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

n = int(input('Введите число N: '))

summ = 0
arr = []

for i in range(1, n+1):
    
    summ = summ + (1 + 1/i)**i
    arr.append(summ)

print(arr)    
# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

n = int(input('N: '))
lst = [(-3) ** i for i in range(1, n+1)] 
print(lst)
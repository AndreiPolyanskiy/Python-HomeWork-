# Найти расстояние между двумя точками пространства
# (числа вводятся через пробел)

from cmath import sqrt

print("Введите координаты точек, через пробел.\nX1 Y1 X2 Y2: ")
number = list(input().split())
number = list(map(int, number))
print(number)

def distance(data):
    res = sqrt((data[2] - data[0])**2 + (data[3] -data[1])**2)
    return res
print(distance(number))

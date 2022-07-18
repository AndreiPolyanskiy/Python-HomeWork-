# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

list_of_number = [0.123, 1.543, 0.743, 2.431, 1.034]
print(list_of_number)

for i in range(len(list_of_number)):
    list_of_number[i] %= 1
print(list_of_number)

min_number = min(list_of_number)
max_number = max(list_of_number)

difference = max_number - min_number

print(f'Максимальная дробная часть: {max_number}')
print(f'Минимальная дробная часть: {min_number}')
print(f'Их разница: {difference}')
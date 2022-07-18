# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number_10 = int(input('Введите число: '))

number_2 = bin(number_10)

print(number_2, type(number_2))
print(format(number_10, 'b'))
print(f'{number_10:b}')
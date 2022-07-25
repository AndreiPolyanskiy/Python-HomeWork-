# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]

number = int(input('Enter number N: '))

list_multiplier = []

for i in range(2, number + 1):
    if number % i == 0:
        count = 1
        for j in range(2, (i//2 + 1)):
            if (i % j == 0):
                count = 0
                break
        if count == 1:
            list_multiplier.append(i)

print(f"Простые множители для числа {number}: ", list_multiplier)
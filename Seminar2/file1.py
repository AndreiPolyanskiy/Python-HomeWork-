number = float(input('Введите вещественное число: '))

if number < 0:
    number = number * -1

strNunber = str(number)
strNunber = strNunber.replace('.','')
lstStr = list(strNunber)
lstNumber = map(int, lstStr)
suma = sum(lstNumber)

print(suma)
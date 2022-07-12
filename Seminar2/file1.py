number = float(input('Введите вещественное число: '))

strNunber = str(number)
strNunber = strNunber.replace('.','')
lstStr = list(strNunber)
lstNumber = map(int, lstStr)
suma = sum(lstNumber)

print(suma)
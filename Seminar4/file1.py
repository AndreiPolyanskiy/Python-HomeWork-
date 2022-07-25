# Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi, а вычислить, используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.
# Пример: при d = 0.001, π = 3.141. 10^(-10)≤ d ≤10^-1

print("Вычисление числа Пи. \n Способы: \n 1 -> Формула Нилаканта \n 2 -> Ряд Тейлора")
number_metod = int(input("Выберете метод вычисления: "))

number_d = input("Enter number d: ")
str_num = str(number_d)
str_num = str_num.replace('.', '')
len_str = len(str_num) - 1

if number_metod == 1:
    k = 2
    a = 0
    n = 10000
    for i in range(1, n, 2):
        d = 4/((i+1)*(i+2)*(i+3))
        f = (-1)**k * d
        a = a + f
        k += 1
    number_pi = 3 + a
else:
    n = 22
    a = 1
    for i in range(1, n):
        d = 1/(i + 2)
        f = (-1)**i * d
        a = a + f
    number_pi = 4 * a
    
print(f"Число ПИ посчитано с помощью метода {number_metod}: ", round(number_pi, len_str))









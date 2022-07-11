# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('x y z  expression; expression2')
for x in range(2):
    for y in range(2):
        for z in range(2):
            expression = not x and not y and not z
            expression2 = not(x or y or z)
            print(x, y, z,'  ',expression,'     ',expression2)
if expression == expression2:
    print('Истина')
else:
    print('Ложь')
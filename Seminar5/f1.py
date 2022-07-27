# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

str_words = "выавпабв пулкуэ опл абвке"
print(f"Изачальный вариант строки: {str_words}")
line_words = str_words.split(' ')

fragment = 'абв'

def correction_str(line , data):
    new_line = []
    for word in line:
        if data not in word:
            new_line.append(word)
    new_str = " ".join(new_line)   
    return new_str

print('Обработанная строка:', correction_str(line_words, fragment))

    
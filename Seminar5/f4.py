# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах

with open("text_file.txt", "r") as t_file:
    line = t_file.read()

print(line)

def RLE_algoritm_coding(data):
    coding_line = ''
    char_line = ''
    count =1

    if not data: return ''

    for char in data:
        if char != char_line:
            if char_line:
                coding_line += str(count) + char_line
            count = 1
            char_line = char
        else: count +=1
    
    else:
        coding_line += str(count) + char_line
        return coding_line

with open("coding_text.txt", "w") as cd_file:
    cd_file.write(RLE_algoritm_coding(line))

def RLE_algoritm_decoding(data):
    decoding_line = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decoding_line += char * int(count)
            count = ''
    return decoding_line

with open("decoding_text.txt", "w") as cd_file:
    cd_file.write(RLE_algoritm_decoding(RLE_algoritm_coding(line)))

# В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.


with open('Text_file.txt', 'w') as data:
    data.write("Mom sewed m4e pants o6ut o1f fab6ric")

data = open('Text_file.txt', 'r')
text1 = data.read().split()
#print(text1)
#print(text1[2])

list_text = []

for i in range(len(text1)) :
    if text1[i].isalpha() == True:
        list_text.append(text1[i])
    else:
        continue

#print(list_text) 
str_text = str(list_text) 
with open('Text_file.txt', 'w') as data:
    data.write(str_text)
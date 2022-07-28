# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.

# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3

lst_words = ["qwe", "asd", "zxc", "qwe", "ertqwe"]

def task_gucntion(data):
    index = 0
    for i in data:
        index +=1
        index_second = index
        for j in (data[index:]):
            if i == j:
                result = str(i) + " second time on position " + str(index_second+1)
                break
            else:
                result = "No second"
            index_second +=1
        if result != "No second":
            break
    return result

print(lst_words) 
print(task_gucntion(lst_words)) 

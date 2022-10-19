# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу,
# открывающую файл на чтение и
# считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

rus = {'One' : 'Odin', 'Two' : 'dva', 'Three' : 'tri', 'Four' : '4etire'}
new_file = []
with open('hw4_file.txt', 'r') as file_obj:

    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] +'  ' + i[1])
        print(new_file)

with open('file_4_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)
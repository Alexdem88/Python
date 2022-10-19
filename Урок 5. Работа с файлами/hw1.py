# 1. Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
my_f = open ('text_hw1.txt', 'w',)
content = input('введите данные для внесения их в файл text_hw1  \n')
while content:
    my_f.writelines(content)
    content = input('введите дополнительные данные, если не хотите вносить данные, нажмите Enter  \n')
    if not content:
        my_f.close()

with open('text_hw1.txt','r', 'encoding=“utf-8”') as file_obj:
    content = file_obj.read()
print(content)
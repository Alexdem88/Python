import sys
# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.



with open('hw2.txt', 'r',encoding='utf-8') as f_obj:
    content = f_obj.read()
    print(content.count('\n'), 'строк в файле hw2.txt')
    i=0
with open("hw2.txt") as f_obj:
    for line in f_obj:
        i+=1

        print(line.count(' ')+1, 'слова в строке №', i)




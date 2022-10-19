list = [1, 2, 'c', 'hello', 'world' ]
li_count  =  int(input('Введите количество значений, которые хотите добавить в список'))
i=0
el=0
while i<li_count:
    list.append(input('введите значение'))
    i +=1
print(list)
for i in list:
    print(type((i)), end=' ')  #вывел в строку, если убрать *end= ' ' будет списком
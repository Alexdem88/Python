# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.
def my_func ():
    list = []
    arg_1= int(input('a'))
    arg_2 =int( input('b'))
    arg_3 = int(input('c'))
    list.append(arg_3)
    list.append(arg_2)
    list.append(arg_1)
    list.remove(min((arg_3,arg_2,arg_1)))
    print(sum(list))
    return

my_func()

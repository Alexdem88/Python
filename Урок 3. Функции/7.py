# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# def int_func()


# def int_func():
#     list = []
#     x = str(input('введите строку: '))
#     x=x.capitalize()
#     list.append(x)
#     list_str = " ".join(list)
#     print(list_str)
#     return
# int_func()  первое решение которое пришло в голову

def int_func ():  #более лаконичное решение
    z = input("введите предложение ")
    print(z.capitalize())
    return
int_func()


def int_func (): #последнее решение дз
    y = input("введите предложение ")
    print(y.title())
    return
int_func()
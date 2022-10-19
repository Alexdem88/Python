# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится
# месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.
# List_winter = [12, 1, 2,]
# List_spring = [3, 4, 5]
# List_summer = [6, 7, 8]
# List_autumn = [9, 10, 11]
#
# x=(int(input('введите месяц')))
#
# if x == int(List_winter[2]) or int(List_winter[0]) or int(List_winter[1]):
#     print('winter')
# elif x == int(List_spring[2]) or int(List_spring[0]) or int(List_spring[1]):
#     print('spring')   ПОЧЕМУ ТАК НЕ РАБОТАЕТ???? ? ??? ??
#ПОЧЕМУ ТАК НЕ РАБОТАЕТ???? ? ??? ??



List_seasons = ['Зима', 'Весна', 'Лето', 'Осень']
Seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}

x=(int(input('введите месяц')))
while x>12:
    x = (int(input('Такого месяца не существует. Введите число от 1 до 12')))

if x == 12 or x == 1 or x==2:
    print(List_seasons [0])
    print(Seasons_dict.get(1))
elif x == 3 or x == 4 or x ==5:
    print(List_seasons[1])
    print(Seasons_dict.get(2))
elif x ==6 or x==7 or x==8:
    print(List_seasons[2])
    print(Seasons_dict.get(3))
elif x ==9 or x == 10 or x == 11:
    print(List_seasons[3])
    print(Seasons_dict.get(4))
else:
    print('нужно было ввести месяц от 1 до 12. Ошибка')

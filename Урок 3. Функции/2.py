# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя
# : имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.


def profile_info(name, surname, year, city, email, phone):
    name = input(' ваше имя ')
    surname = input(' ваша фамилия')
    year = input(' введите год рождения ')
    city = input(' город ')
    email = input(' ваша почта ')
    phone = input(' введите телефон ')

    print("Имя: " + name, "Фамилия: " +surname, "Год рождения: " + year, "Город: " + city, "email: " + email, "telephone" + phone)

    return

profile_info(name='', surname='', year=' ', city=' ', email=' ', phone=' ')



#Либо как то вот так вот
def my_profile2(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone)

my_profile2(name= 'Alex', surname='Demyanenko', year=1988, city='Moscow', email='email@email', phone='+792392931')


# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json
firms={}
p_count, p_sum = 0,0
with open('hw7_j.txt','r') as spisok:
    spisok_line=spisok.readlines()
for line in spisok_line:
    data=line.split()
    profit = float(data[2]) - float(data[3])
    firms.update({data[0]:profit})
    if profit > 0:
        p_count += 1
        p_sum += profit

average_profit = p_sum/p_count
# print(average_profit)
# print(firms, average_profit)
with open('HW_7.json', 'w') as wjs:
    json.dump(firms, wjs)

    js = json.dumps(firms)
    print(f' Файл в формате json : \n 'f' {js}')

# with open('HW_7.json') as file:
#     result=json.load(file)
#     print(result)

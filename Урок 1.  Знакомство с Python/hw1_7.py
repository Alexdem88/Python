x = float(input('дистанция пройденная в первый день'))
y = float(input('цель'))
d = 1
while x < y:
    x *= 1.1
    d += 1
print('требуемое количество дней', d)
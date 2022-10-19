my_rating = [9, 6, 4, 5, 3]
star = int(input('введите свой рейтинг: '))
inserted = False
index = 0
for elem in my_rating:
    if star > elem:
        my_rating.insert(index, star)
        inserted = True
        break
    index += 1
if not inserted:
    my_rating.append(star)

print(my_rating)





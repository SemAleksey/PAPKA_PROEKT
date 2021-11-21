# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

spisok1 = [78, "Alex", 90, "x", 67, [4, 8]]
spisok2 = [67, 98, "hello", "Alex", 35, 90,]

for i in spisok2:
    if i in spisok1:
        spisok1.remove(i)        
print(spisok1)

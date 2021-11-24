# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

print('Ряд Фибоначи начинается с 1 1')
n = int(input('Введите начальный элемент n = '))
m = int(input('Введите конечный элемент m = '))
n = n - 1
def fibonacci(n, m):
    row = [1, 1]
    x = 3
    while x < (m + 1):
        b = row[x - 2] + row[x - 3]
        row.append(b)
        x += 1
    row = row[n:]    
    return row
print(fibonacci(0, m))    
print(fibonacci(n, m))
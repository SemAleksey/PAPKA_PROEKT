# Задача-3: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

random = input('Введите число: ')
max = 0
for i in random:
    if int(i) > int(max):
        max = i
print('Максимальная цифра:', max) 
    
# random = input('Введите число: ')
# print(random[3])
# a = 0
# b = 0
# print(random[a])
# # print(random[a + 1])
# while random[a] > random[a + 1]:
#     print(random[a])
#     b = a
#     a += 1
    
      
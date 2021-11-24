# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
# def my_round(number, ndigits):
#     pass


# print(my_round(2.1234567, 5))
# print(my_round(2.1999967, 5))
# print(my_round(2.9999967, 5))


number = input('Введите число: ')
ndigits = input('Кол-во знаков округления после запятой: ')
def my_round(number, ndigits):
    a = number
    b = ndigits
    a = float(a)
    if a > 0:
        b = int(b)
        a = float(a) * (10**(b + 1))        
        x = a//1        
        a = int(x)
        a_str = str(a)        
        z = int(a_str[b + 1])        
        if z >= 5:
            a = a + 10
            a = (a/10)//1
            a = int(a)
            a = a / 10**b
        else:
            a = (a/10)//1
            a = int(a)
            a = a / 10**b  
        return a
    if a < 0:
        a = a * (-1)
        b = int(b)
        a = float(a) * (10**(b + 1))        
        x = a//1        
        a = int(x)
        a_str = str(a)        
        z = int(a_str[b + 1])
        if z >= 5:
            a = a + 10
            a = (a/10)//1
            a = int(a)
            a = a / 10**b            
        else:
            a = (a/10)//1
            a = int(a)
            a = a / 10**b               
        return (-a)

print(my_round(number, ndigits))


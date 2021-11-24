# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

# def lucky_ticket(ticket_number):
#     pass


# print(lucky_ticket(123006))
# print(lucky_ticket(12321))
# print(lucky_ticket(436751))

ticket_number = input('Шестизначный номер билета: ')
a = int(ticket_number[0])
b = int(ticket_number[1])
c = int(ticket_number[2])
d = int(ticket_number[3])
f = int(ticket_number[4])
g = int(ticket_number[5])

def lucky_ticket():
    if (a + b + c) == (d + f + g):
        return True
    else:
        return False
print(lucky_ticket())
 
# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.

import os

path = os.getcwd()
def list(path):
    for i in os.listdir(path):
        print(i)
list(path)        


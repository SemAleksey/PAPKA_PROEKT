# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
import sys
import shutil

# смотрим путь
print(sys.argv[0])
# делим путь по точке
x = sys.argv[0].split('.')
# создаем название копии
copy_file = x[0] + 'copy' + '.' + x[1]
# создаем копию
shutil.copy(sys.argv[0], copy_file)    

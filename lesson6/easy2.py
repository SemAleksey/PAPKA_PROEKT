# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
path = os.getcwd()

'''
Код для создания директории в текущей папке
'''

# try:
#     os.mkdir(os.path.join(path, 'dir_1'))
# except:
#     print('dir_1 - Такая папка уже существует')    
# try:
#     os.mkdir(os.path.join(path, 'dir_2'))
# except:
#     print('dir_2 - Такая папка уже существует')   
# try:
#     os.mkdir(os.path.join(path, 'dir_3'))
# except:
#     print('dir_3 - Такая папка уже существует')    
# try:
#     os.mkdir(os.path.join(path, 'dir_4'))
# except:
#     print('dir_4 - Такая папка уже существует')  
# try:
#     os.mkdir(os.path.join(path, 'dir_5'))
# except:
#     print('dir_5 - Такая папка уже существует')      
# try:
#     os.mkdir(os.path.join(path, 'dir_6'))
# except:
#     print('dir_6 - Такая папка уже существует')   
# try:
#     os.mkdir(os.path.join(path, 'dir_7'))
# except:
#     print('dir_7 - Такая папка уже существует')   
# try:
#     os.mkdir(os.path.join(path, 'dir_8'))
# except:
#     print('dir_8 - Такая папка уже существует')   
# try:
#     os.mkdir(os.path.join(path, 'dir_9'))
# except:
#     print('dir_9 - Такая папка уже существует') 

'''
Ниже код для удаления указанных в скобках директорий 
'''
# try:
#     os.rmdir('dir_1')
# except:
#     print('dir_1 - Такого файла не существует')    
# try:
#     os.rmdir('dir_2')
# except:
#     print('dir_2 - Такого файла не существует') 
# try:
#     os.rmdir('dir_3')
# except:
#     print('dir_3 - Такого файла не существует') 
# try:
#     os.rmdir('dir_4')
# except:
#     print('dir_4 - Такого файла не существует') 
# try:
#     os.rmdir('dir_5')
# except:
#     print('dir_5 - Такого файла не существует') 
# try:
#     os.rmdir('dir_6')
# except:
#     print('dir_6 - Такого файла не существует') 
# try:
#     os.rmdir('dir_7')
# except:
#     print('dir_7 - Такого файла не существует') 
# try:
#     os.rmdir('dir_8')
# except:
#     print('dir_8 - Такого файла не существует') 
# try:
#     os.rmdir('dir_9')
# except:
#     print('dir_9 - Такого файла не существует')

    
''' Еще вариант для создания директорий '''
# import os
# d = [('dir_' + str(i + 1)) for i in range(9)]
# def make(paths):
#     dir_path = os.path.join(os.getcwd(), paths)
#     try:
#         os.mkdir(dir_path)
#     except:
#         print(dir_path + ' - Такая папка уже существует')  
# for i in d: 
#     make(i)


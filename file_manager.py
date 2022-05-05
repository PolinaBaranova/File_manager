import os
import shutil
import sys
#mport victory
actions = '''Возможные действия:
1 - создать папку;
2 - удалить (файл/папку);
3 - копировать (файл/папку);
4 - просмотр содержимого рабочей директории;
5 - посмотреть только папки;
6 - посмотреть только файлы;
7 - просмотр информации об операционной системе;
8 - создатель программы;
9 - играть в викторину;
10 - мой банковский счет;
11 - смена рабочей директории (*необязательный пункт);
12 - выход.
'''

print(actions)
choice = input('Выберите действие и введите соответствующий номер: ')

if choice == '1':
    folder_name = input('Введите название папки: ')
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f'Папка {folder_name} добавлена в текущий каталог')
        print('Папки в текущем каталоге: ', os.listdir())
    else:
        print('Папка с таким названием уже существует')

elif choice == '2':
    folder_name = input('Введите название папки, которую хотитет удалить: ')
    if os.path.exists(folder_name):
        os.rmdir(folder_name)
        print(f'Папка {folder_name} удалена')
        print('Папки в текущем каталоге: ', os.listdir())
    else:
        print('В текущем каталоге нет указанной папки')

elif choice == '3':
    folder_to_copy = input('Введите название папки, которую хотите скопировать: ')
    shutil.copytree(f'{folder_to_copy}', f'{folder_to_copy}_copy')
    print('Папки в текущем каталоге: ', os.listdir())

elif choice == '4':
    print('Содержимое рабочей директории: ', os.listdir())

elif choice == '5':
    print('Папки текущей директории: ')
    for filename in os.listdir(os.getcwd()):
        if os.path.isdir(os.path.join(os.getcwd(), filename)):
            print(filename)

elif choice == '6':
    print('Файлы текущей директории: ')
    for filename in os.listdir(os.getcwd()):
        if os.path.isfile(os.path.join(os.getcwd(), filename)):
            print(filename)

elif choice == '7':
    print('Инфо об ОС: ', sys.platform)

elif choice == '8':
    print('Создатель программы: Иванова Иванна Ивановна')

elif choice == '9':
    import victory

elif choice == '10':
    import use_functions

else:
    print('Неверный пункт меню')
#   break



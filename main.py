# Разовая задача, удалить лишние столбцы и пробелы из .csv файлов отчётов PerCo

def remove_cell_from_line(line, separator, cell):  # Удаляем ячейку из строки
    pointer = -1  # Указатель на первый символ разделитель
    list_of_pointers = []  # Список с позициями разделителей
    while pointer < len(line):
        pointer = line.find(separator, pointer + 1)
        if pointer == -1:
            break
        else:
            list_of_pointers.append(pointer)
    if cell == 1:
        newline = line[list_of_pointers[0] + 1:]
    elif 1 < cell <= len(list_of_pointers):
        newline = line[:list_of_pointers[cell - 2]] + line[list_of_pointers[cell - 1]:]
    else:
        newline = line
    return newline


def remove_end_spaces_in_cell(line, separator):
    import re
    return re.sub(' +' + separator, separator, line)


import os

directory = 'c:\\Temp\\csv'  # Каталог с файлами
separator = ';'  # Разделитель

os.mkdir(directory + '\\bak')   # Создаём папку для бэкапа файлов

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    bakfile = os.path.join(directory + '\\bak', filename)
    if os.path.isfile(file):
        os.rename(file, bakfile)
        bf = open(bakfile, 'r')
        nf = open(file, 'w')
        for line in bf:
            line = remove_cell_from_line(line, separator, 16)
            line = remove_cell_from_line(line, separator, 15)
            line = remove_cell_from_line(line, separator, 14)
            line = remove_cell_from_line(line, separator, 13)
            line = remove_cell_from_line(line, separator, 12)
            line = remove_cell_from_line(line, separator, 11)
            line = remove_cell_from_line(line, separator, 10)
            line = remove_cell_from_line(line, separator, 9)
            line = remove_cell_from_line(line, separator, 8)
            line = remove_cell_from_line(line, separator, 6)
            line = remove_end_spaces_in_cell(line, separator)
            nf.write(line)
        bf.close()
        nf.close()

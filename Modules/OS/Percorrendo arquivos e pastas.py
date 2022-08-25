'''
Percorrendo arquivos e pastas com o módulo OS
'''
import os

def size_formated(size):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if size < kilo:
        text = 'B'
    elif size < mega:
        size /= kilo
        text = 'K'
    elif size < giga:
        size /= mega
        text = 'M'
    elif size < tera:
        size /= giga
        text = 'G'
    elif size < peta:
        size /= tera
        text = 'T'
    else:
        size /= peta
        text = 'P'
    
    size = round(size, 2)
    return f'{size}{text}'.replace('.', ',')

path_explorer = input('Enter a path: ')
search_sentence = input('Enter the desired term: ')

print()

count = 0

for roots, directorys, archives in os.walk(path_explorer):
    for archive in archives:
        if search_sentence in archive:
            try:
                count += 1
                complete_path = os.path.join(roots, archive)
                archive_name, archive_ext = os.path.splitext(archive)
                archive_size = os.path.getsize(complete_path)
                print('File matched:')
                print(f'File size: {size_formated(archive_size)}')
                print(f'Path file: {complete_path}')
                print(f'Path name: {archive_name}')
                print(f'Path extension: {archive_ext}')
                print()
            except PermissionError as error:
                print('No permissions!...')
            except FileNotFoundError as error:
                print('File not founded!...')
            except Exception as error:
                print('Unknown error:', error)

print(f'{count} file(s) finded in the search...')
'''
OS + SHUTIL - Mover, copiar e apagar arquivos
shutil.move() - mover os arquivos para um novo caminho
shuti.copy() - copiar os arquivos para um novo caminho
shutil.del() - deletar os arquivos de um caminho
'''
import os
import shutil

original_path = input('Enter the original path: ')
new_path = input('Enter the new path: ')

try:
    os.mkdir(new_path)
except FileExistsError as error:
    print(f'The path "{new_path}" already exists!...')

for root, dirs, files in os.walk(original_path):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(new_path, file)
        shutil.move(old_file_path, new_file_path)
        print(f'File {file} moved successfully!')
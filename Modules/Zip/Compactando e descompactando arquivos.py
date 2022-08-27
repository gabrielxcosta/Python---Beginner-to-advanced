'''
Compactando e descompactando arquivos usando o módulo
zipfile e o módulo OS
'''
from zipfile import ZipFile
import os

path = r'C:\Users\55119\Documents\Estudos\Python_NEW'

# Compactando os arquivos
with ZipFile('file.zip', 'w') as zip:
    for file in os.listdir(path):
        complete_path = os.path.join(path, file)
        zip.write(complete_path, file)

# Listando os arquivos presentes no Zip
with ZipFile('file.zip', 'r') as zip:
    for file in zip.namelist():
        print(file)

# Descompactando os arquivos
with ZipFile('file.zip', 'r') as zip:
    zip.extractall('unpacked_file')
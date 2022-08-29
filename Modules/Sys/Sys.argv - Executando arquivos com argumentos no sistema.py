'''
Executando arquivos com argumentos no sistema
com o sys.argv
'''
import sys
import os

arguments = sys.argv
qt_arguments = len(arguments)

if qt_arguments <= 1:
    print('Arguments are missing!...')
    print('-a', 'To list all files in this folder', sep='\t')
    print('-d', 'To list all directories in this folder', sep='\t')
    sys.exit()

just_files = False
if '-a' in arguments:
    just_files = True

just_directories = False
if '-d' in arguments:
    just_directories = True

for file in os.listdir('.'):
    if just_files:
        if os.path.isfile(file):
            print(file)
        
    if just_directories:
        if os.path.isdir(file):
            print(file)
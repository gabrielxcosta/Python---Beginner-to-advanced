'''
Unindo arquivos PDF em um único PDF 
com o módulo PyPDF2
'''
import PyPDF2
import os

path = r'C:\Users\55119\Documents\Estudos\Python\Módulos\PyPDF2'

new_pdf = PyPDF2.PdfFileMerger()
for root, dirs, files in os.walk(path):
    for file in files:
        if '.pdf' in file:
            complete_path = os.path.join(root, file)
            pdf_file = open(complete_path, 'rb')
            new_pdf.append(pdf_file)

with open(fr'{path}\pdf_sample3.pdf', 'wb') as my_new_pdf:
    new_pdf.write(my_new_pdf)
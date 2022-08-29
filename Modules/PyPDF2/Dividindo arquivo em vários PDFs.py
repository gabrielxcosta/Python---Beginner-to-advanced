'''
Dividindo um arquivo PDF em vários outros
com o módulo PyPDF2
'''
import PyPDF2
import os

path = r'C:\Users\55119\Documents\Estudos\Python\Módulos\PyPDF2'

with open(fr'{path}\pdf_sample3.pdf', 'rb') as pdf:
    reader = PyPDF2.PdfFileReader(pdf)
    n_pages = reader.getNumPages()

    for n_page in range(n_pages):
        writer = PyPDF2.PdfFileWriter()
        current_page = reader.getPage(n_page)
        writer.addPage(current_page)

        with open(fr'{path}\split_{n_page + 1}.pdf', 'wb') as new_pdf:
            writer.write(new_pdf)
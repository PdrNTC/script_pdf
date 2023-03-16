import os
from PyPDF2 import PdfReader, PdfWriter
import shutil
import re
from pathlib import Path
from time import sleep

#Recebendo dados do caminho e diretorio onde os arquivos serao criados
pdf_file_path = 'pdf-teste.pdf'
file_base_name = pdf_file_path.replace('.pdf', '')
output_folder_path = os.path.join(os.getcwd(), '')

pdf = PdfReader(pdf_file_path)

#Looping onde sera criado cada PDF separadamente de acordo com a qtd de paginas 
for page_num in range(len(pdf.pages)):#range(10):
    inserir = 0
    pdfWriter = PdfWriter()
    pdfWriter.add_page(pdf._get_page(page_num))
    #Pegando a string de CPF e fazendo a validacao retirando os pontos e tracos do CPF
    texto_pagina = pdf._get_page(page_num).extract_text()
    cpf_extraido = re.findall(r'\s(\d{3}\.\d{3}\.\d{3}-\d{2})', texto_pagina)
    print(cpf_extraido)
    pattern = '\D'
    cpf_convertido = re.sub(pattern, '', cpf_extraido[0])
    print(cpf_convertido)

    with open(os.path.join(output_folder_path, '{0}.pdf'.format(cpf_convertido)), 'wb') as f:
        pdfWriter.write(f)
        f.close()
        print(cpf_convertido)


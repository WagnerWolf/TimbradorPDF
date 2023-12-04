import PyPDF2
import pathlib
import os
files = [f for f in pathlib.Path('input').iterdir() if f.is_file()]
for i in files:
    input_file = "./input/"+ i.name
    output_file = "./output/TIMBRADO_"+i.name
    watermark_file = "timbre.pdf"
    with open(input_file, "rb") as filehandle_input:
        # Faz a leitura do arquivo pdf
        pdf = PyPDF2.PdfReader(filehandle_input)
        
        with open(watermark_file, "rb") as filehandle_watermark:
            # Faz a leitura do arquivo timbre
            watermark = PyPDF2.PdfReader(filehandle_watermark)
            # Pega a primeira pagina do arquivo timbre
            first_page_watermark = watermark.pages[0]
            # Cria um objeto pdf writer para criar o output
            pdf_writer = PyPDF2.PdfWriter()
            # iteração para pegar todas as paginas do arquivo pdf
            for pg in range(len(pdf.pages)):
                first_page = pdf.pages[pg]
            # junta as duas paginas
                first_page.merge_page(first_page_watermark)
            # adiciona a pagina timbrada no pdf writer
                pdf_writer.add_page(first_page)
            
            with open(output_file, "wb") as filehandle_output:
                # escreve o arquivo output
                pdf_writer.write(filehandle_output)
                print('arquivo timbrado: '+str(i))
for i in files:
    os.remove(i)

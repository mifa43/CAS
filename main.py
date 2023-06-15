import PyPDF2
import pandas as pd
from unstdlib.standard.contextlib_ import open_atomic

pdf_path = "ZA 14 GODINA LJUBILEJA (1).pdf"
excel_data = "kontakti.ods"
new_file = "/home/mifa43/Desktop/CAS/newFile.pdf"


def read_pdf(pdf_data, new_file):

    page_text_list = []

    with open(pdf_path, "rb") as pdf_data:

        try:
            pdf_writer = PyPDF2.PdfWriter()
            
            pdf_reader = PyPDF2.PdfReader(pdf_data)

            page_num = len(pdf_reader.pages) 

            for num in range(0, page_num):

                page_object = pdf_reader.pages[num] 

                pdf_text = page_object.extract_text()

                # page_text_list.append(pdf_text)

                new_text = pdf_text.replace("Ostoja Tatić", "Tuta Bugarin")
                
                # page_object.merge_page(new_text)
                print(new_text)

                pdf_writer.add_page(page_object)


                with open_atomic(new_file, "wb") as output_file:
                    pdf_writer.write(output_file)
                
        finally:

            pdf_data.close()

r = read_pdf(pdf_path, new_file)
# print(r)
# write_pdf(r)
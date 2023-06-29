# from database import get_db
# from crud import KontaktiDB

# db = get_db()

# get_contacts = KontaktiDB(db).get_rows_by_number(5, grad_param="Beograd",kampanja_param=None)

# if get_contacts["succes"] == False:

#     print(get_contacts["message"])

# else:

#     for contact in get_contacts["result"]:

#         if contact.is_printed == "False":

#             update = KontaktiDB(db).update_by_id(contact.id)

#             print([contact.id,
#                 contact.ime, 
#                 contact.prezime, 
#                 contact.adresa, 
#                 contact.post_code, 
#                 contact.grad, 
#                 contact.telefon, 
#                 contact.kampanja,
#                 contact.table_name,
#                 contact.indentification_code,
#                 contact.is_printed
#                 ])
        
#         else:

#             print(f"Person with id {contact.id} for grad: {contact.grad} is  alredy printed!")
# This code example demonstrates how to convert HTML document to JPG images.
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import urllib.parse
import os
# options = Options()
# options.add_argument("--headless")  # Opciono: Podešavanje headless režima

# FIREFOXDRIVER_PATH = '/home/mifa43/.wdm/drivers/geckodriver'  # Proverite putanju do vašeg GeckoDriver fajla

# html_directory = '/home/mifa43/Desktop/CAS/htmlOutput'
# output_directory = '/home/mifa43/Desktop/CAS/pdfOutput'

# # Iterirajte kroz HTML fajlove u izvornom direktorijumu
# for filename in os.listdir(html_directory):
#     if filename.endswith('.html'):
#         html_file_path = os.path.join(html_directory, filename)
#         output_pdf_path = os.path.join(output_directory, os.path.splitext(filename)[0] + '.pdf')

#         service = Service(FIREFOXDRIVER_PATH)
#         driver = webdriver.Firefox(service=service, options=options)
#         driver.get("file:///" + urllib.parse.quote(html_file_path))
#         driver.print_page("/home/mifa43/Desktop/CAS/pdfOutput/pls.pdf")
#         # driver.execute_script('window.print();')
#         driver.quit()

from time import sleep
from selenium.webdriver import ChromeOptions
from helium import start_firefox
from selenium.webdriver import FirefoxOptions
# https://www.deskriders.dev/posts/1640791840-selenium-firefox-and-saving-webpage-as-pdf/
# https://www.deskriders.dev/posts/1640791840-selenium-firefox-and-saving-webpage-as-pdf/
# https://www.deskriders.dev/posts/1640791840-selenium-firefox-and-saving-webpage-as-pdf/
# https://www.deskriders.dev/posts/1640791840-selenium-firefox-and-saving-webpage-as-pdf/
path = "/home/mifa43/Desktop/CAS/pdfOutput/"
for i in range(1):
    combo = path + str(i) + ".pdf"
    options = FirefoxOptions()
    options.add_argument("--start-maximized")
    options.set_preference("print.always_print_silent", True)
    options.set_preference("print.printer_Mozilla_Save_to_PDF.print_to_file", True)
    options.set_preference('print.printer_Mozilla_Save_to_PDF.print_to_filename', '{}'.format(combo))
    options.set_preference("print_printer", "Mozilla Save to PDF")
    options.set_preference("print.printer_Mozilla_Save_to_PDF.print_margin_top", 0)
    options.set_preference("print.printer_Mozilla_Save_to_PDF.print_margin_bottom", 0)
    options.set_preference("print.printer_Mozilla_Save_to_PDF.print_margin_left", 0)
    options.set_preference("print.printer_Mozilla_Save_to_PDF.print_margin_right", 0)

    driver = start_firefox("file:///home/mifa43/Desktop/CAS/htmlOutput/MILENA%20ZE%25C4%258CEV%2013.html", options=options)
    driver.execute_script("window.print();")
    sleep(1)  # Found that a little wait is needed for the print to be rendered otherwise the file will be corrupted
    driver.quit()

# from time import sleep
# from selenium.webdriver import ChromeOptions
# from helium import start_firefox
# from selenium.webdriver import FirefoxOptions

# # Putanja gde želite da sačuvate slike
# path = "/home/mifa43/Desktop/CAS/imgOutput"
# # Veličina A4 papira u pikselima
# a4_width = 594
# a4_height = 939
# for i in range(1):
#     combo = path + str(i) + ".png"

#     options = FirefoxOptions()
#     options.add_argument("--start-maximized")
#     options.add_argument("--headless")  # Dodajte ovu opciju da biste sakrili pregledač
#     options.set_preference("devtools.console.stdout.content", True)
#     options.set_preference("devtools.console.stderr.content", True)

#     driver = start_firefox("file:///home/mifa43/Desktop/CAS/htmlOutput/MILENA%20ZE%25C4%258CEV%2013.html", options=options)
#     driver.execute_script("document.querySelector('.pf').style.margin = '0'")
#     driver.execute_script("document.querySelector('.pf').style.boxShadow = 'none'")
#     driver.execute_script("document.querySelector('.pf').style.borderCollapse = 'initial'")
#     # driver.execute_script("document.querySelector('.pf').style.display = 'none'")

#     # Dimenzije pregledača
#     driver.set_window_size(a4_width, a4_height)

#     # Screenshot stranice
#     driver.save_screenshot(combo)

#     driver.quit()



from bs4 import BeautifulSoup
import random
from urllib.parse import quote
from pandasFrame import pd_data, clean_data
# AKO SE JAVI GRESKA SA NEKIM HTML DOKUMENTOM - PROVERI ELEMENT CLASS JER SE UVEK GENERESI NOVI CLASS I JEDINSTVEN JE | CANVA PDF

# Kolko ljudi ce da se procita iz tabele, samim tim i generise pisma
user_range = 5

# Putanja do izvornog html-a od kog nastaju svi drugi html-ovi
html_path = '/home/mifa43/Desktop/CAS/htmlStructure/jubilej-14.html'
real_data = "SBB BROJEVI CELA SRBIJA/Fizicka lica/BG 3 sbb.xlsx"

def randNum():
    """ ### Generator random brojeva
    
    """
    for _ in range(10):

        random_number = random.randint(10000, 99999)

        return f"Vaša indentifikacija: {random_number}"
    
def modify_HTML(source_html: str, user_data: list, user_range: int):
    """ ### Funkcija koja generise novi html i menja vrednosti na osnovu dict mapper-a
    :param
        - `source_html`: str = Izvorni html kod
        - `user_data`: list = Podatci iz DataFrame-a  
        -  `user_range`: int = Isti broj kao i za pandas, koliko ce se html stranica generisati
    """
    # event_date = str(input("Unesi datum dogadjaja npr.('Subota 12.6.2023 u 18:00'): "))

    # event_location = str(input("Unesi lokaciju dogadjaja npr.(Hotel 'Hilton'): "))
    
    # event_addres = str(input("Unesi adresu dogadjaja npr.(Kralja Milana 35): "))
    
    # prebrojavamo index iz zadatog range-a
    for index in range(0, user_range):
        # randum gen funkcija
        mystr = randNum()

        # formatiranje teksta koji ce da se izmeni
        text_id_1 = f'g. {user_data[index]["Ime"]} {user_data[index]["Prezime"]}'
        text_id_2 = f'{user_data[index]["Adresa"]}'
        text_id_3 = f'{user_data[index]["Post Code"]} {user_data[index]["Kampanja"]}'

        #4,5,6,7 su informacije koje se nece toliko cesto menjati vec ce biti jednmom definisane
        # 9 je random generator, 10 je u kombinaciji npr. adresa grad i postanski kod
        text_id_4 = f'Subota 12.6.2023 u 18:00'
        text_id_5 = f'Hotel "Hilton"'
        text_id_6 = f'Kralja Milana 35'
        text_id_7 = f'11000 Beograd'

        text_id_8 = f'Vi g. {user_data[index]["Prezime"]} ste među izabranima prvog kruga dodele poklona!'
        text_id_11 = f'{user_data[index]["Ime"].upper()} {user_data[index]["Prezime"].upper()}'

        # dict/json struktura kroz koju se pronalazi klasa kao i vrednost za izmenu
        mapped_html = {
            "target_tag": "div",
            "target_1": {
                "class": "t m0 x12 h9 y14 ff1 fs2 fc0 sc0 ls5 ws2",
                "new_value": text_id_1,
                },
            "target_2": {
                "class": "t m0 x12 h9 y15 ff1 fs2 fc0 sc0 ls5 ws2",
                "new_value": text_id_2,
                },
            "target_3": {
                "class": "t m0 x12 h9 y16 ff1 fs2 fc0 sc0 ls5 ws2",
                "new_value": text_id_3,
                },
            "target_4": {
                "class": "t m0 xe h9 ye ff1 fs2 fc0 sc0 ls5 ws2",
                "new_value": text_id_4,
                },
            "target_5": {
                "class": "t m0 xe h9 yf ff1 fs2 fc0 sc0 ls5 ws2",
                "new_value": text_id_5,
                },
            "target_6": {
                "class": "t m0 xe h9 y10 ff1 fs2 fc0 sc0 ls5 ws2",
                "new_value": text_id_6,
                },
            "target_7": {
                "class": "t m0 xe h9 y11 ff1 fs2 fc0 sc0 ls0 ws2",
                "new_value": text_id_7,
                },
            "target_8": {
                "class": "t m0 x10 hd y18 ff1 fs5 fc0 sc0 ls5 ws2",
                "new_value": text_id_8,
                },
            "target_9": {
                "class": "t m0 x10 hd y1d ff1 fs5 fc0 sc0 ls5 ws2",
                "new_value": text_id_8,
                },
            "target_10": {
                "class": "t m0 x15 h10 y25 ff1 fs6 fc0 sc0 ls5 ws2",
                "new_value": mystr,
                },
            "target_11": {
                "class": "t m0 x15 h10 y27 ff1 fs6 fc0 sc0 ls5 ws2",
                "new_value": text_id_11,
                }   
        }
        # Citanje html koda
        with open(source_html, "r", encoding="utf-8") as file:

            fcontent = file.read()
        # Provlacenje kroz bs parser
        soup = BeautifulSoup(fcontent, "html.parser")

        for tar in range(1, len(mapped_html.keys())):
            # prolazimo kroz sve key vrednosti i prebrojavamo ih za formatiranje i dinamicko izmenjivanje vrednosti
            key = f"target_{tar}"

            try:
                # Alociranje html koda, gde se pravi izmena
                target_div = soup.find(mapped_html["target_tag"], class_=mapped_html[key]["class"])
                # Izmena vrednosti target elementa
                target_div.string.replace_with(mapped_html[key]["new_value"])

            except:
                # Ako nije pronadjen dizemo exception
                print(f'Nije pronadjen element sa klasom: {mapped_html[key]["class"]}, vrednost: {mapped_html[key]["new_value"]}')

        # Formatiranje putanje do foldera i generisanje imena datoteke | quote() resava UTF-8 enkodovanjwe
        name = "/home/mifa43/Desktop/CAS/htmlOutput/" + quote(user_data[index]["Ime"]) + " " + quote(user_data[index]["Prezime"]) + quote(str(index))
        # html ekstenzija
        name_path = name+".html"
        
        with open(name_path, "w", encoding="UTF-8") as file:
            # Cuvanje novo modifikovanih fajlova
            file.write(str(soup))

# Poziv funkcija
user_data = clean_data(real_data, user_range)

modify_HTML(html_path, user_data, user_range)
from bs4 import BeautifulSoup
import random
from urllib.parse import quote
from pandasFrame import pd_data, clean_data
from database import get_db
from crud import KontaktiDB

# AKO SE JAVI GRESKA SA NEKIM HTML DOKUMENTOM - PROVERI ELEMENT CLASS JER SE UVEK GENERESI NOVI CLASS I JEDINSTVEN JE | CANVA PDF

# Kolko ljudi ce da se procita iz tabele, samim tim i generise pisma
# user_range = int(input("Unesi broj koliko ce sa se generise dokumenta: "))
# grad_param = str(input("Unesi naziv grada: "))
# kampanja_param = str(input("Unesi naziv opstine samo za *Beograd: "))

# Putanja do izvornog html-a od kog nastaju svi drugi html-ovi
# html_path = '/home/mifa43/Desktop/CAS/htmlStructure/jubilej-14.html'
real_data = "SBB BROJEVI CELA SRBIJA/Fizicka lica/BG 3 sbb.xlsx"

def randNum():
    """ ### Generator random brojeva
    
    """
    for _ in range(10):

        random_number = random.randint(10000, 999999)

        return random_number
def get_data():
    # Sesija ka bazi
    db = get_db()   
    rows = KontaktiDB(db).get_all_rows()

    return rows
def modify_HTML(source_html: str, user_range: int, grad: str = None, opstina: str = ""):
    """ ### Funkcija koja generise novi html i menja vrednosti na osnovu dict mapper-a
    :param
        - `source_html`: str = Izvorni html kod
        - `user_data`: list = Podatci iz DataFrame-a  
        -  `user_range`: int = Isti broj kao i za pandas, koliko ce se html stranica generisati
    """
    # event_date = str(input("Unesi datum dogadjaja npr.('Subota 12.6.2023 u 18:00'): "))

    # event_location = str(input("Unesi lokaciju dogadjaja npr.(Hotel 'Hilton'): "))
    
    # event_addres = str(input("Unesi adresu dogadjaja npr.(Kralja Milana 35): "))
    

    # Sesija ka bazi
    db = get_db()   

    # Vrati kontakt 
    get_contacts = KontaktiDB(db).get_rows_by_number(user_range, grad_param=grad,kampanja_param=opstina)

    # Nema vrednosti za dati parametar
    if get_contacts["succes"] == False:

        print(get_contacts["message"])

    else:

        for contact in get_contacts["result"]:

            # randum gen funkcija
            mystr = randNum()

            # Ako je vec iskoriscen preskiacemo ga
            if contact.is_printed == "False":
                
                update = KontaktiDB(db).update_by_id(contact.id, mystr)

                print([contact.id,
                    contact.ime, 
                    contact.prezime, 
                    contact.adresa, 
                    contact.post_code, 
                    contact.grad, 
                    contact.telefon, 
                    contact.kampanja,
                    contact.table_name,
                    contact.indentification_code,
                    contact.is_printed
                    ])

                # formatiranje teksta koji ce da se izmeni
                text_id_1 = f'g. {contact.ime.capitalize()} {contact.prezime.capitalize()}'
                text_id_2 = f'{contact.adresa.capitalize()}'

                # Ako je NaN to su svi ostali gradovi jer samo Beograd ima kampanja svi ostali NaN
                if contact.kampanja == "NaN":

                    text_id_3 = f'{contact.post_code} {contact.grad.capitalize()}'  # Pord postanskog koda stoji i grad

                else:
                    text_id_3 = f'{contact.post_code} {contact.kampanja.capitalize()} {contact.grad.capitalize()}' # Pord postanskog koda stoji i opstina samo ako je Beogrd
                    

                #4,5,6,7 su informacije koje se nece toliko cesto menjati vec ce biti jednmom definisane
                # 9 je random generator, 10 je u kombinaciji npr. adresa grad i postanski kod
                text_id_4 = f'Subota 12.6.2023 u 18:00'
                text_id_5 = f'Hotel "Hilton"'
                text_id_6 = f'Kralja Milana 35'
                text_id_7 = f'11000 Beograd'

                text_id_8 = f'Vi g. {contact.prezime.capitalize()} ste među izabranima prvog kruga dodele poklona!'
                text_id_9 = f"Vaša indentifikacija: {mystr}"
                text_id_11 = f'{contact.ime.upper()} {contact.prezime.upper()}'

                # dict/json struktura kroz koju se pronalazi klasa kao i vrednost za izmenu
                mapped_html = {
                    "target_tag": "div",
                    "target_1": {
                        "class": "t m0 x13 h9 y14 ff1 fs2 fc0 sc0 ls5 ws2",
                        "new_value": text_id_1,
                        },
                    "target_2": {
                        "class": "t m0 x13 h9 y15 ff1 fs2 fc0 sc0 ls5 ws2",
                        "new_value": text_id_2,
                        },
                    "target_3": {
                        "class": "t m0 x13 h9 y16 ff1 fs2 fc0 sc0 ls5 ws2",
                        "new_value": text_id_3,
                        },
                    "target_4": {
                        "class": "t m0 xf h9 ye ff1 fs2 fc0 sc0 ls5 ws2",
                        "new_value": text_id_4,
                        },
                    "target_5": {
                        "class": "t m0 xf h9 yf ff1 fs2 fc0 sc0 ls5 ws2",
                        "new_value": text_id_5,
                        },
                    "target_6": {
                        "class": "t m0 xf h9 y10 ff1 fs2 fc0 sc0 ls5 ws2",
                        "new_value": text_id_6,
                        },
                    "target_7": {
                        "class": "t m0 xf h9 y11 ff1 fs2 fc0 sc0 ls0 ws2",
                        "new_value": text_id_7,
                        },
                    "target_8": {
                        "class": "t m0 x11 hd y18 ff1 fs5 fc0 sc0 ls5 ws2",
                        "new_value": text_id_8,
                        },
                    "target_9": {
                        "class": "t m0 x11 hd y1c ff1 fs5 fc0 sc0 ls5 ws2",
                        "new_value": text_id_8,
                        },
                    "target_10": {
                        "class": "t m0 x16 h10 y24 ff1 fs6 fc0 sc0 ls5 ws2",
                        "new_value": text_id_9,
                        },
                    "target_11": {
                        "class": "t m0 x17 h10 y26 ff1 fs6 fc0 sc0 ls5 ws2",
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
                        print(f'Element with class not founded: {mapped_html[key]["class"]}, value: {mapped_html[key]["new_value"]}')

                # Formatiranje putanje do foldera i generisanje imena datoteke | quote() resava UTF-8 enkodovanjwe
                name = "/home/mifa43/Desktop/CAS/htmlOutput/" + quote(contact.ime) + " " + quote(contact.prezime) + " " + quote(str(contact.id))
                # html ekstenzija
                name_path = name+".html"
                
                with open(name_path, "w", encoding="UTF-8") as file:
                    # Cuvanje novo modifikovanih fajlova
                    file.write(str(soup))
                        
            else:

                print(f"Person with id {contact.id} for grad: {contact.grad} is  alredy printed!")


# Poziv funkcija
# user_data = clean_data(real_data, user_range)

# modify_HTML(html_path, user_range, grad_param, kampanja_param)
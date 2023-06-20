import pandas as pd
import numpy as np

def pd_data(row_number: int = 0) -> list:
    """ ### Citanje podatka iz tabele
    :param
        - `row_number`: str = Koliko da se procita redova iz tabele
    
    """
    list_row = []

    # Učitavanje Excel fajla
    df = pd.read_excel("data.ods")

    for i in range(0, row_number):
        # Prikaz red po rednom broju 0:n
        prvi_red = df.iloc[i]

        # lista alociranih podataka
        list_row.append({
            "ime": prvi_red["ime"],
            "prezime": prvi_red["prezime"],
            "adresa_stanovanja": prvi_red["adresa_stanovanja"],
            "grad": prvi_red["grad"],
            "mesto": prvi_red["mesto"],
            "postanski_kod": prvi_red["postanski_kod"],
            "pol": prvi_red["pol"]
            })
        
    return list_row



def clean_data(path: str = None, row_number: int = 0):
    """### Ciscenje podataka
    :param
        - `path`: str = None | Putanja do excel fajla
    """
    list_row = []

    df = pd.read_excel(path)

    # Formatiranje teksta u odgovarajućim stupcima
    df['Ime'] = df['Ime'].str.title()
    df['Prezime'] = df['Prezime'].str.title()
    df['Adresa'] = df['Adresa'].str.title()
    df['Grad'] = df['Grad'].str.title()
    df['Kampanja'] = df['Kampanja'].str.title()
    
    # Izbacivanje duplikata 
    df.drop_duplicates(inplace=True, subset=['Adresa'])
    
    print(df.head(20))
    # Prikaz formatiranog DataFrame-a
    for i in range(0, row_number):
        # Prikaz red po rednom broju 0:n
        prvi_red = df.iloc[i]

        # lista alociranih podataka

        list_row.append({
        "Ime": prvi_red["Ime"],
        "Prezime": prvi_red["Prezime"],
        "Adresa": prvi_red["Adresa"],
        "Grad": prvi_red["Grad"],
        "Kampanja": prvi_red["Kampanja"],
        "Post Code": prvi_red["Post Code"],
        })
        
    return list_row
# data = clean_data(real_data, 5)
# print(data)
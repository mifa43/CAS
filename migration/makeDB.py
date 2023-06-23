import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

def merge_all_tables():
    """### Funkcija koja koristi Pandas
        #### DataFrame se koristi za ucitavanje 30+ tabela u jednu virtuelnu te kreira bazu od nje """
    
    # Lista naziva datoteka 
    table_list = []

    # Ciljani folder gde se cuvaju podatci
    folder_path = '/home/mifa43/Desktop/CAS/SBB BROJEVI CELA SRBIJA/Fizicka lica'

    # Kreiranje putanje do direktorijuma
    folder = Path(folder_path)

    # Provera da li postoji direktorijum i da li je direktorijum 
    if folder.exists() and folder.is_dir():

        # Rekruzivno izvlacenje datoteka + pretraga za zadatu ekstenziju * oznacava sve
        excel_files = folder.glob('*.xlsx')

        for file in excel_files:

            print(file)

            table_name = file.stem

            try:

                # Otvaramo sve tabele koje se nalaze u direktorijumu
                table = pd.read_excel(file)

                # Zaglavlje svih tabela se konvertuje u mala slova
                table.columns = table.columns.str.lower()

                # Zaglavlja koja su nama potrebna
                required_columns = ['ime', 'prezime', 'adresa', 'post code', 'grad', 'telefon', 'kampanja']

                for column in required_columns:

                    # Ako kolona nije postojeca onda je podrazumevano NaN
                    if column not in table.columns:

                        table[column] = 'NaN'

                table = table[required_columns]
                
                # Ispravljamo nazive grada iz naziva excel datoteke
                city_name = ' '.join(table_name.split(' ')[:-1]).capitalize()

                # Ispravljamo naziv u koloni grad, ako se pojavi neki od navedenih onda je podrazumevano Beograd
                if city_name == "Bg" or city_name == "Bgd" or city_name == "Bg 1" or city_name == "Bg 2" or city_name == "Bg 3" or city_name == "Bg 4":

                    city_name = "Beograd"

                # Sbb je Sbb mladenovac
                if city_name == "Sbb":

                    city_name = "Mladenovac"

                if not city_name:

                    city_name = "Kragujevac"  # Postavi zadani naziv grada na "Kragujevac"
                
                # Dodajemo kolonu grad i vrednosti
                table['grad'] = city_name

                table['table_name'] = table_name
                
                # Dodajemo u listu formatiran DataFrame
                table_list.append(table)

            # Ako se datoteka nije ucitala dizemo izuzetak
            except Exception as e:

                print(f"Greška prilikom učitavanja datoteke {file}: {str(e)}")

        # Prolazimo kroz listu i spajamo sve u jedan DataFrame
        merged_table = pd.concat(table_list, ignore_index=True)
        
        db_path = '/home/mifa43/Desktop/CAS/casKontakt.db'  # Putanja gde ce da se kreira baza

        # Kreiranje Engine-a
        engine = create_engine(f'sqlite:///{db_path}')
        
        # Upisivanje spojenog DataFrame-a u bazu podataka
        merged_table.to_sql('kontakt', engine, index=False, if_exists='replace')
        
        # Kreiranje i excel tabele za laksi debug i analizu
        merged_table.to_excel('/home/mifa43/Desktop/CAS/nove_tabele.xlsx', index=False)

        return merged_table
    
    # Ako direktorijum nije pronadjen dizi gresku
    else:
        print('Navedeni folder ne postoji ili nije direktorijum.')
        return None

merged_table = merge_all_tables()

print(merged_table)

from database import get_db
from crud import KontaktiDB

db = get_db()

usr = KontaktiDB(db).get_rows_by_number(100, grad_param="Novi sad",kampanja_param=None)

if usr["succes"] == False:

    print(usr["message"])

else:

    for i in usr["result"]:
        print([i.ime, 
            i.prezime, 
            i.adresa, 
            i.post_code, 
            i.grad, 
            i.telefon, 
            i.kampanja,
            i.table_name,
            i.indentification_code,
            i.is_printed
            ])
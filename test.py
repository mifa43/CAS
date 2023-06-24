from database import get_db
from crud import KontaktiDB

db = get_db()

get_contacts = KontaktiDB(db).get_rows_by_number(5, grad_param="Beograd",kampanja_param=None)

if get_contacts["succes"] == False:

    print(get_contacts["message"])

else:

    for contact in get_contacts["result"]:

        if contact.is_printed == "False":

            update = KontaktiDB(db).update_by_id(contact.id)

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
        
        else:

            print(f"Person with id {contact.id} for grad: {contact.grad} is  alredy printed!")
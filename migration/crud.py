from sqlalchemy.exc import SQLAlchemyError
from table_model import *
from typing import Optional, AnyStr

class KontaktiDB():

    def __init__(self, db):
        
        self.db = db

    def insert(self, data: dict):
        """Unesi podatke"""
        Base = Kontakti_sbb()

        Base.metadata.create_all(engine)

        try:
            for book_data in data:

                kontakt = Kontakti_sbb(book_data)
            

                self.db.add(kontakt)

            self.db.commit()

            self.db.refresh(kontakt)

        except SQLAlchemyError as sqlerr:

            return {"sqlAlchemyError": sqlerr}

        return {"status": "ok", "table": kontakt.__tablename__}
    
    def get_all_rows(self):
        """Vrati sve vrednosti | SELECT * FROM Kontakti_sbb"""
        all_kontakts = self.db.query(Kontakti_sbb).all()

        return all_kontakts
    
    def get_rows_by_number(self, 
                           number,
                           grad_param,
                           kampanja_param
                           ):
        try:
            
            # Ako je grad_param jednak None onda trazimo vrednost po kampanja_param parametru
            if grad_param == None:

                rows = self.db.query(Kontakti_sbb).filter(Kontakti_sbb.kampanja == kampanja_param).limit(number)  

            # Ako je kampanja_param jednak None onda trazimo vrednost po grad_param parametru
            elif kampanja_param == None:

                rows = self.db.query(Kontakti_sbb).filter(Kontakti_sbb.grad == grad_param).limit(number)
            
            # Ako je grad_param jednak Beograd tek tada mozemo i da trazimo opstine jer kampanja postoji samo za Beograd
            elif grad_param == "Beograd":

                # Ako su grad_param i kampanja_param vece duzine od 0 trazimo po oba zadata parametra
                if grad_param and len(grad_param) > 0 or kampanja_param and len(kampanja_param) > 0:

                    rows = self.db.query(Kontakti_sbb).filter(Kontakti_sbb.grad == grad_param, Kontakti_sbb.kampanja == kampanja_param).limit(number)

            # Ako je rows jednak 0 to znaci da nista nije pronadjeno od zazdatih parametra
            if rows.count() == 0:

                return {"succes": False, "message": f"No rows founded. params = {grad_param}:{kampanja_param}"}

                
            return {"succes": True, "message": f"No rows founded. params = {grad_param}:{kampanja_param}", "result": rows}

        except:
            
            print("Something wet wrong")
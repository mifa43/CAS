from sqlalchemy.exc import SQLAlchemyError
from table_model import *

class KontaktiDB():

    def __init__(self, db):
        
        self.db = db

    def insert(self, data: dict):
        """Unesi podatke"""
        Base = Kontakti_sbb()

        Base.metadata.create_all(engine)

        try:
            for book_data in data:

                book = Kontakti_sbb(book_data)
            

                self.db.add(book)

            self.db.commit()

            self.db.refresh(book)

        except SQLAlchemyError as sqlerr:

            return {"sqlAlchemyError": sqlerr}

        return {"status": "ok", "table": book.__tablename__}
    
    def get_all_rows(self):
        """Vrati sve vrednosti | SELECT * FROM Kontakti_sbb"""
        all_books = self.db.query(Kontakti_sbb).all()

        return all_books
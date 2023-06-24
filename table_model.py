from sqlalchemy import Integer, String, ForeignKey, Column
from database import Base, engine
from sqlalchemy.orm import relationship

class Kontakti_sbb(Base):
    """Model tabele koja ce da se kreira u bazi"""
    
    __tablename__= "kontakt"   #ime tabele
     
    #kolone u tabeli i njihove karakteristike
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    ime = Column("ime", String)
    prezime = Column("prezime", String)
    adresa = Column("adresa",String)
    post_code = Column("post_code", Integer)
    grad = Column("grad",String)   
    telefon = Column("telefon",Integer)
    kampanja = Column("kampanja",String)   
    table_name = Column("table_name",String)   
    indentification_code = Column("indentification_code",Integer)   
    is_printed = Column("is_printed",String)   

    def __str__(self):
          return self.ime
    
    # ime	prezime	adresa	post code	grad	telefon	kampanja	table_name
#
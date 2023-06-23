from sqlalchemy import Integer, String, ForeignKey, Column
from database import Base, engine
from sqlalchemy.orm import relationship

class Kontakti_sbb(Base):
    """Model tabele koja ce da se kreira u bazi"""
    
    __tablename__= "registration"   #ime tabele
     
    #kolone u tabeli i njihove karakteristike
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    ime = Column("ime", String)
    prezime = Column("prezime", String)
    adresa = Column("adresa",String)
    post_code = Column("post_code",String)
    grad = Column("grad",String)   
    telefon = Column("telefon",Integer)
    kampanja = Column("kampanja",String)   


    def __str__(self):
          return self.ime
    
    # ime	prezime	adresa	post code	grad	telefon	kampanja	table_name
#
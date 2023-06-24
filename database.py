from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# connection string ka sqllite
SQLALCHEMY_DATABASE_URL=f"sqlite:////home/mifa43/Desktop/CAS/casKontakt.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    """Otvaramo seassi-u ka bazi"""

    db = SessionLocal()

    try:

        return db

    finally:
        
        db.close()

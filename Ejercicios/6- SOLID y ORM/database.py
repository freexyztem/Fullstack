from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL DE LA BASE DE DATOS
DATABASE_URL = "mysql://user:password@localhost/example.db"

# CREAR EL MOTOR DE LA BASE DE DATOS
engine = create_engine(DATABASE_URL, echo=True)

# CREAR UNA SESIÓN
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

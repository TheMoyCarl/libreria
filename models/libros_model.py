from sqlalchemy import Column, Integer, String, Float
from config.database import Base

class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    precio = Column(Float, nullable=False)

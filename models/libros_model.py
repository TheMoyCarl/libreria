from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Autor(Base):
    __tablename__ = "autores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)

    libros = relationship("Libro", back_populates="autor", cascade="all, delete-orphan")


class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)

    libros = relationship("Libro", back_populates="categoria", cascade="all, delete-orphan")


class Editorial(Base):
    __tablename__ = "editoriales"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)

    libros = relationship("Libro", back_populates="editorial", cascade="all, delete-orphan")


class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    precio = Column(Float, nullable=False)

    autor_id = Column(Integer, ForeignKey("autores.id"))
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    editorial_id = Column(Integer, ForeignKey("editoriales.id"))

    
    autor = relationship("Autor", back_populates="libros")
    categoria = relationship("Categoria", back_populates="libros")
    editorial = relationship("Editorial", back_populates="libros")

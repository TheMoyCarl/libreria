from models.libros_model import Libro
from sqlalchemy.orm import Session

class LibroRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_libros(self):
        return self.db.query(Libro).all()

    def get_libro_by_id(self, libro_id: int):
        return self.db.query(Libro).filter(Libro.id == libro_id).first()

    def create_libro(self, titulo: str, precio: float, autor_id: int, categoria_id: int, editorial_id: int):
        new_libro = Libro(
            titulo=titulo,
            precio=precio,
            autor_id=autor_id,
            categoria_id=categoria_id,
            editorial_id=editorial_id
        )
        self.db.add(new_libro)
        self.db.commit()
        self.db.refresh(new_libro)
        return new_libro

    def update_libro(self, libro_id: int, titulo: str = None, precio: float = None):
        libro = self.get_libro_by_id(libro_id)
        if libro:
            if titulo:
                libro.titulo = titulo
            if precio is not None:
                libro.precio = precio
            self.db.commit()
            self.db.refresh(libro)
        return libro

    def delete_libro(self, libro_id: int):
        libro = self.get_libro_by_id(libro_id)
        if libro:
            self.db.delete(libro)
            self.db.commit()
        return libro

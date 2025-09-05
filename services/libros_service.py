from repositories.libros_repositories import LibroRepository
from sqlalchemy.orm import Session

class LibroService:
    def __init__(self, db: Session):
        self.repo = LibroRepository(db)

    def listar_libros(self):
        return self.repo.get_all_libros()

    def obtener_libro(self, libro_id: int):
        return self.repo.get_libro_by_id(libro_id)

    def crear_libro(self, titulo: str, precio: float, autor_id: int, categoria_id: int, editorial_id: int):
        return self.repo.create_libro(titulo, precio, autor_id, categoria_id, editorial_id)

    def actualizar_libro(self, libro_id: int, titulo: str = None, precio: float = None):
        return self.repo.update_libro(libro_id, titulo, precio)

    def borrar_libro(self, libro_id: int):
        return self.repo.delete_libro(libro_id)

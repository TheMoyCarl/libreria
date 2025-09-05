from flask import Blueprint, request, jsonify
from services.libros_service import LibroService
from config.database import get_db_session as get_db

libros_bp = Blueprint("libros", __name__, url_prefix="/libros")

@libros_bp.route("/", methods=["GET"])
def listar_libros():
    db = next(get_db())
    service = LibroService(db)
    libros = service.listar_libros()
    return jsonify([{"id": l.id, "titulo": l.titulo, "precio": l.precio} for l in libros])

@libros_bp.route("/<int:libro_id>", methods=["GET"])
def obtener_libro(libro_id):
    db = next(get_db())
    service = LibroService(db)
    libro = service.obtener_libro(libro_id)
    if libro:
        return jsonify({"id": libro.id, "titulo": libro.titulo, "precio": libro.precio})
    return jsonify({"mensaje": "Libro no encontrado"}), 404

@libros_bp.route("/", methods=["POST"])
def crear_libro():
    db = next(get_db())
    service = LibroService(db)
    data = request.json
    libro = service.crear_libro(
        titulo=data.get("titulo"),
        precio=data.get("precio"),
        autor_id=data.get("autor_id"),
        categoria_id=data.get("categoria_id"),
        editorial_id=data.get("editorial_id")
    )
    return jsonify({"mensaje": "Libro creado", "id": libro.id}), 201

@libros_bp.route("/<int:libro_id>", methods=["PUT"])
def actualizar_libro(libro_id):
    db = next(get_db())
    service = LibroService(db)
    data = request.json
    libro = service.actualizar_libro(libro_id, data.get("titulo"), data.get("precio"))
    if libro:
        return jsonify({"mensaje": "Libro actualizado"})
    return jsonify({"mensaje": "Libro no encontrado"}), 404

@libros_bp.route("/<int:libro_id>", methods=["DELETE"])
def borrar_libro(libro_id):
    db = next(get_db())
    service = LibroService(db)
    libro = service.borrar_libro(libro_id)
    if libro:
        return jsonify({"mensaje": "Libro eliminado"})
    return jsonify({"mensaje": "Libro no encontrado"}), 404

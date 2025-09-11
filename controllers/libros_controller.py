from flask import Blueprint, request, jsonify
from services.libros_service import LibroService
from config.database import get_db_session

libros_bp = Blueprint('libros_bp', __name__)
service = LibroService(get_db_session())

@libros_bp.route('/libros', methods=['GET'])
def get_libros():
    libros = service.listar_libros()
    return jsonify([{"id": l.id, "titulo": l.titulo, "precio": l.precio} for l in libros]), 200

@libros_bp.route('/libros/<int:libro_id>', methods=['GET'])
def get_libro(libro_id):
    libro = service.obtener_libro(libro_id)
    if libro:
        return jsonify({"id": libro.id, "titulo": libro.titulo, "precio": libro.precio}), 200
    return jsonify({"error": "Libro no encontrado"}), 404

@libros_bp.route('/libros', methods=['POST'])
def create_libro():
    data = request.get_json()
    libro = service.crear_libro(
        titulo=data.get("titulo"),
        precio=data.get("precio"),
        autor_id=data.get("autor_id"),
        categoria_id=data.get("categoria_id"),
        editorial_id=data.get("editorial_id")
    )
    return jsonify({"id": libro.id, "titulo": libro.titulo}), 201

@libros_bp.route('/libros/<int:libro_id>', methods=['PUT'])
def update_libro(libro_id):
    data = request.get_json()
    libro = service.actualizar_libro(libro_id, data.get("titulo"), data.get("precio"))
    if libro:
        return jsonify({"id": libro.id, "titulo": libro.titulo}), 200
    return jsonify({"error": "Libro no encontrado"}), 404

@libros_bp.route('/libros/<int:libro_id>', methods=['DELETE'])
def delete_libro(libro_id):
    libro = service.borrar_libro(libro_id)
    if libro:
        return jsonify({"message": "Libro eliminado"}), 200
    return jsonify({"error": "Libro no encontrado"}), 404
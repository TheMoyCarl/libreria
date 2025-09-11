from flask import Blueprint, request, jsonify, g
from services.libros_service import LibroService
from config.database import get_db_session

libros_bp = Blueprint('libros_bp', __name__)

@libros_bp.before_request
def before_request():
    g.db = get_db_session()
    g.service = LibroService(g.db)

@libros_bp.teardown_request
def teardown_request(exception=None):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@libros_bp.route('/libros', methods=['GET'])
def get_libros():
    libros = g.service.listar_libros()
    return jsonify([{"id": l.id, "titulo": l.titulo, "precio": l.precio} for l in libros]), 200

@libros_bp.route('/libros/<int:libro_id>', methods=['GET'])
def get_libro(libro_id):
    libro = g.service.obtener_libro(libro_id)
    if libro:
        return jsonify({"id": libro.id, "titulo": libro.titulo, "precio": libro.precio}), 200
    return jsonify({"error": "Libro no encontrado"}), 404

@libros_bp.route('/libros', methods=['POST'])
def create_libro():
    data = request.get_json()
    libro = g.service.crear_libro(
        titulo=data.get("titulo"),
        precio=data.get("precio")
    )
    return jsonify({"id": libro.id, "titulo": libro.titulo}), 201

@libros_bp.route('/libros/<int:libro_id>', methods=['PUT'])
def update_libro(libro_id):
    data = request.get_json()
    libro = g.service.actualizar_libro(libro_id, data.get("titulo"), data.get("precio"))
    if libro:
        return jsonify({"id": libro.id, "titulo": libro.titulo}), 200
    return jsonify({"error": "Libro no encontrado"}), 404

@libros_bp.route('/libros/<int:libro_id>', methods=['DELETE'])
def delete_libro(libro_id):
    libro = g.service.borrar_libro(libro_id)
    if libro:
        return jsonify({"message": "Libro eliminado"}), 200
    return jsonify({"error": "Libro no encontrado"}), 404

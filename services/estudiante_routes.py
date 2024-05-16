from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.estudiante import Estudiante
from schemas.estudiante_schema import estudiante_schema, estudiantes_schema

estudiante_routes = Blueprint('estudiante_routes', __name__)

@estudiante_routes.route('/estudiante', methods=['GET'])
def get_estudiante():
    estudiantes = Estudiante.query.all()
    result = estudiantes_schema.dump(estudiantes)
    data = {
        'message': 'Todos los Estudiantes',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

@estudiante_routes.route('/estudiante/<int:cod_alumno>', methods=['GET'])
def get_Estudiante(cod_alumno):
    estudiantes = Estudiante.query.get(cod_alumno)

    if not estudiantes:
        data = {
            'message': 'Estudiante no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = estudiante_schema.dump(estudiantes)

    data = {
        'message': 'Estudiante encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)
from utils.ma import ma
from marshmallow import fields

class PersonaSchema(ma.Schema):
    id_persona = fields.Integer()
    nombres = fields.String()
    apellidos = fields.String()
    dni = fields.String()
    edad = fields.Integer()
    genero = fields.String()
    direccion = fields.String()
    provincia = fields.String()

persona_schema = PersonaSchema()
personas_schema = PersonaSchema(many=True)

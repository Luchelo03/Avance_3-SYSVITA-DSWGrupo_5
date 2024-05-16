from utils.ma import ma
from model.estudiante import Estudiante
from marshmallow import fields
from schemas.persona_schema import PersonaSchema

class EstudianteSchema(ma.Schema):
    class Meta:
        model = Estudiante
        fields = ('cod_alumno', 'id_persona', 'facultad', 'persona')

    persona = fields.Nested(PersonaSchema)

estudiante_schema = EstudianteSchema()
estudiantes_schema = EstudianteSchema(many=True)
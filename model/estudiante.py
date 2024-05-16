from utils.db import db
from dataclasses import dataclass
from model.persona import Persona

@dataclass
class Estudiante(db.Model):
    __tablename__ = 'estudiante'
    cod_alumno: int
    id_persona: int
    facultad: str

    cod_alumno = db.Column(db.Integer, primary_key=True)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'))
    facultad = db.Column(db.String(50))

    persona = db.relationship('Persona', backref='estudiante')

    def __init__(self, cod_alumno, id_persona, facultad):
        self.cod_alumno = cod_alumno
        self.id_persona = id_persona
        self.facultad = facultad
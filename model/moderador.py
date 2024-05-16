from utils.db import db
from dataclasses import dataclass
from model.persona import Persona

@dataclass
class Moderador(db.Model):
    __table__ = 'moderador'
    id_persona = db.Column(db.Integer, primary_key=True)
    disponibilidad = db.Column(db.Boolean, default=False)
    
    persona = db.relationship()
    
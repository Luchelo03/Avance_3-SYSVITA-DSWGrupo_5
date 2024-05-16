from utils.db import db
from dataclasses import dataclass
from model.persona import Persona

@dataclass
class Especialista(db.Model):
    __tablename__='especialista'
    cod_especialista: int
    id_persona: int 
    disponible: bool
    licencia: str
    
    cod_especialista = db.Column(db.Integer, primary_key=True)
    id_persona = db.Column(db.Integer, db.ForeignKey('id_persona'))
    disponible = db.Column(db.Boolean, default=False)
    licencia = db.Column(db.String(50))
    
    especialista=db.relationship('Persona', backref='especialista')
    
    def __init__(self, cod_especialista, id_persona, disponible, licencia):
        self.cod_especialista = cod_especialista
        self.id_persona = id_persona
        self.disponible = disponible
        self.licencia = licencia
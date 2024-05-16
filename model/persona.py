from utils.db import db
from dataclasses import dataclass

@dataclass
class Persona(db.Model):
    __tablename__ = 'persona'
    id_persona: int
    nombres: str
    apellidos: str
    dni: str
    edad: int
    genero: str
    direccion: str
    provincia: str

    id_persona = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    dni = db.Column(db.String(8))
    edad = db.Column(db.Integer)
    genero = db.Column(db.String(1))
    direccion = db.Column(db.String(100))
    provincia = db.Column(db.String(50))

    def __init__(self, id_persona, nombres, apellidos, dni, edad, genero, direccion, provincia):
        self.id_persona = id_persona
        self.nombres = nombres
        self.apellidos = apellidos
        self.dni = dni
        self.edad = edad
        self.genero = genero
        self.direccion = direccion
        self.provincia = provincia
from dataclasses import dataclass

@dataclass
class Profesor:
    idProfesor: int
    identificacionProfesor: str
    nombreProfesor: str
    apellidoProfesor: str
    correoPersonal: str
    correoInstitucional: str
    especialidad: str
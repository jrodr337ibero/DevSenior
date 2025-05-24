from model.entidades.estudiante import Estudiante
from model.database.execute_queries_db import EjecutarDb
class EstudianteModel:
    def __init__(self, estudiante = Estudiante):
        self.estudiante = estudiante
        
    
    def crear_estudiante(self):
        try:
            self.cursor = EjecutarDb()
            query = "INSERT INTO estudiantes (nombre, correo, fecha_nacimiento) VALUES (%s, %s, %s)"
            params = (self.estudiante.nombre, self.estudiante.correo,self.estudiante.fecha_nacimiento)
            self.cursor.insert(query, params)
            return "ok"
        except Exception as e:
            print(f"Error al crear estudiante: {e}")
            return None
    
    def obtener_estudiantes(self):
        try:
            self.cursor = EjecutarDb()
            query = "SELECT * FROM estudiantes"
            response = self.cursor.consultar(query)
            return response
        except Exception as e:
            print(f"Error al obtener estudiantes: {e}")
    
    def obtener_estudiante_por_nombre(self, nombre):
        try:
            self.cursor = EjecutarDb()
            query = "SELECT * FROM estudiantes WHERE nombre = %s"
            params = (nombre,)
            return self.cursor.consultar(query, params)
        except Exception as e:
            print(f"Error al obtener estudiante: {e}")
            return None
    
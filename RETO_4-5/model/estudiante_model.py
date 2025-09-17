from model.entidades.estudiante import Estudiante
from model.database.execute_queries_db import EjecutarDb
class EstudianteModel:
    def __init__(self, estudiante = Estudiante):
        self.estudiante = estudiante
        
    
    def crear_estudiante(self):
        try:
            self.cursor = EjecutarDb()
            query = """INSERT INTO estudiantes (identificacionEstudiante, 
                                                nombreEstudiante, 
                                                apellidoEstudiante,
                                                fechaNacimientoEstudiante,
                                                correoPersonalEstudiante,
                                                correoInstitucionalEstudiante
                                                ) VALUES (%s, %s, %s, %s, %s, %s)"""
            params = (self.estudiante.identificacionEstudiante, 
                      self.estudiante.nombreEstudiante,
                      self.estudiante.apellidoEstudiante,
                      self.estudiante.fechaNacimientoEstudiante,
                      self.estudiante.correoPersonalEstudiante,
                      self.estudiante.correoInstitucionalEstudiante)
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
            query = "SELECT * FROM estudiantes WHERE nombreEstudiante = %s"
            params = (nombre,)
            return self.cursor.consultar(query, params)
        except Exception as e:
            print(f"Error al obtener estudiante: {e}")
            return None
        
    def cargar_drop_estudiante_db(self):
        try:
            self.cursor = EjecutarDb()
            query = """SELECT idEstudiante, 
                              concat(nombreEstudiante, 
                              ' ', apellidoEstudiante, 
                              ' ', 
                              '-', 
                              identificacionEstudiante) 
                              nombre
                        FROM estudiantes"""
            return self.cursor.consultar(query)
        except Exception as e:
            print(f"Error al obtener estudiante: {e}")
            return None
    
from model.database.conexion_db import ConexionDB
from model.entidades.profesor import Profesor
from model.database.execute_queries_db import EjecutarDb
from dataclasses import astuple

class ProfesorModel:
    def __init__(self, profesor = Profesor):
        self.profesor = profesor
        self.cursor = EjecutarDb()
    
    def crear_profesor(self):
        
        query = """INSERT INTO profesores (
                    idProfesor,
                    identificacionProfesor, 
                    nombreProfesor, 
                    apellidoProfesor, 
                    correoPersonal, 
                    correoInstitucional, 
                    especialidad) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        try:
            datos_docente = astuple(self.profesor)
            self.cursor.insert(query, datos_docente)
            return {"estado":True}
        except Exception as e:
            print(f"Error al crear profesor: {e}")
            return {
                "estado":False,
                "mensaje":str(e)
            }
    
    def lista_docentes(self):
        try:
            query = "SELECT idProfesor, nombreProfesor FROM profesores"
            return self.cursor.consultar(query)
        except Exception as ex:
            print("Error en lista_docentes")
            
    def consultar_docentes(self, nombre):
        try:
            self.cursor = EjecutarDb()
            query = """SELECT P.idProfesor, 
                              identificacionProfesor, 
                              nombreProfesor, 
                              apellidoProfesor, 
                              correoPersonal, 
                              correoInstitucional
                              especialidad, 
                              descripcionCurso
                        FROM Profesores P
                        JOIN Cursos C ON C.idProfesor = P.idProfesor"""
            params = (nombre,)
            if nombre is not None:
                query = query + ' WHERE nombreProfesor = %s '
                return self.cursor.consultar(query, params)
            else:
                return self.cursor.consultar(query)
        except Exception as ex:
            print("Error en consultar_docentes")
        
        
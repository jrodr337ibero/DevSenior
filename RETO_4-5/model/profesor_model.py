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
            return "ok"
        except Exception as e:
            print(f"Error al crear profesor: {e}")
            return None
    
    def obtener_profesores(self):
        query = "SELECT * FROM profesores"
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener profesores: {e}")
            return []
    
    def obtener_profesor_por_id(self, id_profesor):
        query = "SELECT * FROM profesores WHERE id_profesor = %s"
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, (id_profesor,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener profesor: {e}")
            return None
    
    def obtener_cursos_profesor(self, id_profesor):
        query = "SELECT * FROM cursos WHERE id_profesor = %s"
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, (id_profesor,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener cursos del profesor: {e}")
            return []
        
    def lista_docentes(self):
        try:
            query = "SELECT idProfesor, nombreProfesor FROM profesores"
            return self.cursor.consultar(query)
        except Exception as ex:
            print("Error en lista_docentes")
            
    def consultar_docentes(self):
        try:
            query = """SELECT P.idProfesor, identificacionProfesor, nombreProfesor, apellidoProfesor, correoPersonal, correoInstitucional
                        especialidad, descripcionCurso
                        FROM Profesores P
                        JOIN Cursos C ON C.idProfesor = P.idProfesor"""
            return self.cursor.consultar(query)
        except Exception as ex:
            print("Error en consultar_docentes")
        
        
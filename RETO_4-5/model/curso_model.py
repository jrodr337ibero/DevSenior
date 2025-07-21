from model.entidades.curso import Curso
from model.database.execute_queries_db import EjecutarDb

class CursoModel:
    def __init__(self, curso = Curso):
        self.curso = curso
        
    def crear_curso(self):
        try:
            self.cursor = EjecutarDb()
            query = "INSERT INTO cursos (descripcionCurso, idProfesor) VALUES (%s, %s)"
            params = (self.curso.descripcionCurso, self.curso.idProfesor)
            return self.cursor.insert(query, params)
        except Exception as e:
            print(f"Error al crear curso: {e}")
            return None
    
    def obtener_cursos(self):
        try:
            self.cursor = EjecutarDb()
            query = """
            SELECT c.*, p.nombre as nombre_profesor, p.apellido as apellido_profesor 
            FROM cursos c
            JOIN profesores p ON c.id_profesor = p.id_profesor
            """
            return self.cursor.consultar(dictionary=True)
        except Exception as e:
            print(f"Error al obtener cursos: {e}")
            return []
    
    def obtener_curso_por_id(self, id_curso):
        try:
            self.cursor = EjecutarDb()
            query = """
            SELECT c.*, p.nombre as nombre_profesor, p.apellido as apellido_profesor 
            FROM cursos c
            JOIN profesores p ON c.id_profesor = p.id_profesor
            WHERE c.id_curso = %s
            """
            return self.cursor.consultar(dictionary=True)
        except Exception as e:
            print(f"Error al obtener curso: {e}")
            return None
        
    def lista_cursos(self):
        try:
            self.cursor = EjecutarDb()
            query = "SELECT idCurso, descripcionCurso FROM cursos"
            return self.cursor.consultar(query)
        except Exception as ex:
            print("Error en lista_docentes")
            
    def lista_semanas(self):
        try:
            self.cursor = EjecutarDb()
            query = "SELECT idSemana, diaSemana FROM semana"
            return self.cursor.consultar(query)
        except Exception as ex:
            print("Error ")
            
    def lista_horas(self):
        try:
            self.cursor = EjecutarDb()
            query = "SELECT idHora, Hora FROM hora"
            return self.cursor.consultar(query)
        except Exception as ex:
            print("Error ")
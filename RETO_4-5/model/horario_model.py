from model.database.execute_queries_db import EjecutarDb
from model.entidades.horario import Horario
from dataclasses import astuple

class HorarioModel:
    def __init__(self, horario = Horario):
        self.horario = horario
    
    def agregar_horario(self):
       
        try:
            self.cursor = EjecutarDb()
            query = """INSERT INTO horarios 
                        (idCurso, idDiaSemana, idHoraInicio, idHoraFin) 
                        VALUES (%s, %s, %s, %s)"""
                    
            datos_horario = astuple(self.horario)
            self.cursor.insert(query, datos_horario)
        except Exception as e:
            print(f"Error al agregar horario: {e}")
            return None
    
    def obtener_horarios_curso(self, id_curso):
        try:
            self.cursor = EjecutarDb()
            query = "SELECT * FROM horarios WHERE id_curso = %s ORDER BY dia_semana, hora_inicio"
            return self.cursor.consultar(query, (id_curso,))
        except Exception as e:
            print(f"Error al obtener horarios: {e}")
            return []
    
    def obtener_horarios_dia(self, dia_semana):
       
        try:
            self.cursor = EjecutarDb()
            query = """
                SELECT h.*, c.nombre_curso, p.nombre as nombre_profesor, p.apellido as apellido_profesor
                FROM horarios h
                JOIN cursos c ON h.id_curso = c.id_curso
                JOIN profesores p ON c.id_profesor = p.id_profesor
                WHERE h.dia_semana = %s
                ORDER BY h.hora_inicio
                """
            return self.cursor.consultar(query, (dia_semana,))
        except Exception as e:
            print(f"Error al obtener horarios del día: {e}")
            return []
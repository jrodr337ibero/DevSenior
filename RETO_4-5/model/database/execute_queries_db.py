from model.database.conexion_db import ConexionDB


class EjecutarDb:
    def __init__(self):
        self.db = ConexionDB()
        self.connection = self.db.get_conexion()
        self.cursor = self.connection.cursor()
    
    def insert(self, quey: str, params: tuple):
        try:
            self.cursor.execute(quey, (params))
            self.connection.commit()
        finally:
            self.cursor.close()
            
    def consultar(self, query: str, params = None):
        try:
            self.cursor.execute(query, params)
            response = self.cursor.fetchall()
            return response
        finally:
            self.cursor.close()
            
    def actualizar(self, query: str, params: tuple):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
        finally:
            self.cursor.close()
            
    def eliminar(self, query: str, params: tuple):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
        finally:
            self.cursor.close()
       
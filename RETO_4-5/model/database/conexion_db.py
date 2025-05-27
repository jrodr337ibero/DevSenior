import mysql.connector
from mysql.connector import Error

class ConexionDB:
    __instancia = None

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super(ConexionDB, cls).__new__(cls)
        return cls.__instancia

    def __init__(self):
        if not hasattr(self, '_conexion') or not self._conexion.is_connected():
            try:
                self._conexion = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='Academia'
                )
                if self._conexion.is_connected():
                    print('Conexión establecida')
            except Error as ex:
                print('Error de conexión a la base de datos:', ex)
                self._conexion = None

    def get_conexion(self):
        if self._conexion and self._conexion.is_connected():
            return self._conexion
        return None

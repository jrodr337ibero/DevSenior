from model.entidades.estudiante import Estudiante
from model.estudiante_model import EstudianteModel
from tkinter import messagebox, ttk

class EstudianteController:
    def __init__(self):
        self.model = EstudianteModel()
    
    def registrar_estudiante(self, nombre, correo, fecha_nacimiento):
        id = None
        insert_estudiante = Estudiante(id, nombre, correo, fecha_nacimiento)
        self.model = EstudianteModel(insert_estudiante)
        
        estudiante_id = self.model.crear_estudiante()
        if estudiante_id:
            messagebox.showinfo("Estudiante guardado", f"El estudiante '{nombre}' fue guardado correctamente.")
    
    def listar_estudiantes(self):
        estudiantes = self.model.obtener_estudiantes()
        return estudiantes
    
    def buscar_estudiante(self, nombre):
        if nombre:
            estudiante = self.model.obtener_estudiante_por_nombre(nombre)
            if not len(estudiante):
                messagebox.showinfo("Buscar", f"No se encontraron datos con el filtro de busqueda -> '{nombre}'")
            return estudiante
    
    def reporte_cursos_estudiante(self):
        id_estudiante = self.view.pedir_id_estudiante()
        if id_estudiante:
            pass
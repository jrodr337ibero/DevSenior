from model.entidades.curso import Curso
from model.curso_model import CursoModel
from tkinter import messagebox, ttk

class CursoController:
    def __init__(self):
        self.model = CursoModel()
    
    def registrar_curso(self, descripcion, id_profesor):
        
        if id_profesor is None:
            messagebox.showinfo("Info", f"Por favor seleccione un docente")
        else:
            insert_curso = Curso(descripcion, id_profesor)
            self.model = CursoModel(insert_curso)
            self.model.crear_curso()
            messagebox.showinfo("Info", f"Curso creado con exito")
            
    def cargar_drop_curso(self) -> list:
        return self.model.lista_cursos()
    
    def cargar_drop_semanas(self) -> list:
        return self.model.lista_semanas()
    
    def cargar_drop_horas(self) -> list:
        return self.model.lista_horas()
    
    def estudiante_en_curso(self):
        return self.model.estudiantes_en_curso_db()
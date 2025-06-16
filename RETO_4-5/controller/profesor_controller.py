from model.entidades.profesor import Profesor
from model.profesor_model import ProfesorModel
from tkinter import messagebox

class ProfesorController:
    def __init__(self):
        self.model = ProfesorModel()
    
    def registrar_profesor(self, identificacionProfesor, nombreProfesor, apellidoProfesor, correoPersonal, 
                           correoInstitucional, 
                           especialidad):
        insert_estudiante = Profesor(None,
                                     identificacionProfesor,
                                     nombreProfesor, 
                                     apellidoProfesor, 
                                     correoPersonal, 
                                     correoInstitucional, 
                                     especialidad)
        self.model = ProfesorModel(insert_estudiante)
        
        docente_id = self.model.crear_profesor()
        if docente_id:
            messagebox.showinfo("Docente guardado", f"El docente '{nombreProfesor} {apellidoProfesor}' fue guardado correctamente.")
    
    def cargar_drop_docente(self) -> list:
        return self.model.lista_docentes()
    
    def consultar_docente_curso(self):
        return self.model.consultar_docentes()
            
    
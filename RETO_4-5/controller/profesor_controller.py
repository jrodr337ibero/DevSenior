from model.entidades.profesor import Profesor
from model.profesor_model import ProfesorModel
from tkinter import messagebox

class ProfesorController:
    def __init__(self):
        self.model = ProfesorModel()
    
    def registrar_profesor(self, identificacionProfesor, 
                           nombreProfesor, 
                           apellidoProfesor, 
                           correoPersonal, 
                           correoInstitucional, 
                           especialidad):
        try:
            insert_profesor = Profesor(None,
                                     identificacionProfesor,
                                     nombreProfesor, 
                                     apellidoProfesor, 
                                     correoPersonal, 
                                     correoInstitucional, 
                                     especialidad)
            self.model = ProfesorModel(insert_profesor)
        
            response = self.model.crear_profesor()
            if response.get('estado'):
                messagebox.showinfo("Docente guardado", f"El docente '{nombreProfesor} {apellidoProfesor}' fue guardado correctamente.")
            else:
                messagebox.showinfo("Error", f"No fue posible crear el registro del docente {response.get('mensaje')}")
        except Exception as e:
            messagebox.showinfo(f"Error al crear el docente {str(e)}")
    
    def cargar_drop_docente(self) -> list:
        return self.model.lista_docentes()
    
    def consultar_docente_curso(self, nombre = None):
        return self.model.consultar_docentes(nombre)
            
    
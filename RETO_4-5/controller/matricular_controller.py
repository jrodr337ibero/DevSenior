from model.entidades.matricula import Matricula
from model.matricula_model import MatriculaModel
from tkinter import messagebox

class MatriculaController:
    def __init__(self):
        self.model = MatriculaModel()
    
    def matricular_estudiante(self, idEstudiante, idCurso):
        
        if idEstudiante and idCurso:
            matricula = Matricula(idEstudiante, idCurso)
            self.model = MatriculaModel(matricula)
            matricula_id = self.model.matricular_estudiante()
            
            if matricula_id:
                messagebox.showinfo("Exito", "Estudiante fue matriculado con éxito")
                
    def cargar_drop_matriculas(self):
        return self.model.cargar_drop_matriculas_db()
    
    def eliminar_matricula(self, idMatricula):
        if idMatricula:
            if self.model.eliminar_matricula(idMatricula):
                messagebox.showinfo("Exito","Matrícula eliminada con éxito")
            else:
                messagebox.showinfo("Error","Error al eliminar matrícula")
                
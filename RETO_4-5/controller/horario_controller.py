from model.horario_model import HorarioModel
from tkinter import messagebox, ttk
from model.entidades.horario import Horario

class HorarioController:
    def __init__(self):
        self.model = HorarioModel()
    
    def registrar_horario(self, idCurso, idDiaSemana, idHoraInicio, idHoraFin):
        
        if idCurso is None:
            messagebox.showinfo("Info", f"Por favor seleccione un curso")
        if idDiaSemana is None:
            messagebox.showinfo("Info", f"Por favor seleecione un dia")
        if idHoraInicio is None:
            messagebox.showinfo("Info", f"Por favor seleecione hora inicio")
        if idHoraFin is None:
            messagebox.showinfo("Info", f"Por favor seleecione hora fin")
        
        else:
            insert_horario = Horario(idCurso, idDiaSemana, idHoraInicio, idHoraFin)
            self.model = HorarioModel(insert_horario)
            self.model.agregar_horario()
            messagebox.showinfo("Info", f"Horario creado con exito")
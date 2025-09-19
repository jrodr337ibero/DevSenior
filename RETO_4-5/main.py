from view.gestion_cursos import GestionCursos
import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    GestionCursos(root, ttk)
    root.mainloop()



if __name__== "__main__":
    main()
    
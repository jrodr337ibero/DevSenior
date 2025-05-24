from view.gestion_cursos import GestionCursos
import tkinter as tk
from tkinter import ttk, messagebox


def main():
    root = tk.Tk()
    GestionCursos(root, ttk, messagebox)
    root.mainloop()



if __name__== "__main__":
    main()
    
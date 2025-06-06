from controller.estudiante_controller import EstudianteController
import tkinter as tk
from tkinter import ttk

class GestionCursos:
    def __init__(self, root, ttk, messagebox):
        self.root = root
        self.root.title("Sistema de gestion academica")
        self.root.geometry("900x550")
        self.root.config(bg="#f0f2f5")

        contenedor = tk.Frame(self.root, bg="#f0f2f5")
        contenedor.pack(fill='both', expand=True)

        menu_frame = tk.Frame(contenedor, bg="#2c3e50", width=180)
        menu_frame.pack(side="left", fill="y")

        self.main_frame = tk.Frame(contenedor, bg="white")
        self.main_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

        self.button_style = {
            "font": ("Segoe UI", 11),
            "bg": "#34495e",
            "fg": "white",
            "activebackground": "#1abc9c",
            "activeforeground": "white",
            "bd": 0,
            "relief": tk.FLAT,
            "anchor": "w",
            "padx": 20,
            "pady": 8
        }

        tk.Button(menu_frame, text="Inicio", command=self.mostrar_inicio, **self.button_style).pack(fill="x", pady=2)

        self.btn_cursos = tk.Button(menu_frame, text="Cursos", **self.button_style)
        self.btn_cursos.pack(fill="x", pady=2)
        self.btn_cursos.bind("<Button-1>", self.mostrar_menu_cursos)
        
        self.btn_estudiante = tk.Button(menu_frame, text="Estudiante", **self.button_style)
        self.btn_estudiante.pack(fill="x", pady=2)
        self.btn_estudiante.bind("<Button-1>", self.submenu_estudiante)

        self.menu_cursos = tk.Menu(self.root, tearoff=False, bg="white", fg="black", font=("Segoe UI", 10))
        self.menu_cursos.add_command(label="Agregar Curso", command=lambda: self._actualizar_contenido("Agregar Curso"))
        self.menu_cursos.add_command(label="Listar Cursos", command=lambda: self._actualizar_contenido("Lista de Cursos"))
        
        self.menu_estudiante = tk.Menu(self.root, tearoff=False, bg="white", fg="black", font=("Sego UI", 10))
        self.menu_estudiante.add_command(label="Agregar Estudiante", command=lambda: self.agregar_estudiante())
        self.menu_estudiante.add_command(label="Consultar Estudiante", command=lambda: self.consultar_estudiante())

        tk.Button(menu_frame, text="Configuración", command=self.mostrar_configuracion, **self.button_style).pack(fill="x", pady=2)
        tk.Button(menu_frame, text="Salir", command=self.root.destroy, **self.button_style).pack(fill="x", pady=2)

        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        barra_menus = tk.Menu()
        menu_archivo = tk.Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(label="Nuevo", accelerator="Ctrl+N", compound=tk.LEFT)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.root.destroy)
        barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
        self.root.config(menu=barra_menus)
        self.estudiante_controller = EstudianteController()
        
        
    def submenu_estudiante(self, event=None):
        x = self.btn_estudiante.winfo_rootx() + self.btn_estudiante.winfo_width()
        y = self.btn_estudiante.winfo_rooty()
        self.menu_estudiante.tk_popup(x, y)

    def mostrar_menu_cursos(self, event=None):
        x = self.btn_cursos.winfo_rootx() + self.btn_cursos.winfo_width()
        y = self.btn_cursos.winfo_rooty()
        self.menu_cursos.tk_popup(x, y)
        

    def mostrar_inicio(self):
        self._actualizar_contenido("Bienvenido al sistema de gestión")

    def mostrar_configuracion(self):
        self._actualizar_contenido("Opciones de configuración")

    def _actualizar_contenido(self, texto):
        for widget in self.notebook.winfo_children():
            widget.destroy()
        frame = tk.Frame(self.notebook, bg="white")
        label = tk.Label(
            frame,
            text=texto,
            font=("Segoe UI", 14, "bold"),
            bg="white",
            fg="#2c3e50"
        )
        label.pack(pady=40)
        self.notebook.add(frame, text="Vista")
        self.notebook.select(frame)

    def agregar_estudiante(self):

        for widget in self.notebook.winfo_children():
            widget.destroy()

        frame = tk.Frame(self.notebook, bg="white")
        frame.columnconfigure(0, weight=0)
        frame.columnconfigure(1, weight=1)

        label = tk.Label(
            frame, text='Agregar estudiante',
            font=("Segoe UI", 14, "bold"), bg="white", fg="#2c3e50"
        )
        label.grid(row=0, column=0, columnspan=2, pady=(40))

        label_nombre = tk.Label(
            frame, text="Nombre del Estudiante:",
            bg="white", font=('Arial Narrow', 12, 'bold')
        )
        label_nombre.grid(row=1, column=0, sticky="e", padx=(50, 10), pady=10)

        self.nombre_var = tk.StringVar()
        entry_nombre = tk.Entry(
            frame, textvariable=self.nombre_var,
            font=('Arial', 11), width=40
        )
        entry_nombre.grid(row=1, column=1, padx=(10, 50), pady=10, sticky="w")

        label_correo = tk.Label(
            frame, text="Correo del Estudiante:",
            bg="white", font=('Arial Narrow', 12, 'bold')
        )
        label_correo.grid(row=2, column=0, sticky="e", padx=(50, 10), pady=10)

        self.correo_var = tk.StringVar()
        entry_correo = tk.Entry(
            frame, textvariable=self.correo_var,
            font=('Arial', 11), width=40
        )
        entry_correo.grid(row=2, column=1, padx=(10, 50), pady=10, sticky="w")

        label_fecha = tk.Label(
            frame, text="Fecha de Nacimiento:",
            bg="white", font=('Arial Narrow', 12, 'bold')
        )
        label_fecha.grid(row=3, column=0, sticky="e", padx=(50, 10), pady=10)

        self.fecha_var = tk.StringVar()
        entry_fecha = tk.Entry(
            frame, textvariable=self.fecha_var,
            font=('Arial', 11), width=40
        )
        entry_fecha.grid(row=3, column=1, padx=(10, 50), pady=10, sticky="w")
        self.boton_agregar = tk.Button(
            frame,
            text="Agregar Estudiante",
            font=("Arial", 11, 'bold'),
            bg="#27ae60", fg="white",
            padx=10, pady=5,
            command=lambda: self.estudiante_controller.registrar_estudiante(self.nombre_var.get(), self.correo_var.get(), self.fecha_var.get())
        )
        self.boton_agregar.grid(row=4, column=0, columnspan=2, pady=(20, 30))

        self.notebook.add(frame, text="Datos del Estudiante")
        self.notebook.select(frame)

    
        
    def consultar_estudiante(self):
        for widget in self.notebook.winfo_children():
            widget.destroy()
            
        self.frame = tk.Frame(self.notebook, bg="white")
        self.frame.columnconfigure(0, weight=0)
        self.frame.columnconfigure(1, weight=1)
        
        
        label = tk.Label(
            self.frame, text='Consultar Estudiantes',
            font=("Segoe UI", 14, "bold"), bg="white", fg="#2c3e50"
        )
        label.grid(row=0, column=0, columnspan=2, pady=(40))
        
        label_nombre = tk.Label(
            self.frame, text="Nombre del Estudiante:",
            bg="white", font=('Arial Narrow', 12, 'bold')
        )
        label_nombre.grid(row=1, column=0, sticky="e", padx=(50, 10), pady=10)
        
        self.nombre_var = tk.StringVar()
        entry_nombre = tk.Entry(
            self.frame, textvariable=self.nombre_var,
            font=('Arial', 11), width=40
        )
        entry_nombre.grid(row=1, column=1, padx=(10, 50), pady=10, sticky="w")
        
        self.boton_agregar = tk.Button(
            self.frame,
            text="Consultar",
            font=("Arial", 11, 'bold'),
            bg="#27ae60", fg="white",
            padx=10, pady=5,
            command=lambda: self.data_grid_mostrar_estudiantes()
        )
        self.boton_agregar.grid(row=4, column=0, columnspan=2, pady=(20, 30))
        self.notebook.add(self.frame, text="Consultar Estudiantes")
        self.notebook.select(self.frame)
        
        
    def data_grid_mostrar_estudiantes(self):
        
        nombre = self.nombre_var.get()
        print(nombre)
        if self.nombre_var.get() != '':
            response = self.estudiante_controller.buscar_estudiante(self.nombre_var.get())
        else:
            response = self.estudiante_controller.listar_estudiantes()
            
        self.estudiantes =  ttk.Treeview(self.frame, columns=("Nombre", "Correo", "Fecha Nacimiento"), show="headings")
        self.estudiantes.heading("Nombre", text="Nombre")
        self.estudiantes.heading("Correo", text="Correo")
        self.estudiantes.heading("Fecha Nacimiento", text="Fecha Nacimiento")
        self.estudiantes.grid(row=3, column=0, columnspan=2)
        
        for item in self.estudiantes.get_children():
            self.estudiantes.delete(item)
        
        for estudiante in response:
            self.estudiantes.insert('', 'end', values=(
                estudiante[1],
                estudiante[2],
                estudiante[3]
            ))
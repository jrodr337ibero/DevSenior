import tkinter as tk
from tkinter import ttk
from controller.estudiante_controller import EstudianteController
from controller.profesor_controller import ProfesorController
from controller.curso_controller import CursoController
from controller.horario_controller import HorarioController
from tkinter import messagebox

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
        self.btn_cursos.bind("<Button-1>", self.submenu_curso)
        
        self.btn_estudiante = tk.Button(menu_frame, text="Estudiante", **self.button_style)
        self.btn_estudiante.pack(fill="x", pady=2)
        self.btn_estudiante.bind("<Button-1>", self.submenu_estudiante)
        
        self.btn_docente = tk.Button(menu_frame, text="Docentes", **self.button_style)
        self.btn_docente.pack(fill="x", pady=2)
        self.btn_docente.bind("<Button-1>", self.submenu_docente)
        
        self.menu_cursos = tk.Menu(self.root, tearoff=False, bg="white", fg="black", font=("Segoe UI", 10))
        self.menu_cursos.add_command(label="Agregar Curso", command=lambda: self.agregar_curso())
        self.menu_cursos.add_command(label="Listar Cursos", command=lambda: self._actualizar_contenido("Lista de Cursos"))
        self.menu_cursos.add_command(label="Asignar Horario", command=lambda: self.agregar_horario())
        
        self.menu_estudiante = tk.Menu(self.root, tearoff=False, bg="white", fg="black", font=("Sego UI", 10))
        self.menu_estudiante.add_command(label="Agregar Estudiante", command=lambda: self.agregar_estudiante())
        self.menu_estudiante.add_command(label="Consultar Estudiante", command=lambda: self.consultar_estudiante())

        self.menu_docente = tk.Menu(self.root, tearoff=False, bg="white", fg="black", font=("Sego UI", 10))
        self.menu_docente.add_command(label="Agregar Docente", command=lambda: self.agregar_docentes())
        self.menu_docente.add_command(label="Consultar Docente", command=lambda: self.consultar_docente())
        
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
        self.profesor_controller = ProfesorController()
        self.curso_controller = CursoController()
        self.horario_controller = HorarioController()
        
        
    def submenu_curso(self, event=None):
        x = self.btn_cursos.winfo_rootx() + self.btn_cursos.winfo_width()
        y = self.btn_cursos.winfo_rooty()
        self.menu_cursos.tk_popup(x, y)
        
    def submenu_estudiante(self, event=None):
        x = self.btn_estudiante.winfo_rootx() + self.btn_estudiante.winfo_width()
        y = self.btn_estudiante.winfo_rooty()
        self.menu_estudiante.tk_popup(x, y)

    def submenu_docente(self, event=None):
        x = self.btn_docente.winfo_rootx() + self.btn_docente.winfo_width()
        y = self.btn_docente.winfo_rooty()
        self.menu_docente.tk_popup(x, y)

    def mostrar_inicio(self):
        self._actualizar_contenido("Bienvenido al sistema de gestión")

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
        
        label_identificacion = tk.Label(
            frame, text="Identificacion:",
            bg="white", font=('Arial Narrow', 12, 'bold')
        )
        label_identificacion.grid(row=1, column=0, sticky="e", padx=(150, 10), pady=10)
        
        self.identificacion_var = tk.StringVar()
        entry_identificacion = tk.Entry(
            frame, textvariable=self.identificacion_var,
            font=('Arial', 11), width=40
        )
        entry_identificacion.grid(row=1, column=1, padx=(10, 50), pady=10, sticky="w")

        label_nombre = tk.Label(
            frame, text="Nombre:",
            bg="white", font=('Arial Narrow', 12, 'bold')
        )
        label_nombre.grid(row=2, column=0, sticky="e", padx=(150, 10), pady=10)
        
        self.nombre_var = tk.StringVar()
        entry_nombre = tk.Entry(
            frame, textvariable=self.nombre_var,
            font=('Arial', 11), width=40
        )
        entry_nombre.grid(row=2, column=1, padx=(10, 50), pady=10, sticky="w")
        
        label_apellido = tk.Label(
            frame, text="Apellido:",
            bg="white", font=('Arial Narrow', 12, 'bold')
        )
        label_apellido.grid(row=3, column=0, sticky="e", padx=(50, 10), pady=10)

        self.apellido_var = tk.StringVar()
        entry_apellido = tk.Entry(
            frame, textvariable=self.apellido_var,
            font=('Arial', 11), width=40
        )
        entry_apellido.grid(row=3, column=1, padx=(10, 50), pady=10, sticky="w")
        
        label_fecha_nacimiento = tk.Label(
            frame, text="Fecha nacimiento:",
            bg="white", font=('Arial Narrow', 12, 'bold')
        )
        label_fecha_nacimiento.grid(row=4, column=0, sticky="e", padx=(50, 10), pady=10)

        self.fecha_nacimiento_var = tk.StringVar()
        entry_fecha_nacimiento = tk.Entry(
            frame, textvariable=self.fecha_nacimiento_var,
            font=('Arial', 11), width=40
        )
        entry_fecha_nacimiento.grid(row=4, column=1, padx=(10, 50), pady=10, sticky="w")
        
        label_correo_personal = tk.Label(
            frame, text="Correo personal:",
            bg="white", font=('Arial Narrow', 12, 'bold')
        )
        label_correo_personal.grid(row=5, column=0, sticky="e", padx=(50, 10), pady=10)

        self.correo_personal_var = tk.StringVar()
        entry_correo_personal = tk.Entry(
            frame, textvariable=self.correo_personal_var,
            font=('Arial', 11), width=40
        )
        entry_correo_personal.grid(row=5, column=1, padx=(10, 50), pady=10, sticky="w")
        
        label_correo_institucional = tk.Label(
            frame, text="Correo Institucional:",
            bg="white", font=('Arial Narrow', 12, 'bold')
        )
        label_correo_institucional.grid(row=6, column=0, sticky="e", padx=(50, 10), pady=10)

        self.correo_institucional_var = tk.StringVar()
        entry_correo_institucional = tk.Entry(
            frame, textvariable=self.correo_institucional_var,
            font=('Arial', 11), width=40
        )
        entry_correo_institucional.grid(row=6, column=1, padx=(10, 50), pady=10, sticky="w")
       
        self.boton_agregar = tk.Button(
            frame,
            text="Agregar Estudiante",
            font=("Arial", 11, 'bold'),
            bg="#27ae60", fg="white",
            padx=10, pady=5,
            command=lambda: self.insert_estudiante()
        )
        self.boton_agregar.grid(row=7, column=0, columnspan=2, pady=(20, 30))
        self.notebook.add(frame, text="Datos del Estudiante")
        self.notebook.select(frame)
        
    def agregar_curso(self):
        
        for widget in self.notebook.winfo_children():
            widget.destroy()

        frame = tk.Frame(self.notebook, bg="white")
        frame.columnconfigure(0, weight=0)
        frame.columnconfigure(1, weight=1)

        label = tk.Label(
            frame, text='Agregar curso',
            font=("Segoe UI", 14, "bold"), bg="white", fg="#2c3e50"
        )
        label.grid(row=0, column=0, columnspan=2, pady=(40))

        label_nombre = tk.Label(
            frame, text="Nombre:",
            bg="white", font=('Arial Narrow', 12, 'bold')
        )
        label_nombre.grid(row=1, column=0, sticky="e", padx=(150, 10), pady=10)
        
        self.nombre_var = tk.StringVar()
        entry_nombre = tk.Entry(
            frame, textvariable=self.nombre_var,
            font=('Arial', 11), width=40
        )
        entry_nombre.grid(row=1, column=1, padx=(10, 50), pady=10, sticky="w")
        
        label_docente = tk.Label(
            frame, text="Docente:",
            bg="white", font=('Arial Narrow', 12, 'bold')
        )
        label_docente.grid(row=2, column=0, sticky="e", padx=(150, 10), pady=10)
        
        cargar_drop = self.profesor_controller.cargar_drop_docente()
        self.diccionario = dict(cargar_drop)
            
        self.cb = ttk.Combobox(frame, values=list(self.diccionario.values()), font=('Arial', 11), width=40)
        self.cb.set("Seleccione docente")
        self.cb.grid(row=2, column=1, padx=(10, 50), pady=10, sticky="w")
        self.cb.bind("<<ComboboxSelected>>", self.al_cambiar)
        self.id_docente = next((k for k, v in self.diccionario.items() if v == self.cb.get()), None)
        self.boton_agregar = tk.Button(
            frame,
            text="Agregar Curso",
            font=("Arial", 11, 'bold'),
            bg="#27ae60", fg="white",
            padx=10, pady=5,
            command=lambda: self.curso_controller.registrar_curso(self.nombre_var.get(), self.id_docente)
        )
        self.boton_agregar.grid(row=6, column=0, columnspan=2, pady=(20, 30))

        self.notebook.add(frame, text="Curso")
        self.notebook.select(frame)
        
    def al_cambiar(self, event):
        seleccion = self.cb.get()
        self.id_docente = next((k for k, v in self.diccionario.items() if v == seleccion), None)
        
    def seleccionar_curso(self, event):
        seleccion = self.cb1.get()
        self.id_curso = next((k for k, v in self.diccionario.items() if v == seleccion), None)
        
    def seleccionar_dia_semana(self, event):
        seleccion = self.cb2.get()
        self.id_semana = next((k for k, v in self.diccionario_semana.items() if v == seleccion), None)
        
    def seleccionar_hora_inicio(self, event):
        seleccion = self.cb3.get()
        for c, v in  self.diccionario_horas_inicio.items():
            if str(v) == seleccion:
                self.id_hora_inicio = c        
        
    def seleccionar_hora_fin(self, event):
        seleccion = self.cb4.get()
        for c, v in  self.diccionario_horas_fin.items():
            if str(v) == seleccion:
                self.id_hora_fin = c
        
    def agregar_docentes(self):

        for widget in self.notebook.winfo_children():
            widget.destroy()

        frame = tk.Frame(self.notebook, bg="white")
        frame.columnconfigure(0, weight=0)
        frame.columnconfigure(1, weight=1)

        label = tk.Label(
            frame, text='Agregar docente',
            font=("Segoe UI", 14, "bold"), bg="white", fg="#2c3e50"
        )
        label.grid(row=0, column=0, columnspan=2, pady=(40))

        label_identificacion = tk.Label(
            frame, text="Identificacón:",
            bg="white", font=('Arial Narrow', 12, 'bold')
        )
        label_identificacion.grid(row=1, column=0, sticky="e", padx=(150, 10), pady=10)
        
        self.identificacion_var = tk.StringVar()
        entry_identificacion = tk.Entry(
            frame, textvariable=self.identificacion_var,
            font=('Arial', 11), width=40
        )
        entry_identificacion.grid(row=1, column=1, padx=(10, 50), pady=10, sticky="w")
        
        label_nombre = tk.Label(
            frame, text="Nombre:",
            bg="white", font=('Arial Narrow', 12, 'bold')
        )
        label_nombre.grid(row=2, column=0, sticky="e", padx=(150, 10), pady=10)
        
        self.nombre_var = tk.StringVar()
        entry_nombre = tk.Entry(
            frame, textvariable=self.nombre_var,
            font=('Arial', 11), width=40
        )
        entry_nombre.grid(row=2, column=1, padx=(10, 50), pady=10, sticky="w")
        
        label_apellido = tk.Label(
            frame, text="Apellido:",
            bg="white", font=('Arial Narrow', 12, 'bold')
        )
        label_apellido.grid(row=3, column=0, sticky="e", padx=(50, 10), pady=10)

        self.apellido_var = tk.StringVar()
        entry_apellido = tk.Entry(
            frame, textvariable=self.apellido_var,
            font=('Arial', 11), width=40
        )
        entry_apellido.grid(row=3, column=1, padx=(10, 50), pady=10, sticky="w")
        
        label_correo_personal = tk.Label(
            frame, text="Correo personal:",
            bg="white", font=('Arial Narrow', 12, 'bold')
        )
        label_correo_personal.grid(row=4, column=0, sticky="e", padx=(50, 10), pady=10)

        self.correo_personal_var = tk.StringVar()
        entry_correo_personal = tk.Entry(
            frame, textvariable=self.correo_personal_var,
            font=('Arial', 11), width=40
        )
        entry_correo_personal.grid(row=4, column=1, padx=(10, 50), pady=10, sticky="w")
        
        label_correo_institucional = tk.Label(
            frame, text="Correo Institucional:",
            bg="white", font=('Arial Narrow', 12, 'bold')
        )
        label_correo_institucional.grid(row=5, column=0, sticky="e", padx=(50, 10), pady=10)

        self.correo_institucional_var = tk.StringVar()
        entry_correo_institucional = tk.Entry(
            frame, textvariable=self.correo_institucional_var,
            font=('Arial', 11), width=40
        )
        entry_correo_institucional.grid(row=5, column=1, padx=(10, 50), pady=10, sticky="w")
        
        label_especialidad = tk.Label(
            frame, text="Especialidad:",
            bg="white", font=('Arial Narrow', 12, 'bold')
        )
        label_especialidad.grid(row=6, column=0, sticky="e", padx=(50, 10), pady=10)

        self.especialidad_var = tk.StringVar()
        entry_especialidad_var = tk.Entry(
            frame, textvariable=self.especialidad_var,
            font=('Arial', 11), width=40
        )
        entry_especialidad_var.grid(row=6, column=1, padx=(10, 50), pady=10, sticky="w")
        
        self.boton_agregar = tk.Button(
            frame,
            text="Agregar Docentes",
            font=("Arial", 11, 'bold'),
            bg="#27ae60", fg="white",
            padx=10, pady=5,
            command=lambda: self.insert_docentes()
        )
        self.boton_agregar.grid(row=7, column=0, columnspan=2, pady=(20, 30))
        self.notebook.add(frame, text="Datos del Docente")
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
            
        self.estudiantes =  ttk.Treeview(self.frame, columns=("Identificación", "Nombre", "Apellido", 'Fecha Nacimiento', 'Correo Personal', 'Correo Institucional'), show="headings")
        self.estudiantes.heading("Identificación", text="Identificación")
        self.estudiantes.heading("Nombre", text="Nombre")
        self.estudiantes.heading("Apellido", text="Apellido")
        self.estudiantes.heading("Fecha Nacimiento", text="Fecha Nacimiento")
        self.estudiantes.heading("Correo Personal", text="Correo Personal")
        self.estudiantes.heading("Correo Institucional", text="Correo Institucional")
        self.estudiantes.grid(row=3, column=0, columnspan=2)
        
        for item in self.estudiantes.get_children():
            self.estudiantes.delete(item)
        
        for estudiante in response:
            self.estudiantes.insert('', 'end', values=(
                estudiante[1],
                estudiante[2],
                estudiante[3],
                estudiante[4],
                estudiante[5]
            ))
    
    def consultar_docente(self):
        for widget in self.notebook.winfo_children():
            widget.destroy()
            
        self.frame = tk.Frame(self.notebook, bg="white")
        self.frame.columnconfigure(0, weight=0)
        self.frame.columnconfigure(1, weight=1)
        
        label = tk.Label(
            self.frame, text='Consultar Docentes',
            font=("Segoe UI", 14, "bold"), bg="white", fg="#2c3e50"
        )
        label.grid(row=0, column=0, columnspan=2, pady=(40))
        
        label_identificacion = tk.Label(
            self.frame, text="ID Docente:",
            bg="white", font=('Arial Narrow', 12, 'bold')
        )
        label_identificacion.grid(row=1, column=0, sticky="e", padx=(50, 10), pady=10)
        
        self.identificacion_var = tk.StringVar()
        entry_identificacion = tk.Entry(
            self.frame, textvariable=self.identificacion_var,
            font=('Arial', 11), width=40
        )
        entry_identificacion.grid(row=1, column=1, padx=(10, 50), pady=10, sticky="w")
        
        self.boton_consultar = tk.Button(
            self.frame,
            text="Consultar",
            font=("Arial", 11, 'bold'),
            bg="#27ae60", fg="white",
            padx=10, pady=5,
            command=lambda: self.data_grid_mostrar_docente()
        )
        self.boton_consultar.grid(row=4, column=0, columnspan=2, pady=(20, 30))
        self.notebook.add(self.frame, text="Consultar Docente")
        self.notebook.select(self.frame)
        
        
    def data_grid_mostrar_docente(self):
    
        identificacion = self.identificacion_var.get()
        print(identificacion)
        if identificacion != '':
            response = self.profesor_controller.consultar_docente_curso()
        else:
            response = self.profesor_controller.consultar_docente_curso()
            
        if len(response) > 0:
            
            self.dataGrid =  ttk.Treeview(self.frame, columns=("identificacionProfesor", 
                                                                "nombreProfesor",
                                                                "correoInstitucional",
                                                                "descripcionCurso"), show="headings")
            self.dataGrid.heading("identificacionProfesor", text="Identificación")
            self.dataGrid.heading("nombreProfesor", text="Nombre")
            self.dataGrid.heading("correoInstitucional", text="Correo Institucional")
            self.dataGrid.heading("descripcionCurso", text="Descripción Curso")
            self.dataGrid.grid(row=3, column=0, columnspan=2)
        else:
            messagebox.showinfo("Consulta", "En el momento no se encuentran docentes registrados a un curso.")
        
        for item in self.dataGrid.get_children():
            self.dataGrid.delete(item)
        
        for item in response:
            self.dataGrid.insert('', 'end', values=(
                item[1],
                item[2] + ' ' + item[3],
                item[5],
                item[6]
            ))
            
    def agregar_horario(self):

        for widget in self.notebook.winfo_children():
            widget.destroy()

        frame = tk.Frame(self.notebook, bg="white")
        frame.columnconfigure(0, weight=0)
        frame.columnconfigure(1, weight=1)
        
        label = tk.Label(
            frame, text='Agregar Horario',
            font=("Segoe UI", 14, "bold"), bg="white", fg="#2c3e50"
        )
        label.grid(row=0, column=0, columnspan=2, pady=(40))
        
        cargar_drop = self.curso_controller.cargar_drop_curso()
        self.diccionario = dict(cargar_drop)
        
        self.cb1 = ttk.Combobox(frame, values=list(self.diccionario.values()), font=('Arial', 11), width=40)
        self.cb1.set("Seleccione curso")
        self.cb1.grid(row=2, column=1, padx=(240, 50), pady=10, sticky="w")
        self.cb1.bind("<<ComboboxSelected>>", self.seleccionar_curso)
        self.id_curso = next((k for k, v in self.diccionario.items() if v == self.cb1.get()), None)
        
        cargar_drop_semana = self.curso_controller.cargar_drop_semanas()
        self.diccionario_semana = dict(cargar_drop_semana)
        
        self.cb2 = ttk.Combobox(frame, values=list(self.diccionario_semana.values()), font=('Arial', 11), width=40)
        self.cb2.set("Seleccione dia")
        self.cb2.grid(row=3, column=1, padx=(240, 50), pady=10, sticky="w")
        self.cb2.bind("<<ComboboxSelected>>", self.seleccionar_dia_semana)
        self.id_semana = next((k for k, v in self.diccionario_semana.items() if v == self.cb2.get()), None)
        
        cargar_drop_horas_inicio = self.curso_controller.cargar_drop_horas()
        self.diccionario_horas_inicio = dict(cargar_drop_horas_inicio)
        
        self.cb3 = ttk.Combobox(frame, values=list(self.diccionario_horas_inicio.values()), font=('Arial', 11), width=40)
        self.cb3.set("Seleccione Hora inicio")
        self.cb3.grid(row=4, column=1, padx=(240, 50), pady=10, sticky="w")
        self.cb3.bind("<<ComboboxSelected>>", self.seleccionar_hora_inicio)
        self.id_hora_inicio = next((k for k, v in self.diccionario_horas_inicio.items() if v == self.cb3.get()), None)
        
        cargar_drop_horas_fin = self.curso_controller.cargar_drop_horas()
        self.diccionario_horas_fin = dict(cargar_drop_horas_fin)
        
        self.cb4 = ttk.Combobox(frame, values=list(self.diccionario_horas_fin.values()), font=('Arial', 11), width=40)
        self.cb4.set("Seleccione hora fin")
        self.cb4.grid(row=5, column=1, padx=(240, 50), pady=10, sticky="w")
        self.cb4.bind("<<ComboboxSelected>>", self.seleccionar_hora_fin)
        self.id_hora_fin = next((k for k, v in self.diccionario_horas_fin.items() if v == self.cb4.get()), None)

        
        
        self.boton_agregar = tk.Button(
            frame,
            text="Agregar Horario",
            font=("Arial", 11, 'bold'),
            bg="#27ae60", fg="white",
            padx=10, pady=5,
            command=lambda: self.horario_controller.registrar_horario(self.id_curso, 
                                                                    self.id_semana,
                                                                    self.id_hora_inicio, 
                                                                    self.id_hora_fin)
        )
        self.boton_agregar.grid(row=7, column=0, columnspan=2, pady=(20, 30))

        self.notebook.add(frame, text="Datos del Docente")
        self.notebook.select(frame)
        
    def insert_estudiante(self):
        self.estudiante_controller.registrar_estudiante(self.identificacion_var.get(),
                                                        self.nombre_var.get(), 
                                                        self.apellido_var.get(),
                                                        self.fecha_nacimiento_var.get(),
                                                        self.correo_personal_var.get(),
                                                        self.correo_institucional_var.get())
        self.limpiar_campos()
        
    def insert_docentes(self):
        self.profesor_controller.registrar_profesor(self.identificacion_var.get(), 
                                                                        self.nombre_var.get(), 
                                                                        self.apellido_var.get(), 
                                                                        self.correo_personal_var.get(), 
                                                                        self.correo_institucional_var.get(), 
                                                                        self.especialidad_var.get())
        self.limpiar_campos()
        
    def limpiar_campos(self):
        if hasattr(self, "identificacion_var"):
            self.identificacion_var.set("")
        if hasattr(self, "nombre_var"):
            self.nombre_var.set("")
        if hasattr(self, "apellido_var"):
            self.apellido_var.set("")
        if hasattr(self, "fecha_nacimiento_var"):
            self.fecha_nacimiento_var.set("")
        if hasattr(self, "correo_personal_var"):
            self.correo_personal_var.set("")
        if hasattr(self, "correo_institucional_var"):
            self.correo_institucional_var.set("")
        if hasattr(self, "especialidad_var"):
            self.especialidad_var.set("")
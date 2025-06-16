drop database academia;
CREATE DATABASE IF NOT EXISTS academia;
USE academia;

CREATE TABLE Estudiantes (
    idEstudiante INT AUTO_INCREMENT PRIMARY KEY,
    identificacionEstudiante VARCHAR(100) UNIQUE,
    nombreEstudiante VARCHAR(100) NOT NULL,
    apellidoEstudiante VARCHAR(100),
    fechaNacimientoEstudiante DATE,
    correoPersonalEstudiante VARCHAR(100),
    correoInstitucionalEstuadiante varchar(100)
);

CREATE TABLE Profesores (
    idProfesor INT AUTO_INCREMENT PRIMARY KEY,
    identificacionProfesor VARCHAR(100) UNIQUE,
    nombreProfesor VARCHAR(100),
    apellidoProfesor varchar(100),
    correoPersonal VARCHAR(100) UNIQUE NOT NULL,
    correoInstitucional varchar(100),
    especialidad VARCHAR(100)
);

CREATE TABLE Cursos (
    idCurso INT AUTO_INCREMENT PRIMARY KEY,
    descripcionCurso VARCHAR(100) NOT NULL,
    idProfesor INT,
    FOREIGN KEY (idProfesor) REFERENCES Profesores(idProfesor)
);

CREATE TABLE Matriculas (
    idMatricula INT AUTO_INCREMENT PRIMARY KEY,
    idEstudiante INT,
    idCurso INT,
    fechaMatricula DATETIME,
    FOREIGN KEY (idEstudiante) REFERENCES Estudiantes(idEstudiante),
    FOREIGN KEY (idCurso) REFERENCES Cursos(idCurso)
);

CREATE TABLE Semana (
	idSemana INT AUTO_INCREMENT PRIMARY KEY,
    diaSemana VARCHAR(50) UNIQUE
);

CREATE TABLE Hora (
	idHora INT AUTO_INCREMENT PRIMARY KEY,
    Hora TIME UNIQUE
);

CREATE TABLE Horarios (
    idHorario INT AUTO_INCREMENT PRIMARY KEY,
    idCurso INT,
    idDiaSemana INT  NOT NULL,
    idHoraInicio INT NOT NULL,
    idHoraFin INT NOT NULL,
    FOREIGN KEY (idCurso) REFERENCES Cursos(idCurso),
    FOREIGN KEY (idHoraInicio) REFERENCES Hora(idHora),
    FOREIGN KEY (idHoraFin) REFERENCES Hora(idHora),
    FOREIGN KEY (idDiaSemana) REFERENCES Semana(idSemana)
);

INSERT INTO semana (idSemana,diaSemana) VALUES(1,'Lunes');
INSERT INTO semana (idSemana,diaSemana) VALUES(2,'Martes');
INSERT INTO semana (idSemana,diaSemana) VALUES(3,'Miercoles');
INSERT INTO semana (idSemana,diaSemana) VALUES(4,'Jueves');
INSERT INTO semana (idSemana,diaSemana) VALUES(5,'Viernes');
INSERT INTO semana (idSemana,diaSemana) VALUES(6,'Sabado');
INSERT INTO semana (idSemana,diaSemana) VALUES(7,'Domingo');


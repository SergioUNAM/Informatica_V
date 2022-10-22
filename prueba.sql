-- Crear una base de datos llamada estudiantes
CREATE DATABASE estudiantes;

-- Crear una tabla llamada alumnos
CREATE TABLE alumnos (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

-- Insertar datos en la tabla alumnos
INSERT INTO alumnos (nombre, apellido) VALUES ('Juan', 'Perez');

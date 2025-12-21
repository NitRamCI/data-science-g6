CREATE Table alumno(
    id_alumno INT NOT NULL primary key AUTO_INCREMENT,
    nro_documento VARCHAR(20) NOT NULL,
    nombre VARCHAR(225) NOT NULL,
    email VARCHAR(100)

);

#alterar una tabla

ALTER Table alumno
ADD COLUMN nota int DEFAULT 0;

#eliminar una tabla
DROP TABLE alumno;


INSERT INTO alumno (nombre, nro_documento, email) VALUES ('martin', '12345678', 'martin@gmail.com');


SELECT * FROM alumno;

CREATE TABLE empresa(id int not NULL primary key AUTO_INCREMENT COMMENT 'primary key', ruc VARCHAR(12) NOT NULL UNIQUE, nombre VARCHAR(225) NOT NULL, direccion TEXT);

INSERT INTO alumno (nombre, nro_documento, email) VALUES
('juan', '87654321', 'juan @gmail.com'),
('ana', '11223344', 'ana@gmail.com'),   
('lucia', '44332211', 'luis@gmail.com'),
('carlos', '55667788', 'carlos@gmail.com'),
('maria', '88776655', 'maria@gmail.com');

UPDATE alumno SET email = 'carlos@gmail.com' WHERE id = 4;

SELECT * from alumno;

SELECT nombre, email FROM alumno WHERE nro_documento = '11223344';


create Table cursos(
    id_curso int not null PRIMARY KEY AUTO_INCREMENT,
    nombre varchar(200) not NULL);


INSERT into cursos(nombre) VALUES
('Matematica'),
('Fisica'),
('Quimica'),
('Biologia'),
('Historia');

create table registro_matricula(
    id_matricula INT not NULL PRIMARY KEY AUTO_INCREMENT,
    id_alumno int not NULL,
    id_curso int not NULL,
    fecha_matricula date NOT NULL,
    FOREIGN KEY (id_alumno) REFERENCES alumno(id_alumno),
    FOREIGN key (id_curso) REFERENCES cursos(id_curso)
);

ALTER TABLE alumno
CHANGE id id_alumno INT NOT NULL AUTO_INCREMENT;

CREATE Table alumno(
    id INT NOT NULL primary key AUTO_INCREMENT,
    nro_documento VARCHAR(20) NOT NULL,
    nombre VARCHAR(225) NOT NULL,
    email VARCHAR(100)

);

#alterar una tabla

ALTER Table alumno
ADD COLUMN nota int DEFAULT 0;

#eliminar una tabla
DROP TABLE alumno;

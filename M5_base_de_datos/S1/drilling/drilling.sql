-- Crear una base de datos desde el Shell de PostgreSQL, llamada nuevo_curso.
CREATE DATABASE nuevo_curso;
-- Crear 3 usuarios desde el Shell de PostgreSQL.
CREATE USER usuario1 WITH PASSWORD '123';
CREATE USER usuario2 WITH PASSWORD '123';
CREATE USER usuario3 WITH PASSWORD '123';
-- Listar la nueva base de datos creada desde el Shell de postgreSQL.
\l
-- Ingresar a la base de datos desde el Shell de postgreSQL.
\c nuevo_curso

DROP USER usuario1;

DROP DATABASE nuevo_curso;

--------------------------------------------
-- Variables de entorno para windows
--------------------------------------------
C:\Program Files\PostgreSQL\{version}\bin
C:\Program Files\PostgreSQL\{version}\lib

C:\Program Files\PostgreSQL\15\bin
C:\Program Files\PostgreSQL\15\lib
--------------------------------------------
--conectar a la base de datos desde psql shell
--------------------------------------------
Server [localhost]: localhost (127.0.0.1)
Database [postgres]: postgres
Port [5432]: 5432
Username [postgres]: postgres
Contraseña para usuario postgres: <PASSWORD> al instalar la base de datos

-----------------------------------------------
-- Conectarse a la base de datos desde cualquier terminal, necesario tener las variables de entorno
-----------------------------------------------
psql -U {username} -W -d {database_name}
psql -U postgres -W -d postgres

-----------------------------------------------
-- Comandos básicos de psql
-----------------------------------------------
help                         | ayuda general
\l                           | listar las bases de datos
\dt                          | listar las tablas de una base de datos      
\du                          | listar los usuarios de una base de datos
\copyright                   | para ver los términos de distribución
\h                           | para ayuda de órdenes SQL
\?                           | para ayuda de órdenes psql
\g                           |o punto y coma («;») para ejecutar la consulta
\q                           | salir del shell
\c {database_name}           | conectarse a una base de datos
q                            | salir

--Lenguaje SQL: Lenguaje de consulta estructurada (Structured Query Language)
-- agregar ; para ejecutar la consulta al final de cada sentencia

- Crear una base de datos desde el Shell de PostgreSQL.
CREATE DATABASE {database_name};
CREATE database {database_name};
CREATE database database_test;
CREATE DATABASE database_test;
create database database_test;

- Borrar una base de datos desde el Shell de PostgreSQL.
DROP DATABASE {database_name};
DROP DATABASE database_test;

- Crear 1 usuario desde el Shell de PostgreSQL.
CREATE USER {username} WITH PASSWORD '{<PASSWORD>}';

- Borrar un usuario desde el Shell de PostgreSQL.
DROP USER {username};

- Listar la nueva base de datos creada desde el Shell de postgreSQL.
\l

- Ingresar a la base de datos desde el Shell de postgreSQL.
\c {database_name}
\c database_test
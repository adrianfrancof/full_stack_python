--TABLA categorias
--PK categoria_id, nombre

--Tabla productos
-- PK producto_id, nombre, precio, FK categoria_id

CREATE DATABASE S2;

CREATE TABLE categorias(
    categoria_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50)
);

CREATE TABLE productos(
    producto_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    precio INT,
    categoria INT,
     --FOREIGN KEY campo_tabla_actual REFERENCES tabla_referencia(campo_referencia)
    FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id)
);

-- Insercción de registros única, uno en uno cada registro
INSERT INTO categorias(nombre) VALUES('ELECTRÓNICA');
INSERT INTO categorias(nombre) VALUES('ROPA');
INSERT INTO categorias(nombre) VALUES('HOGAR');

-- Insercción de registros múltiples, todos los registros en una query
INSERT INTO productos(nombre, precio, categoria_id) VALUES
-- (nombre, precio, categoria_id),
('Teléfono', 100000, 1), --atributos de la tabla separados con comas
('Televisión', 150000, 1),
('Pantalon', 15000, 2),
('Polera', 20000,2),
('Tetera',50000, 3),
('Mesa', 90000, 3);

-- consultar todas las filas de la tabla categorias
SELECT * FROM categorias;

-- consultar todas las finas de la tabla productos
SELECT * FROM productos;

-- eliminar tabla a traves de comandos
-- para eliminar una tabla se debe comenzar por la tabla con mas referencias o claves foraneas y luego borrar las tablas que tienen menos referencias o claves foraneas.
DROP TABLE productos;
DROP TABLE categorias;
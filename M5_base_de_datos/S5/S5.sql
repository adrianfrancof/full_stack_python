-- Empresa
CREATE TABLE empresa(
    rut VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(120),
    direccion VARCHAR(120),
    telefono VARCHAR(15),
    correo VARCHAR(80),
    web VARCHAR(50)
);

-- Cliente
CREATE TABLE cliente(
    rut VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(120),
    correo VARCHAR(80),
    direccion VARCHAR(120),
    celular VARCHAR(15)
);

-- Herramienta
CREATE TABLE herramienta(
    id_herramienta INT PRIMARY KEY,
    nombre VARCHAR(120),
    precio_dia INT
);

-- Arriendo
CREATE TABLE arriendo(
    folio INT PRIMARY KEY,
    fecha DATE,
    dias INT,
    valor_dia INT,
    garantia VARCHAR(30),
    id_herramienta INT,
    rut_cliente VARCHAR(10)
);

ALTER TABLE {tabla} ADD CONSTRAINT fk_{tabla}_{nombre_atributo} FOREIGN KEY ({nombre_atributo}) REFERENCES {tabla_referencia}({{nombre_atributo_referencia}});

ALTER TABLE arriendo ADD CONSTRAINT fk_arriendo_id_herramienta FOREIGN KEY (id_herramienta) REFERENCES herramienta(id_herramienta);

ALTER TABLE arriendo ADD CONSTRAINT fk_arriendo_rut_cliente FOREIGN KEY (rut_cliente) REFERENCES cliente(rut);

COMMIT;

BEGIN --inicio de transacción


SAVEPOINT primero; --guarda el estado actual de la base de datos
-- 1.- Inserte los datos de una empresa
INSERT into empresa VALUES
('11111111-1','Arrienda Herramientas','0123 Avenida Real',1234567890,'datosarriendo@herramientas.es','arrimientas.es');

SAVEPOINT segundo;

-- 2.- Inserte 5 herramientas
INSERT into herramienta VALUES
(1,'Taladro Electrico',10000),
(2,'Cierra Electrica',20000),
(3,'Pistola de Clavos',30000),
(4,'Lijadora',40000),
 (5,'Serrucho Electrico',50000);

ROLLBACK TO SAVEPOINT primero;
ROLLBACK TO SAVEPOINT segundo;


BEGIN --inicio de transacción

SAVEPOINT primero;
-- 3.- Inserte 3 clientes							  
INSERT into cliente VALUES
('22222222-2','Juan Perez','j.perez@mail.com','1 Calle Uno',2222222222),
('33333333-3','Juanita Sánches','j.sanches@mail.com','2 Calle Dos',3333333333),
('44444444-4','Marcelo Ugarte','m.ugarte@mail.com','3 Calle Tres',4444444444);

SAEPOINT segundo;

-- 4. Elimina el ultimo cliente
DELETE FROM {tabla} WHERE {atributo_campo} = {valor};
DELETE FROM cliente WHERE rut = '44444444-4';

SAVEPOINT tercero;

-- 5. Elimina la primera herramienta
DELETE FROM herramienta WHERE id_herramienta = 1;

SAVEPOINT cuarto;

-- 6.- Inserte 2 arriendos para cada cliente
INSERT into arriendo (folio, fecha, dias, valor_dia, garantia, id_herramienta, rut_cliente) 
VALUES
(1,'12/11/22',5,20000,'Eficacia en 5 dias o menos',2,'22222222-2'),
(2,'12/11/22',2,30000,'Eficacia en 2 dias o menos',3,'22222222-2'),
(3,'12/11/22',1,40000,'Eficacia en 1 dia',4,'33333333-3'),
(4,'12/11/22',3,40000,'Eficacia en solo 3 dias',4,'33333333-3');

SAVEPOINT quinto;

-- 7. Modifique el correo del primer cliente
UPDATE cliente SET correo = 'jperez@mail.com' WHERE rut = '22222222-2';

SAVEPOINT sexto;

-- 8. Liste todas las herramientas
SELECT * FROM herramienta;

-- 9. Liste todos los arriendos del cliente '33333333-3'
SELECT * FROM arriendo WHERE rut_cliente = '33333333-3';

-- 10. Liste los clientes cuyo nombre contenga la letra 'a'
SELECT * FROM cliente WHERE nombre LIKE '%a%';
SELECT * FROM cliente WHERE UPPER(nombre) LIKE '%A%';
SELECT * FROM cliente WHERE LOWER(nombre) LIKE '%a%';

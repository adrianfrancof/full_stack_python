-- Tabla empresa

BEGIN;
CREATE TABLE empresa(
    rut VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(50),
    direccion VARCHAR(255),
    telefono VARCHAR(14),
    correo VARCHAR(255),
    web VARCHAR(255)
);

 -- Tabla cliente
CREATE TABLE cliente(
    rut VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(50),
    correo VARCHAR(255),
    direccion VARCHAR(255),
    telefono VARCHAR(14),
    alta BOOLEAN
);

 -- Tabla tipo_vehiculo
CREATE TABLE tipo_vehiculo(
    id_tipo_vehiculo SERIAL PRIMARY KEY,
    nombre VARCHAR(255)
);

 -- Tabla mantencion
CREATE TABLE mantencion(
    id_mantencion SERIAL PRIMARY KEY,
    fecha DATE,
    trabajos_realizados VARCHAR(255),
    folio INT -- CONSTRAINT fk_mantencion_folio FOREIGN KEY (folio) REFERENCES venta(folio)
);

 -- Tabla Venta
CREATE TABLE venta(
    folio SERIAL PRIMARY KEY,
    fecha DATE,
    monto INT,
    rut_cliente VARCHAR(10), -- CONSTRAINT fk_venta_rut_cliente FOREIGN KEY (rut_cliente) REFERENCES cliente(rut_cliente);
    id_vehiculo INT -- CONSTRAINT fk_venta_id_vehiculo FOREIGN KEY (id_vehiculo) REFERENCES vehiculo(id_vehiculo);
);

 -- Tabla vehiculo
CREATE TABLE vehiculo(
    id_vehiculo SERIAL PRIMARY KEY,
    patente VARCHAR(10),
    marca VARCHAR(50),
    modelo VARCHAR(50),
    color VARCHAR(50),
    precio INT,
    frecuencia_mantencion INT,
    id_marca INT, -- CONSTRAINT fk_vehiculo_id_marca FOREIGN KEY (id_marca) REFERENCES marca(id_marca);
    id_tipo_vehiculo INT -- CONSTRAINT fk_vehiculo_id_tipo_vehiculo FOREIGN KEY (id_tipo_vehiculo) REFERENCES tipo_vehiculo(id_tipo_vehiculo);
);

 -- Tabla marca
CREATE TABLE marca(
    id_marca SERIAL PRIMARY KEY,
    nombre VARCHAR(50)
);

-- Alterar las tablas luego de la creación para agregar las claves foraneas
--ALTER TABLE {nombre_tabla} ADD CONSTRAINT fk_{nombre_tabla}_{campo_referencia} FOREIGN KEY (campo_referencia) REFERENCES {tabla_externa}(campo_referencia_tabla_externa);
ALTER TABLE mantencion ADD CONSTRAINT fk_mantencion_folio FOREIGN KEY (folio) REFERENCES venta(folio);

ALTER TABLE venta ADD CONSTRAINT fk_venta_rut_cliente FOREIGN KEY (rut_cliente) REFERENCES cliente(rut);
ALTER TABLE venta ADD CONSTRAINT fk_venta_id_vehiculo FOREIGN KEY (id_vehiculo) REFERENCES vehiculo(id_vehiculo);

ALTER TABLE vehiculo ADD CONSTRAINT fk_vehiculo_id_marca FOREIGN KEY (id_marca) REFERENCES marca(id_marca);
ALTER TABLE vehiculo ADD CONSTRAINT fk_vehiculo_id_tipo_vehiculo FOREIGN KEY (id_tipo_vehiculo) REFERENCES tipo_vehiculo(id_tipo_vehiculo);


INSERT INTO empresa (rut, nombre, direccion, telefono, correo, web) VALUES
('11111111-1', 'Empresa 1', 'Av. Principal 123', '987654321', 'contacto@empresa1.cl', 'www.empresa1.cl'),
('22222222-2', 'Empresa 2', 'Calle Secundaria 456', '912345678', 'contacto@empresa2.cl', 'www.empresa2.cl');

INSERT INTO cliente (rut, nombre, correo, direccion, telefono, alta) VALUES
('33333333-3', 'Juan Pérez', 'juan.perez@gmail.com', 'Calle A 789', '987654321', true),
('44444444-4', 'Ana Gómez', 'ana.gomez@gmail.com', 'Av. B 321', '912345678', true);


INSERT INTO marca (id_marca, nombre) VALUES
(1, 'Toyota'),
(2, 'Honda'),
(3, 'Ford');

INSERT INTO tipo_vehiculo (id_tipo_vehiculo, nombre) VALUES
(1, 'Sedán'),
(2, 'SUV'),
(3, 'Camioneta');

INSERT INTO vehiculo (id_vehiculo, patente, marca, modelo, color, precio, frecuencia_mantencion, id_marca, id_tipo_vehiculo) VALUES
(1, 'ABC123', 'Corolla', '2020', 'Rojo', 15000, 6, 1, 1),
(2, 'DEF456', 'Civic', '2019', 'Negro', 18000, 6, 2, 1),
(3, 'GHI789', 'Ranger', '2020', 'Blanco', 25000, 12 , 3, 3);

INSERT INTO venta (folio, fecha, monto, rut_cliente, id_vehiculo) VALUES
(1001, '2020-01-10', 15000, '33333333-3', 1),
(1002, '2020-01-15', 18000, '44444444-4', 2);

INSERT INTO mantencion (id_mantencion, fecha, trabajos_realizados, folio) VALUES
(1, '2020-06-10', 'Cambio de aceite', 1001),
(2, '2020-06-20', 'Revisión general', 1002);

-- Tabla empresa
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

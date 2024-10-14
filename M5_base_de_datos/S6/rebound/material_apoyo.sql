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
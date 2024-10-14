Transacciones con PostgreSQL:

PostgreSQL admite transacciones para garantizar la integridad de los datos y mantener la consistencia de la base de datos.
--------------------------------------------------------------------

Propiedades ACID:

Atomicidad: Una transacción se considera atómica, lo que significa que todas las operaciones dentro de una transacción se realizan como una unidad indivisible. Si alguna operación dentro de la transacción falla, todas las operaciones se deshacen (rollback), y si todas las operaciones tienen éxito, se confirman (commit).

Consistencia: Las transacciones en PostgreSQL deben mantener la consistencia de la base de datos. Esto significa que las transacciones deben llevar la base de datos desde un estado válido a otro estado válido, sin violar las restricciones de integridad definidas en la base de datos.

Aislamiento: La propiedad de aislamiento garantiza que cada transacción se ejecute de manera aislada de otras transacciones concurrentes. Esto evita que las transacciones interfieran entre sí y garantiza la coherencia de los datos.

Durabilidad: Una vez que una transacción ha sido confirmada (commit), sus cambios se vuelven permanentes y se mantendrán incluso en caso de fallos del sistema o reinicios posteriores.

--------------------------------------------------------------------
DCL (Data Control Language):
El DCL se utiliza en PostgreSQL para controlar los permisos y privilegios en la base de datos. 

GRANT: Concede privilegios a los usuarios o roles sobre objetos de base de datos.
REVOKE: Revoca los privilegios previamente otorgados a los usuarios o roles sobre objetos de base de datos.

--------------------------------------------------------------------
TCL (Transaction Control Language):
El TCL se utiliza en PostgreSQL para controlar las transacciones y los cambios en la base de datos

BEGIN: Inicia una transacción explícitamente.

COMMIT: Confirma una transacción, guardando los cambios realizados.

ROLLBACK: Deshace una transacción, revirtiendo los cambios realizados.

SAVEPOINT: Establece un punto de guardado dentro de una transacción, lo que permite deshacer solo parte de los cambios realizados.

RELEASE SAVEPOINT: Elimina un punto de guardado previamente establecido.

ROLLBACK TO SAVEPOINT: Deshace los cambios realizados después de un punto de guardado específico, sin deshacer los cambios anteriores a ese punto.

-- Confirmación automatica de transacción



















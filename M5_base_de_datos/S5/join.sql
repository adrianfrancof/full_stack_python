INNER JOIN: El INNER JOIN se utiliza para combinar las filas 
de dos o más tablas en función de una condición de coincidencia. 
Devuelve solo las filas que tienen una coincidencia en ambas tablas.

SELECT *
FROM tabla1
INNER JOIN tabla2 ON tabla1.columna = tabla2.columna;

--------------------------------------------------------------------------------------------------------

LEFT JOIN (o LEFT OUTER JOIN): El LEFT JOIN se utiliza para combinar todas las filas 
de la tabla izquierda con las filas coincidentes de la tabla derecha. 
Si no hay una coincidencia en la tabla derecha, se devolverá NULL para los campos de la tabla derecha.

SELECT *
FROM tabla1
LEFT JOIN tabla2 ON tabla1.columna = tabla2.columna;

--------------------------------------------------------------------------------------------------------

RIGHT JOIN (o RIGHT OUTER JOIN): El RIGHT JOIN se utiliza para combinar todas las filas 
de la tabla derecha con las filas coincidentes de la tabla izquierda.
Si no hay una coincidencia en la tabla izquierda, se devolverá NULL para los campos de la tabla izquierda.

SELECT *
FROM tabla1
RIGHT JOIN tabla2 ON tabla1.columna = tabla2.columna;

--------------------------------------------------------------------------------------------------------

FULL JOIN (o FULL OUTER JOIN): El FULL JOIN se utiliza para combinar todas las filas de ambas tablas, 
incluyendo las filas que no tienen coincidencias en la otra tabla. 
Si no hay una coincidencia, se devolverá NULL para los campos correspondientes de la tabla opuesta.

SELECT *
FROM tabla1
FULL JOIN tabla2 ON tabla1.columna = tabla2.columna;

--------------------------------------------------------------------------------------------------------
Es importante tener en cuenta que los operadores OUTER JOIN (LEFT OUTER JOIN, RIGHT OUTER JOIN y FULL OUTER JOIN) 
son compatibles en PostgreSQL y se pueden utilizar para realizar consultas que involucren combinaciones externas izquierdas, derechas o completas. 
El operador OUTER es opcional y se puede omitir en las cláusulas JOIN. Por ejemplo, LEFT JOIN y LEFT OUTER JOIN son equivalentes en PostgreSQL.


--Obtener los clientes que no tienen órdenes asociadas
--Obtener los clientes que tienen órdenes asociadas
--Obtener los artículos que no han sido incluidos en ninguna orden
--Obtener las órdenes realizadas por clientes que pertenecen a una ciudad específica
--Obtener todas las órdenes junto con la información del cliente y el artículo correspondiente
--Obtener los clientes que han realizado órdenes de un artículo específico
--Obtener el total gastado por cada cliente en todas las órdenes
--Obtener los clientes que no han realizado ninguna orden
--Obtener los artículos con su precio y el número de órdenes en las que se han vendido



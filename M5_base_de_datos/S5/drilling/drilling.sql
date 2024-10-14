--1. crear base de datos peliculas
CREATE DATABASE peliculas;

--2. crear tablas basadas en archivos.csv
BEGIN;
CREATE TABLE peliculas(
    id INT PRIMARY KEY,
    pelicula VARCHAR(255),
    estreno INT,
    director VARCHAR(255)
);

CREATE TABLE reparto(
    id_pelicula INT,
    actor VARCHAR(255),
    CONSTRAINT fk_reparto_id_peliculas 
    FOREIGN KEY (id_pelicula) REFERENCES peliculas(id)
);
COMMIT;

--3. cargar datos a las tablas, poblar tabla peliculas y reparto
-- desde consola con psql
\COPY "peliculas" FROM 'C:\Users\{usuario}\peliculas.csv' WITH CSV;
\COPY "reparto" FROM 'C:\Users\{usuario}\reparto.csv' WITH CSV;

-- 7. Listar todos los actores que aparecen en la película Titanic. indicando pelicula, estreno, director, reparto
SELECT pelicula, estreno, director, actor 
FROM peliculas
JOIN reparto
ON peliculas.id = reparto.id_pelicula
WHERE pelicula = 'Titanic';

-- con alias
SELECT p.pelicula, p.estreno, p.director, r.actor 
FROM peliculas AS p
JOIN reparto as r
ON p.id = r.id_pelicula
WHERE pelicula = 'Titanic';

-- 8. Listar los 10 directores más populares, indicando nombre del director y la cantidad de películas que dió.
SELECT director, COUNT(*) AS cantidad_peliculas
FROM peliculas
GROUP BY director;
ORDER BY cantidad_peliculas DESC
LIMIT 10;

-- 9. Indicar cuantos actores distintos hay
SELECT COUNT(DISTINCT actor) AS total_distintos FROM reparto;
SELECT DISTINCT actor FROM reparto;

-- 10. Indicar las peliculas estrenadas entre los años 1990 y 1999. Ordenar por año ascendente
SELECT pelicula, estreno FROM peliculas 
WHERE estreno 
BETWEEN 1990 AND 1999
ORDER BY pelicula ASC;

SELECT pelicula, estreno FROM peliculas 
WHERE estreno 
BETWEEN 1990 AND 1999
ORDER BY estreno ASC;

-- 11. Listar los actores de la pelicula mas nueva
SELECT r.actor, p.pelicula, p.estreno FROM peliculas AS p
JOIN reparto AS r
ON p.id = r.id_pelicula
ORDER BY p.estreno DESC;

SELECT MAX(estreno) FROM peliculas;

SELECT r.actor, p.pelicula, p.estreno FROM peliculas AS p
JOIN reparto AS r
ON p.id = r.id_pelicula
WHERE estreno = (SELECT MAX(estreno) FROM peliculas);

SELECT r.actor, p.pelicula, p.estreno FROM peliculas AS p
JOIN reparto AS r
ON p.id = r.id_pelicula
WHERE p.estreno = (SELECT MAX(estreno) FROM peliculas);

SELECT r.actor, p.pelicula, p.estreno FROM peliculas AS p
JOIN reparto AS r
ON p.id = r.id_pelicula
WHERE p.estreno = 2008;

-- 12. Inserte los datos de una nueva pelicula solo en memoria y otra pelicula en el disco duro
BEGIN;

SAVEPOINT uno;
INSERT INTO peliculas VALUES(101, 'Harry Potter', 2003, 'Chris Columbus');

SAVEPOINT dos;
INSERT INTO peliculas VALUES(102, 'Joker 2', 2024, 'Todd Phillips');

ROLLBACK TO dos;
COMMIT;

-- 13. Actualice 5 directors utilizando rollback para deshacer el registro
BEGIN;

UPDATE peliculas SET autor = 'Miguel de Cervantes' WHERE id = 1;
UPDATE peliculas SET autor = 'Antoine SaintExupery' WHERE id = 2;
UPDATE peliculas SET autor = 'Maquiavelo' WHERE id = 3;
UPDATE peliculas SET autor = 'Henry Kissinger' WHERE id = 4;
UPDATE peliculas SET autor = 'Miguel de Cervantes' WHERE id = 5;

UPDATE peliculas SET director = CASE
    WHEN id = 1 THEN 'Miguel de Cervantes'
    WHEN id = 2 THEN 'Antoine SaintExupery'
    WHEN id = 3 THEN 'Maquiavelo'
    WHEN id = 4 THEN 'Henry Kissinger'
    WHEN id = 5 THEN 'Miguel de Cervantes'
    END
WHERE id IN (1, 2, 3, 4, 5);

ROLLBACK;

-- 14. Inserte 3 actores a la pelicula Rambo utilizando SAVEPOINT
SELECT * FROM peliculas WHERE LOWER(pelicula) LIKE '%rambo%';

BEGIN;
SAVEPOINT uno;
INSERT INTO reparto VALUES 
(72, 'Fulanito'),
(72, 'Mengano'),
(73, 'Sutano');
ROLLBACK TO uno;

-- 15. Elimina las peliculas estrenadas el año 2008 solo en memoria
-- ERROR:  Key (id)=(6) is still referenced from table "reparto".update or delete on table "peliculas" violates foreign key constraint "fk_reparto_id_peliculas" on table "reparto"
BEGIN;
ALTER TABLE reparto DROP CONSTRAINT fk_reparto_id_peliculas;
SELECT * FROM peliculas WHERE estreno = 2008;
DELETE FROM peliculas WHERE estreno = 2008;
ROLLBACK;


BEGIN;
ALTER TABLE reparto DISABLE TRIGGER ALL;
ALTER TABLE peliculas DISABLE TRIGGER ALL;
DELETE FROM peliculas WHERE estreno = 2008;

ALTER TABLE reparto ENABLE TRIGGER ALL;
ALTER TABLE peliculas ENABLE TRIGGER ALL;
ROLLBACK;

-- 16. Inserte 2 actores para cada pelicula estrenada el 2001
SELECT * FROM peliculas WHERE estreno = 2001;
-- 13	"El SeÃ±or de los anillos: La comunidad del anillo"	2001	"Peter Jackson"
-- 16	"Monstruos S.A."	2001	"Pete Docter"
-- 55	"El viaje de Chihiro"	2001	"Hayao Miyazaki"
-- 78	"AmÃ©lie"	2001	"Jean-Pierre Jeunet"
-- 94	"Ocean's Eleven"	2001	"Steven Spielberg"
-- 99	"Mouling Rouge"	2001	"Baz Luhrmann"

BEGIN;
SAVEPOINT uno;
INSERT INTO reparto VALUES 
(13, 'Fulanito'),
(13, 'Perez'),
(16, 'Mengano'),
(16, 'Maria'),
(55, 'Sutano'),
(55, 'Jose'),
(78, 'Karla'),
(78, 'Javiera'),
(94, 'Jacinto'),
(94, 'Luis'),
(99, 'Beatriz'),
(99, 'Natalia');
ROLLBACK TO uno;

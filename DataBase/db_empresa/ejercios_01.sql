-- =================================
-- Ejercicios de SQL
-- =================================

-- =================================
-- Consultas básicas
-- =================================

-- 1.- Lista el nombre y salario de todos los empleados ordenados de mayor a menor.

SELECT nombre,salario
FROM dbo.empleados
ORDER BY salario DESC

-- 2.- Muestra los empleados que trabajan en el departamento de Tecnología.
-- 1° opción
SELECT *
FROM dbo.empleados
WHERE id_depto = (
    SELECT id_depto
    FROM dbo.departamentos
    WHERE nombre = 'Tecnología')

-- 2° opción

SELECT e.*
FROM dbo.empleados e
JOIN dbo.departamentos d ON d.id_depto = e.id_depto
WHERE d.nombre = 'Tecnología'

-- 3.- Calcula el salario promedio por cada departamento.

SELECT d.nombre, ROUND( AVG( e.salario ),2) AS avgSalario
FROM dbo.empleados e
JOIN dbo.departamentos d ON d.id_depto = e.id_depto
GROUP by d.nombre 
ORDER BY avgSalario DESC

-- 4.- Encuentra los 5 empleados con los salarios más altos.

WITH promedio_general as (
    SELECT AVG(salario) as avgSalario
    FROM dbo.empleados
)

SELECT  TOP  5 e.nombre+' '+e.apellido as nombre_emp,e.salario
FROM empleados e
CROSS JOIN promedio_general pg 
WHERE  e.salario > pg.avgSalario
ORDER BY e.salario DESC

-- 5.- Obtén el total de ventas realizadas por cada empleado.

WITH tb_ventasTotal as (
    SELECT id_empleado, COUNT(id_venta) as cantidadVentas , SUM (monto) as totalVentas
    FROM dbo.ventas
    GROUP BY id_empleado
)

SELECT  e.nombre+' '+e.apellido as nombre_emp, vt.cantidadVentas , vt.totalVentas
FROM empleados e
JOIN tb_ventasTotal vt ON  e.id_empleado = vt.id_empleado

-- =================================
-- Consultas intermedias
-- =================================

-- 1.- Muestra el nombre de cada proyecto y la cantidad de empleados asignados.
-- 2.- Lista los empleados que han trabajado en más de 2 proyectos.
-- 3.- Calcula cuánto dinero ha vendido cada departamento (usando JOIN empleados → ventas).
-- 4.- Encuentra el empleado con mayor monto acumulado en ventas.
-- 5.- Muestra los proyectos que superaron un total de 1000 horas asignadas.

-- ==================================
-- Consultas avanzadas (CTE, subconsultas, funciones ventana)
-- ==================================
-- 1.- Usando un CTE, muestra el salario promedio y marca a los empleados por encima o debajo del promedio.
-- 2.- Encuentra los 3 mejores vendedores por monto total de ventas (función RANK() o ROW_NUMBER()).
-- 3.- Calcula el monto total de ventas acumulado por mes.
-- 4.- Obtén el nombre de los proyectos y el promedio de horas asignadas por empleado.
-- 5.- Encuentra qué empleados nunca han realizado ventas.

-- ==================================
-- Ejercicios de ETL
-- ==================================
-- 1.- Extracción: Crea una tabla ventas_filtradas que contenga solo las ventas del año 2022.
-- 2.- Transformación: Convierte los nombres de empleados a mayúsculas y guárdalos en una tabla temporal.
-- 3.- Carga: Genera una tabla resumen_ventas con el total de ventas por departamento y guárdala.
-- 4.- Limpia los registros de ventas con monto menor a 400 y muéstralos en una tabla aparte ventas_invalidas.
-- 5.- Exporta las ventas de 2022 a formato CSV usando tu cliente SQL (simulando un flujo ETL real).

-- ===================================
-- Ejercicios de PL/SQL
-- ===================================
--Crea un procedimiento que reciba un id_empleado y devuelva el total de ventas hechas por ese empleado.
--Haz un procedimiento que aumente en un 10% el salario de todos los empleados del departamento de Ventas.
--Escribe una función que devuelva el empleado top vendedor de un año específico.
--Usa un cursor para recorrer todas las ventas y calcular un bono del 5% para cada empleado.
--Crea un trigger que inserte en una tabla log_ventas cada vez que se registra una nueva venta.
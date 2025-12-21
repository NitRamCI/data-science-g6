use db_g6

select max(salario) from empleado;

SELECT DISTINCT pais from empleado;


SELECT pais, COUNT(*) from empleado
GROUP BY pais order by count(*) DESC;

SELECT pais, count(*) from empleado
GROUP BY pais
HAVING count(*) >= 100;
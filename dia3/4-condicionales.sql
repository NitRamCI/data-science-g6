SELECT 
nombre, salario,
CASE 
    WHEN salario < 3000 THEN 'Bajo'
    WHEN salario BETWEEN 3000 AND 7000 THEN 'Medio'
    ELSE 'Alto'
END AS nivel_salarial
from empleado;

SELECT nombre, pais,
CASE 
    WHEN pais='Peru' THEN 'nacional'  
    ELSE  'extranjero'
END
from empleado;
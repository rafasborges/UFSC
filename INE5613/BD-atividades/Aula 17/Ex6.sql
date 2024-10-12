SELECT nome 
FROM pacientes 
WHERE codp = SOME(SELECT codp FROM consultas WHERE hora < ALL(SELECT hora FROM consultas WHERE "data" = '2020/10/14'));


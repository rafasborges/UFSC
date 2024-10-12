SELECT a.nroa, a.andar
FROM Ambulatorios a
NATURAL JOIN Medicos
NATURAL JOIN Consultas
WHERE data = '2020/10/12';

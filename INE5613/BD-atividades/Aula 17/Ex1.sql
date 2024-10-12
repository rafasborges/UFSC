SELECT nome
FROM Pacientes
WHERE codp IN (SELECT codp FROM Consultas WHERE hora > '14:00');

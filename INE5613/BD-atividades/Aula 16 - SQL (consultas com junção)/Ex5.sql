SELECT codp, nome
FROM Pacientes
NATURAL JOIN Consultas
WHERE hora > '14:00';
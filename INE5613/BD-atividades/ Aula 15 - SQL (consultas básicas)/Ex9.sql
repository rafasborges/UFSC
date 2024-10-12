SELECT codp, nome
FROM Pacientes
WHERE idade > 25 AND doenca IN ('tendinite', 'fratura', 'gripe', 'sarampo');

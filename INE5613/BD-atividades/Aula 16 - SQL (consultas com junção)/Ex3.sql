SELECT DISTINCT Medicos.nome, Medicos.idade
FROM Medicos JOIN Consultas ON Medicos.codm = Consultas.codm
JOIN Pacientes ON Consultas.codp = Pacientes.codp
WHERE Pacientes.nome = 'Ana';

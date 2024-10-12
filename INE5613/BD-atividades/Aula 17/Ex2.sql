SELECT nome, idade
FROM Medicos
WHERE codm IN (SELECT codm FROM Consultas WHERE codp = (SELECT codp FROM Pacientes WHERE nome = 'Ana'));

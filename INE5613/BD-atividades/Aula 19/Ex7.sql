UPDATE Medicos
SET cidade = (SELECT cidade FROM Pacientes WHERE nome = 'Paulo'),
    idade = 2 * (SELECT idade FROM Pacientes WHERE nome = 'Ana')
WHERE nome = 'Pedro';

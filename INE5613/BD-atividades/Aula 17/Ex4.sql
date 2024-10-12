SELECT CPF
FROM Medicos
WHERE nroa = in (SELECT nroa FROM Ambulatorios WHERE andar = 1);

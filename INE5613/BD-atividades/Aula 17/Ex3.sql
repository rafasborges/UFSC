SELECT nroa, andar
FROM Ambulatorios
WHERE nroa NOT IN (SELECT nroa FROM Medicos WHERE nroa IS NOT NULL);

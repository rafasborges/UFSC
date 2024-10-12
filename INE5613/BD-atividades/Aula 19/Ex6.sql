DELETE FROM Ambulatorios
WHERE nroa NOT IN (SELECT DISTINCT nroa FROM Medicos where nroa is NOT NULL);

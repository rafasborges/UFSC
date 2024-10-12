SELECT a1.nroa
FROM Ambulatorios a1
JOIN Ambulatorios a2 ON a1.andar = a2.andar
WHERE a2.nroa = 5;
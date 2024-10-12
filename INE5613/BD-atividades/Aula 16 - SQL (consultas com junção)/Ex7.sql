SELECT a.*, m.codm, m.nome 
FROM Ambulatorios a
LEFT JOIN Medicos m ON a.nroa = m.nroa;

SELECT M.nome, A.nroa, A.andar
FROM Medicos M
JOIN Ambulatorios A ON M.nroa = A.nroa
ORDER BY A.nroa;

SELECT M.nome
FROM Medicos M
JOIN Consultas C ON M.codm = C.codm
GROUP BY M.nome
HAVING COUNT(C.codp) > 1;

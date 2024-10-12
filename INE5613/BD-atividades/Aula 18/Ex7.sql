SELECT M.nome, M.CPF
FROM Medicos M
JOIN (
    SELECT nroa
    FROM Medicos
    WHERE nome = 'Pedro'
) AS P ON M.nroa = P.nroa;
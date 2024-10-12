SELECT M.nome, M.CPF, C.data
FROM Medicos M
JOIN Consultas C ON M.codm = C.codm
WHERE M.especialidade = 'ortopedia'
AND EXISTS (
    SELECT *
    FROM Consultas C2
    JOIN Pacientes P ON C2.codp = P.codp
    WHERE C2.codm = M.codm
    AND P.nome = 'Ana'
);

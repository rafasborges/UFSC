SELECT M.nome, M.CPF
FROM Medicos M
WHERE M.especialidade = 'ortopedia'
AND NOT EXISTS (
    SELECT *
    FROM Pacientes P
    WHERE P.cidade = 'Florianopolis'
    AND NOT EXISTS (
        SELECT *
        FROM Consultas C
        WHERE C.codm = M.codm
        AND C.codp = P.codp
    )
);


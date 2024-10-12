SELECT nome, CPF
FROM Medicos M
WHERE NOT EXISTS (
    SELECT *
    FROM Pacientes P
    WHERE NOT EXISTS (
        SELECT *
        FROM Consultas C
        WHERE C.codm = M.codm
        AND C.codp = P.codp
    )
);
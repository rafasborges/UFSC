SELECT P.nome, P.cidade
FROM Pacientes P
JOIN (
    SELECT codp
    FROM Consultas C
    JOIN Medicos M ON C.codm = M.codm
    WHERE M.especialidade = 'ortopedia'
) AS O ON P.codp = O.codp;

SELECT C.data, C.hora
FROM Consultas C
JOIN (
    SELECT codm, data, hora
    FROM Medicos
    WHERE nome = 'Maria'
) AS M ON C.codm = M.codm;


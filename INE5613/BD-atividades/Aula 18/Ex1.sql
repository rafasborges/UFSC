SELECT m.nome, m.cpf
FROM medicos m
WHERE EXISTS (
    SELECT 1
    FROM pacientes p
    WHERE m.cpf = p.cpf
);
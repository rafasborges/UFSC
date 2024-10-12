 SELECT m.CPF, m.nome AS nome_medico, c.data, p.nome AS nome_paciente
FROM Medicos m
LEFT JOIN Consultas c ON m.codm = c.codm
LEFT JOIN Pacientes p ON c.codp = p.codp;

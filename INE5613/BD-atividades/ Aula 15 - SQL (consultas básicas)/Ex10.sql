SELECT CPF, nome, idade
FROM Medicos
WHERE cidade = 'Florianopolis'
UNION
SELECT CPF, nome, idade
FROM Pacientes
WHERE cidade = 'Florianopolis'
UNION
SELECT CPF, nome, idade
FROM Funcionarios
WHERE cidade = 'Florianopolis';

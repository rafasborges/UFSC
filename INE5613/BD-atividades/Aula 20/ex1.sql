CREATE VIEW FuncFlorianopolis AS
SELECT codf, nome, CPF, idade
FROM Funcionarios
WHERE cidade = 'Florianopolis';

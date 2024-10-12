SELECT Funcionarios.nome, Medicos.nome
FROM Funcionarios full join Medicos on Funcionarios.cidade = Medicos.cidade

SELECT Medicos.nome, Medicos.cpf
FROM Medicos join Pacientes on Medicos.cpf = Pacientes.cpf 
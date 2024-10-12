insert into medicos
SELECT m.codm+1, f.nome, f.idade, f.cidade, f.cpf, (SELECT especialidade from medicos WHERE codm = 2), (SELECT nroa from medicos WHERE codm = 2) 
from funcionarios f join medicos m on codf=3 and codm = (SELECT max(codm) from medicos)

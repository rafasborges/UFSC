SELECT nome, cpf 
FROM funcionarios 
WHERE salario < ALL(SELECT max(salario) FROM funcionarios);

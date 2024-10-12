Atividades de laboratório SQL 

--> Aula 13
Atividade 1)
1) Criar as seguintes tabelas, considerando que os atributos sublinhados fazem parte da chave primária e os em itálico são chaves estrangeiras (não acentuem as palavras!):
a) Ambulatorios: nroa (int), andar (numeric(2)) (não nulo), capacidade (smallint)
b) Medicos: codm (int), nome (varchar(40)) (não nulo), idade (smallint) (não nulo), cidade (varchar(40)), CPF (numeric(11)) (não nulo e único), especialidade (varchar(30)), nroa (int)
c) Pacientes: codp (int), nome (varchar(40)) (não nulo), idade (smallint) (não nulo), cidade (varchar(40)), CPF (numeric(11)) (não nulo e único), doenca (varchar(40)) (não nulo)
d) Funcionarios: codf (int), nome (varchar(40)) (não nulo), idade (smallint) (não nulo), cidade (varchar(40)), CPF (numeric(11)) (não nulo e único), salário (numeric(10)), cargo (varchar(40))
e) Consultas: codm (int), codp (int), data (date), hora (time)
2) Alterar a tabela Funcionarios, removendo o atributo cargo
3) Criar um índice para o atributo cidade na tabela Pacientes
   
--> Aula 14
Atividade 2)
Realizar as seguintes atualizações:
1) O paciente Paulo mudou-se para Ilhota
2) A consulta do médico 1 com o paciente 4 passou para às 12:00 horas do dia 4 de Novembro de 2020
3) A consulta do médico 3 com o paciente 4 passou para às 14h30
4) O funcionário 4 deixou a clínica
5) As consultas após as 19 horas devem ser excluídas
6) Os médicos que residem em Biguacu e Palhoca devem ser excluídos

--> Aula 15
Realizar as seguintes consultas no BD:
Exercícios
1) Buscar os dados dos médicos com menos de 40 anos ou com especialidade diferente de traumatologia
2) Buscar o nome e a idade dos pacientes que não residem em Florianópolis
3) Buscar o nome e a idade (em meses) dos pacientes
4) Qual o horário da última consulta marcada para o dia 13/10/2020?
5) Qual a média de idade dos médicos e o total de ambulatórios atendidos por eles?
6) Buscar o código, o nome e o salário líquido dos funcionários. O salário líquido é o salário cadastrado menos 20%
7) Buscar o nome dos funcionários que terminam com a letra 'a'
8) Buscar o nome e a especialidade dos médicos cuja segunda e a última letra de seus nomes seja a letra 'o'
9) Buscar os códigos e nomes dos pacientes com mais de 25 anos que estão com tendinite, fratura, gripe ou sarampo
10) Buscar os CPFs, nomes e idades de todas as pessoas (médicos, pacientes ou funcionários) que residem em Florianópolis

--> Aula 16
Responda o que se pede utilizando junção (não natural):
1) Buscar o nome e CPF dos médicos que também são pacientes do hospital
2) Buscar nomes de funcionários e de médicos (exibir pares de nomes) que residem na mesma cidade
3) Buscar o nome e idade dos médicos que têm consulta marcada com a paciente cujo nome é Ana
4) Buscar o número dos ambulatórios que estão no mesmo andar do ambulatório 5
Responda o que se pede utilizando junção natural:
5) Buscar o código e o nome dos pacientes com consulta marcada para horários após às 14 horas
6) Buscar o número e o andar dos ambulatórios cujos médicos possuem consultas marcadas para o dia 12/10/2020
Responda o que se pede utilizando junção externa (e também junção, se necessário):
7) Buscar os dados de todos os ambulatórios e, para aqueles ambulatórios onde médicos dão atendimento, exibir também os códigos e nomes destes médicos
8) Buscar o CPF e o nome de todos os médicos e, para aqueles médicos que possuem consultas marcadas, exibir também o nome dos paciente e a data da consulta

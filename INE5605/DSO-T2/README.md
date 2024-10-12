Trabalho DSO - Sistema de Restaurante

Alunas: Betina Ferrão e Rafaela Borges.
Problema: 
Implementar um sistema orientado a objetos em Python para o gerenciamento de um sistema de restaurante.

Escopo de desenvolvimento: 
O sistema de gerenciamento de restaurantes auxilia no controle e organização das atividades do ambiente. Com esse sistema é possível melhorar a experiência do cliente ao otimizar processos e assegurar o sucesso do estabelecimento.
Primeiramente, é necessário cadastrar os requisitos essenciais para o funcionamento do restaurante: as mesas, os funcionários e os itens do cardápio. Para cadastrar uma mesa é necessário informar seu número e sua capacidade. O status da mesa é inicializado como falso, pois a mesa está vazia. A Pessoa possui um nome e cpf. O funcionário herda de Pessoa, contendo nome, cpf, salário e comissão. Além disso, os itens do cardápio devem ser adicionados, com os seguintes atributos: nome, descrição, código e preço.
Com a chegada de clientes, é necessário realizar o cadastro deles, informando o nome do responsável, seu cpf, sua idade e o número de convidados. O Cliente também herda de Pessoa. Para cadastrar uma reserva é indispensável informar um cliente, a mesa que ele e seus convidados serão alocados, após realizada a consulta sobre a disponibilidade da mesma, e um funcionário responsável. Após realizada a reserva, os pedidos poderão ser feitos. O pedido terá um código, uma lista de itens e a reserva relacionada. O sistema deverá conter os relatórios finais e calcular os ganhos totais do restaurante do dia, além de tratar as possíveis exceções.
Nas telas será permitido ao atendente incluir, alterar, listar e excluir as entidades, chamando os métodos de seus respectivos controladores.

O sistema deve permitir emitir os seguintes relatórios:

Relatório de reservas: mostra o número de reservas realizadas em um dia.
Relatório de pedidos: mostra qual o item mais pedido no restaurante em um dia.
Relatório de clientes: mostra quantos clientes foram atendidos em um dia.
Relatório de ganho total: mostra qual foi o valor total ganho entre os pedidos no dia.

Considere algumas regras:

1- Somente pode ser registrado o cliente responsável que tiver mais de 18 anos.
2- O número de clientes e convidados em uma mesa não pode exceder a sua capacidade máxima.
3- O cliente não poderá pedir um item que não consta no cardápio.
4- Quando o dia finalizar, as listas de clientes, reservas e pedidos deverão ser zeradas e os funcionários, mesas e itens do cardápio mantidos.

Restrições de escopo: 

Para esse tema, serão considerados:
Cadastros: clientes, funcionários, mesas e itens do cardápio.
Registros: reservas e pedidos.
Relatórios: número de reservas realizadas em um dia, item mais pedido, quantidade de clientes atendidos no dia e valor total no dia.


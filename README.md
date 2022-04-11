# python
 
 Desafio 1 - Cadastro de Usuário:

- Página de "Olá, visitante!": feito.✅

- Função cadastro (user, email, senha): feito.✅

- Função login (user, senha): feito*🟡
Consegui apenas fazer o login pelo user.

- Função troca de senha: feito.✅

- Função inserção de CPF e PIS: feito com problemas.*🟡
A inserção de CPF e de PIS no banco de dados foi implementada porém não consegui conectar ela a um usuário específico.

- Função inserção de Endereço: feito com problemas.*🟡
A inserção do endereço no banco de dados foi implementada porém também tive dificuldades para conectar ela a um user apenas.

- Função "Olá {NOME_DO_USUARIO}": não feito.❌

- Função Logout: feito.✅

- Função de edição de dados cadastrais: feito com problemas*🟡
A função de editar uma tabela está criada, porém o acesso a essa função não consegui fazer, tem que ser escrita manualmente o link com o ID da tabela que se quer alterar.

- Função delete user: não feito.❌

Aprendizados 😁:
Visão aplicada de Banco de Dados e criação de projeto pelo Django foram coisas que eu nunca tinha visto antes.
O projeto sendo gerido e organizado através das funcionalidades do Git e Github foi uma experiência satisfatória para mim.
Pesquisa e resolução de problemas durante o desenvolvimento também é algo que desperta autonomia e um pouco de independência durante o desenvolvimento de um projeto.
Funcionalidades de Python, MySQL, HTML e CSS novas.

Dificuldades 🥵:
Entender o funcionamento de um banco de dados não é uma tarefa tão simples.
Para eu ter completado o nível 1 com êxito eu teria que, de alguma forma, buscar as informações do banco para mostrar na minha app web:
 - Buscar o nome do usuario para fazer o "Olá {NOME_DO_USUARIO}".
 - Buscar os dados cadastrados na tabela para eles aparecerem na hora de edita-los e tornar mais fácil a edição no caso de uma edição mínima.
 
Relacionamento de tabelas:
 - O conteúdo sobre relacionamento de tabelas e python é um pouco escasso, tive aulas de banco de dados, aprendi sobre relacionamento na teoria (usando primary key e foreign key) e mesmo assim não consegui relacionar da forma correta.
Uma das coisas que mais me faltou foi saber criar um cadastro já com (user, email, senha, cpf, pis e endereço) de uma vez e direcionar todos esses dados para um user só. Para que apenas ele pudesse alterar os dados dele. Sinto que isso é um dificuldade relacionada à inexperiência com banco de dados.

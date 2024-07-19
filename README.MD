## Visão Geral

Este projeto Django é um Desafio Backend da Lacrei Saúde. A proposta é desenvolver uma API para gerenciar consultas médicas e informações de profissionais de saúde. A aplicação permite realizar operações CRUD (Criar, Ler, Atualizar, Excluir) no modelo PessoaProfissional, incluindo detalhes como nome, profissão, especialidade e informações de contato, além de gerenciar o cadastro de consultas.


### Instale as Dependências

```bash
pip install -r requirements.txt
```

### Aplique as Migrações do Banco de Dados

```bash
python manage.py migrate
```

### Para criar um banco de dados execute
```bash
python manage.py pessoaProfissional_db
python manage.py consultaProfissional_db
```

### Inicie o Servidor de Desenvolvimento

```bash
python manage.py runserver
```

A aplicação estará disponível em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## App Contas

### Modelos

- **PessoaProfissional**: Armazena informações sobre profissionais de saúde,  Nome Social, nome completo, profissão, especialidade médica e CPF. Utiliza um gerenciador de usuários personalizado para criar e gerenciar usuários com diferentes permissões.

### Serializers

- **PessoaProfissionalSerializer**: Converte o modelo `PessoaProfissional` para JSON e vice-versa. Inclui todos os campos do modelo para operações CRUD.

### Views

- **PessoaProfissionalViewSet**: Fornece endpoints para operações CRUD no modelo `PessoaProfissional`. Implementa permissões personalizadas para garantir que apenas administradores e o próprio usuário possam atualizar ou excluir seus dados.

### URLs

Define rotas para listar, criar, atualizar e excluir registros de `PessoaProfissional`. As rotas são configuradas para aceitar requisições HTTP específicas (GET, POST, PUT, PATCH, DELETE).

## Arquitetura de Permissões

- **Permissões Personalizadas**: `IsOwnerOrAdmin` permite que apenas o próprio usuário ou administradores realizem atualizações e exclusões de registros. Todos os outros métodos são acessíveis a qualquer usuário autenticado.

## Testes do Modelo PessoaProfissional

### Configurações

- **Logging**: O módulo logging é configurado para registrar informações sobre a execução dos testes em um arquivo chamado `pessoa_profissional_test.log`.

### Métodos de Teste

#### setUp

O método `setUp` é executado antes de cada teste. Ele prepara o ambiente para os testes:

- Define dados de exemplo como email, senha, nome completo, profissão, endereço, celular, nome social, CPF, especialidade médica e uma imagem de documento.
- Cria um usuário com os dados fornecidos utilizando o método `create_user` do gerenciador de usuários. Isso garante que cada teste comece com um ambiente consistente e um usuário `PessoaProfissional` criado.

#### test_pessoa_profissional_creation

Testa a criação do modelo `PessoaProfissional` para garantir que todos os campos sejam armazenados corretamente:

- **Validações**: Verifica se os valores dos campos criados coincidem com os dados fornecidos.
- **Arquivo de Imagem**: Confirma se o arquivo de imagem foi anexado corretamente.
- **Logging**: Registra uma mensagem de sucesso no arquivo de log, incluindo a data e a hora da criação do usuário e as informações do objeto.

#### test_user_str_method

Testa o método `__str__` do modelo `PessoaProfissional` para garantir que ele retorna o nome social do usuário:

- **Validação**: Compara a saída do método `__str__` com o nome social definido.

### Considerações

- **Objetivo**: Os testes garantem que o modelo `PessoaProfissional` esteja funcionando conforme esperado, com a criação correta dos registros e a implementação correta do método de string.
- **Cobertura**: O teste cobre a criação do modelo e a verificação da representação textual, ajudando a assegurar que a aplicação esteja gerenciando os dados de maneira apropriada.

## App Consulta

Este aplicativo é responsável pelo gerenciamento de consultas médicas na aplicação. Ele permite a criação, leitura, atualização e exclusão de registros de consultas realizadas com profissionais de saúde.

### Modelos

- **Consulta**: Representa uma consulta médica realizada por um profissional de saúde.

  **Campos**:
  - `medico`: Relaciona-se com o modelo `PessoaProfissional`, representando o profissional que realizou a consulta. O campo é opcional e é removido da base de dados caso o profissional seja excluído.
  - `valor`: Armazena o valor da consulta como um número decimal, com até 10 dígitos e 2 casas decimais.
  - `data`: Armazena a data da consulta. O valor padrão é a data atual.

  **Meta**:
  - `verbose_name`: Nome legível para o modelo, "Consulta".
  - `verbose_name_plural`: Nome plural legível para o modelo, "Consultas".

  **Método**:
  - `__str__`: Retorna uma string que representa a consulta, incluindo o nome social do médico e o valor da consulta.

### Serializers

- **ConsultaSerializer**: É responsável pela conversão dos dados do modelo `Consulta` para JSON e vice-versa.

  **Campos**:
  - `medico_nome_social`: Obtém o nome social do médico relacionado, de forma somente leitura.
  - `especialidade_medica`: Obtém a especialidade médica do médico relacionado, de forma somente leitura.

  **Meta**:
  - `model`: Define o modelo `Consulta` como o modelo a ser serializado.
  - `fields`: Especifica os campos a serem incluídos na serialização: `id`, `especialidade_medica`, `valor`, `data`, `medico_nome_social`.

Aqui está a atualização para a seção do README, incluindo a funcionalidade de filtragem:

### Views

- **ConsultaViewSet**: Fornece uma interface para realizar operações CRUD no modelo `Consulta` e permite a filtragem das consultas por ID do `medico`.

  - **queryset**: Define a consulta padrão para buscar todos os registros de `Consulta`.
  - **serializer_class**: Especifica o `ConsultaSerializer` para a serialização dos dados.
  - **filter_backends**: Configurado para usar o `DjangoFilterBackend` para permitir a filtragem dos registros.
  - **filterset_class**: Define o `ConsultaFilter` para possibilitar a filtragem das consultas por ID do `medico`.


## Testes do Modelo Consulta

### Configurações

- **Logging**: O módulo logging é configurado para registrar informações sobre a execução dos testes em um arquivo chamado `consulta_test.log`. Isso facilita a depuração e fornece um histórico das operações realizadas durante os testes.

### Métodos de Teste

#### setUp

O método `setUp` é executado antes de cada teste e prepara o ambiente com dados necessários:

- **Criação do Médico**: Um objeto `PessoaProfissional` é criado para ser usado como médico em consultas. Os dados do médico incluem email, senha, nome completo, profissão, endereço, celular, nome social, CPF, especialidade médica e um campo `foto_documento` configurado como `None` (pode ser ajustado conforme necessário).
- **Criação da Consulta**: Um objeto `Consulta` é criado associando o médico criado anteriormente. São definidos o valor da consulta e a data da consulta, utilizando o método `timezone.now().date()` para garantir que a data seja a atual.

#### test_consulta_creation

Este teste verifica se a criação do modelo `Consulta` está funcionando corretamente:

- **Validações**: Recupera o objeto `Consulta` do banco de dados com base no médico associado e verifica se o médico, o valor e a data da consulta correspondem aos valores fornecidos durante a criação.
- **Logging**: Registra uma mensagem no arquivo de log indicando que a criação da consulta foi bem-sucedida, incluindo as informações do objeto e a data e hora da criação.

#### test_consulta_str_method

Este teste verifica se o método `__str__` do modelo `Consulta` retorna corretamente a representação textual esperada:

- **Validação**: Compara a saída do método `__str__` com a string formatada que inclui o nome social do médico e o valor da consulta, garantindo que a representação textual da consulta esteja correta.

### Considerações

- **Objetivo**: Os testes garantem que o modelo `Consulta` seja criado corretamente e que o método de representação textual (`__str__`) funcione como esperado.
- **Cobertura**: O teste cobre a criação do modelo `Consulta` e a verificação da representação textual, assegurando que a funcionalidade do modelo esteja de acordo com os requisitos.
```


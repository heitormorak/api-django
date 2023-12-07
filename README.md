# API DJANGO - CONSULTAS/PROFISSIONAIS

## Objetivo

O projeto pretende criar API para CRUD de profissionais e consultas, onde uma consulta possui um profissional atrelado e uma data. 
O profissional possui nome, nome social e cpf, para esse contexto.
É possível pesquisar a consulta pelo id do profissional.

## Ambiente Virtual

### Criando o Ambiente Virtual

1. Clone o repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/heitormorak/api-django.git
   ```

2. Navegue até o diretório do projeto:

   ```
   cd api-django   
   ```

3. Crie o ambiente virtual:
- No Linux/macOS:
   ```
    python3 -m venv venv    
   ```

- No Windows:
   ```
    python -m venv venv    
   ```

4. Ative o ambiente virtual:
- No Linux/macOS:
   ```
    source venv/bin/activate    
   ```

- No Windows:
   ```
    .\venv\Scripts\Activate    
   ```

5. Instale as dependências:
   ```
    pip install -r requirements.txt    
   ```

### Rodando a API REST

1. Aplique as migrações do banco de dados:
   ```
    python manage.py migrate
   ```

2. Inicie o servidor:
   ```
    python manage.py runserver
   ```

3. Acesse a aplicação em http://localhost:8000/

## Arquitetura

O projeto segue uma arquitetura baseada no padrão Model-View-Controller (MVC), com a adição do Django Rest Framework para a criação da APIs RESTful. Aqui estão algumas justificativas para as escolhas de arquitetura:

### Modelos
Os modelos (models.py) definem a estrutura do banco de dados e são responsáveis por representar os dados da aplicação. A escolha de modelos específicos visa uma organização clara e coesa das entidades do sistema.

### Serializers
Os serializers (serializers.py) são usados para converter os modelos em formatos que podem ser facilmente renderizados em JSON. Isso é necessário para a exposição dos dados por meio da API RESTful.

### Views
As visualizações (views.py) tratam das requisições HTTP e interagem com os modelos e serializers para processar os dados. As views são projetadas para serem modulares e reutilizáveis.

### URLs
O arquivo urls.py configura as rotas da aplicação, associando visualizações a caminhos específicos. Isso facilita a navegação e compreensão da estrutura da API.


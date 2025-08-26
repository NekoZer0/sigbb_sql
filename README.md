
17. **Migrar todas as tabelas necessárias para o funcionamento correto da aplicação**
    - `uv run manage.py migrate`
    - `uv self update`
    - *Este comando garante que está a usar a versão mais recente do [uv](https://github.com/astral-sh/uv), uma ferramenta moderna para gestão de ambientes Python e dependências. Manter o uv atualizado previne problemas de compatibilidade e traz melhorias de performance.*

2. **Criar um novo projecto**
    - `uv init <nome do projecto>`
    - *Inicializa um novo ambiente de projecto Python, criando os ficheiros necessários para gerir dependências e configurações. Substitua `<nome do projecto>` pelo nome desejado para o seu projecto.*

3. **Adicionar dependências Django**
    - `uv add django django-extensions`
    - *Adiciona o [Django](https://www.djangoproject.com/), um framework web popular para Python, e [django-extensions](https://django-extensions.readthedocs.io/), um conjunto de extensões úteis para desenvolvimento com Django. Estes pacotes ficam registados no ficheiro de dependências do projecto.*

4. **Criar a estrutura inicial do projecto Django**
    - `uv run django-admin startproject <nome_do_projecto> .`
    - *Este comando utiliza o `django-admin` para criar a estrutura base do seu projecto Django no diretório atual. O uso de `uv run` garante que o comando seja executado dentro do ambiente gerido pelo uv, utilizando as dependências corretas.*

5. **Executar o servidor**
    - `uv run manage.py runserver`
    - *Este comando inicia o servidor de desenvolvimento do Django, permitindo-lhe aceder à aplicação através do navegador. O uso de `uv run` garante que o servidor é executado no ambiente isolado, com todas as dependências corretas.*

6. **Criar uma aplicação Django**
    - `uv run manage.py startapp <nome da aplicação>`
    - *Cria uma nova aplicação chamada `produto` dentro do seu projeto Django. As aplicações permitem organizar funcionalidades distintas dentro do projeto.*

7. **Adicionar dependências de desenvolvimento**
    - `uv add --dev <nome da dependência>`
    - *Adiciona uma dependência apenas para o ambiente de desenvolvimento, sem afetar o ambiente de produção. Substitua `<nome da dependência>` pelo pacote desejado.*

8. **Instalar todas as dependências do projecto**
    - `uv sync --no-dev`
    - *Este comando instala todas as dependências listadas no ficheiro de dependências do projecto, exceto as dependências de desenvolvimento. É útil para preparar o ambiente de produção, garantindo que apenas os pacotes necessários para execução da aplicação sejam instalados.*

9. **Criar um alias para simplificar comandos longos**
    - `alias uvm='uv run manage.py'`
    - `alias uvr='uv run'`
    - *Estes comandos criam atalhos (aliases) no seu terminal para facilitar a execução de comandos frequentes. O alias `uvm` permite executar rapidamente comandos do `manage.py` dentro do ambiente uv, enquanto `uvr` simplifica a execução de qualquer comando Python no ambiente gerido pelo uv. Para tornar os aliases permanentes, adicione-os ao ficheiro de configuração do seu shell, como `.bashrc` ou `.zshrc`.*

10. **Adicionar a aplicação ao `INSTALLED_APPS`**
    - No ficheiro `<nome_do_projecto>/settings.py`, adicione o nome da aplicação criada (por exemplo, `produtos`) à lista `INSTALLED_APPS`:
        ```python
        INSTALLED_APPS = [
            'django.contrib.admin',
            # ... outros apps padrão ...
            'produtos',
        ]
        ```
    - *Isto garante que o Django reconhece a nova aplicação e a inclui no projeto.*

11. **Configurar as URLs principais do projeto**
    - No ficheiro `<nome_do_projecto>/urls.py`, importe o `include`  de `django.urls` e adicione uma rota para a aplicação:
        ```python
        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('produtos/', include('produtos.urls')),
        ]
        ```
    - *O uso de `include` permite delegar o roteamento das URLs da aplicação para um ficheiro próprio dentro da pasta da app.*

12. **Criar o ficheiro de URLs da aplicação**
    - Dentro da pasta da aplicação (por exemplo, `produtos`), crie um ficheiro chamado `urls.py` com o seguinte conteúdo:
        ```python
        from django.urls import path
        from . import views

        urlpatterns = [
            path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
        ]
        ```
    - *Este ficheiro define as rotas específicas da aplicação, associando URLs às funções de visualização (views).*

13. **Criar a view para a rota da aplicação**
    - No ficheiro `views.py` da aplicação, defina a função que será chamada pela rota criada:
        ```python
        from django.shortcuts import render
        from django.http import HttpResponse

        def cadastrar_produto(request):
            return HttpResponse("Página de cadastro de produto.")
        ```
    - *Esta função retorna uma resposta simples para testar se a rota está a funcionar corretamente. Pode ser expandida para renderizar templates ou processar formulários conforme necessário.*

14. **Criar a pasta de templates e o ficheiro HTML da aplicação**
    - Dentro da pasta da aplicação (por exemplo, `produtos`), crie uma pasta chamada `templates`. Dentro desta pasta, crie um ficheiro chamado `cadastrar.html` que irá conter o código HTML da página de cadastro.
    - No ficheiro `views.py`, altere a função para renderizar o template:
        ```python
        from django.shortcuts import render

        def cadastrar_produto(request):
            return render(request, 'cadastrar.html')
        ```
    - *A criação da pasta `templates` e do ficheiro `cadastrar.html` permite separar a lógica da aplicação da camada visual. O método `render` procura o ficheiro HTML na pasta de templates e exibe-o quando a rota correspondente é acedida.*

15. **Criar o formulário de cadastro com método POST e nomes nos inputs**

    - No ficheiro `cadastrar.html` dentro da pasta `templates` da aplicação, adicione o seguinte formulário:
        - *O atributo `action` define para onde o formulário será enviado, enquanto o `method="post"` garante que os dados sejam enviados de forma segura. Os atributos `name` nos inputs permitem que os valores sejam recuperados no backend através de `request.POST`. O token `{% csrf_token %}` protege contra ataques CSRF.*

        ```html
        <form action="/produtos/cadastrar/" method="post">
            {% csrf_token %}
            <div class="form-group">
                <label for="exampleInputNome">Nome do produto</label>
                <input name="nome_do_produto" type="text" class="form-control" id="exampleInputNome" aria-describedby="nomeHelp" placeholder="Insira o nome do produto">
                <small id="nomeHelp" class="form-text text-muted">Nunca vamos compartilhar seu produto com ninguém.</small>
            </div>
            <div class="form-group">
                <label for="exampleInputPreco">Preço do produto</label>
                <input name="preco_do_produto" type="number" class="form-control" id="exampleInputPreco" placeholder="Insira o preço do produto">
            </div>
            <button type="submit" class="btn btn-primary">Cadastrar</button>
        </form>
        ```
16. **Tratar o método da requisição e capturar dados do formulário**

    - No ficheiro `views.py` da aplicação, ajuste a função para diferenciar entre requisições GET e POST:
        - *Quando o método for `GET`, apenas exibe o formulário HTML. Quando for `POST`, recupera os dados enviados pelo formulário usando `request.POST.get('<nome_do_input>')` e pode processá-los conforme necessário.*

        ```python
        from django.shortcuts import render
        from django.http import HttpResponse

        def cadastrar_produto(request):
            if request.method == 'GET':
                return render(request, 'cadastrar.html')
            elif request.method == 'POST':
                nome = request.POST.get('nome_do_produto')
                preco = request.POST.get('preco_do_produto')
                return HttpResponse(f'Produto cadastrado: {nome}, Preço: {preco}')
        ```
    - *O atributo `request.method` permite identificar o tipo de requisição (GET ou POST). O método `request.POST.get()` é utilizado para obter os valores enviados pelo formulário, usando os nomes definidos nos campos do HTML.*

17. **Migrar todas as tabelas necessárias para o funcionamento correto da aplicação**
    - `uv run manage.py migrate`
    - *Este comando aplica todas as migrações pendentes, criando ou atualizando as tabelas no banco de dados conforme definido pelos modelos do Django. É importante executar este comando sempre que houver alterações nos modelos para garantir que o banco de dados esteja sincronizado com o código.*

18. **Criar o modelo da aplicação**
    - No ficheiro `models.py` da sua aplicação (por exemplo, `produtos/models.py`), defina o modelo que representa a tabela no banco de dados:
        ```python
        from django.db import models

        class Produto(models.Model):
            nome = models.CharField(max_length=100)
            preco = models.DecimalField(max_digits=10, decimal_places=2)
        ```
    - *O modelo `Produto` define os campos que serão armazenados na tabela do banco de dados, utilizando o ORM do Django para facilitar a manipulação dos dados.*

19. **Criar e aplicar as migrações do novo modelo**
    - Para criar as migrações com base no novo modelo, execute:
        - `uv run manage.py makemigrations`
    - Para aplicar as migrações e criar a tabela no banco de dados, execute:
        - `uv run manage.py migrate`
    - *O comando `makemigrations` gera os ficheiros de migração que descrevem as alterações no modelo, enquanto o comando `migrate` aplica essas alterações ao banco de dados, criando ou modificando as tabelas conforme necessário.*

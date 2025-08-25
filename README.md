## Explicação dos passos

1. **Actualizar o uv**
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

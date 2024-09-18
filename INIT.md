## Instalações:
```
python -m pip install Django

pip install pylint-django

python -m pip install django-tailwind

# Recarregamentos automáticos de página durante o desenvolvimento - tailwind
python -m pip install django-tailwind[reload]

```

## 01. Criar o projeto:
```
django-admin startproject biblioteca .

```

## 02. Criar uma aplicação:
```
python manage.py startapp app_biblioteca
```

## 03. Rodar o projeto / aplicação para testar o funcionamento:
```
python manage.py runserver

```

## 04. Configurar o Tailwind:
[Tailwind-Django](https://django-tailwind.readthedocs.io/en/latest/installation.html)


## 05. Iniciar o Django Tailwind no modo de desenvolvimento:
```
python manage.py tailwind start
```

## 06. Criar uma rota e página para o caminho root (http://127.0.0.1:8000/)
```
# 06.1 Criar página de layout em views.py em 'app_biblioteca'
# 06.2 Criar a rota em urls.py na pasta 'biblioteca'
```

## 07. Incluir o nome da aplicação em INSTALLED_APPS de 'settings.py':
```
INSTALLED_APPS = [
    'app_biblioteca.apps.AppBibliotecaConfig',
    ...
    ...
]
```

## 08. Configuração Brasil:
```
# Em settings.py de 'biblioteca':
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'
```


## 09. Configurando o Banco de Dados:
```
python manage.py migrate
```


## 09.1. Criar o model e executar a migração: https://docs.djangoproject.com/pt-br/5.1/intro/tutorial02/
```
python manage.py makemigrations app_biblioteca
```

## 09.2. comando sqlmigrate recebe o nome da migração e o seu SQL.
```
python manage.py sqlmigrate app_biblioteca 0001
```


## 09.3. Aplicando as alterações (modelos) ao Banco de Dados:
```
python manage.py migrate
```


## 09.4. checa problemas no seu projeto sem criar migrations ou tocar seu banco de dados.
```
python manage.py check
```


## 10. Area administrativa: criando um usuário administrativo
```
python manage.py createsuperuser
```

## 10.1 Torne a aplicação de app_bliblioteca editável no site de administração
```
# No módulo admin.py de 'app_bliblioteca' registrar os modelos
from .models import Autor

admin.site.register(Autor)
```

## Biblioteca para uso de imagens no db:
```
python -m pip install Pillow
```

[crispy-tailwind](https://github.com/django-crispy-forms/crispy-tailwind)
## Formuario Django:
```
python -m pip install crispy-tailwind
```

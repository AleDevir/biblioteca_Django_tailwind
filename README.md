## Iniciar o Django Tailwind no modo de desenvolvimento:
```
python manage.py tailwind start
```

## Rodar o projeto / aplicação:
```
python manage.py runserver

```

## pylint
```
pylint --load-plugins pylint_django --django-settings-module=biblioteca.settings biblioteca app_biblioteca

```
## migrations

### registrar as alterações em migrations
```
python manage.py makemigrations app_biblioteca
```

### Aplicar as alterações de migrations no db
```
python manage.py migrate
```
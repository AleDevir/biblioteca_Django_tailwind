# Generated by Django 4.2.16 on 2024-09-18 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_biblioteca', '0008_autor_informacaoes_livro_informacaoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='fonte_informacao',
            field=models.CharField(default='', max_length=100, verbose_name='Fonte'),
        ),
        migrations.AddField(
            model_name='livro',
            name='fonte_informacao',
            field=models.CharField(default='', max_length=100, verbose_name='Fonte'),
        ),
    ]

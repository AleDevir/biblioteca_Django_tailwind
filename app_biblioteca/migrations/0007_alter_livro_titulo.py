# Generated by Django 4.2.16 on 2024-09-17 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_biblioteca', '0006_remove_livro_capa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='titulo',
            field=models.CharField(max_length=300, verbose_name='Título'),
        ),
    ]

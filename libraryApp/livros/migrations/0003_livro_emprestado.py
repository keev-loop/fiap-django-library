# Generated by Django 3.2 on 2021-05-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_livro_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='emprestado',
            field=models.BooleanField(default=False),
        ),
    ]

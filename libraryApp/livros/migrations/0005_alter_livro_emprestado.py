# Generated by Django 3.2 on 2021-05-13 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0004_alter_livro_emprestado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='emprestado',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-15 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_aluno_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(upload_to='media'),
        ),
    ]
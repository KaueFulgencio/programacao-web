# Generated by Django 4.2.4 on 2023-08-17 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_projeto_final', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='email',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='senha',
            field=models.TextField(max_length=255),
        ),
    ]

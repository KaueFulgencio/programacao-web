# Generated by Django 4.2.4 on 2023-08-17 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.TextField(max_length=200)),
                ('senha', models.TextField(max_length=200)),
            ],
        ),
    ]

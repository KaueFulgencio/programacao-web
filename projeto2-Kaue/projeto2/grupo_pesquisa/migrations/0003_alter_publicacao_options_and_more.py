# Generated by Django 4.2.4 on 2023-11-05 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grupo_pesquisa', '0002_alter_integrante_foto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publicacao',
            options={'verbose_name_plural': 'Publicações'},
        ),
        migrations.AlterField(
            model_name='publicacao',
            name='ano_publicacao',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='publicacao',
            name='autores',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='publicacao',
            name='integrante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publicacoes', to='grupo_pesquisa.integrante'),
        ),
    ]

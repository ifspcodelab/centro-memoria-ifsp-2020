# Generated by Django 3.0.7 on 2020-12-09 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituicao', '0003_instituicao_descricao_acervo'),
    ]

    operations = [
        migrations.AddField(
            model_name='instituicao',
            name='youtube',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Youtube'),
        ),
    ]

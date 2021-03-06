# Generated by Django 3.0.7 on 2020-08-06 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_auto_20200806_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='texto',
            field=models.TextField(default='Inauguração aconteceu nesta terça-feira (05), no Câmpus São Paulo. O Centro abriga um grande acervo que testifica os caminhos percorridos pelo Instituto em 110 anos de atividades.', verbose_name='Texto sobre evento'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evento',
            name='descricao',
            field=models.TextField(max_length=250, verbose_name='Descrição'),
        ),
    ]

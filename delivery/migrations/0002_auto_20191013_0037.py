# Generated by Django 2.2.4 on 2019-10-13 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='avatar',
            field=models.ImageField(blank=True, default='pics/None/no-img.png', null=True, upload_to='pics/clientes/'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='quantidade_comentarios',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

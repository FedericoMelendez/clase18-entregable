# Generated by Django 4.0.6 on 2022-07-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0002_familiares_hobbie_familiares_ultimo_mensaje_enviado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiares',
            name='hobbie',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-26 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiares',
            name='hobbie',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='familiares',
            name='ultimo_mensaje_enviado',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='familiares',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

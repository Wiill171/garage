# Generated by Django 5.0.3 on 2024-04-16 23:15

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0005_rename_data_ordem_ordem_data_criacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordem',
            name='observacoes',
            field=models.CharField(blank=builtins.all, max_length=250),
        ),
    ]

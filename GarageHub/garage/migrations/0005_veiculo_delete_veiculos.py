# Generated by Django 4.2.11 on 2024-03-17 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0004_veiculos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('placa', models.CharField(max_length=250)),
                ('motor', models.CharField(max_length=150)),
                ('ano', models.CharField(max_length=50)),
                ('data_criacao', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Veiculos',
        ),
    ]
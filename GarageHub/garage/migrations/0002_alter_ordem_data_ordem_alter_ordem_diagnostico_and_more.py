from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0001_initial'),
    ]

    operations = [
        # Alterações na Ordem
        migrations.AlterField(
            model_name='ordem',
            name='data_ordem',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ordem',
            name='diagnostico',
            field=models.TextField(default='Descreva o problema observado', max_length=150),
        ),
        
        # Alterações no Veiculo
        migrations.AlterField(
            model_name='veiculo',
            name='data_criacao',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
# Generated by Django 4.1.3 on 2022-11-29 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=50)),
                ('complemento', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=50)),
                ('ecliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro_cliente.cliente')),
            ],
        ),
    ]

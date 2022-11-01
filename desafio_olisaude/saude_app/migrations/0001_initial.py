# Generated by Django 3.0.8 on 2022-10-11 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('costumer_name', models.CharField(max_length=40, verbose_name='Nome do Cliente')),
                ('birthday', models.DateField(verbose_name='Data de Nascimento')),
                ('sex', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Sexo')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
            ],
            options={
                'verbose_name': 'Lista de Clientes',
            },
        ),
        migrations.CreateModel(
            name='ProblemsHearth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_name', models.CharField(max_length=50, verbose_name='Problema de Saúde')),
                ('degree_problem', models.IntegerField(choices=[(1, 'Um'), (2, 'Dois')], verbose_name='Grau de Problema')),
                ('atualization_date', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
            ],
            options={
                'verbose_name': 'Problemas de Saúde',
            },
        ),
    ]

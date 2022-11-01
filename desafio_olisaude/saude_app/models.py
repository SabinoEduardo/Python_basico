from django.db import models


# Create your models here.

class Customer(models.Model):
    class Degree(models.IntegerChoices):
        um = 1
        dois = 2

    values_choices = [
        ('M', 'Masculino'),
        ('F', 'Feminino')
    ]
    code = models.AutoField(primary_key=True)
    costumer_name = models.CharField(max_length=40, null=False, verbose_name='Nome do Cliente')
    birthday = models.DateField(auto_now=False, auto_now_add=False, null=False, verbose_name='Data de Nascimento')
    sex = models.CharField(max_length=1, choices=values_choices, verbose_name='Sexo')
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True, null=False, verbose_name='Data de Criação')

    def __str__(self):
        return self.costumer_name

    class Meta:
        verbose_name = 'Lista de Cliente'


class ProblemHearth(models.Model):

    class Degree(models.IntegerChoices):
        um = 1
        dois = 2

    code_costumer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=False,
                                      verbose_name='Nome do Cliente', default='Select')
    problem_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Problema de Saúde')
    degree_problem = models.IntegerField(choices=Degree.choices, verbose_name='Grau de Problema')
    atualization_date = models.DateTimeField(
                                            auto_now=True, auto_now_add=False, null=False,
                                            verbose_name='Data de Atualização'
                                                )

    def __str__(self):
        return self.problem_name

    class Meta:
        verbose_name = 'Problemas de Saúde'

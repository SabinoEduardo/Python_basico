from django.forms import ModelForm
from saude_app.models import Customer, ProblemHearth


class CostumerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('costumer_name', 'birthday', 'sex')


class ProblemsForm(ModelForm):
    class Meta:
        model = ProblemHearth
        fields = ('code_costumer', 'problem_name', 'degree_problem')

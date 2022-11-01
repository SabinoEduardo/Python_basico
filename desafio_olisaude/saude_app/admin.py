from django.contrib import admin
from saude_app.models import (Customer, ProblemHearth)


# Register your models here.

class Customers(admin.ModelAdmin):
    list_display = [
            'code',
            'costumer_name',
            'birthday', 'sex',
            'creation_date',
    ]


admin.site.register(Customer, Customers)


class ProblemsHearthList(admin.ModelAdmin):
    list_display = [
            'problem_name',
            'degree_problem',
            'atualization_date'
    ]


admin.site.register(ProblemHearth, ProblemsHearthList)

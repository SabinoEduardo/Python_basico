from saude_app.models import Customer, ProblemHearth
from django.shortcuts import render, redirect
from saude_app.conect_db import select_problems
from saude_app.forms import CostumerForm, ProblemsForm
from http import HTTPStatus


# Create your views here.


def list_costumers(request):
    if request.method == 'GET':
        status_code = HTTPStatus.OK.value
        msg = HTTPStatus.OK.phrase
        problems = list(ProblemHearth.objects.values())
        costumers = list(Customer.objects.values())
        data = {
            'costumer': costumers,
            'problems': problems,
            'code': status_code,
            'msg': msg
        }
        return render(request, 'base.html', data)


def create_costumer(request):
    form = CostumerForm(request.POST or None)
    if form.is_valid():
        form.save()
        if 'save_and_continue' in form.cleaned_data:
            return redirect('/create_costumer')
        elif 'save' in form.cleaned_data:
            # do unsubscribe
            return redirect('/costumer')
    context = {'formset': form}
    return render(request, 'create_costumer.html', context)


def add_problems(request):
    form = ProblemsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/add_problem')
    context = {'formset': form}
    return render(request, 'create_costumer.html', context)


def get_costumer(request, code):
    costumer = Customer.objects.filter(code=code)
    if costumer:
        problems = list(ProblemHearth.objects.filter(code_costumer_id=code))
        status_code = HTTPStatus.OK.value
        msg = HTTPStatus.OK.phrase
        data = {
            'costumer': costumer,
            'problems': problems,
            'code': status_code,
            'msg': msg
        }
    else:
        status_code = HTTPStatus.NOT_FOUND.value
        msg = HTTPStatus.NOT_FOUND.phrase
        data = {
            'code': status_code,
            'msg': msg
        }
    return render(request, 'get_costumer.html', data)


def calculate_score(request):
    data_problem_score = select_problems()
    costumers = list(Customer.objects.values())
    status_code = HTTPStatus.OK.value
    msg = HTTPStatus.OK.phrase
    data = {
        'costumer': costumers,
        'problems': data_problem_score,
        'code': status_code,
        'msg': msg
    }
    return render(request, 'calculate_score.html', data)

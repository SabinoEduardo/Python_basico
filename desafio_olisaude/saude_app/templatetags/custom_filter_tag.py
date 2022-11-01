from django import template
import json
from datetime import datetime


register = template.Library()


@register.simple_tag
def list_costumer_json(date_costumers, date_problems):
    list_date = list()
    for date_costumer in date_costumers:
        n = 0
        dict_costumer = dict()
        dict_problem = dict()
        for date_problem in date_problems:
            for key, value in date_costumer.items():
                if date_costumer['code'] == date_problem['code_costumer_id']:
                    if isinstance(value, datetime):
                        n += 1
                        dict_problem[f'problem_name {n}'] = date_problem['problem_name']
                        dict_problem[f'degree_problem {n}'] = date_problem['degree_problem']
                        dict_costumer['problems'] = dict_problem
                        date_creation = value.strftime('%Y/%m/%d %I:%M:%S %p')
                        dict_costumer[key] = str(date_creation)
                    elif isinstance(value, int):
                        dict_costumer[key] = int(value)
                    else:
                        dict_costumer[key] = str(value).title()
                    date_atulization = date_problem['atualization_date'].strftime('%Y/%m/%d %I:%M:%S %p')
                    dict_costumer['atualization_date'] = str(date_atulization)

                else:
                    if isinstance(value, datetime):
                        dict_costumer['problems'] = dict_problem
                        date_creation = value.strftime('%Y/%m/%d %I:%M:%S %p')
                        dict_costumer[key] = str(date_creation)
                    elif isinstance(value, int):
                        dict_costumer[key] = int(value)
                    else:
                        dict_costumer[key] = str(value).title()
        list_date.append(dict_costumer.copy())
    date = json.dumps(list_date, indent=4, ensure_ascii=False)
    return date


@register.simple_tag
def get_costumer_json(date_costumer, date_problems):
    dict_costumer = dict()
    dict_problem = dict()
    for date in date_costumer:
        dict_costumer['code'] = int(date.code)
        dict_costumer['costumer_name'] = str(date.costumer_name).title()
        dict_costumer['birthday'] = str(date.birthday)
        dict_costumer['sex'] = str(date.sex)
        dict_costumer['creation_date'] = str(date.creation_date.strftime('%Y/%m/%d %I:%M:%S %p'))

    n = 1
    for date in date_problems:
        dict_problem[f'problem_name {n}'] = str(date.problem_name)
        dict_problem[f'degree_problem {n}'] = int(date.degree_problem)
        n += 1
    dict_costumer['problems'] = dict_problem
    date = json.dumps(dict_costumer, indent=4, ensure_ascii=False)
    return date


@register.simple_tag
def list_problem_score_json(date_problems, date_costumers):
    list_dados = list()
    dict_score = dict()
    for date_problem in date_problems:
        for date_costumer in date_costumers:
            if date_costumer['code'] == date_problem[0]:
                dict_score['costumer_code'] = date_costumer['code']
                dict_score['costumer_name'] = date_costumer['costumer_name'].title()
                dict_score['score'] = float(date_problem[1])
                list_dados.append(dict_score.copy())
    date = json.dumps(list_dados, indent=4)
    return date

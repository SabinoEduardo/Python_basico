from minhas_funcoes import add_task, desfazer_lista, refazer_lista
from time import sleep

lista_tarefas = list()
new_list = list()
a = []
print("_" * 40)
print(f"{'Menu':>30}")
print(f"1 - Adicionar Tarefa")
print(f"2 - Desfazer Lista")
print(f"3 - Refazer Lista")
print(f"4 - Ver Lista de tarefas")
print(f"5 - Fechar o programa")
print("_"*40)
while True:
    op = input("Escolha uma opção:")
    print("_" * 40)
    if op.isnumeric():
        if int(op) == 1:
            print(f" -- Adicionar Tarefa --")
            tarefa = input("Tarefa:")
            add_task(lista_tarefas, tarefa)
        elif int(op) == 2:
            desfazer_lista(lista_tarefas, new_list)
        elif int(op) == 3:
            refazer_lista(lista_tarefas, new_list)
        elif int(op) == 4:
            if len(lista_tarefas) > 0:
                for k, v in enumerate(lista_tarefas):
                    print(f"Tarefa {k + 1} - {v}")
            else:
                print("Lista de tarefas está vazia")
        else:
            break
    sleep(0.5)

print("Até mais")

def adicionar_tarefa(lista_tarefas, tarefas):
    lista_tarefas.append(tarefas)


def deletar_tarefa(lista_tarefas, tarefas_deletadas):
    """
        Esta função serve para deletar a ultima tarefa da lista e guarda esta tarefa em outra lista.
    """
    if not lista_tarefas:
        print("Nada a deletar")
        return
    tarefas_deletadas.append(lista_tarefas[-1])
    lista_tarefas.pop()


def repor_tarefa(lista_tarefas, tarefas_deletadas):
    """
        Esta função serve para repor ultima tarefa deletada da lista de tarefas.
    """
    if not tarefas_deletadas:
        print("Nada a repor")
        return
    else:
        lista_tarefas.append(tarefas_deletadas[-1])
        tarefas_deletadas.pop()

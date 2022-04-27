def add_task(lista, task):
    lista.append(task)


def desfazer_lista(lista, nova_lista):
    if len(lista) == 0:
        print("Nada a desfazer")
        return
    nova_lista.append(lista[len(lista)-1])
    lista.pop()


def refazer_lista(lista, nova_lista):
    if len(nova_lista) == 0:
        print("Nada a refazer")
        return
    else:
        lista.append(nova_lista[len(nova_lista)-1])
        nova_lista.pop()

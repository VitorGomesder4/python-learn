lista_tarefas = []
lista_tarefas_completadas = []
print("Digite 'help' para exibir o menu\n")

while True:
    input_cli = input("").lower()
    if input_cli == "help":
        print("""Menu:
1. Adicionar tarefa
2. Ver tarefas
3. Atualizar tarefas
4. Completar tarefas
5. Deletar tarefas
6. Exit (Pode ser usado para sair de qualquer instancia)""")
        
    elif input_cli in ["adicionar tarefa", "1"]:
        while True:
            tarefa_adicionar = input("Digite suas tarefas a adicionar (exit para terminar): ")
            if tarefa_adicionar in lista_tarefas:
                print("Essa tarefa ja existe\n")
                continue
            elif tarefa_adicionar == "exit":
                print("Voltando ao menu..\n")
                break
            else:
                lista_tarefas.append(tarefa_adicionar)
                continue

    elif input_cli in ["ver tarefa", "2"]:
        print("Tarefas: \n")
        for indice, tarefa in enumerate(lista_tarefas):
            print(f"Tarefa: {indice + 1}: {tarefa}", end=" ")
        print("\n")
        print("Tarefas completadas: \n")
        for indice, tarefa_completada in enumerate(lista_tarefas_completadas):
            print(f"Tarefa: {indice + 1}: {tarefa_completada}", end=" ")
        print()

    elif input_cli in ["atualizar tarefa", "3"]:
        while True:
            tarefa_atualizar = input("Digite a tarefa a ser atualizada: ")
            if tarefa_atualizar == "exit":
                print("Voltando ao menu..\n")
                break
            elif tarefa_atualizar in lista_tarefas:
                for i in range(len(lista_tarefas)):
                    if lista_tarefas[i] == tarefa_atualizar:
                        while True:
                            nova_tarefa = input("Digite a nova tarefa: \n")
                            if nova_tarefa in lista_tarefas:
                                print("Essa tarefa ja existe\n")
                                continue
                            else:
                                lista_tarefas[i] = nova_tarefa
                                print(f"Tarefa atualizada: {lista_tarefas[i]}\n")
                                break
                break

    elif input_cli in ["completar tarefa", "4"]:
        while True:
            tarefa_completar = input("Digite sua tarefa a completar (exit para sair): ")
            if tarefa_completar == "exit":
                print("Voltando ao menu..\n")
                break

            elif tarefa_completar in lista_tarefas:
                lista_tarefas_completadas.append(tarefa_completar)
                lista_tarefas.remove(tarefa_completar)
                print(f"Tarefa '{tarefa_completar}' completada.\n")
                break

            else:
                print("Essa tarefa não se encontra na lista\n")
                continue
            break

    elif input_cli in ["deletar tarefa", "5"]:
        while True:
            tarefa_deletar = input("Digite sua tarefa a deletar: ")

            if tarefa_deletar in lista_tarefas:
                for tarefa in lista_tarefas:
                    if tarefa == tarefa_deletar:
                        lista_tarefas.remove(tarefa)
                        print(f"Tarefa '{tarefa}' removida")
                break

            elif tarefa_deletar in lista_tarefas_completadas:
                for tarefa in lista_tarefas_completadas:
                    if tarefa == tarefa_deletar:
                        lista_tarefas_completadas.remove(tarefa)
                        print(f"Tarefa '{tarefa}' removida")
                break

            elif tarefa_deletar == "exit":
                print("Voltando ao menu..\n")
                break

            else:
                print("Tarefa não encontrada para delete\n")
                continue
while True:
    print("Menu:\n1 Adicionar tarefa\n2 Vizualizar tarefas\n3 Atualizar tarefa\n4 Completar tarefa\n5 Deletar tarefa completada\n6 Sair")
    input_cli = str(input(""))
    match input_cli:
        case "1":
            print("Adicionando")
        case "2":
            print("Visualizando")
        case "3":
            print("Atualizando")
        case "4":
            print("Completando")
        case "5":
            print("Deletando")
        case "6":
            print("Exit")
            break
        case _:
            print("Opção inválida. Tente novamente.")
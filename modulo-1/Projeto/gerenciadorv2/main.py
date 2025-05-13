from gerenciadorv2 import GerenciadorDeTarefasv2

print("""Help para ver o menu:
      1.Adicionar tarefa
      2.Vizualizar tarefas
      3.Atualizar tarefas
      4.Completar tarefas
      5.Deletar tarefas
      6.Sair\n""")
while True:
    inputcli = input().lower().strip()

    match inputcli:

        case "1":
            tarefa = input("Digite a tarefa: ")
            GerenciadorDeTarefasv2.adicionar_tarefa(tarefa)
            pass

        case "2":
            GerenciadorDeTarefasv2.ver_tarefas()
            pass

        case "3":
            GerenciadorDeTarefasv2.atualizar_tarefas()
            pass

        case "4":
            GerenciadorDeTarefasv2.completar_tarefas()
            pass

        case "5":
            GerenciadorDeTarefasv2.deletar_tarefas()
            pass

        case "6":
            GerenciadorDeTarefasv2.exit()
            pass

        case "help":
            GerenciadorDeTarefasv2.exibir_menu()
            pass
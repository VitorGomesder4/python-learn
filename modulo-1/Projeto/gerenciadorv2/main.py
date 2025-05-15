from gerenciadorv2_corrigido import GerenciadorDeTarefasv2

gerenciador = GerenciadorDeTarefasv2()

programa = True

print("""Help para ver o menu:
      1.Adicionar tarefa
      2.Vizualizar tarefas
      3.Atualizar tarefas
      4.Completar tarefas
      5.Deletar tarefas
      6.Sair\n""")

while programa:

    inputcli = input().strip()

    match inputcli:

        case "1":
            gerenciador.adicionar_tarefas()

        case "2":
            gerenciador.ver_tarefas()
            pass

        case "3":
            gerenciador.atualizar_tarefas()
            pass

        case "4":
            gerenciador.completar_tarefas()
            pass

        case "5":
            gerenciador.deletar_tarefas()
            pass

        case "6":
            programa = gerenciador.exit()
            

        case "help":
            gerenciador.exibir_menu()
            pass
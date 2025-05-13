class GerenciadorDeTarefasv2():
    
    def __init__(self):
        self.lista_tarefas = []

    def adicionar_tarefas(self, tarefa):
        self.lista_tarefas.append(tarefa)

    def ver_tarefas(self):
        pass

    def atualizar_tarefas(self, tarefa):
        pass

    def completar_tarefas(self, tarefa):
        pass

    def deletar_tarefas(self, tarefa):
        self.lista_tarefas.remove(tarefa)

    def exit():
        pass

    def exibir_menu():
        print("""Help para ver o menu:
        1.Adicionar tarefa
        2.Vizualizar tarefas
        3.Atualizar tarefas
        4.Completar tarefas
        5.Deletar tarefas
        6.Sair\n""")
        pass
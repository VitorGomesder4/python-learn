class GerenciadorDeTarefasv2():
    
    def __init__(self):
        self.lista_tarefas = []
        self.lista_tarefas_completadas = []

    def adicionar_tarefas(self):
        contador = 1
        print("'stop' para parar de adicionar tarefas")

        while True:
            tarefa = input(f"Tarefa {contador}: ").lower().strip()

            if tarefa == "stop":
                print("Parando...\n")
                break

            else:
                self.lista_tarefas.append(tarefa.capitalize())
                print(f"Tarefa '{tarefa}' adicionada com sucesso! \n")
                contador += 1
                continue

    def ver_tarefas(self):
        for tarefa in self.lista_tarefas:
            print(tarefa, end=" ")
        print()

    def atualizar_tarefas(self):

        tarefa = input("Digite a tarefa a atualizar: ").strip().lower().capitalize()
        for i in self.lista_tarefas:
            if i == tarefa:
                antiga_tarefa = i
                i = input("Digite a nova tarefa: ")
                result = print(f"Tarefa {antiga_tarefa} atualizada para {i}.\n")
                break

            else:
                result = print("tarefa não encontrada.\n")
                break

        return result

    def completar_tarefas(self):
        tarefa = input("Digite a tarefa a completar: ").strip().lower().capitalize()

        if tarefa in self.lista_tarefas:
            self.lista_tarefas_completadas.append(tarefa)
            result = print(f"Tarefa '{tarefa}' completada.\n")

        else:
            result = print("tarefa não encontrada.\n")

        return result

    def deletar_tarefas(self):

        print("""Voce deseja:
              1. Deletar tarefas atuais
              2. Deletar tarefas na lista de completas""")
        input_ = input()
        if input_ == "1":
            tarefa = input("Digite a tarefa a deletar: ").strip().lower().capitalize()

            try:
                self.lista_tarefas.remove(tarefa)
            except ValueError:
                print(f"Erro: {ValueError}.\nValor '{tarefa}' nao encontrado.\n")
            
        elif input_ == "2":
            tarefa = input("Digite a tarefa a deletar: ").strip().lower().capitalize()

            try:
                self.lista_tarefas_completadas.remove(tarefa)
            except ValueError:
                print(f"Erro: {ValueError}.\nValor '{tarefa}' nao encontrado.\n")


    def exit(self):
        inputcli = input("Tem certeza que deseja finalizar o programa? (s/n): ").strip().lower()
        while True:

            if inputcli in ["s", "sim"]:
                return False
            
            elif inputcli in ["n", "nao", "não"]:
                return True
            
            else:
                print("Comando invalido")
                continue

    def exibir_menu(self):
        result = print("""Help para ver o menu:
        1.Adicionar tarefa
        2.Vizualizar tarefas
        3.Atualizar tarefas
        4.Completar tarefas
        5.Deletar tarefas
        6.Sair\n""")
        return result
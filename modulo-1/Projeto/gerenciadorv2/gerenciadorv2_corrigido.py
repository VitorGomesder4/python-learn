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
        if not self.lista_tarefas:  # Mostrar mensagem se lista vazia
            print("Nenhuma tarefa cadastrada.\n")
            return
        
        for indice, tarefa in enumerate(self.lista_tarefas, start = 1):
            print(f"Indice. [{indice}]. Tarefa = [{tarefa}]")  # Mostrar uma por linha para melhor leitura
        print()

    def atualizar_tarefas(self):
        tarefa = input("Digite a tarefa a atualizar: ").strip().lower().capitalize()
        for idx, tarefa_atual in enumerate(self.lista_tarefas):  # Percorrer com índice para alterar lista
            if tarefa_atual == tarefa:
                nova_tarefa = input("Digite a nova tarefa: ").strip().capitalize()
                self.lista_tarefas[idx] = nova_tarefa  # Atualizar lista corretamente
                print(f"Tarefa '{tarefa}' atualizada para '{nova_tarefa}'.\n")
                return  # Sai após atualizar
        
        print("Tarefa não encontrada.\n")  # Se não achar, só imprime aqui (fora do loop)

    def completar_tarefas(self):
        tarefa = input("Digite a tarefa a completar: ").strip().lower().capitalize()

        if tarefa in self.lista_tarefas:
            self.lista_tarefas_completadas.append(tarefa)
            print(f"Tarefa '{tarefa}' completada.\n")  # Não atribuir resultado do print a variável

        else:
            print("Tarefa não encontrada.\n")

    def deletar_tarefas(self):
        print("""Você deseja:
              1. Deletar tarefas atuais
              2. Deletar tarefas na lista de completas""")
        escolha = input()
        if escolha == "1":
            tarefa = input("Digite a tarefa a deletar: ").strip().lower().capitalize()

            try:
                self.lista_tarefas.remove(tarefa)
                print(f"Tarefa '{tarefa}' removida da lista atual.\n")
            except ValueError as e:  # Capturar exceção como e para mostrar mensagem correta
                print(f"Erro: {e}\nValor '{tarefa}' não encontrado.\n")
            
        elif escolha == "2":
            tarefa = input("Digite a tarefa a deletar: ").strip().lower().capitalize()

            try:
                self.lista_tarefas_completadas.remove(tarefa)
                print(f"Tarefa '{tarefa}' removida da lista de completas.\n")
            except ValueError as e:
                print(f"Erro: {e}\nValor '{tarefa}' não encontrado.\n")

    def exit(self):
        while True:  # Loop para repetir até receber entrada válida
            inputcli = input("Tem certeza que deseja finalizar o programa? (s/n): ").strip().lower()
            if inputcli in ["s", "sim"]:
                return False
            
            elif inputcli in ["n", "nao", "não"]:
                return True
            
            else:
                print("Comando inválido")

    def exibir_menu(self):
        print("""Help para ver o menu:
        1.Adicionar tarefa
        2.Visualizar tarefas
        3.Atualizar tarefas
        4.Completar tarefas
        5.Deletar tarefas
        6.Sair\n""")  # print não precisa retornar valor
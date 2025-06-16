import time
import textwrap

class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
        self.__strength_modifier = 1
        self.__redutor_dano = 1
    
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def get_strength_modifier(self):
        return self.__strength_modifier
    
    @property
    def redutor_dano(self):
        return self.__redutor_dano
    
    @redutor_dano.setter
    def redutor_dano(self, valor):
        self.__redutor_dano = valor

    def exibir_detalhes(self):
        return f"{self.get_nome()}\nHP: {self.get_vida()} LVL: {self.get_nivel()}"
    
    def receber_ataque(self, dano):
        self.__vida -= dano * self.__redutor_dano
        if self.__vida <= 0:
            self.__vida = 0
    
    def ataque_normal(self, alvo):
        dano_base = self.__nivel * 2
        dano_final = ((dano_base) + self.__strength_modifier) * alvo.redutor_dano
        alvo.receber_ataque(dano_final)
        print(f"\n{self.get_nome()} atacou {alvo.get_nome()} e causou {dano_final} de dano\n")

class Heroi(Personagem):

    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"\n{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"
    
    def ataque_especial(self, alvo):
        dano = (self.get_nivel() * 5) + self.get_strength_modifier()
        alvo.receber_ataque(dano)
        print(f"\n{self.get_nome()} usou {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano\n")

    def fortalecer(self, lvl_skill):

        if lvl_skill == 1:
            percentual_redutor = 90

        elif lvl_skill == 2:
            percentual_redutor = 85

        elif lvl_skill == 3:
            percentual_redutor = 80

        else:
            raise ValueError("\nInvalido\n")
        
        self.redutor_dano *= percentual_redutor/100

        print(f"\n{self.get_nome()} se fortaleceu (Redutor de dano de {100 - percentual_redutor}%)")

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"\n{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"

class Batalha:
    """ Classe Orquestradora do jogo """

    def __init__(self) -> None:
        self.heroi = Heroi(nome = "Player", vida = 100, nivel = 5, habilidade = "Heavy punch")
        self.inimigo = Inimigo(nome="Morcego", vida = 30, nivel = 3, tipo = "Aerial")

    def iniciar_batalha(self):
        """ Fazer gestão da batalha em turnos """
        print("Iniciando batalha\n")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            
            print(textwrap.dedent(f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢖⣒⣶⣦⣴⣶⣶⣤⣄⠀⠀⠀⠀⠀⠀          _________________               _________________
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣡⣿⣿⣿⣿⣿⣿⣿⡿⠛⠀⠀⢠⣶⣦         ~-.              \  |\___/|  /              .-~
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿             ~-.           \ / o o \ /           .-~
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄                >           \\  W  //           <
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠉⠙⣿⣿⡇               /             /~---~\             \
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣋⠀⠀⠀⠀⠈⠉⠁              /_            |       |            _\
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄                      ~-.       |       |        .-~
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿                           ;     \     /        i
⠀⠀⠀⠀⠀⢠⣴⣾⣿⣿⣿⣿⡿⠋⠁⠀⠈⠻⢿⠛⣿⣿⣿⣿⡇                       /___      /\   /\      ___\
⠀⠀⠀⠀⣀⣾⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⡿⠇                            ~-. /  \_/  \ .-~
⠀⠀⠀⣼⣿⡿⠿⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⡇                                 V         V
⠀⠀⠀⠿⣿⣿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠿⢿⣷⡦

        {self.heroi.get_nome()}                                   {self.inimigo.get_nome()} 
        {self.heroi.exibir_detalhes()}                            {self.inimigo.exibir_detalhes()}
"""))
            time.sleep(0.5)
            #Turno do player
            escolha = input(f"1- Ataque normal, 2- {self.heroi.get_habilidade()} ,3- fortalecer ").strip()

            if escolha == "1":
                self.heroi.ataque_normal(self.inimigo)
                time.sleep(1.5)
            
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
                time.sleep(1.5)

            elif escolha == "3":
                self.heroi.fortalecer(1)
                time.sleep(1.5)
            
            else:
                print("Escolha invalida selecione 1 ou 2\n")
                continue

            #Turno do inimigo
            
            if self.inimigo.get_vida() > 0:
                self.inimigo.ataque_normal(self.heroi)
                time.sleep(1.5)

        if self.heroi.get_vida() <= 0: #Se o heroi morreu
            print("\nDefeat..\n")

        elif self.inimigo.get_vida() <= 0: #Se o inimigo morreu
            print("\nVictory!\n")

        else:
            print("???")

jogo = Batalha()
jogo.iniciar_batalha()
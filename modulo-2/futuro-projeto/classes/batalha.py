import time
import textwrap
from classes.personagem import Personagem
from classes.heroi import Heroi
from classes.inimigo import Inimigo

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
            #Turno do player
            print(f"\n{self.heroi.get_nome()}'s turn")
            escolha = input(f"1- Ataque normal, 2- {self.heroi.get_habilidade()} ,3- fortalecer ").strip()

            if escolha == "1":
                self.heroi.ataque_normal(self.inimigo)
                time.sleep(2)
            
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
                time.sleep(2)

            elif escolha == "3":
                self.heroi.fortalecer(3)
                time.sleep(2)
            
            else:
                print("Escolha invalida selecione 1 ou 2\n")
                continue

            #Turno do inimigo
            print(f"\n{self.inimigo.get_nome()}'s turn")
            if self.inimigo.get_vida() > 0:
                self.inimigo.ataque_normal(self.heroi)
                time.sleep(2)

        if self.heroi.get_vida() <= 0: #Se o heroi morreu
            print("\nDefeat..\n")

        elif self.inimigo.get_vida() <= 0: #Se o inimigo morreu
            print("\nVictory!\n")

        else:
            print("???")
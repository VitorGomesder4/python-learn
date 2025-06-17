import random
from classes.personagem import Personagem

class Heroi(Personagem):

    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"\n{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"
    
    def ataque_especial(self, alvo):
        dano = (self.get_nivel() * random.randrange(1, 4)) + self.strength_modifier
        alvo.receber_ataque(dano)
        print(f"\n{self.get_nome()} usou {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano\n")

    def fortalecer(self, lvl_skill):

        if lvl_skill == 1:
            percentual_redutor = 90
            self.strength_modifier = 1
        elif lvl_skill == 2:
            percentual_redutor = 85
            self.strength_modifier = 2
        elif lvl_skill == 3:
            percentual_redutor = 80
            self.strength_modifier = 3
        else:
            raise ValueError("\nInvalido\n")

        self.redutor_dano *= percentual_redutor/100

        print(f"\n{self.get_nome()} se fortaleceu (Redutor de dano de {100 - percentual_redutor}%)")
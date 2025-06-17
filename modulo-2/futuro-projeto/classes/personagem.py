import random
class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
        self.__strength_modifier = 0
        self.__redutor_dano = 1
    
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    @property
    def strength_modifier(self):
        return self.__strength_modifier
    
    @strength_modifier.setter
    def strength_modifier(self, valor):
        self.__strength_modifier = valor
    
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
        dano_base = self.get_nivel() * random.randrange(1, 4)
        dano_final = ((dano_base) + self.__strength_modifier) * alvo.redutor_dano
        alvo.receber_ataque(dano_final)
        print(f"\n{self.get_nome()} atacou {alvo.get_nome()} e causou {dano_final} de dano\n")
        print(f"Agora {alvo.get_nome()} possui {alvo.get_vida()} de hp\n")
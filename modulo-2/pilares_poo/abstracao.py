print(f"\nExemplo de abstração:\n")

#Classes abstratas são um bom habito para trabalhar com Banco de dados

from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self, cor) -> None:
        self.cor = cor

    def ligar(self):
        return f"Ligando carro {self.cor}"
    
    def desligar(self):
        return f"Desligando carro {self.cor}"

carro_amarelo = Carro("Amarelo") #Sera preciso que a classe carro implemente os metodos da classe abstrata para funcionar

print(carro_amarelo.ligar().lower())
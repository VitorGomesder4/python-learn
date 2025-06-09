class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} esta amamentando"
    
class Ave(Animal):
    def voar(self):
        return f"{self.nome} Voando"
    
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return "Sons de morcego"
    
morcego = Morcego(nome = "Batman")

#Acessando os metodos herdados da classe Animal

print("Nome do morcego:", morcego.nome)
print("Som do morcego:", morcego.emitir_som())

#Acessando os metodos herdados das classes Mamifero e Ave
print("Morcego amamentando:", morcego.amamentar())
print("Morcego voando:", morcego.voar())
#Exemplo de herança

print('\nExemplo Herança:')

class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andou.\n")

    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "AU AU AU"
    
class Gato(Animal):
    def emitir_som(self):
        return "MIAAAAU"
    
#Cachorro e Gato apresentam polimofirsmo a parte de emitir som

dog = Cachorro("Felix")
cat = Gato("João")

animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} Faz: {animal.emitir_som()}")
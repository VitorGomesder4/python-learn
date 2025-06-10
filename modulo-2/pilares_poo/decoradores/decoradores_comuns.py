# @classmethod
# @staticmethod

class MinhaClasse:
    valor = 10 #atributo da classe

    def __init__(self, nome) -> None:
        self.nome = nome

    #requer uma instancia
    def metodo_instancia(self):
        return f"Ola {self.nome} com valor {self.valor}"
    
    @classmethod
    def metodo_de_classe(cls):
        return f"Método de classe chamado para valor = {cls.valor}" #O método de classe apenas acessa os atributos da classe e não dos metodos, self.nome não funcionaria
    
    @staticmethod
    def metodo_estatico(): #Não recebe argumentos
        return "Método estático chamado"

obj = MinhaClasse(nome = "Vitor")

print(obj.metodo_instancia())

#para acessar metodos da classe é preciso instaciar ele antes, ja um atributo predefinido não é preciso

print(MinhaClasse.metodo_de_classe())

#chamando metodo estatico
print(MinhaClasse.metodo_estatico())


#Para que usamos o class method
class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    @classmethod #Podemos criar o class method para uma função que instancia a classe
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, ano)

configuracao = "Toyota,Corolla,2022"

carro = Carro.criar_carro(configuracao)

print(f"\nMarca: {carro.marca}\nModelo: {carro.modelo}\nAno: {carro.ano}\n")

#Para que usamos o static method
class Matematica:

    @staticmethod #O static method pode ser usada para quando queremos usar uma função especifica sem precisar instanciar a classe
    def somar(a, b):
        x = a + b
        return f"{a} + {b} = {x}"
    
print(Matematica.somar(a = 5, b = 5))
#Atenção: Criar muitos static methos não é um bom sinal de programação
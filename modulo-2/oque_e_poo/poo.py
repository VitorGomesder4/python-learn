#Clase é um modelo que define a estrutura e comportamento dos objetos

#Classe exemplo
class Pessoa():
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def descricao(self):
        return f"Nome: {self.nome} & Idade: {self.idade}"

    def cantar(self):
        return f"Larilarila para voce {self.nome}"
    
#Objeto exemplo

pessoa = Pessoa("Vitor", 18) #criação de uma instancia a partir da classe Pessoa

print(f"\n{pessoa.descricao()}\n")

pessoa2 = Pessoa(nome = "Rodrigo", idade = 52)

print(f"\n{pessoa2.descricao()}\n")
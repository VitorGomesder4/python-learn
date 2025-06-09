#Mudar o comportamento de uma classe sem mexer no codigo original

print("1\n")
def meu_decorador(func):

    def wrapper():
        print("Antes da função ser chamada\n")
        func()
        print("\nDepois de ser chamada\n")

    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função foi chamada")

minha_funcao()

print("\n2\n")

class MeuDecoradorDeClasses:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> any:
        print("Antes da função ser chamada (Decorador de classe)\n")
        self.func()
        print("\nDepois de ser chamada (Decorador de classe)\n")

@MeuDecoradorDeClasses
def segunda_funcao():
    print("Segunda funcao foi chamada")

segunda_funcao()
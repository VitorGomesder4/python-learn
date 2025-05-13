# Exemplo
def saudacao(nome):
    print(f"Ola {nome}\n")

saudacao("Joao")

# Quadrado de um número
def quadrado(x):
    result = x ** 2
    return result

numero = 5
quadrado_num = quadrado(numero)
print("O quadrado de", numero, "é", quadrado_num, "\n")

#chamando função com multiplos parametros
def soma(x, y):
    soma_r = x + y
    return soma_r

numerox = 5
numeroy = 5

resultadosoma = soma(numerox, numeroy)
print("O resultado da soma de", numerox, "e", numeroy, "é", resultadosoma, "\n")
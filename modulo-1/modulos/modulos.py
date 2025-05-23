print("Exemplo de importação de módulo padrão: ")
from math import sqrt #importando apenas a função de raiz

raiz_quad = sqrt(4)
print(raiz_quad)

print("\nExemplo de criação e utilização de um módulo personalizado: ")

from meu_modulo import saudacao, quadrado #importando duas funções do meu modulo

meu = saudacao(" vItor")
print(meu)

quad = quadrado(5)
print("{:.2f}".format(quad))
#tupla
tupla = ("Vitor", 1, 2, 3)

print(f"tupla[0]: {tupla[0]}\n")

#metodo count() conta quantas vezes o valor aparece
contagem = tupla.count("Vitor")
print(f"contagem: {contagem}\n")

#metodo index() procura o elemento especificado
print("Vitor se encontra em:")
print(tupla.index("Vitor"))
for i in range(10):
    print(i + 1, end=" ")

print(),print()

lista = [1, 2, 3, 4]

for x in lista:
    print(x, end=" ") #end para não haver quebra de linha

print(),print()


dicionario = {"cidade": "New york", "rua": "8", "sol": False}

for key_value in dicionario.items():
    print(key_value, end="  ")

print(),print()

#range() retorna um intervalo numerico
#[0,1,2,3,4...]
lista0a10 = list(range(1, 5))

for i in range(0, len(lista0a10)):
    print("Indice: ", i)
    print("Elemento", lista0a10[i])

#enumerate()
lista_enum = [1,2,3,4,5]
print(),print()

for indice, valor in enumerate(lista_enum):
    print(f"{indice}: {valor}", end=" ") 
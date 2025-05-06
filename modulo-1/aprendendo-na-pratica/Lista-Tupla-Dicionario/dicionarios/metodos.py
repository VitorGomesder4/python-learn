#Metodos do dicionarios

humano = {"nome": "Maria", "rg": 23043526, "idade": 32}

humano["nome"] = "Mariadb"

#metodo remover par chave-valor

del humano["rg"]

print(humano)

#metodos: keys(), values(), items()

keys = humano.keys()
values = humano.values()
items = list(humano.items()) #transformando o dict_items em lista pois mesmo que o dictitems seja iteravel não é indexavel

print(f"""
Keys: {keys}
Values: {values}
Items: {items}
""")

print(f"Primeiro valor items: {items[0][0]}")
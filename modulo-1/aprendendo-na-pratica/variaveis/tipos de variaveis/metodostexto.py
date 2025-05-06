nome = " Vi tor"

#metodo lower() e upper()

nomeminus = nome.lower() #retorna tudo minusculo
nome.upper() #retorna tudo maiusculo

#metodo count() e find()
print("metodo count:")
print(nomeminus.count("v"))
print()
print("metodo find:")
print(nomeminus.find(" "))
print()

#metodo encode() decode()
print("metodo encode:")
print(nome.encode().decode())
print()
#metodo replace()
print("metodo replace")
print(nomeminus.replace("v", "V"))

#metodo join()

print("metodo join:")
print(" ".join(nomeminus))
print()
#metodo strip() e rstrip()
nome_tratado = nomeminus.strip(" ")
print(f"nome_tratado: {nome_tratado}\n")

nome_tratado_apenasdireita = nomeminus.rstrip(" ")
print(f"nome_tratado_apenasdireita: {nome_tratado_apenasdireita}\n")

#metodo split()
listasubstrings = nome_tratado.split(" ")
print(f"listasubstrings: {listasubstrings}\n")

#metodo startswith()
print(nome_tratado.startswith("vi"))
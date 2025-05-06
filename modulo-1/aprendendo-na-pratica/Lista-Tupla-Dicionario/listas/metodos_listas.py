lista = [0, 1, 2, 3, 4]
print(lista)
print()


#metodo append() adicionar elementos no final da lista
lista.append(5)

#metodo insert() insere um elemento em um indice especificado
print(lista.insert(0, 6))


print(lista)
print()

#metodo sort() e sorted()
#como podemos ver inserimos o 6 no começo do lista logo ela não esta ordenada

#lista_sorted = lista.sorted() #ordena uma nova lista separada e retorna    
#print(lista_sorted)                                                               ! APENAS PARA VERSÕES A PARTIR DE 3.13.3 !
#print()

lista.sort() #ordena a lista atual
print(lista)
print()

#metodo index() retorna o indice do elemento

print(f"lista.index(5): {lista.index(5)}\n")

#metodo pop() remove o elemento e retorna
lixo = lista.pop(0)
print(f"removido: {lixo}")
print()

#metodo remove() remove o elemento por valor
lista.remove(4)
print(f"lista removido por valor: {lista}")
print()
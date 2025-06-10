from classes.temp import Personagem, Heroi, Inimigo

heroi = Heroi(nome = "Hero", vida = 100, nivel = 5, habilidade = "Block")
print(heroi.exibir_detalhes())

inimigo = Inimigo(nome="Morcego", vida=100, nivel=3, tipo="Aerial")
print(inimigo.exibir_detalhes())
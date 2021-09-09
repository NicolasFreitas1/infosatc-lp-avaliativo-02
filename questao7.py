#Nicolas Andrade de Freitas
#Turma 2190

lista_filme = ["Vingadores", "Invocação do Mal"]
lista_jogos = ["Free Fire", "Fortnite"]
lista_livros = ["Diario de um Banana", "Harry Potter"]
lista_esporte = ["Basquete", "Tenis de Mesa"]
#criação das listas
#A)
lista_filme.append("Esquadrão Suicida")
lista_filme.append("Homem Aranha De Volta ao Lar")
print(lista_filme)

lista_jogos.append("Valorant")
lista_jogos.append("CSGO")
print(lista_jogos)

lista_livros.append("Diario de Anne Frank")
lista_livros.append("Pequeno Principe")
print(lista_livros)

lista_esporte.append("Futebol")
lista_esporte.append("Volei")
print(lista_livros)

#B)
lista_geral = [lista_filme, lista_jogos, lista_livros, lista_esporte]

#C)
print(lista_livros[2])

#D)
del lista_esporte[1]
print(lista_esporte)

#E)
lista_geral.append("[matematica , Portugues]")
print(lista_geral)



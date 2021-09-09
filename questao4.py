#Nicolas Andrade de Freitas
#Turma 2190

item1 = input("Digite um primeiro item qualquer ")
item2 = input("Digite um segundo item qualquer ")
item3 = input("Digite um terceiro item qualquer ")
#peço para digitar 3 itens aleatorios
lista1 = [item1, item2, item3]
#crio uma lista com esses itens
print("Esta é a primeira lista: {}".format(lista1))
#mostro a lista na tela
lista2 = lista1.copy()
#copio a primeira lista
print("Esta é a segunda lista, copia da primeira: {}".format(lista2))
#mostro a segunda lista
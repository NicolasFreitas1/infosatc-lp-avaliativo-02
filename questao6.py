#Nicolas Andrade de Freitas
#Turma 2190

e1 = input("Digite o primeiro elemento: ")
e2 = input("Digite o segundo elemento: ")
e3 = input("Digite o terceiro elemento: ")
#peço pra digitar 3 elementos

lista = [e1, e2, e3]
#coloco os elementos na lista
e = input("Qual elemento voce quer saber a posição da lista: ")

if e in lista:
    print("{} esta na posição: ".format(e), lista.index(e))
else:
    print("{} nao está na lista ".format(e))

#verificação do elemento, se ele esta na lista ou nao, e também sua posição na lista
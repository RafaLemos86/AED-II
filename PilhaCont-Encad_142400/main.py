from pilhaEncad import *
from pilhaCont import *
from produto import *

# produtos para testes
fruta1 = Product('morango', 2.80)
fruta2 = Product('maca', 1.75)
fruta3 = Product('pera', 3)
fruta4 = Product('bergamota', 5.5)
###################################


###################### TESTES PARA LISTA DE CONTIGUIDADE ######################
listaC = PilhaCont(3)

### INSERCOES E REMOCOES###

listaC.push(fruta1)
listaC.push(fruta2)
listaC.push(fruta3)
listaC.push(fruta4)
# fruta4 nao foi add pq nao tem espaco no vetor
print(listaC)
listaC.pop()
# remocao da fruta3 e insercao da 4
listaC.push(fruta4)
print(listaC.peek())
##################################

### CRIACAO DE UMA 2 LISTA PARA COMPARACAO ###

lista2C = PilhaCont(3)
lista2C.push(fruta1)
lista2C.push(fruta2)
lista2C.push(fruta4)

#####COMPARACAO E PRINT PARA CONFERIR ####
print(lista2C)
print(listaC)
lista2C.compare(listaC)


###################### TESTES PARA LISTA ENCADEADA ######################
listaE = PilhaEncad()

### INSERCOES E REMOCOES###
listaE.push(fruta3)
listaE.push(fruta1)
listaE.push(fruta4)
print(listaE)
# remocao da fruta4 e print do topo
listaE.pop()
print(listaE.peek())
##############################

### CRIACAO DE UMA 2 LISTA PARA COMPARACAO ###
print(listaE)
lista2E = PilhaEncad()
lista2E.push(fruta1)
lista2E.push(fruta3)

#####COMPARACAO E PRINT PARA CONFERIR ####
print(lista2E)
print(listaE)
lista2E.compare(listaE)
print(5 % 2)

from linkedList import *
from Produto import *

produto_a = product('banana', 4)
produto_b = product('maca', 5)
produto_c = product('laranja', 6)
produto_d = product('morango', 10)

lista = LinkedList()

lista.insert(1, produto_a)
lista.insert(1, produto_b)

print(lista)

# print(lista.consult_dado(produto_b))
lista.remove(3)
# print(lista)


# Chamada recursiva
print(lista.consult_dadoRec(produto_b, lista.head, 1))
print(lista.consult_dado(produto_b))
print(lista.consult_position(2))

lista.remove(1)
# print(lista)

lista.clean_list()
# print(lista)

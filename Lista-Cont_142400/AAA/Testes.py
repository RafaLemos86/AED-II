from Lista import *
from Produto import *

produto_a = product('banana', 4)
produto_b = product('maca', 5)
produto_c = product('laranja', 6)

lista = lista(5)

lista.insert(1, produto_a)
# print(lista.consult_dado(produto_a))

lista.insert(2, produto_b)
lista.insert(3, produto_c)
print(lista)
print(lista.consult_position(2))
# # print(lista.consult_position(3))

lista.remove(2)
# print(lista.consult_position(2))
# lista.remove(1)
# print(lista.consult_position(1))


# lista.clean_vector()
# print(lista)

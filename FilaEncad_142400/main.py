from pilhaEncad import *
from filaEncad import *

lista = FilaEncad()
lista.push(3)
lista.push(10)
lista.push(20)
lista.push(2)
lista.push(1)
lista.push(50)
lista.push(7)

print(lista)
lista.pop()
print(lista.peek())

ordenada = lista.ordenar()
print(ordenada)

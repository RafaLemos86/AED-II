from pilhaEncad import *


class Node:
    def __init__(self, dado):
        self.dado = dado
        self.next = None


class FilaEncad:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.size = 0

    def push(self, elem):
        # adiciona elemento na fila
        node = Node(elem)
        if self.size == 0:
            self.first = node
        else:
            self.last.next = node

        self.last = node
        self.size += 1

    def pop(self):
        # exclui elemento
        if self.size > 0:
            self.first = self.first.next
            self.size -= 1
        else:
            return 0

    def peek(self):
        # retorna o topo da pilha
        if self.size > 0:
            return self.first.dado
        else:
            return 0

    # funcao auxiliar
    def empty(self):
        return self.first == None

    # Desenfileirar
    def dequeue(self):
        if self.size > 0:
            self.first = self.first.next

    # funcao para usar o print
    def __str__(self) -> str:
        node = self.first
        output = ''
        while(node):
            output += '[' + str(node.dado) + '] -->'
            node = node.next
        return output

    def ordenar(self):
        if self.empty():
            return 0

        pilha_ordenada = StackLinked()
        pilha_desordenada = StackLinked()

        while not self.empty():
            value = self.peek()

            while not pilha_ordenada.empty() and pilha_ordenada.peek() >= value:
                pilha_ordenadaValor = pilha_ordenada.pop()
                pilha_desordenada.push(pilha_ordenadaValor)

            pilha_ordenada.push(value)

            while not pilha_desordenada.empty():
                pilha_desordenadaValor = pilha_desordenada.pop()
                pilha_ordenada.push(pilha_desordenadaValor)

            self.dequeue()

        print('-------------------')
        print(str(pilha_ordenada))
        print('-------------------')

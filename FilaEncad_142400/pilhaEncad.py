class Node:
    def __init__(self, dado):
        self.dado = dado
        self.next = None


class StackLinked:
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def push(self, elem):
        # adiciona no topo da pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        self.size = self.size + 1
        return node

    def pop(self):
        # exclui elemento
        if self.size > 0:
            node = self.top
            self.top = self.top.next
            self.size = self.size - 1
            return node.dado
        else:
            return False

    def peek(self):
        # retorna o topo da pilha
        if self.size > 0:
            return self.top.dado
        else:
            return False

    def __repr__(self):
        r = ''
        pointer = self.top
        while pointer:
            r = r + str(pointer.dado) + '--> '
            pointer = pointer.next
        return r

    def empty(self):
        return self.top == None

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class PilhaEncad:
    def __init__(self):
        self.top = None
        self.size = 0

    # empilhar um elemento
    def push(self, dado):
        nodo = Nodo(dado)
        # se a lista estiver vaiza, top e o nodo
        if self.size < 0:
            self.top = nodo
        # se a lista nao estiver vazia
        else:
            nodo.next = self.top
            self.top = nodo
        self.size += 1

    # remove o topo
    def pop(self):
        if self.size > 0:
            self.top = self.top.next
        else:
            return 0

        self.size -= 1

    # exclui todos os elementos
    def clear(self):
        if self.size == 0:
            return 0

        while self.size > 0:
            self.pop()

    # retorna o topo da lista
    def peek(self):
        if self.size > 0:
            return self.top.data
        return 0

    # comparar duas listas
    def compare(self, list2):
        # verificar se o tamanho e igual
        if self.size == list2.size:
            pointer1 = self.top
            pointer2 = list2.top
            # enquanto existir um ponteiro, verificar se o dado e igual
            while pointer1:
                if pointer1.data == pointer2.data:
                    pointer1 = pointer1.next
                    pointer2 = pointer2.next
                else:
                    # encontrou um dado diferente
                    print('as listas não são iguais')
                    return 0
            # nao encontrou erro
            print('As listas são iguais')
            return 1
        else:
            # tamanhos diferentes
            print('as listas não são iguais')
            return 0

    # funcao para retornar o print
    def __repr__(self):
        string = ''
        pointer = self.top
        while pointer:
            string = string + '--> ' + str(pointer.data) + '\n'
            pointer = pointer.next
        return string

    def __str__(self):
        return self.__repr__()

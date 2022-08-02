class Node:
    # todo no tem um dado e um proximo elemento
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # cabeca da lista e vazia e seu tamanho e 0
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, position, dado):
        # em caso de insercao na primeira posicao
        if position == 1:
            node = Node(dado)
            node.next = self.head
            self.head = node

        # nao existe posicao LOGICA 0
        elif (position <= 0) or (position > self.get_size()+1):
            return 0

        else:
            pointer = self.head
            # ponteiro para em uma posicao anterior, lista comeca em 1 por isso -2
            for i in range(position - 2):
                if pointer:
                    pointer = pointer.next
                else:
                    return 0
            # fazer a troca
            node = Node(dado)
            node.next = pointer.next
            pointer.next = node
        self.size += 1

    def remove(self, position):
        # se a lista tiver vaiza, nao remove nada
        if self.get_size() == 0:
            return 0

        # remocao na primeira posicao, passa a cabeca para o next
        elif position == 1:
            self.head = self.head.next

        else:
            before = self.head
            pointer = self.head.next
            # i comeca no 2 pois se fosse 1 cairia no elif
            i = 2
            while pointer:
                # enquanto pointer exisitir, procurar a posicao para fazer a troca
                if i == position:
                    before.next = pointer.next
                    pointer.next = None
                # incrementar ponteiros e contador
                pointer = pointer.next
                i += 1
                before = before.next
        # decrementar o tamanho ao final do processo
        self.size -= 1

    # tamanho da lista deve ser maior que 0

    def consult_position(self, position):
        if (self.get_size() > 0) and (position <= self.get_size()) and (position > 0):
            pointer = self.head
            # percorre do inicio ate posicao e retorna o dado dela
            for i in range(position - 1):
                if pointer:
                    pointer = pointer.next
                else:
                    return 0
            if pointer:
                return pointer.data
            else:
                return 0
        else:
            return 0

    def consult_dadoRec(self, dado, aux, position):
        if aux.next == None:
            return 0
        else:
            if aux.data == dado:
                return position
            else:
                return self.consult_dadoRec(dado, aux.next, position+1)

    # lista deve ser maior que 0
    def consult_dado(self, dado):
        if self.get_size() > 0:
            pointer = self.head
            # enquanto ponteiro existir, verificar se o dado e o mesmo do paramentro
            contador = 1
            while (pointer):
                if (pointer.data == dado):
                    return contador
                pointer = pointer.next
                contador += 1
            return 0
        else:
            return 0

    # enquanto tiver elemento na lista, chamar funcao remove
    def clean_list(self):
        if self.get_size() > 0:
            pointer = self.head
            while pointer:
                self.remove(pointer)
        else:
            return 0
        self.size = 0

    # funcao para retorna representar lista
    def __repr__(self):
        string = ''
        pointer = self.head
        while pointer:
            string = string + str(pointer.data) + ' --> '
            pointer = pointer.next
        return string

    # funcao para dar o print na lista
    def __str__(self):
        return self.__repr__()

      # funcao para retornar tamanho
    def get_size(self):
        return self.size

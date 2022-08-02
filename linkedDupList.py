class Node:
    # todo no tem um dado e um proximo elemento
    def __init__(self, data):
        self.data = data
        self.next = None
        self.ant = None


class LinkedDup:
    # cabeca da lista e vazia e seu tamanho e 0
    def __init__(self):
        self.head = None
        self.end = None
        self.size = 0

    def insert(self, position, dado):
        # em caso de insercao na primeira posicao
        node = Node(dado)
        if position == 1:
            # Para casos onde a lista n tem nada
            if self.head == None:
                self.head = node
                self.end = node
            else:
                # quando a lista ja tiver um head
                node.next = self.head
                self.head.ant = node
                self.head = node
        # nao existe posicao LOGICA 0
        elif (position <= 0) or (position > self.get_size()+1):
            return 0

        else:
            # caso onde a insercao nao e na posicao 1
            pointer = self.head
            # ponteiro para em uma posicao anterior, lista comeca em 1 por isso -2
            for i in range(position - 2):
                if pointer:
                    pointer = pointer.next
                else:
                    return 0
            # fazer a insercao na ultima posicao
            if pointer.next == None:
                node.ant = pointer
                pointer.next = node
                self.end = node
            # para o caso de inserir no meio da lista
            else:
                node.ant = pointer
                node.next = pointer.next
                pointer.next.ant = node
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
                # enquanto pointer existir, procurar a posicao para fazer a troca
                if i == position:
                    # se a remocao for no meio da lista
                    if pointer.next != None:
                        before.next = pointer.next
                        pointer.next.ant = before.next
                    else:
                        # caso seja o rabo da lista, apenas fazer o anterior nao apontar para nada
                        # colocar o end no lugar certo
                        before.next = None
                        self.end = before
                # incrementar ponteiros e contador
                pointer = pointer.next
                before = before.next
                i += 1
        # decrementar o tamanho ao final do processo
        self.size -= 1

    # informa a posicao e retorna o dado

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

    # informa o dado e retorna a posicao
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

    # funcao para imprimir a lista ao contrario
    def inversePrint(self):
        string = ''
        # ponteiro comeca no final
        pointer = self.end
        while pointer:
            string = string + '<--' + str(pointer.data) + ' --> '
            # decrementar pointeiro
            pointer = pointer.ant
        return string

    # funcao para retorna representar lista
    def __repr__(self):
        string = ''
        pointer = self.head
        while pointer:
            string = string + '<--' + str(pointer.data) + ' --> '
            pointer = pointer.next
        return string

    # funcao para dar o print na lista
    def __str__(self):
        return self.__repr__()

      # funcao para retornar tamanho
    def get_size(self):
        return self.size

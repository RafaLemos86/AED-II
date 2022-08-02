class lista:
    # Logo na estrutura da lista, deve-se ter um inicio, fim e tamanho maximo
    def __init__(self, max_length):
        self.max_length = max_length
        self.start = -1
        self.end = -1
        self.vector = [None] * self.max_length

    # se o inicio da minha lista for -1, sinal que ela é vazia
    def empty(self):
        if (self.start == -1 or self.end == -1):
            return 1
        else:
            return 0

    # retorna tamanho da lista em numero lógico, por isso do +1, para nao contar a posicao 0
    def size(self):
        return self.end - self.start + 1

    def insert(self, position, dado):
        # conferir se há espaço na lista, depois, se a posição é válida
        if ((self.start != 0 or self.end != self.max_length - 1) and (position > 0) and (position <= self.size() + 1)):
            if (self.empty()):
                self.start = 0
                self.end = 0
            # se tiver espaço no fim da lista, inserir lá
            elif (self.start + position - 1) > (self.end - position - 1):
                for i in range(self.end, self.start + position - 2, -1):
                    self.vector[i+1] = self.vector[i]
                # NÃO ESQUECENDO DE POR O FINAL PRA PROX POSITION!!
                self.end = self.end + 1
            else:
                # PERCORRER PARA O INICIO
                for i in range(self.start, self.start + position - 1):
                    self.vector[i-1] = self.vector[i]
                    # MUDAR A POSICAO NO INICIO!!
                self.start = self.start - 1
            self.vector[self.start + position - 1] = dado
            return 1
        else:
            return 0

    # a 'formula' para posicao do objeto é sempre essa
    def consult_position(self, position):
        if not self.empty():
            return self.vector[self.start + position - 1]

    # percorrer lista e informar a posicao LOGICA
    def consult_dado(self, dado):
        if not self.empty():
            for i in range(self.start, self.end - self.start + 1):
                if self.vector[i] == dado:
                    return i + 1
        else:
            return 0

    # reseta vetor para posicao inicial
    def clean_vector(self):
        if not self.empty():
            self.start = -1
            self.end = -1
        else:
            return 0

    # Remover elemento de uma posição
    def remove(self, position):
        # se o tamanho for um, a lista é excluida
        if self.size() == 1:
            self.clean_vector()
        # se a posicao for maior que o espaco da lista, retorna 0
        elif (position > self.end - self.start + 1) or (position <= 0):
            return 0
        else:
            # Percorrer para o final/inicio
            if (self.start + position - 1) > (self.end - position - 1):
                for i in range(self.start + position - 1, self.end + 1):
                    self.vector[i] = self.vector[i+1]
                self.end -= 1

                # percorrendo do inicio/final
            else:
                for i in range(self.start + position - 1, self.start + 1):
                    self.vector[i] = self.vector[i-1]
                self.start += 1

    def __repr__(self):
        string = ''
        for i in range(self.start, self.end+1):
            string = string + str(self.vector[i]) + ' ||| '
        return string

    # funcao para dar o print na lista
    def __str__(self):
        return self.__repr__()

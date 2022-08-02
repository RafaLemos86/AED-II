class PilhaCont:
    def __init__(self, max_length):
        self.vector = [None] * max_length
        self.base = 0
        self.top = -1
        self.max = max_length - 1
        self.size = 0

    # adiciona um elemento
    def push(self, dado):
        if self.max > self.top:
            self.top = self.top + 1
            self.vector[self.top] = dado
        else:
            return 0
        self.size += 1

    # remove um elemento
    def pop(self):
        if self.size > 0:
            self.top -= 1
        self.size -= 1

    # exclui a lista
    def clear(self):
        while self.size > 0:
            self.pop()

    # retorna o topo
    def peek(self):
        if self.size > 0:
            return self.vector[self.top]

    # comparar duas listas
    def compare(self, list2):
        # verificar se o tamanho e o mesmo
        if self.size == list2.size:
            for i in range(self.size):
                # percorrer lista verificando cada valor
                if self.vector[i] != list2.vector[i]:
                    print('as listas nao sao iguais')
                    return 0
            # se sair do range sem erro, são iguais
            print('as listas sao iguais')
            return 1
        else:
            # listas de tamanhos diferentes
            print('as listas não são iguais')
            return 0

    # funcao para retorna o print
    def __repr__(self):
        index = self.top
        string = ''
        for i in range(self.size):
            string = string + '| ' + str(self.vector[index]) + '\n'
            index -= 1
        return string

    def __str__(self):
        return self.__repr__()

class Table:
    # Logo na estrutura da lista, deve-se ter um inicio, fim e tamanho maximo
    def __init__(self, max_length):
        self.max_length = max_length
        self.start = -1
        self.end = -1
        self.keys = [None] * (self.max_length + 1)
        self.values = [None] * (self.max_length + 1)

    # se o inicio da minha lista for -1, sinal que ela é vazia
    def empty(self):
        if (self.start == -1 or self.end == -1):
            return 1
        else:
            return 0

    # retorna tamanho da lista em numero lógico, por isso do +1, para nao contar a posicao 0
    def size(self):
        if not self.empty():
            return self.end - self.start + 1
        else:
            return 0

    def insert(self, key, value):
        # caso ja exista uma chave igual, substituir os valores
        if self.type_search(key, 1) > 0:
            self.values[self.type_search(key, 0)] = value
        # criar chave e valor novos, verifcando se tem espaco no vetor
        elif (self.size() < self.max_length):
            # caso a lista estiver vazia, inserir na posicao 1
            if self.empty():
                self.end = 1
                self.start = 1
            # se nao, encrementar final e inserir no novo campo
            else:
                self.end += 1
            self.values[self.end] = value
            self.keys[self.end] = key

        else:
            return 0

    # remove elemento a partir da chave
    def remove(self, key):
        # se a chave for > 0, ela existe
        if self.type_search(key, 0) > 0:
            for i in range(self.type_search(key, 0), self.end):
                # passar o que tem no proximo elemento, para o anterior
                self.values[i] = self.values[i + 1]
                self.keys[i] = self.keys[i + 1]
            self.end -= 1
        else:
            return 0

    # busca linear
    def linear_search(self, key):
        if not self.empty():
            for i in range(self.start, self.end + 1):
                if self.keys[i] == key:
                    return i
            else:
                return 0
        else:
            return 0

    # busca binaria
    def binary_search(self, key):
        short = 1
        high = self.size()
        while high >= short:
            middle = (short + high) // 2
            kick = self.keys[middle]
            if kick == key:
                return middle
            if kick > key:
                high = middle - 1
            if kick < key:
                short = middle + 1
        return 0

        

    # escolher o tipo de busca
    def type_search(self, key, option):
        if option == 0:
            return self.binary_search(key)
        elif option == 1:
            return self.linear_search(key)
        else:
            return self.binary_search(key)

    def order_insert(self, key, value):
        # caso ja exista uma chave igual, substituir os valores
        if self.type_search(key, 0) > 0:
            self.values[self.type_search(key, 0)] = value
        # criar chave e valor novos, verifcando se tem espaco no vetor
        elif (self.size() < self.max_length):
            # caso a lista estiver vazia, inserir na posicao 1
            if self.empty():
                self.end = 1
                self.start = 1
                self.values[self.end] = value
                self.keys[self.end] = key
            # se nao, encrementar final e inserir no novo campo
            else:
                # index igual o final da lista
                index = self.end
                # enquanto os valores estiverem maior que a chave, desloca-los para direita do vetor
                while index != 0 and self.keys[index] > key:
                    self.keys[index + 1] = self.keys[index]
                    self.values[index + 1] = self.values[index]
                    index -= 1
                # depois de deslocar, inserir
                self.end += 1
                self.keys[index + 1] = key
                self.values[index + 1] = value
        else:
            return 0

    # Consultar o valor a partir da chave
    def consult(self, key):
        # se o valor da posicao da chave for > 0, ele existe
        if self.type_search(key, 1) > 0:
            # retorna o valor
            return self.values[self.type_search(key, 0)]
        else:
            return 0

    # apagar todos os eleme

    def clean_vector(self):
        if self.size() > 0:
            self.start = -1
            self.end = -1
        else:
            return 0

    # funcao para print
    def __repr__(self):
        if not self.empty():
            string = ''
            for i in range(self.start, self.end+1):
                string = string + "Chave: " + \
                    str(self.keys[i]) + ' Informações: ' + \
                    str(self.values[i]) + ' | ' + '\n'
            return string

    # funcao para dar o print na lista
    def __str__(self):
        return self.__repr__()

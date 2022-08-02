def somaDigito(number):
    # caso base
    # se o numero for 0, a soma e 0
    if number == 0:
        return 0
    # resto da divisao + recursao da divisao inteira
    return (number % 10) + somaDigito(number // 10)


print(somaDigito(143))

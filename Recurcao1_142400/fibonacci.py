from tkinter import N


def FibonacciRec(number):
    # se number for 1 ou 0 retorna ele mesmo
    if number in {0, 1}:
        return number
    # caso recursivo
    return FibonacciRec(number - 1) + FibonacciRec(number - 2)


def FibonacciLinear(number):
    # retorna 1
    if number == 1:
        return [1]
    # retorna os dois primeiros da lista
    if number == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, number):
        # soma todos os annteriores
        fibs.append(fibs[-1] + fibs[-2])
    # retorna ultimo da lista
    return fibs[-1]

# JEITO FEITO EM AULA


def f(n):
    if n in {0, 1}:
        return n
    c = 1
    n1 = 0
    n2 = 1
    while (c < n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        c += 1
    return n3


print(FibonacciRec(11))
print(FibonacciLinear(11))
print(f(11))

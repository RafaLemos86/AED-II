def FatorialLinear(number):
    # para caso o parametro for 0 ou 1
    if number in {0, 1}:
        return 1
    # multiplica o numero pelo seus antecessores
    cont = number - 1
    for i in range(cont):
        number = number * cont
        cont -= 1
    return number


def FatorialRec(number):
    # caso base é 0
    if number == 0:
        return 1
    # recurcao
    return number * FatorialRec(number - 1)


print(FatorialLinear(5))
print(FatorialRec(5))

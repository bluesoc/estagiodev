#!/bin/python3

# Usar um gerador é mais eficaz e eficiente para economizar memória.

# Gerador Fibonnaci
def genFibo():
    # Valor Inicial da Sequência
    a, b = 0, 1

    # Gera infinitamente,
    # Sem agredir a memória
    while True:
        yield a
        b = a + b
        a = b - a


def isFibo(numero: int):
    generator = genFibo()

    for i in range(0, numero):
        x = next(generator)

        # Mostra numero da sequencia
        #print(x)

        if x == numero:
            print(f"Numero {numero} pertence a sequencia Fibonnaci.")
            break
        elif x > numero:
            print(f"Numero {numero} nao pertence a sequencia Fibonnaci.")
            break

# Testes e validação:
isFibo(3)
isFibo(27)
isFibo(55)
isFibo(67)
isFibo(144)
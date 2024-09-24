#!/bin/python3

def soma(indice: int, k: int):
    soma = 0
    while k < indice:
        k += 1
        soma = soma + k

    print(soma)
    return soma

resultado = soma(13, 0)


# int INDICE = 13
# SOMA = 0
# K = 0

# Resultado igual: 91

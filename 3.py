#!/bin/python3
from statistics import mean
import json

def menorFaturamento(faturamento: list):
    return json.dumps({'faturamento': min(faturamento)})

def maiorFaturamento(faturamento: list):
    return json.dumps({'faturamento': max(faturamento)})

def mediaFaturamento(faturamento: list):
    return mean(faturamento)


def superouMedia(faturamento: list):
    media = mediaFaturamento(faturamento_diario)

    superouList = []
    tamanho = len(faturamento)

    # O(n)
    for i in range(0, tamanho):
        if faturamento[i] > media:
            superouList.append(faturamento[i])

    return superouList


# Numeros de faturamento aleatorios
# gerados para serem exemplos. 

faturamento_Objeto = {
    1: 250.50,  2: 300.75,  3: 150.20,  4: 400.00,  5: 500.10,
    8: 600.25,  9: 700.80, 10: 800.90, 11: 900.00, 12: 1000.50,
   15: 1100.60, 16: 1200.70, 17: 1300.80, 18: 1400.90, 19: 1500.00,
   22: 1600.10, 23: 1700.20, 24: 1800.30, 25: 1900.40, 26: 2000.50,
   29: 2100.60, 30: 2200.70
}


faturamento_diario = list(faturamento_Objeto.values())

# Menor Valor Faturado
print("Menor Valor Faturado:")
print(menorFaturamento(faturamento_diario))

# Maior Valor Faturado
print("Maior Valor Faturado:")
print(maiorFaturamento(faturamento_diario))

# Media de Faturamento
print("Media de Faturamento:")
print(mediaFaturamento(faturamento_diario))


# Dias que Superaram a média de Faturamento
print("Superou Média:")
print(superouMedia(faturamento_diario))

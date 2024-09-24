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


# Abre arquivo JSON

with open("dados.json") as file:
    faturamento_Objeto = json.load(file)


faturamento_diario = [item['valor'] for item in faturamento_Objeto if item.get('valor') > 0]


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

#!/bin/python3

string = "Hello World! Quero um estagio"

tamanho = len(string) - 1

# Reverte string
# Usa enumerate para gerar indices.
for i, j in enumerate(string):
    print(string[tamanho - i], end='')

print()
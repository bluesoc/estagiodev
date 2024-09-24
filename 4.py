#!/bin/python3

# Faturamento mensal por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Faturamento total
faturamento_total = sum(faturamento.values())

print("Percentual de representação:")

for estado, valor in faturamento.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")

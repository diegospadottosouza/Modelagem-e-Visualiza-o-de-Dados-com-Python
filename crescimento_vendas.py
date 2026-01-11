# Entrada dos dados
mes_anterior = input()
vendas_anterior = float(input())

mes_atual = input()
vendas_atual = float(input())

# Cálculo do crescimento percentual
crescimento = ((vendas_atual - vendas_anterior) / vendas_anterior) * 100

# Saída formatada
print(f"Crescimento percentual de vendas: {crescimento:.2f}%")
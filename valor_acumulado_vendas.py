# Entrada: quantidade de meses
n = int(input())

acumulado = 0
resultados = []

for _ in range(n):
    mes = input()
    valor = float(input())
    acumulado += valor
    resultados.append(f"{mes}: {acumulado:.1f}")

# Saída
for r in resultados:
    print(r)
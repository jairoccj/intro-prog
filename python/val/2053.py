matriz = []
for i in range(9):
    matriz.append([0] * 4)

for i in range(20):
    linha, coluna = map(int, input().split())
    matriz[linha][coluna] += 1

maior = float('-inf')

for i in range(9):
    for j in range(4):
        if maior < matriz[i][j]:
            maior = matriz[i][j]

for i in range(9):
    for j in range(4):
        if maior == matriz[i][j]:
            print(i, j)